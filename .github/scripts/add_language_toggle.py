from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

if '/* bilingual language switcher */' in s:
    raise SystemExit('Language switcher already present')

css = """

  /* -------------------- LANGUAGE TOGGLE -------------------- */
  .lang-toggle{
    display:inline-flex;align-items:center;justify-content:center;
    min-width:46px;height:40px;padding:0 12px;
    border:1px solid rgba(246,244,241,0.48);
    color:var(--offwhite);
    font-family:'IBM Plex Sans',sans-serif;
    font-size:0.82rem;font-weight:600;letter-spacing:0.10em;
    border-radius:2px;
    transition:color .2s ease,border-color .2s ease,background-color .2s ease;
  }
  .lang-toggle:hover{color:var(--gold);border-color:var(--gold);background:rgba(224,162,27,0.06);}
  .lang-toggle:focus-visible{outline:2px solid var(--gold);outline-offset:3px;}
  header.scrolled .lang-toggle{color:var(--ink);border-color:rgba(30,33,18,0.28);}
  header.scrolled .lang-toggle:hover{color:var(--gold-dark);border-color:var(--gold-dark);}
  @media (max-width:760px){
    .nav-links-wrap .lang-toggle{
      color:var(--offwhite)!important;border-color:rgba(246,244,241,0.42)!important;
      align-self:flex-start;min-width:54px;height:44px;
    }
  }
"""
s = s.replace('</style>', css + '\n</style>', 1)

