/* MVG V407 — Dual-Gate Replay Console. Browser-local public fixture replay. */
(function(){
  const FIXTURE_INDEX='/assets2/fixtures/dual-gate-replay/v407/index.json';
  const $=(s,r=document)=>r.querySelector(s); const $$=(s,r=document)=>Array.from(r.querySelectorAll(s));
  let fixtures=[], active=null, toastEl;
  function toast(msg){ if(!toastEl){toastEl=document.createElement('div');toastEl.className='mvg-replay-toast';document.body.appendChild(toastEl)} toastEl.textContent=msg;toastEl.classList.add('show');clearTimeout(toastEl._t);toastEl._t=setTimeout(()=>toastEl.classList.remove('show'),1700); }
  function canonicalize(value){
    if(value===null || typeof value!=='object') return JSON.stringify(value);
    if(Array.isArray(value)) return '['+value.map(canonicalize).join(',')+']';
    return '{'+Object.keys(value).sort().map(k=>JSON.stringify(k)+':'+canonicalize(value[k])).join(',')+'}';
  }
  function sha256Fallback(ascii){
    function rightRotate(value, amount){ return (value>>>amount) | (value<<(32-amount)); }
    let mathPow=Math.pow, maxWord=mathPow(2,32), result='', words=[], i, j;
    let asciiBitLength=ascii.length*8;
    let h=[], k=[], primeCounter=0;
    function isPrime(n){ for(let f=2; f*f<=n; f++) if(n%f===0) return false; return true; }
    for(let candidate=2; primeCounter<64; candidate++) if(isPrime(candidate)){ if(primeCounter<8) h[primeCounter]=(mathPow(candidate,.5)*maxWord)|0; k[primeCounter]=(mathPow(candidate,1/3)*maxWord)|0; primeCounter++; }
    ascii += '\x80';
    while(ascii.length%64-56) ascii += '\x00';
    for(i=0;i<ascii.length;i++){ j=ascii.charCodeAt(i); words[i>>2] |= j << ((3-i)%4)*8; }
    words[words.length]=((asciiBitLength/maxWord)|0); words[words.length]=(asciiBitLength|0);
    for(j=0;j<words.length;){
      let w=words.slice(j,j+=16), a=h[0], b=h[1], c=h[2], d=h[3], e=h[4], f=h[5], g=h[6], hh=h[7];
      for(i=0;i<64;i++){
        let w15=w[i-15], w2=w[i-2];
        let word=i<16 ? w[i] : (w[i]=(w[i-16] + (rightRotate(w15,7)^rightRotate(w15,18)^(w15>>>3)) + w[i-7] + (rightRotate(w2,17)^rightRotate(w2,19)^(w2>>>10)))|0);
        let t1=(hh + (rightRotate(e,6)^rightRotate(e,11)^rightRotate(e,25)) + ((e&f)^((~e)&g)) + k[i] + word)|0;
        let t2=((rightRotate(a,2)^rightRotate(a,13)^rightRotate(a,22)) + ((a&b)^(a&c)^(b&c)))|0;
        hh=g; g=f; f=e; e=(d+t1)|0; d=c; c=b; b=a; a=(t1+t2)|0;
      }
      h[0]=(h[0]+a)|0; h[1]=(h[1]+b)|0; h[2]=(h[2]+c)|0; h[3]=(h[3]+d)|0; h[4]=(h[4]+e)|0; h[5]=(h[5]+f)|0; h[6]=(h[6]+g)|0; h[7]=(h[7]+hh)|0;
    }
    for(i=0;i<h.length;i++){ for(j=3;j+1;j--){ let b=(h[i]>>(j*8))&255; result += ((b<16)?'0':'')+b.toString(16); } }
    return 'sha256:'+result;
  }
  async function sha256(text){ if(window.crypto && crypto.subtle && window.TextEncoder){ const data=new TextEncoder().encode(text); const hash=await crypto.subtle.digest('SHA-256',data); return 'sha256:'+Array.from(new Uint8Array(hash)).map(b=>b.toString(16).padStart(2,'0')).join(''); } return sha256Fallback(unescape(encodeURIComponent(text))); }
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));}
  function pretty(o){return JSON.stringify(o,null,2);}
  function copy(text,msg){ if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(()=>toast(msg||'Copied')).catch(()=>fallback(text,msg));} else fallback(text,msg); }
  function fallback(text,msg){const t=document.createElement('textarea');t.value=text;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();try{document.execCommand('copy')}catch(e){}t.remove();toast(msg||'Copied');}
  function download(name,text,type='application/json;charset=utf-8'){const b=new Blob([text],{type});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},200);}
  function reviewerNote(f){return [
    'Subject: Meridian Verity / Public Dual-Gate Replay Receipt', '',
    'I am forwarding a public replay fixture for one dual-gate action acceptance decision.', '',
    'Fixture: '+f.title, 'Decision: '+f.decision, 'Reason: '+f.reason_code, '',
    'This public replay uses synthetic fixtures only. It contains no customer data, no secrets, no production credentials, no vendor-private fields, and no production authorization credential.', '',
    'What to inspect:', '1. Gate 0 denies before inference when required request evidence is missing or invalid.', '2. Gate 1 permits before commit only when the proposed external effect is fresh, scoped, unreplayed, and policy-bound.', '3. The DecisionReceipt binds action_digest, policy_digest, nonce, epoch, reason code, and evidence reference.', '4. The EvidencePack is exportable for reviewer inspection.', '',
    'Suggested next step:', 'Route to the technical owner for artifact/profile fit, freshness/challenge semantics, action-digest binding, controlled effect handoff, final decision placement, and written-scope implementation depth.', '',
    'Public replay console: https://meridianverity.com/action-acceptance/replay/'
  ].join('\n');}
  function cls(dec){return dec.toLowerCase()==='accept'?'accept':dec.toLowerCase()==='hold'?'hold':'fail'}
  async function verifyFixture(f){
    const actionDigest=await sha256(canonicalize(f.action_proposal));
    const policyDigest=await sha256(canonicalize(f.policy_profile));
    const receiptDigest=await sha256(canonicalize(f.gate_decision.decision_receipt));
    const packDigest=await sha256(canonicalize(f.evidence_pack));
    return {actionDigest, policyDigest, receiptDigest, packDigest, ok: actionDigest===f.expected.action_digest && policyDigest===f.expected.policy_digest && receiptDigest===f.expected.receipt_digest && packDigest===f.expected.evidence_pack_digest};
  }
  function renderList(index){const wrap=$('[data-replay-fixtures]'); if(!wrap)return; wrap.innerHTML=index.fixtures.map((f,i)=>`<button class="mvg-replay-fixture" type="button" data-fixture-index="${i}" aria-selected="${i===0?'true':'false'}"><strong>${esc(f.title)}</strong><span>${esc(f.summary)}</span><i class="mvg-replay-pill ${cls(f.decision)}">${esc(f.decision)}</i></button>`).join('');}
  function renderChecks(f,calc){const status=calc.ok?'pass':'fail'; const synthetic={label:'Fixture consistency',status,detail:calc.ok?'Local digest recomputation matches the expected public fixture digests.':'One or more public fixture digests did not match.'}; const checks=[synthetic].concat(f.checks||[]); return checks.map(c=>`<div class="mvg-replay-check" data-status="${esc(c.status)}"><em>${esc(c.status)}</em><div><strong>${esc(c.label)}</strong><span>${esc(c.detail)}</span></div></div>`).join('');}
  function renderTimeline(f){const steps=f.timeline||[];return steps.map((s,i)=>`<article class="mvg-replay-step ${i===1||i===4?'gate':''}"><em>${i===1?'Gate 0':i===4?'Gate 1':'0'+(i+1)}</em><strong>${esc(s.step)}</strong><span>${esc(s.detail)}</span></article>`).join('');}
  function renderArtifacts(){const arr=[['ActionProposal','Exact proposed effect'],['VerifierPosture','Evidence posture input'],['PolicyProfile','Active policy boundary'],['GateDecision','ACCEPT / HOLD / FAIL'],['DecisionReceipt','Machine-verifiable record'],['EvidencePack','Exportable review basis']]; return arr.map(a=>`<article class="mvg-replay-artifact"><strong>${a[0]}</strong><span>${a[1]}</span></article>`).join('');}
  async function loadFixture(ref){ if(typeof ref==='number') return fixtures[ref]; if(ref && typeof ref==='object') return ref; const res=await fetch(ref,{cache:'no-store'}); if(!res.ok) throw new Error('Fixture fetch failed'); return await res.json();}
  async function show(ref){ try{ const f=await loadFixture(ref); active=f; const calc=await verifyFixture(f); const sel=String(typeof ref==='number'?ref:fixtures.indexOf(f)); $$('[data-fixture-index]').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.fixtureIndex===sel))); $('[data-replay-title]').textContent=f.title; $('[data-replay-decision]').textContent=f.decision; $('[data-replay-decision]').className='mvg-replay-decision '+cls(f.decision); $('[data-replay-summary]').textContent=f.summary; $('[data-replay-reason]').textContent=f.reason_code; $('[data-replay-action-digest]').textContent=calc.actionDigest; $('[data-replay-policy-digest]').textContent=calc.policyDigest; $('[data-replay-receipt-digest]').textContent=calc.receiptDigest; $('[data-replay-pack-digest]').textContent=calc.packDigest; $('[data-replay-checks]').innerHTML=renderChecks(f,calc); $('[data-replay-timeline]').innerHTML=renderTimeline(f); $('[data-replay-artifacts]').innerHTML=renderArtifacts(); $('[data-replay-receipt]').textContent=pretty(f.gate_decision.decision_receipt); $('[data-replay-pack]').textContent=pretty(f.evidence_pack); $('[data-replay-proof]').textContent=calc.ok?'Public replay verified locally.':'Fixture digest mismatch. Do not rely on this fixture until reviewed.';
      const corpus=f.corpus||{};
      const set=(sel,val)=>{const el=$(sel); if(el) el.textContent=val||'—'};
      set('[data-replay-corpus-vector]', corpus.vector_id || f.vector_id || f.id);
      set('[data-replay-corpus-id]', corpus.id || 'MVG-DGER-CORPUS-2026-001');
      set('[data-replay-corpus-decision]', f.decision);
      set('[data-replay-corpus-receipt]', calc.receiptDigest);
      set('[data-replay-corpus-pack]', calc.packDigest);
      $$('[data-open-corpus-vector]').forEach(a=>{a.href='/datasets/dual-gate-conformance-corpus/#'+encodeURIComponent(f.id||'vector');});
      $$('[data-open-corpus-pack]').forEach(a=>{a.href='/datasets/dual-gate-conformance-corpus/MVG-DGER-CORPUS-2026-001_v1.0.0_PUBLIC_SYNTHETIC.zip';});
      $$('[data-copy-passport-line]').forEach(b=>b.onclick=()=>copy('Vector '+(corpus.vector_id||f.id)+' / '+f.decision+' / '+f.reason_code+' / receipt '+calc.receiptDigest+' / EvidencePack '+calc.packDigest, 'Passport line copied')); } catch(e){ console.error(e); toast('Fixture could not load'); } }
  async function init(){ const host=$('[data-v407-replay-console]') || $('[data-v406-replay-console]'); if(!host)return; try{const idx=await (await fetch(FIXTURE_INDEX,{cache:'no-store'})).json(); fixtures=idx.fixtures||[]; renderList(idx); $('[data-replay-fixtures]').addEventListener('click',e=>{const b=e.target.closest('[data-fixture-index]'); if(b) show(Number(b.dataset.fixtureIndex));}); if(fixtures[0]) show(0); } catch(e){ console.error(e); $('[data-replay-proof]').textContent='Static fixture index is unavailable. The page remains a public-safe explanation surface.'; }
    $$('[data-copy-receipt]').forEach(b=>b.addEventListener('click',()=>active&&copy(pretty(active.gate_decision.decision_receipt),'Receipt copied')));
    $$('[data-copy-note]').forEach(b=>b.addEventListener('click',()=>active&&copy(reviewerNote(active),'Reviewer note copied')));
    $$('[data-download-receipt]').forEach(b=>b.addEventListener('click',()=>active&&download(active.id+'-DecisionReceipt.json',pretty(active.gate_decision.decision_receipt))));
    $$('[data-download-pack]').forEach(b=>b.addEventListener('click',()=>active&&download(active.id+'-EvidencePack.json',pretty(active.evidence_pack))));
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init); else init();
})();
