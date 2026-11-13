
const q=document.getElementById('q');
const rows=[...document.querySelectorAll('.row')];
const chips=[...document.querySelectorAll('.chip[data-tier]')];
let tier='all';
function apply(){
  const s=(q.value||'').trim().toLowerCase();
  rows.forEach(r=>{
    const okT = tier==='all' || r.dataset.tier===tier;
    const okS = !s || (r.dataset.search||'').includes(s);
    r.style.display = (okT&&okS)?'':'none';
  });
  const n=rows.filter(r=>r.style.display!=='none').length;
  const c=document.getElementById('count'); if(c) c.textContent=n;
}
if(q) q.addEventListener('input',apply);
chips.forEach(ch=>ch.addEventListener('click',()=>{
  chips.forEach(x=>x.classList.remove('on')); ch.classList.add('on');
  tier=ch.dataset.tier; apply();
}));
apply();