js = r'''

  /* bilingual language switcher */
  (() => {
    const translations = [
      ['nav.primary-nav a[href="#servicios"]', 'Services'],
      ['nav.primary-nav a[href="#enfoque"]', 'Our Approach'],
      ['nav.primary-nav a[href="#contacto"]', 'Contact'],
      ['.nav-links-wrap > .nav-cta', 'Discuss a Project'],
      ['.hero-content .kicker', 'ENERGY · INDUSTRY · INFRASTRUCTURE'],
      ['.hero-content h1', 'Technical capability to deliver.'],
      ['.hero-content p', 'Tres Puntos develops and executes solutions for energy, industrial and infrastructure operations and projects across Venezuela, combining field experience, rapid response and technology-enabled project control.'],
      ['.hero-actions .btn-primary', 'Explore Services →'],
      ['.hero-actions .btn-outline', 'Discuss a Project'],
      ['.hero-caption .kicker', 'ENERGY · VENEZUELA'],
      ['.hero-caption p', 'Local experience. Disciplined execution.'],
      ['.servicios .section-head .kicker', 'OUR CAPABILITIES'],
      ['.servicios .section-head h2', 'Solutions for energy, industry and infrastructure.'],
      ['.service-card:nth-child(1) h3', 'Specialized Oil & Gas Services'],
      ['.service-card:nth-child(1) .service-body p', 'Well testing, pumping, maintenance and operational support services for production and intervention activities.'],
      ['.service-card:nth-child(2) h3', 'Infrastructure & Construction'],
      ['.service-card:nth-child(2) .service-body p', 'Construction, rehabilitation, upgrades and installation of industrial infrastructure and facilities.'],
      ['.service-card:nth-child(3) h3', 'Operational Support'],
      ['.service-card:nth-child(3) .service-body p', 'Procurement, transportation, mobilization, and supply of equipment and materials tailored to each project’s needs.'],
      ['.enfoque .section-head .kicker', 'OUR APPROACH'],
      ['.enfoque .section-head h2', 'Strong execution requires visibility.'],
      ['.enfoque .section-head p', 'At Tres Puntos, we combine field experience with digital tracking tools that keep progress, resources, milestones and critical decisions visible and up to date. This allows us to anticipate deviations, respond faster and keep every project under control.'],
      ['.diferenciadores .section-head .kicker', 'HOW WE CREATE VALUE'],
      ['.diferenciadores .section-head h2', 'Field presence. Decision-ready information. The ability to respond.'],
      ['.diff-item:nth-child(1) h3', 'Technical judgment'],
      ['.diff-item:nth-child(1) p', 'We understand operational realities and turn each requirement into an executable solution.'],
      ['.diff-item:nth-child(2) h3', 'Agile response'],
      ['.diff-item:nth-child(2) p', 'We make decisions close to the operation and move quickly as conditions change.'],
      ['.diff-item:nth-child(3) h3', 'Technology & data'],
      ['.diff-item:nth-child(3) p', 'We use digital tools to track progress, centralize information and improve project visibility.'],
      ['.diff-item:nth-child(4) h3', 'Execution control'],
      ['.diff-item:nth-child(4) p', 'We track milestones, resources, costs and critical variables to keep each project aligned with its objectives.'],
      ['.cierre-main .kicker', 'BUSINESS DEVELOPMENT'],
      ['.cierre-main h2', 'Let’s talk about your next project.'],
      ['.cierre-main p', 'Tell us what you need to solve. We can structure a technical and operational solution and take it through execution.'],
      ['.cierre-main .btn-primary', 'Talk to Tres Puntos →'],
      ['.cierre-info', 'Tres Puntos C.A.\nCaracas, Venezuela\nNationwide deployment capability'],
      ['.footer-tagline', 'Energy · Industry · Infrastructure']
    ];
    const altTranslations = [
      ['.hero-media img', 'Coastal refinery and industrial facilities overlooking the sea.'],
      ['.service-card:nth-child(1) img', 'Oilfield pumpjacks at sunset.'],
      ['.service-card:nth-child(2) img', 'Industrial construction site with concrete structures, formwork and tower crane.'],
      ['.service-card:nth-child(3) img', 'Technical team overseeing heavy-equipment mobilization at an industrial port.'],
      ['.enfoque .bg-img img', 'Industrial plant illuminated at night.'],
      ['.cierre-media img', 'Coastal refinery complex surrounded by vegetation.']
    ];
    const originals = new Map();
    translations.forEach(([selector]) => { const el=document.querySelector(selector); if(el) originals.set(selector,el.textContent); });
    const originalAlts = new Map();
    altTranslations.forEach(([selector]) => { const el=document.querySelector(selector); if(el) originalAlts.set(selector,el.getAttribute('alt')||''); });
    const originalTitle=document.title;
    const brand=document.querySelector('.brand');
    const menuButton=document.getElementById('menuToggle');
    const originalBrandLabel=brand?.getAttribute('aria-label')||'';
    const originalMenuLabel=menuButton?.getAttribute('aria-label')||'';
    const langButton=document.createElement('button');
    langButton.type='button'; langButton.className='lang-toggle'; langButton.textContent='EN';
    langButton.setAttribute('aria-label','Switch to English');
    const navWrap=document.getElementById('navLinks');
    const navCta=navWrap?.querySelector('.nav-cta');
    if(navWrap) navWrap.insertBefore(langButton,navCta||null);
    function applyLanguage(lang){
      const english=lang==='en';
      document.documentElement.lang=english?'en':'es';
      document.title=english?'Tres Puntos C.A. — Energy · Industry · Infrastructure':originalTitle;
      translations.forEach(([selector,enText])=>{ const el=document.querySelector(selector); if(el) el.textContent=english?enText:(originals.get(selector)||''); });
      altTranslations.forEach(([selector,enAlt])=>{ const el=document.querySelector(selector); if(el) el.setAttribute('alt',english?enAlt:(originalAlts.get(selector)||'')); });
      if(brand) brand.setAttribute('aria-label',english?'Tres Puntos, home':originalBrandLabel);
      if(menuButton) menuButton.setAttribute('aria-label',english?'Open menu':originalMenuLabel);
      langButton.textContent=english?'ES':'EN';
      langButton.setAttribute('aria-label',english?'Cambiar a español':'Switch to English');
      langButton.title=english?'Español':'English';
      localStorage.setItem('tp-lang',english?'en':'es');
    }
    langButton.addEventListener('click',()=>applyLanguage(document.documentElement.lang==='en'?'es':'en'));
    applyLanguage(localStorage.getItem('tp-lang')==='en'?'en':'es');
  })();
'''
s = s.replace('</script>', js + '\n</script>', 1)
p.write_text(s, encoding='utf-8')
