/* Public readiness demo only. No network calls. */
const sample = {
  assessment_id: "browser-demo-sample",
  organization_context: "public workshop sample",
  responses: [
    { item_id: "ARI-01-01", status: "YES" },
    { item_id: "ARI-01-02", status: "PARTIAL" },
    { item_id: "ARI-02-01", status: "PARTIAL" },
    { item_id: "ARI-03-01", status: "NO" },
    { item_id: "ARI-04-01", status: "UNKNOWN" }
  ],
  boundary: "public browser demo only; not certification, compliance approval, production readiness, procurement approval, or an allow/deny decision"
};
function score(status){ return status === "YES" ? 2 : status === "PARTIAL" ? 1 : 0; }
function run(){
  let data;
  try { data = JSON.parse(document.getElementById('input').value); } catch(e){ document.getElementById('output').textContent = 'Invalid JSON: '+e.message; return; }
  const responses = Array.isArray(data.responses) ? data.responses : [];
  const earned = responses.reduce((a,r)=>a+score(String(r.status||'').toUpperCase()),0);
  const max = Math.max(responses.length*2,2);
  const maturity = Math.round(earned/max*100);
  const posture = maturity >= 80 ? 'DISCUSSION_READY_FOR_CONFORMANCE_HANDOFF' : maturity >= 60 ? 'HOLD_FOR_IMPLEMENTATION_REVIEW' : 'FOUNDATIONAL_DISCUSSION_NEEDED';
  const report = { report_type:'browser public readiness discussion report', posture, discussion_maturity:maturity, responses:responses.length, network_used:'no', boundary:'not certification, compliance approval, production readiness, procurement approval, evidence verification, or an allow/deny decision' };
  document.getElementById('output').textContent = JSON.stringify(report,null,2);
}
document.getElementById('sample').onclick = () => { document.getElementById('input').value = JSON.stringify(sample,null,2); };
document.getElementById('run').onclick = run;
document.getElementById('sample').click();
