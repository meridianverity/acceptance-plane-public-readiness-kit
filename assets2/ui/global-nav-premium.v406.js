/* MVG v404 — Enterprise nav restraint + Public Reviewer Bundle bridge.
   Proof Packet = executive action boundary
   Verify = local reproducibility
   Trust Center = institutional assurance
   Procurement = buyer checklist + artifacts
   Licensing = commercial/IP rail
   Resources = forwardable reviewer material
*/
(function(){
  const header = document.querySelector('[data-mvg-apple-nav]');
  if(!header) return;

  const protectedActionReview = '/contact/?route=protected-action-review#first-email';
  header.querySelectorAll('.mvg-contact-action').forEach((a)=>{
    a.setAttribute('href', protectedActionReview);
    a.setAttribute('aria-label', 'Start a 20-minute Protected Action Review');
    if ((a.textContent || '').trim().toLowerCase() === 'contact') a.textContent = 'Start Review';
  });
  header.querySelectorAll('.mvg-mobile-review').forEach((a)=>{
    a.setAttribute('href', protectedActionReview);
    a.setAttribute('aria-label', 'Start a 20-minute Protected Action Review');
    a.textContent = 'Start Review';
  });

  const normalizePath = (p) => (p || '/').replace(/\/index\.html$/,'/').replace(/\/+$/,'/') || '/';
  const path = normalizePath(window.location.pathname);
  const links = Array.from(header.querySelectorAll('[data-nav-path]'));

  const owners = [
    ['verify', [
      '/verify/',
      '/verify/haltseal/',
      '/verify/challenge/',
      '/verify-airgap-kit/',
      '/verify-assurance/',
      '/verify-diligence/',
      '/run-the-verifier/',
      '/run-verifier/',
      '/verifier-replay/',
      '/ai-agent-verification-receipts/'
    ]],
    ['trust', [
      '/trust-center/',
      '/trust/',
      '/trust-center/keys/',
      '/trust-center/witness-quorum/',
      '/trust/security-review/',
      '/trust/security-addendum/',
      '/trust/evidence/',
      '/security-review/'
    ]],
    ['procurement', [
      '/procurement/',
      '/ai-agent-procurement-checklist/',
      '/procurement/ticket-pack/',
      '/procurement/evidence-toolbox/',
      '/procurement/security/',
      '/procurement/audit/',
      '/procurement/legal/',
      '/no-silent-pass/',
      '/buyers/'
    ]],
    ['licensing', [
      '/licensing/',
      '/agentic-commerce-acceptance/',
      '/acceptance-boundary-api/',
      '/products/haltseal/',
      '/patents/',
      '/patents/orprg/',
      '/patents/novacov/',
      '/permit-receipts/effect-boundary-review/',
      '/acceptance-keyhole-devkit/'
    ]],
    ['resources', [
      '/reviewer-bundle/',
      '/technical-reports/',
      '/technical-reports/dual-gate-evidence-rails/',
      '/action-acceptance/',
      '/resources/',
      '/ai-acceptance-crosswalks/',
      '/resources/protected-action-receipt-profile/',
      '/resources/rfp-clause-protected-action-receipts/',
      '/resources/acceptance-plane-share-kit/',
      '/signals/',
      '/products/',
      '/controls/',
      '/why-now/',
      '/mission/',
      '/research/',
      '/press/',
      '/legal/',
      '/executive/',
      '/control-gap/',
      '/control-continuity/',
      '/hold-drill/',
      '/protected-action-register/'
    ]],
    ['review', [
      '/review/',
      '/review/protected-action/',
      '/execution-boundary/',
      '/instruction-promotion-gates/',
      '/instruction-promotion/',
      '/content-is-not-authority/',
      '/permit-receipts/',
      '/permit-receipt/',
      '/evidence-packs/',
      '/evidence-pack/',
      '/protected-actions/',
      '/approval-receipts/',
      '/proof-before-impact/',
      '/ai-agent-action-controls/'
    ]],
    ['search', ['/search/']],
    ['contact', ['/contact/']]
  ];

  let activeSection = '';
  for (const [section, prefixes] of owners){
    if(prefixes.some((p) => path === p || path.startsWith(p))){ activeSection = section; break; }
  }
  links.forEach((a) => {
    if(a.dataset.navPath === activeSection) a.setAttribute('aria-current','page');
    else a.removeAttribute('aria-current');
  });

  const panel = header.querySelector('[data-nav-panel]');
  const panelGrid = header.querySelector('[data-nav-panel-grid]');

  const panelData = {
    review: [
      {k:'Start here', t:'Protected Action Review', d:'Bring one AI action boundary. Map the public-safe proof path in 20 minutes.', c:'Start review', u:'/contact/?route=protected-action-review#first-email', feature:true, badges:['One action boundary','Public-safe first','20-minute review']},
      {k:'Public packet', t:'Proof Packet', d:'Build a public-safe action brief before private scope.', c:'Open packet', u:'/review/', links:[
        ['Learn the review','/review/protected-action/']
      ]},
      {k:'Boundary', t:'Execution Boundary', d:'Name where the proposed action becomes an external effect.', c:'Open boundary', u:'/execution-boundary/'},
      {k:'Evidence', t:'Evidence Packs', d:'Show what proof survived ACCEPT, HOLD, or REFUSE.', c:'Open packs', u:'/evidence-packs/'},
      {k:'Actions', t:'Protected Actions', d:'Know which AI actions require proof before impact.', c:'Open actions', u:'/protected-actions/'}
    ],
    verify: [
      {k:'Verify locally', t:'Local verification', d:'Inspect public evidence before private scope. No upload required.', c:'Verify locally', u:'/verify/', feature:true, badges:['No upload required','Public artifacts only','Browser-local review']},
      {k:'Replay route', t:'Run the Verifier', d:'Reproduce the public outcome in your browser.', c:'Run verifier', u:'/run-the-verifier/'},
      {k:'Gateway receipt', t:'Gateway proof receipt', d:'Inspect HALTSEAL proof for one gateway action.', c:'Open receipt', u:'/verify/haltseal/'},
      {k:'Offline review', t:'Offline verifier kit', d:'Review artifacts without uploads or network calls.', c:'Open offline kit', u:'/verify-airgap-kit/'},
      {k:'Challenge route', t:'Verifier challenge', d:'Test public fixtures before relying on the rail.', c:'Open challenge', u:'/verify/challenge/'}
    ],
    trust: [
      {k:'Trust Center', t:'Current public state', d:'Public posture, trust anchors, witness status, and reviewer routes.', c:'Open trust center', u:'/trust-center/', feature:true, badges:['Public posture','Trust anchors','Witness status']},
      {k:'Security review', t:'Security review kit', d:'Security controls, reviewer notes, and public artifact paths.', c:'Open security kit', u:'/trust/security-review/', links:[
        ['Security addendum','/trust/security-addendum/']
      ]},
      {k:'Trust anchors', t:'Public keys & anchors', d:'Inspect public anchors before relying on artifacts.', c:'Open anchors', u:'/trust-center/keys/'},
      {k:'Evidence request', t:'Evidence request route', d:'Ask for public-safe evidence before private scope.', c:'Request evidence', u:'/trust/evidence/'},
      {k:'Witness status', t:'Witness quorum', d:'Track independent replay and witnessed public state.', c:'Open witness status', u:'/trust-center/witness-quorum/'}
    ],
    procurement: [
      {k:'Buyer start', t:'AI agent procurement checklist', d:'Ask the right questions before AI agents act.', c:'Open checklist', u:'/ai-agent-procurement-checklist/', feature:true, badges:['Buyer checklist','Public-safe artifacts','Vendor-risk review']},
      {k:'Buyer route', t:'Procurement kit', d:'Attach public-safe proof before private scope.', c:'Open kit', u:'/procurement/'},
      {k:'Attachable proof', t:'Evidence packs', d:'Show the package that survived the decision.', c:'Open packs', u:'/evidence-packs/', links:[
        ['Ticket pack','/procurement/ticket-pack/'],
        ['Evidence toolbox','/procurement/evidence-toolbox/']
      ]},
      {k:'Buyer language', t:'No silent approval', d:'Missing proof is not approval.', c:'Open language kit', u:'/no-silent-pass/'},
      {k:'Security review', t:'Security review route', d:'Headers, CSP, release evidence, and reviewer pointers.', c:'Open security route', u:'/procurement/security/'}
    ],
    licensing: [
      {k:'Start here', t:'Agentic Commerce Acceptance', d:'Before agents move money, call tools, mutate APIs, release data, or trigger workflows: prove acceptance before impact.', c:'Open acceptance map', u:'/agentic-commerce-acceptance/', feature:true, badges:['Acceptance before impact','Gateway review','Written scope'], links:[
        ['Start partner review','/contact/?route=agentic-commerce-review#first-email'],
        ['Payment-agent gateway','/products/haltseal/payment-agent-gateway/'],
        ['ORPRG permit rail','/patents/orprg/']
      ]},
      {k:'Runtime control', t:'HALTSEAL Gateway Review', d:'Require current permit evidence before action. Identify the last gateway, first HOLD, proof receipt, and scope questions.', c:'Open gateway review', u:'/products/haltseal/gateway-review/', links:[
        ['HALTSEAL proof receipt','/verify/haltseal/']
      ]},
      {k:'Permit rail', t:'ORPRG Permit-Before-Commit', d:'For protected external effects: require current permit evidence before commit. Implementation and licensing stay under written scope.', c:'Open ORPRG brief', u:'/patents/orprg/', links:[
        ['Effect-boundary review','/permit-receipts/effect-boundary-review/']
      ]},
      {k:'Integration', t:'Acceptance Boundary API', d:'Boundary before action for gateways, meshes, API mutations, commit hooks, and protected workflows.', c:'Open API route', u:'/acceptance-boundary-api/', links:[
        ['Keyhole DevKit','/acceptance-keyhole-devkit/']
      ]},
      {k:'Diligence', t:'Patent record & scope', d:'Issued records and public briefs before NDA. Rights, field-of-use, and terms move under written diligence.', c:'Request diligence', u:'/licensing/request-diligence/', links:[
        ['Patent index','/patents/']
      ]}
    ],
    resources: [
      {k:'Resource hub', t:'Reviewer resources', d:'Crosswalks, clause language, receipt profiles, signals, and handoff material.', c:'Open resources', u:'/resources/', feature:true, badges:['Crosswalks','Clause language','Forwardable material'], links:[
        ['Reviewer bundle','/reviewer-bundle/'],
        ['Action acceptance','/action-acceptance/'],
        ['Replay console','/action-acceptance/replay/'],
        ['Conformance corpus','/action-acceptance/conformance/'],
        ['Technical reports','/technical-reports/dual-gate-evidence-rails/'],
        ['Receipt profile','/resources/protected-action-receipt-profile/'],
        ['RFP clause kit','/resources/rfp-clause-protected-action-receipts/'],
        ['Share kit','/resources/acceptance-plane-share-kit/']
      ]},
      {k:'Framework maps', t:'AI acceptance crosswalks', d:'Map NIST, ISO, OWASP, and MITRE to acceptance before impact.', c:'Open crosswalks', u:'/ai-acceptance-crosswalks/'},
      {k:'Architecture', t:'Proof architecture', d:'Boundary, gates, receipts, evidence packs, and verifier routes.', c:'Open architecture', u:'/resources/#proof-architecture'},
      {k:'Field notes', t:'Meridian Signals', d:'Field notes for serious reviewers.', c:'Open Signals', u:'/signals/', links:[
        ['Agentic payments','/signals/agentic-payments-need-proof-before-money-moves/']
      ]},
      {k:'RFP language', t:'RFP clause kit', d:'Copy buyer language for proof-before-impact receipts.', c:'Open clause kit', u:'/resources/rfp-clause-protected-action-receipts/'}
    ]
  };

  links.forEach((a) => {
    const section = a.dataset.navPath;
    if(panelData[section]){
      a.dataset.panelSection = section;
      a.setAttribute('aria-haspopup','true');
      a.setAttribute('aria-expanded','false');
    }
  });

  let closeTimer = null;
  let activeTrigger = null;

  function esc(value){
    return String(value == null ? '' : value).replace(/[&<>"']/g, (m) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
  }

  function renderPanelCard(item){
    const badges = Array.isArray(item.badges) && item.badges.length
      ? `<div class="mvg-panel-badge-row">${item.badges.map((b) => `<span class="mvg-panel-badge">${esc(b)}</span>`).join('')}</div>`
      : '';
    const miniLinks = item.links ? `<div class="mvg-panel-link-list">${item.links.map((l) => `<a class="mvg-panel-mini-link" href="${esc(l[1])}"><span>${esc(l[0])}</span><span aria-hidden="true">→</span></a>`).join('')}</div>` : '';
    return `
      <div class="mvg-panel-card${item.feature ? ' is-pa-feature' : ''}">
        <div class="mvg-panel-kicker">${esc(item.k)}</div>
        <strong class="mvg-panel-title">${esc(item.t)}</strong>
        <span class="mvg-panel-desc">${esc(item.d)}</span>
        ${badges}
        <div class="mvg-panel-action-stack">
          <a class="mvg-panel-cta" href="${esc(item.u)}">${esc(item.c)}<span aria-hidden="true">→</span></a>
          ${miniLinks}
        </div>
      </div>`;
  }

  function setTriggerExpanded(trigger, value){
    links.forEach((a) => { if(a.dataset.panelSection) a.setAttribute('aria-expanded','false'); });
    if(trigger) trigger.setAttribute('aria-expanded', value ? 'true' : 'false');
  }

  function openPanel(section, trigger){
    if(!panel || !panelGrid || !panelData[section] || window.matchMedia('(max-width: 980px)').matches) return;
    clearTimeout(closeTimer);
    activeTrigger = trigger || activeTrigger;
    panelGrid.innerHTML = panelData[section].map(renderPanelCard).join('');
    panel.dataset.section = section;
    panel.dataset.open = 'true';
    panel.setAttribute('aria-hidden','false');
    setTriggerExpanded(activeTrigger, true);
  }

  function closePanel(){
    if(!panel) return;
    panel.dataset.open='false';
    panel.setAttribute('aria-hidden','true');
    setTriggerExpanded(null, false);
    activeTrigger = null;
  }

  function scheduleClose(){
    clearTimeout(closeTimer);
    closeTimer = setTimeout(closePanel, 130);
  }

  header.querySelectorAll('[data-panel-section]').forEach((a) => {
    a.addEventListener('mouseenter', () => openPanel(a.dataset.panelSection, a));
    a.addEventListener('focus', () => openPanel(a.dataset.panelSection, a));
    a.addEventListener('mouseleave', scheduleClose);
  });
  if(panel){
    panel.addEventListener('mouseenter', () => clearTimeout(closeTimer));
    panel.addEventListener('mouseleave', scheduleClose);
  }

  const mobileGroups = [
    {title:'Proof Packet', promise:'What is this?', items:[
      ['Protected Action Review','one action boundary', protectedActionReview],
      ['Proof Packet','public-safe packet', '/review/'],
      ['Execution Boundary','map one boundary', '/execution-boundary/'],
      ['Evidence Packs','proof objects', '/evidence-packs/'],
      ['Protected Actions','action surfaces', '/protected-actions/']
    ]},
    {title:'Verify', promise:'Can I verify it?', items:[
      ['Local verification','no upload required', '/verify/'],
      ['Run the Verifier','browser replay', '/run-the-verifier/'],
      ['Gateway proof receipt','HALTSEAL receipt', '/verify/haltseal/'],
      ['Offline verifier kit','no network calls', '/verify-airgap-kit/'],
      ['Verifier challenge','test fixtures', '/verify/challenge/']
    ]},
    {title:'Trust Center', promise:'Can security trust it?', items:[
      ['Current public state','trust center', '/trust-center/'],
      ['Security review kit','reviewer notes', '/trust/security-review/'],
      ['Public keys & anchors','trust anchors', '/trust-center/keys/'],
      ['Evidence request route','public-safe ask', '/trust/evidence/'],
      ['Witness quorum','independent state', '/trust-center/witness-quorum/']
    ]},
    {title:'Procurement', promise:'Can buyers evaluate it?', items:[
      ['AI agent checklist','buyer start', '/ai-agent-procurement-checklist/'],
      ['Procurement kit','attach proof', '/procurement/'],
      ['Evidence packs','survived decision', '/evidence-packs/'],
      ['No silent approval','buyer language', '/no-silent-pass/'],
      ['Security review route','reviewer pointers', '/procurement/security/']
    ]},
    {title:'Licensing', promise:'Can we license or integrate?', items:[
      ['Agentic Commerce Acceptance','acceptance map', '/agentic-commerce-acceptance/'],
      ['HALTSEAL Gateway Review','runtime control', '/products/haltseal/gateway-review/'],
      ['ORPRG Permit-Before-Commit','permit rail', '/patents/orprg/'],
      ['Acceptance Boundary API','integration route', '/acceptance-boundary-api/'],
      ['Patent record & scope','diligence', '/licensing/request-diligence/']
    ]},
    {title:'Resources', promise:'Can I forward material?', items:[
      ['Reviewer bundle','public-safe handoff', '/reviewer-bundle/'],
      ['Action acceptance','attested action boundary', '/action-acceptance/'],
      ['Replay console','local fixtures', '/action-acceptance/replay/'],
      ['Conformance corpus','public vectors', '/action-acceptance/conformance/'],
      ['Technical reports','DOI-backed record', '/technical-reports/dual-gate-evidence-rails/'],
      ['Reviewer resources','handoff material', '/resources/'],
      ['AI acceptance crosswalks','framework maps', '/ai-acceptance-crosswalks/'],
      ['Meridian Signals','field notes', '/signals/'],
      ['RFP clause kit','buyer language', '/resources/rfp-clause-protected-action-receipts/']
    ]}
  ];

  function renderMobileGroup(group, index){
    const open = index === 0 ? ' open' : '';
    return `<details class="mvg-sheet-section"${open}>
      <summary><strong>${esc(group.title)}</strong><span>${esc(group.promise)}</span></summary>
      <div class="mvg-sheet-section-body">
        ${group.items.map((item) => `<a href="${esc(item[2])}"><span>${esc(item[0])}</span><small>${esc(item[1])}</small></a>`).join('')}
      </div>
    </details>`;
  }

  const mobileList = header.querySelector('.mvg-sheet-list');
  if(mobileList && !mobileList.dataset.v401Nav){
    mobileList.dataset.v401Nav = 'true';
    mobileList.innerHTML = `
      <a data-primary="true" href="${protectedActionReview}"><strong>Start Review</strong><span>Bring one action boundary</span></a>
      ${mobileGroups.map(renderMobileGroup).join('')}
      <a class="mvg-sheet-utility-link" href="/search/"><strong>Search</strong><span>Find exact public route</span></a>
      <button class="mvg-sheet-utility-link" data-theme-toggle-v161="" type="button"><strong>Appearance</strong><span data-theme-label="">Toggle light / dark</span></button>`;
  }

  const sheet = header.querySelector('[data-mobile-sheet]') || document.querySelector('[data-mobile-sheet]');
  // Move the mobile sheet out of the filtered/sticky header so position:fixed uses the viewport, not the nav bar.
  if(sheet && sheet.parentElement !== document.body){ document.body.appendChild(sheet); }
  const openBtn = header.querySelector('[data-mobile-menu-open]');
  const closeBtn = sheet ? sheet.querySelector('[data-mobile-menu-close]') : header.querySelector('[data-mobile-menu-close]');
  let lastFocus = null;
  function focusables(){ return sheet ? Array.from(sheet.querySelectorAll('a[href],button:not([disabled]),summary')) : []; }
  function openSheet(){
    if(!sheet) return;
    lastFocus = document.activeElement;
    sheet.hidden = false;
    openBtn && openBtn.setAttribute('aria-expanded','true');
    document.body.classList.add('mvg-nav-locked');
    const f = focusables();
    (f[0] || sheet).focus({preventScroll:true});
  }
  function closeSheet(){
    if(!sheet || sheet.hidden) return;
    sheet.hidden = true;
    openBtn && openBtn.setAttribute('aria-expanded','false');
    document.body.classList.remove('mvg-nav-locked');
    if(lastFocus && lastFocus.focus) lastFocus.focus({preventScroll:true});
  }
  openBtn && openBtn.addEventListener('click', openSheet);
  closeBtn && closeBtn.addEventListener('click', closeSheet);
  sheet && sheet.addEventListener('click', (ev) => { if(ev.target === sheet) closeSheet(); });
  sheet && sheet.addEventListener('keydown', (ev) => {
    if(ev.key !== 'Tab') return;
    const f = focusables();
    if(!f.length) return;
    const first = f[0], last = f[f.length - 1];
    if(ev.shiftKey && document.activeElement === first){ ev.preventDefault(); last.focus(); }
    else if(!ev.shiftKey && document.activeElement === last){ ev.preventDefault(); first.focus(); }
  });
  document.addEventListener('keydown', (ev) => {
    if(ev.key === 'Escape'){
      closePanel();
      closeSheet();
    }
  });

  window.MVGNavV404 = {openPanel, closePanel, panelData, mobileGroups};
  const params = new URLSearchParams(window.location.search || '');
  const forcedPanel = params.get('mvgNavPanel') || params.get('navPanel');
  if(forcedPanel && panelData[forcedPanel]) requestAnimationFrame(() => openPanel(forcedPanel));
})();
