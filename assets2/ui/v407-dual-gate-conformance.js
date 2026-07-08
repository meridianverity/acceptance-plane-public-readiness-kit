/* MVG V407 — Evidence Passport local controls */
(function(){
  const $=(s,r=document)=>r.querySelector(s); const $$=(s,r=document)=>Array.from(r.querySelectorAll(s));
  let toastEl; function toast(msg){if(!toastEl){toastEl=document.createElement('div');toastEl.className='mvg-v407-toast';document.body.appendChild(toastEl)}toastEl.textContent=msg;toastEl.classList.add('show');clearTimeout(toastEl._t);toastEl._t=setTimeout(()=>toastEl.classList.remove('show'),1700)}
  function copy(t,m){if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(()=>toast(m||'Copied')).catch(()=>fallback(t,m))}else fallback(t,m)}
  function fallback(t,m){const e=document.createElement('textarea');e.value=t;e.style.position='fixed';e.style.opacity='0';document.body.appendChild(e);e.select();try{document.execCommand('copy')}catch(_){}e.remove();toast(m||'Copied')}
  function download(name,text,type='text/markdown;charset=utf-8'){const b=new Blob([text],{type});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},200)}
  async function text(url){const r=await fetch(url,{cache:'no-store'}); if(!r.ok) throw new Error(url); return await r.text()}
  async function init(){const page=$('[data-v407-conformance]'); if(!page)return; let passport=''; try{passport=await text('/datasets/dual-gate-conformance-corpus/EVIDENCE_PASSPORT.md'); const p=$('[data-v407-passport]'); if(p)p.textContent=passport;}catch(e){passport=($('[data-v407-passport]')||{}).textContent||''}
    $$('[data-copy-passport]').forEach(b=>b.addEventListener('click',()=>copy(passport,'Evidence Passport copied')));
    $$('[data-download-passport]').forEach(b=>b.addEventListener('click',()=>download('MVG-DGER-CORPUS-2026-001_EVIDENCE_PASSPORT.md',passport)));
    $$('[data-copy-corpus-citation]').forEach(b=>b.addEventListener('click',()=>copy('Lee, Y. B. (2026). Dual-Gate Conformance Corpus for Attested Agentic AI. Meridian Verity Group. Public synthetic corpus supplement to DOI: 10.5281/zenodo.21244937.','Corpus citation copied')));
    $$('[data-copy-reviewer-note]').forEach(b=>b.addEventListener('click',()=>copy(['Subject: Meridian Verity / Dual-Gate Conformance Corpus','', 'I am forwarding a public synthetic conformance corpus for dual-gate action acceptance review.', '', 'This corpus contains 29 public synthetic vectors covering ACCEPT, HOLD, and FAIL. It includes reference DecisionReceipts, EvidencePacks, schemas, a conformance matrix, manifest, and SHA256 sums.', '', 'Boundary: no customer data, no secrets, no production credentials, no private vendor fields, no production authorization credential, and no patent license by publication.', '', 'Suggested review: inspect the Evidence Passport, run the public replay console, verify reference receipts, then route architecture-fit and written-scope diligence if implementation depth is needed.'].join('\n'),'Reviewer note copied')));
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init); else init();
})();
