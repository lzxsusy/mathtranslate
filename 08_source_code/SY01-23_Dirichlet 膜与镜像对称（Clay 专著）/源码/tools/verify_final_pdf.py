#!/usr/bin/env python3
"""Verify PDF build mechanics without extracting or reviewing manuscript text."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import logging
from pathlib import Path
import re
import shutil
import subprocess
import sys

from pypdf import PdfReader
from pypdf.generic import (
    ArrayObject, ByteStringObject, DictionaryObject, IndirectObject,
    NameObject, NullObject, NumberObject, StreamObject, TextStringObject,
)

PROJECT = Path(__file__).resolve().parents[1]
A4_PT = (210 * 72 / 25.4, 297 * 72 / 25.4)
A4_TOLERANCE_PT = 0.75
EXPECTED_INDEX_REFERENCES = 643
EXPECTED_INDEX_IDS = 537


def remove_tex_comments(text):
    """Remove unescaped TeX comments without interpreting any TeX commands."""
    return "".join(
        strip_comment(line) for line in text.splitlines(keepends=True)
    )


def strip_comment(line):
    for pos, char in enumerate(line):
        if char != "%":
            continue
        count = 0
        while pos - count - 1 >= 0 and line[pos - count - 1] == "\\":
            count += 1
        if count % 2 == 0:
            return line[:pos] + ("\n" if line.endswith("\n") else "")
    return line


def brace_group(text, start):
    """Read one balanced group, allowing nested math and texorpdfstring."""
    while start < len(text) and text[start].isspace():
        start += 1
    if start >= len(text) or text[start] != "{":
        raise ValueError("Expected a TeX brace group at offset " + str(start))
    depth = 0
    pos = start
    while pos < len(text):
        char = text[pos]
        if char in "{}":
            backslashes = 0
            while pos - backslashes - 1 >= 0 and text[pos - backslashes - 1] == "\\":
                backslashes += 1
            if backslashes % 2 == 0:
                depth += 1 if char == "{" else -1
                if depth == 0:
                    return text[start + 1:pos], pos + 1
        pos += 1
    raise ValueError("Unclosed TeX brace group at offset " + str(start))


def top_level_groups(payload):
    result = []
    pos = 0
    while pos < len(payload):
        if payload[pos].isspace():
            pos += 1
            continue
        value, pos = brace_group(payload, pos)
        result.append(value)
    return result


def read_aux_labels(path, anomalies):
    labels = {}
    files = []
    visiting = set()
    visited = set()

    def read_file(filename):
        filename = filename.resolve()
        if filename in visiting:
            anomalies.append({"kind": "aux_input_cycle", "file": str(filename)})
            return
        if filename in visited:
            return
        if not filename.is_file():
            anomalies.append({"kind": "missing_aux_input", "file": str(filename)})
            return
        visiting.add(filename)
        text = remove_tex_comments(filename.read_text(encoding="utf-8"))
        files.append(str(filename))
        # Arguments, particularly the title field, are parsed with balanced
        # groups rather than a regex that stops at the first closing brace.
        for token in re.finditer(r"\\(newlabel|@input)(?![A-Za-z@])", text):
            try:
                name, end = brace_group(text, token.end())
                if token[1] == "@input":
                    read_file(filename.parent / name)
                    continue
                payload, _ = brace_group(text, end)
                fields = top_level_groups(payload)
                if len(fields) < 2:
                    raise ValueError("newlabel has fewer than two fields")
                if name in labels:
                    anomalies.append({"kind": "duplicate_aux_label", "label": name,
                                      "file": str(filename)})
                labels[name] = {
                    "number": fields[0], "printed_page": fields[1],
                    "title": fields[2] if len(fields) > 2 else "",
                    "destination": fields[3] if len(fields) > 3 else "",
                    "field_count": len(fields), "aux_file": str(filename),
                }
            except (ValueError, OSError) as error:
                anomalies.append({"kind": "malformed_aux_command",
                                  "file": str(filename), "offset": token.start(),
                                  "message": str(error)})
        visiting.remove(filename)
        visited.add(filename)

    read_file(Path(path))
    return labels, files


def index_ids(path):
    text = remove_tex_comments(path.read_text(encoding="utf-8"))
    result = []
    for token in re.finditer(r"\\BookIndexPage(?![A-Za-z@])", text):
        value, _ = brace_group(text, token.end())
        result.append(value)
    return result


def dereference(value):
    return value.get_object() if isinstance(value, IndirectObject) else value


def object_identity(value):
    if isinstance(value, IndirectObject):
        return ("indirect", value.idnum, value.generation)
    reference = getattr(value, "indirect_reference", None)
    if isinstance(reference, IndirectObject):
        return ("indirect", reference.idnum, reference.generation)
    return ("direct", id(value))


def destination_name(value):
    if isinstance(value, ByteStringObject):
        data = bytes(value)
        if data.startswith((b"\xfe\xff", b"\xff\xfe")):
            return data.decode("utf-16")
        return data.decode("latin-1")
    if isinstance(value, NameObject):
        return str(value)[1:]  # Legacy /Dests dictionaries use PDF names.
    return str(value)


class PDFMechanics:
    def __init__(self, reader, anomalies):
        self.reader = reader
        self.anomalies = anomalies
        self.pages = list(reader.pages)
        self.page_by_reference = {}
        self.page_by_identity = {}
        for number, page in enumerate(self.pages):
            reference = getattr(page, "indirect_reference", None)
            if isinstance(reference, IndirectObject):
                self.page_by_reference[(reference.idnum, reference.generation)] = number
            self.page_by_identity[id(page)] = number
        self.names = {}
        self.name_occurrences = []
        self.destination_checks = []
        self.internal_link_records = []
        self.external_link_records = []
        self.other_link_records = []
        self.annotation_count = 0
        self.link_annotation_count = 0
        self.goto_action_count = 0
        self.outline_records = []

    def error(self, kind, context, **details):
        self.anomalies.append({"kind": kind, "context": context, **details})

    def read_names(self):
        root = self.reader.trailer["/Root"]
        seen = set()

        def add(name, value, context):
            name = destination_name(name)
            self.name_occurrences.append({"name": name, "context": context})
            if name in self.names:
                self.error("duplicate_named_destination", context, name=name)
            else:
                self.names[name] = value

        def tree(reference, context):
            key = object_identity(reference)
            if key in seen:
                self.error("repeated_or_cyclic_destination_name_tree", context)
                return
            seen.add(key)
            node = dereference(reference)
            if not isinstance(node, DictionaryObject):
                self.error("invalid_destination_name_tree_node", context)
                return
            pairs = dereference(node.get("/Names", ArrayObject()))
            if not isinstance(pairs, ArrayObject) or len(pairs) % 2:
                self.error("malformed_destination_name_pairs", context)
            else:
                for i in range(0, len(pairs), 2):
                    add(pairs[i], pairs[i + 1], context + "/Names[" + str(i) + "]")
            children = dereference(node.get("/Kids", ArrayObject()))
            if not isinstance(children, ArrayObject):
                self.error("invalid_destination_name_tree_kids", context)
                return
            for i, child in enumerate(children):
                tree(child, context + "/Kids[" + str(i) + "]")

        names = dereference(root.get("/Names", DictionaryObject()))
        if isinstance(names, DictionaryObject) and "/Dests" in names:
            tree(names.raw_get("/Dests"), "catalog/Names/Dests")
        legacy = dereference(root.get("/Dests", DictionaryObject()))
        if isinstance(legacy, DictionaryObject):
            for name, value in legacy.items():
                add(name, value, "catalog/Dests")
        else:
            self.error("invalid_legacy_destination_dictionary", "catalog/Dests")

    def page_number(self, value):
        if isinstance(value, IndirectObject):
            number = self.page_by_reference.get((value.idnum, value.generation))
            if number is not None:
                return number
        obj = dereference(value)
        if isinstance(obj, (int, NumberObject)) and not isinstance(obj, bool):
            number = int(obj)
            return number if 0 <= number < len(self.pages) else None
        reference = getattr(obj, "indirect_reference", None)
        if isinstance(reference, IndirectObject):
            number = self.page_by_reference.get((reference.idnum, reference.generation))
            if number is not None:
                return number
        return self.page_by_identity.get(id(obj))

    def destination(self, value, context, seen=None):
        seen = set() if seen is None else seen
        if isinstance(value, IndirectObject):
            identity = object_identity(value)
            if identity in seen:
                self.error("cyclic_destination_reference", context)
                return {"valid": False}
            seen = seen | {identity}
        obj = dereference(value)
        if isinstance(obj, (str, TextStringObject, ByteStringObject, NameObject)):
            name = destination_name(obj)
            key = ("name", name)
            if key in seen:
                self.error("cyclic_named_destination", context, name=name)
                return {"valid": False, "name": name}
            if name not in self.names:
                self.error("missing_named_destination", context, name=name)
                return {"valid": False, "name": name}
            result = self.destination(self.names[name], context, seen | {key})
            return {**result, "name": name}
        if isinstance(obj, DictionaryObject) and "/D" in obj:
            return self.destination(obj.raw_get("/D"), context, seen)
        if not isinstance(obj, ArrayObject) or len(obj) < 2:
            self.error("invalid_explicit_destination", context,
                       object_type=type(obj).__name__)
            return {"valid": False}
        page = self.page_number(obj[0])
        mode = str(dereference(obj[1]))
        expected = {"/XYZ": 5, "/Fit": 2, "/FitH": 3, "/FitV": 3,
                    "/FitR": 6, "/FitB": 2, "/FitBH": 3, "/FitBV": 3}
        valid = page is not None and mode in expected and len(obj) == expected.get(mode)
        if page is None:
            self.error("destination_page_not_in_document", context)
        if mode not in expected or len(obj) != expected.get(mode):
            self.error("invalid_destination_mode_or_arity", context,
                       mode=mode, argument_count=len(obj))
        for value in obj[2:]:
            value = dereference(value)
            if not isinstance(value, (int, float, NullObject)):
                valid = False
                self.error("invalid_destination_coordinate", context,
                           object_type=type(value).__name__)
            if mode == "/FitR" and isinstance(value, NullObject):
                valid = False
                self.error("null_fit_rectangle_coordinate", context)
        return {"valid": valid, "physical_page": page + 1 if page is not None else None,
                "mode": mode}

    def verify_named_destinations(self):
        for name, value in self.names.items():
            self.destination_checks.append({
                "name": name, **self.destination(value, "named destination " + name)
            })

    def read_annotations(self):
        for page_number, page in enumerate(self.pages, 1):
            for number, reference in enumerate(dereference(page.get("/Annots", ArrayObject()))):
                annotation = dereference(reference)
                context = "page " + str(page_number) + " annotation " + str(number)
                self.annotation_count += 1
                if not isinstance(annotation, DictionaryObject):
                    self.error("invalid_annotation_dictionary", context)
                    continue
                is_link = annotation.get("/Subtype") == "/Link"
                if is_link:
                    self.link_annotation_count += 1
                if "/Dest" in annotation:
                    result = self.destination(annotation.raw_get("/Dest"), context)
                    if is_link:
                        self.internal_link_records.append({"page": page_number, **result})
                elif "/A" in annotation:
                    action = dereference(annotation.raw_get("/A"))
                    if not isinstance(action, DictionaryObject):
                        self.error("invalid_annotation_action", context)
                        continue
                    action_type = str(action.get("/S", ""))
                    if action_type == "/GoTo":
                        result = self.destination(action.get("/D"), context)
                        if is_link:
                            self.internal_link_records.append({"page": page_number, **result})
                    elif is_link and action_type in ("/URI", "/GoToR", "/GoToE", "/Launch"):
                        self.external_link_records.append({
                            "page": page_number, "action": action_type,
                            "uri": str(action.get("/URI", "")),
                        })
                    elif is_link:
                        self.other_link_records.append({"page": page_number,
                                                        "action": action_type})
                elif is_link:
                    self.error("link_annotation_without_target", context)

    def verify_all_goto_actions(self):
        """Inspect reachable action dictionaries, including /Next and /AA."""
        visited = set()
        pending = [(self.reader.trailer.raw_get("/Root"), "catalog")]
        while pending:
            reference, context = pending.pop()
            obj = dereference(reference)
            if not isinstance(obj, (DictionaryObject, ArrayObject)):
                continue
            identity = object_identity(reference)
            if identity in visited:
                continue
            visited.add(identity)
            if isinstance(obj, StreamObject):
                continue  # No content streams or font programs are interpreted.
            if isinstance(obj, DictionaryObject):
                if obj.get("/S") == "/GoTo":
                    self.goto_action_count += 1
                    self.destination(obj.get("/D"), context)
                for name, child in obj.items():
                    pending.append((child, (context + "/" + str(name).lstrip("/"))[-240:]))
            else:
                for number, child in enumerate(obj):
                    pending.append((child, (context + "[" + str(number) + "]")[-240:]))

    def read_outlines(self):
        root = dereference(self.reader.trailer["/Root"].get("/Outlines"))
        if root is None:
            return
        if not isinstance(root, DictionaryObject):
            self.error("invalid_outline_root", "catalog/Outlines")
            return
        visited = set()

        def siblings(reference, depth):
            while reference is not None:
                identity = object_identity(reference)
                if identity in visited:
                    self.error("cyclic_or_repeated_outline_item", "outlines",
                               depth=depth)
                    return
                visited.add(identity)
                item = dereference(reference)
                if not isinstance(item, DictionaryObject):
                    self.error("invalid_outline_item", "outlines", depth=depth)
                    return
                number = len(self.outline_records) + 1
                context = "outline " + str(number)
                entry = {"number": number, "depth": depth,
                         "title": str(item.get("/Title", ""))}
                if "/Dest" in item:
                    entry["destination"] = self.destination(item.raw_get("/Dest"), context)
                elif "/A" in item:
                    action = dereference(item.raw_get("/A"))
                    if isinstance(action, DictionaryObject) and action.get("/S") == "/GoTo":
                        entry["destination"] = self.destination(action.get("/D"), context)
                    else:
                        entry["external_or_other_action"] = str(action.get("/S", "")) if isinstance(action, DictionaryObject) else None
                else:
                    entry["group_without_destination"] = True
                self.outline_records.append(entry)
                if "/First" in item:
                    siblings(item.raw_get("/First"), depth + 1)
                reference = item.raw_get("/Next") if "/Next" in item else None

        if "/First" in root:
            siblings(root.raw_get("/First"), 0)


def read_font_table(path, anomalies):
    executable = shutil.which("pdffonts")
    if not executable:
        anomalies.append({"kind": "pdffonts_not_available"})
        return {"fonts": [], "exit_code": None, "stdout": "", "stderr": ""}
    result = subprocess.run([executable, str(path)], capture_output=True, text=True)
    fonts = []
    lines = result.stdout.splitlines()
    if result.returncode:
        anomalies.append({"kind": "pdffonts_failed", "exit_code": result.returncode,
                          "stderr": result.stderr})
    if result.stderr.strip():
        anomalies.append({"kind": "pdffonts_diagnostic", "message": result.stderr.strip()})
    if len(lines) < 2:
        anomalies.append({"kind": "missing_pdffonts_table"})
    else:
        # pdffonts columns have minimum widths: long font names push the
        # subsequent fields right. Read embedding flags from the row's end.
        row_tail = re.compile(
            r"^(.*?)\s+(\S+)\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+(\d+)\s+(\d+)\s*$"
        )
        font_type = re.compile(
            r"(CID Type 0C \(OT\)|CID Type 0 \(OT\)|CID TrueType|"
            r"CID Type 0C|CID Type 0|Type 1C \(OT\)|Type 1 \(OT\)|"
            r"TrueType \(OT\)|Type 1C|Type 1|Type 3|TrueType|unknown)$"
        )
        for line in lines[2:]:
            if not line.strip():
                continue
            match = row_tail.match(line)
            type_match = font_type.search(match[1].rstrip()) if match else None
            if not match or not type_match:
                anomalies.append({"kind": "unparsed_pdffonts_row", "row": line})
                continue
            name = match[1][:type_match.start()].strip()
            kind = type_match[1]
            encoding, embedded, subset, unicode_map = match.group(2, 3, 4, 5)
            object_id = match[6] + " " + match[7]
            fonts.append({"name": name, "type": kind, "encoding": encoding,
                          "embedded": embedded == "yes", "subset": subset == "yes",
                          "unicode_mapping": unicode_map == "yes", "object_id": object_id,
                          "pdffonts_row": line})
            if embedded != "yes":
                anomalies.append({"kind": "unembedded_font", "font": name,
                                  "object_id": object_id, "reported_embedding": embedded})
    return {"tool": executable, "fonts": fonts, "exit_code": result.returncode,
            "stdout": result.stdout, "stderr": result.stderr}


def verify(args):
    anomalies = []
    warnings = []

    class PDFLogCapture(logging.Handler):
        def emit(self, log_record):
            warnings.append({"kind": "pypdf_diagnostic",
                             "level": log_record.levelname,
                             "message": log_record.getMessage()})

    handler = PDFLogCapture()
    logger = logging.getLogger("pypdf")
    logger.addHandler(handler)
    pdf, aux = Path(args.pdf).resolve(), Path(args.aux).resolve()
    record = {"role": "final PDF build mechanics; no manuscript review or original PDF comparison",
              "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "pdf": str(pdf), "aux": str(aux),
              "index_source": str(PROJECT / "index-zh.tex"),
              "anomalies": anomalies, "warnings": warnings}
    try:
        before = (pdf.stat().st_size, pdf.stat().st_mtime_ns)
        record["pdf_sha256"] = hashlib.sha256(pdf.read_bytes()).hexdigest()
        record["aux_sha256"] = hashlib.sha256(aux.read_bytes()).hexdigest()
        reader = PdfReader(pdf)
        checks = PDFMechanics(reader, anomalies)
        record["page_count"] = len(checks.pages)
        pages = []
        for number, page in enumerate(checks.pages, 1):
            sizes = {}
            for name, box in (("media", page.mediabox), ("crop", page.cropbox)):
                width, height = float(box.width), float(box.height)
                sizes[name] = [width, height]
                if any(abs(a - b) > A4_TOLERANCE_PT
                       for a, b in zip(sorted((width, height)), A4_PT)):
                    anomalies.append({"kind": "non_a4_page_box", "physical_page": number,
                                      "box": name, "size_pt": [width, height]})
            pages.append({"physical_page": number, "boxes_pt": sizes,
                          "rotation": int(page.get("/Rotate", 0))})
        record["page_sizes"] = {"expected_a4_pt": A4_PT,
                                "tolerance_pt": A4_TOLERANCE_PT, "pages": pages}
        record["font_embedding"] = read_font_table(pdf, anomalies)
        checks.read_names()
        checks.verify_named_destinations()
        checks.read_annotations()
        checks.verify_all_goto_actions()
        checks.read_outlines()
        record["named_destinations"] = {
            "raw_occurrence_count": len(checks.name_occurrences),
            "unique_name_count": len(checks.names),
            "destinations": checks.destination_checks,
        }
        record["navigation"] = {
            "annotation_count": checks.annotation_count,
            "link_annotation_count": checks.link_annotation_count,
            "internal_link_count": len(checks.internal_link_records),
            "external_link_count": len(checks.external_link_records),
            "other_link_count": len(checks.other_link_records),
            "all_reachable_goto_action_count": checks.goto_action_count,
            "external_links": checks.external_link_records,
            "other_links": checks.other_link_records,
            "outline_count": len(checks.outline_records),
            "outline_depth_counts": dict(sorted(Counter(
                item["depth"] for item in checks.outline_records).items())),
            "outlines": checks.outline_records,
        }
        citations = []
        for number in range(1, 477):
            name = f"cite.0@ref{number:03d}"
            citations.append({"name": name, **checks.destination(name, "bibliography " + name)})
        record["bibliography_destinations"] = {
            "expected_count": 476, "valid_count": sum(x["valid"] for x in citations),
            "destinations": citations,
        }
        labels, aux_files = read_aux_labels(aux, anomalies)
        ids = index_ids(PROJECT / "index-zh.tex")
        if len(ids) != EXPECTED_INDEX_REFERENCES:
            anomalies.append({"kind": "index_source_reference_count_mismatch",
                              "expected": EXPECTED_INDEX_REFERENCES, "actual": len(ids)})
        if len(set(ids)) != EXPECTED_INDEX_IDS:
            anomalies.append({"kind": "index_source_unique_id_count_mismatch",
                              "expected": EXPECTED_INDEX_IDS, "actual": len(set(ids))})
        page_labels = reader.page_labels
        mappings = {}
        for identifier in dict.fromkeys(ids):
            label = labels.get("src:" + identifier)
            context = "index src:" + identifier
            if not label or not label["destination"]:
                anomalies.append({"kind": "missing_index_aux_destination",
                                  "source_id": identifier})
                mappings[identifier] = {"source_id": identifier, "valid": False}
                continue
            result = checks.destination(label["destination"], context)
            entry = {"source_id": identifier, "aux_destination": label["destination"],
                     "aux_printed_page": label["printed_page"], **result}
            if result.get("valid"):
                actual_label = page_labels[result["physical_page"] - 1]
                entry["pdf_page_label"] = actual_label
                if re.fullmatch(r"(?:[0-9]+|[ivxlcdmIVXLCDM]+)", label["printed_page"]) and actual_label != label["printed_page"]:
                    anomalies.append({"kind": "index_aux_pdf_page_label_mismatch",
                                      "source_id": identifier,
                                      "aux_printed_page": label["printed_page"],
                                      "pdf_page_label": actual_label})
            mappings[identifier] = entry
        unique_destinations = {entry["aux_destination"] for entry in mappings.values()
                               if entry.get("valid")}
        if len(unique_destinations) != EXPECTED_INDEX_IDS:
            anomalies.append({"kind": "index_unique_pdf_destination_count_mismatch",
                              "expected": EXPECTED_INDEX_IDS, "actual": len(unique_destinations)})
        # Confirm the generated index actually contains the corresponding
        # annotation targets, not merely that the names exist somewhere.
        index_label = labels.get("chap:index")
        index_start = checks.destination(index_label["destination"], "index chapter") if index_label and index_label["destination"] else {"valid": False}
        annotation_targets = Counter()
        if not index_start.get("valid"):
            anomalies.append({"kind": "missing_index_chapter_destination"})
        else:
            annotation_targets.update(item["name"] for item in checks.internal_link_records
                                      if item["page"] >= index_start["physical_page"]
                                      and item.get("name") in unique_destinations)
            expected_targets = Counter(mappings[identifier].get("aux_destination") for identifier in ids)
            for name, count in expected_targets.items():
                if name and annotation_targets[name] < count:
                    anomalies.append({"kind": "missing_rendered_index_link_annotations",
                                      "destination": name, "expected_minimum": count,
                                      "actual": annotation_targets[name]})
        record["auxiliary_labels"] = {"files": aux_files, "label_count": len(labels)}
        record["index_navigation"] = {
            "expected_reference_count": EXPECTED_INDEX_REFERENCES,
            "source_reference_count": len(ids), "source_unique_id_count": len(set(ids)),
            "valid_unique_id_count": sum(entry["valid"] for entry in mappings.values()),
            "unique_pdf_destination_count": len(unique_destinations),
            "rendered_index_internal_link_count": sum(annotation_targets.values()),
            "index_start": index_start, "references_in_source_order": ids,
            "mappings": list(mappings.values()),
        }
        if before != (pdf.stat().st_size, pdf.stat().st_mtime_ns):
            anomalies.append({"kind": "pdf_changed_during_verification"})
        if record["aux_sha256"] != hashlib.sha256(aux.read_bytes()).hexdigest():
            anomalies.append({"kind": "aux_changed_during_verification"})
    except Exception as error:
        anomalies.append({"kind": "verification_exception",
                          "exception_type": type(error).__name__, "message": str(error)})
    finally:
        logger.removeHandler(handler)
    record["passed"] = not anomalies
    return record


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--aux", required=True, type=Path)
    parser.add_argument("--record", required=True, type=Path)
    args = parser.parse_args(argv)
    record = verify(args)
    args.record.parent.mkdir(parents=True, exist_ok=True)
    args.record.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
    summary = {key: record.get(key) for key in ("passed", "page_count", "pdf_sha256")}
    summary.update(record=str(args.record.resolve()),
                   anomaly_count=len(record["anomalies"]),
                   warning_count=len(record["warnings"]))
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if record["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
