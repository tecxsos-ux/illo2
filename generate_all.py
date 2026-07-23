import json

catalog = json.load(open('ilo-webapp/catalog.json'))

products_map = {}
for p in catalog:
    products_map[p['slug'].lower()] = {
        'en': p['name']['en'],
        'de': p['name']['de'],
        'fr': p['name']['fr'],
        'eur': p['priceEur'],
        'chf': p['priceChf'],
        'catLabels': p['catLabels']
    }

json_products = json.dumps(products_map, indent=2)

js_content = f"""(function() {{
  const PRODUCTS = {json_products};

  const TRANSLATIONS = {{
    en: {{
      shippingEur: "Free EU shipping over € 49.00 · Factory-direct from Hong Kong",
      shippingChf: "Free shipping over CHF 49.00 · Factory-direct from Hong Kong",
      navShop: "Shop",
      navAbout: "About",
      navWholesale: "Wholesale",
      heroBadge: "Factory-direct from Hong Kong since 1986",
      heroTitle: "Colorful organisation, made in Hong Kong.",
      heroSubtitle: "Bags, pouches and organisers in every colour of the workday — designed, cut and sewn in our own factory, shipped direct to Switzerland & Europe.",
      heroCtaPrimary: "Shop the collection",
      heroCtaSecondary: "Wholesale",
      catTitle: "Shop by category",
      catSubtitle: "Eight families of organisers, one factory.",
      viewAll: "View all products →",
      bestTitle: "Best sellers",
      bestSubtitle: "The colours Europe keeps reordering.",
      addToCart: "+ Add to cart",
      storyTitle: "Factory-direct since 1986",
      storySubtitle: "EASYMATE began on a Hong Kong factory floor nearly four decades ago. Today the ilo line brings the same colourful, hard-working organisers straight from our sewing lines to your door — no middlemen, no markups.",
      storyCta: "Read our story",
      footerTagline: "Colorful bags & pouches, factory-direct from Hong Kong since 1986.",
      footerAccept: "We accept",
      footerShips: "Ships from Hong Kong · EU VAT & duties calculated at checkout · 14-day returns (EU)",
      shopTitle: "The collection",
      shopSubtitle: "All 48 organisers, direct from the factory floor.",
      catAll: "All",
      sortLabel: "Sort",
      sortFeatured: "Featured",
      sortLow: "Price: low to high",
      sortHigh: "Price: high to low",
      sortName: "Name A–Z",
      langLabel: "Language",
      currLabel: "Currency"
    }},
    de: {{
      shippingEur: "Kostenloser Versand in die EU ab € 49.00 · Direkt ab Hongkonger Manufaktur",
      shippingChf: "Kostenloser Versand ab CHF 49.00 · Direkt ab Hongkonger Manufaktur",
      navShop: "Shop",
      navAbout: "Über uns",
      navWholesale: "Grosshandel",
      heroBadge: "Direkt ab Hongkonger Manufaktur seit 1986",
      heroTitle: "Farbenfrohe Ordnung, hergestellt in Hongkong.",
      heroSubtitle: "Taschen, Etuis und Organizer in allen Farben des Arbeitstages – in unserer eigenen Manufaktur entworfen, zugeschnitten und genäht, direkt in die Schweiz & EU geliefert.",
      heroCtaPrimary: "Kollektion entdecken",
      heroCtaSecondary: "Grosshandel",
      catTitle: "Kategorien",
      catSubtitle: "Acht Familien von Organizern, eine Manufaktur.",
      viewAll: "Alle Produkte ansehen →",
      bestTitle: "Bestseller",
      bestSubtitle: "Die Farben, die Europa immer wieder nachbestellt.",
      addToCart: "+ In den Warenkorb",
      storyTitle: "Direkt ab Fabrik seit 1986",
      storySubtitle: "EASYMATE begann vor fast vier Jahrzehnten in einer Manufaktur in Hongkong. Heute bringt die ilo-Linie dieselben farbenfrohen, robusten Organizer direkt von den Nähstrassen zu Ihnen – ohne Zwischenhändler.",
      storyCta: "Unsere Geschichte",
      footerTagline: "Farbenfrohe Taschen & Etuis, direkt ab Hongkonger Manufaktur seit 1986.",
      footerAccept: "Wir akzeptieren",
      footerShips: "Versand aus Hongkong · EU-MwSt. & Zölle an der Kasse berechnet · 14 Tage Rückgabe (EU)",
      shopTitle: "Die Kollektion",
      shopSubtitle: "Alle 48 Organizer, direkt aus der Manufaktur.",
      catAll: "Alle",
      sortLabel: "Sortierung",
      sortFeatured: "Empfohlen",
      sortLow: "Preis: aufsteigend",
      sortHigh: "Preis: absteigend",
      sortName: "Name A–Z",
      langLabel: "Sprache",
      currLabel: "Währung"
    }},
    fr: {{
      shippingEur: "Livraison UE offerte dès € 49.00 · Direct d'usine à Hong Kong",
      shippingChf: "Livraison offerte dès CHF 49.00 · Direct d'usine à Hong Kong",
      navShop: "Boutique",
      navAbout: "À propos",
      navWholesale: "Vente en gros",
      heroBadge: "Direct d'usine à Hong Kong depuis 1986",
      heroTitle: "Une organisation colorée, fabriquée à Hong Kong.",
      heroSubtitle: "Sacs, pochettes et organiseurs dans toutes les couleurs du quotidien — conçus, découpés et cousus dans notre propre usine, expédiés en Suisse & Europe.",
      heroCtaPrimary: "Découvrir la collection",
      heroCtaSecondary: "Vente en gros",
      catTitle: "Magasiner par catégorie",
      catSubtitle: "Huit familles d'organiseurs, une seule usine.",
      viewAll: "Voir tous les produits →",
      bestTitle: "Meilleures ventes",
      bestSubtitle: "Les couleurs que l'Europe réassortit en boucle.",
      addToCart: "+ Ajouter au panier",
      storyTitle: "Direct d'usine depuis 1986",
      storySubtitle: "EASYMATE a commencé sur le parquet d'une usine de Hong Kong il y a près de quatre décennies. Aujourd'hui, la gamme ilo apporte ces mêmes organiseurs colorés directement de nos lignes de couture.",
      storyCta: "Notre histoire",
      footerTagline: "Sacs & pochettes colorés, direct d'usine à Hong Kong depuis 1986.",
      footerAccept: "Nous acceptons",
      footerShips: "Expédié depuis Hong Kong · TVA et droits UE calculés à la caisse · Retours 14 jours (UE)",
      shopTitle: "La collection",
      shopSubtitle: "Les 48 organiseurs, directement sorties d'usine.",
      catAll: "Tous",
      sortLabel: "Trier par",
      sortFeatured: "En vedette",
      sortLow: "Prix : croissant",
      sortHigh: "Prix : décroissant",
      sortName: "Nom A–Z",
      langLabel: "Langue",
      currLabel: "Devise"
    }}
  }};

  function getLang() {{
    return localStorage.getItem('ilo_lang') || 'en';
  }}

  function getCurrency() {{
    return localStorage.getItem('ilo_currency') || 'EUR';
  }}

  function setLang(lang) {{
    localStorage.setItem('ilo_lang', lang);
    applyState();
  }}

  function setCurrency(curr) {{
    localStorage.setItem('ilo_currency', curr);
    applyState();
  }}

  function formatPrice(eur, chf, curr) {{
    if (curr === 'CHF') {{
      return 'CHF ' + (chf || eur).toFixed(2);
    }}
    return '€ ' + (eur).toFixed(2);
  }}

  function applyState() {{
    const lang = getLang();
    const curr = getCurrency();
    const t = TRANSLATIONS[lang] || TRANSLATIONS.en;
    const langIdx = lang === 'de' ? 1 : (lang === 'fr' ? 2 : 0);

    // 1. Language buttons UI
    document.querySelectorAll('[aria-label="Language"] button').forEach(btn => {{
      const bLang = btn.textContent.trim().toLowerCase();
      const isActive = bLang === lang;
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      btn.className = isActive
        ? 'rounded-full px-2.5 py-1 text-xs font-semibold uppercase transition-colors bg-ink text-cream'
        : 'rounded-full px-2.5 py-1 text-xs font-semibold uppercase transition-colors text-muted hover:text-ink';
    }});

    // 2. Currency buttons UI
    document.querySelectorAll('[aria-label="Currency"] button').forEach(btn => {{
      const bText = btn.textContent.trim();
      const isEur = bText === '€' || bText === 'EUR';
      const isActive = (isEur && curr === 'EUR') || (!isEur && curr === 'CHF');
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      btn.className = isActive
        ? 'rounded-full px-2.5 py-1 text-xs font-semibold transition-colors bg-ink text-cream'
        : 'rounded-full px-2.5 py-1 text-xs font-semibold transition-colors text-muted hover:text-ink';
    }});

    // 3. Update shipping header text
    const shipText = document.querySelector('header .bg-ink p');
    if (shipText) {{
      shipText.textContent = curr === 'CHF' ? t.shippingChf : t.shippingEur;
    }}

    // 4. Update Nav links text (header + mobile drawer)
    const navLinks = document.querySelectorAll('header nav[aria-label="Main"] ul li a');
    if (navLinks.length >= 3) {{
      if (navLinks[0]) navLinks[0].textContent = t.navShop;
      if (navLinks[1]) navLinks[1].textContent = t.navAbout;
      if (navLinks[2]) navLinks[2].textContent = t.navWholesale;
    }}

    const drawerNavLinks = document.querySelectorAll('#mobile-menu-drawer .mobile-nav-link');
    if (drawerNavLinks.length >= 3) {{
      drawerNavLinks[0].textContent = t.navShop;
      drawerNavLinks[1].textContent = t.navAbout;
      drawerNavLinks[2].textContent = t.navWholesale;
    }}

    const drawerLangLabel = document.querySelector('#mobile-menu-drawer .mobile-lang-label');
    if (drawerLangLabel) drawerLangLabel.textContent = t.langLabel;

    const drawerCurrLabel = document.querySelector('#mobile-menu-drawer .mobile-curr-label');
    if (drawerCurrLabel) drawerCurrLabel.textContent = t.currLabel;

    // 5. Update Add to cart buttons
    document.querySelectorAll('button').forEach(btn => {{
      const txt = btn.textContent;
      if (txt.includes('Add to cart') || txt.includes('In den Warenkorb') || txt.includes('Ajouter au panier')) {{
        btn.textContent = t.addToCart;
      }}
    }});

    // 6. Update Product Cards (Titles, Category labels, Prices)
    document.querySelectorAll('a[href*="/product/"]').forEach(link => {{
      const href = link.getAttribute('href') || '';
      const parts = href.split('/').filter(Boolean);
      const slug = parts[parts.length - 1] ? parts[parts.length - 1].toLowerCase() : '';
      const product = PRODUCTS[slug];
      if (!product) return;

      const pTitle = link.querySelector('h3');
      if (pTitle) {{
        pTitle.textContent = product[lang] || product.en;
      }}

      const pImg = link.querySelector('img');
      if (pImg) {{
        pImg.alt = product[lang] || product.en;
      }}

      // Category label inside card
      const pCat = link.querySelector('p.text-muted');
      if (pCat && product.catLabels) {{
        const catSpan = pCat.querySelector('span');
        const catName = product.catLabels[langIdx] || product.catLabels[0];
        if (catSpan) {{
          pCat.innerHTML = catSpan.outerHTML + ' ' + catName;
        }} else {{
          pCat.textContent = catName;
        }}
      }}

      // Price tag inside card
      const priceEls = link.querySelectorAll('p');
      priceEls.forEach(p => {{
        if (p.textContent.includes('€') || p.textContent.includes('CHF')) {{
          p.textContent = formatPrice(product.eur, product.chf, curr);
        }}
      }});
    }});

    // 7. Update main text on Home page if present
    const heroTitle = document.querySelector('main h1');
    if (heroTitle && heroTitle.textContent.includes('organisation')) {{
      heroTitle.textContent = t.heroTitle;
    }}
  }}

  function setupEvents() {{
    document.querySelectorAll('[aria-label="Language"] button').forEach(btn => {{
      btn.onclick = (e) => {{
        e.preventDefault();
        const l = btn.textContent.trim().toLowerCase();
        setLang(l);
      }};
    }});

    document.querySelectorAll('[aria-label="Currency"] button').forEach(btn => {{
      btn.onclick = (e) => {{
        e.preventDefault();
        const bText = btn.textContent.trim();
        const c = (bText === '€' || bText === 'EUR') ? 'EUR' : 'CHF';
        setCurrency(c);
      }};
    }});
  }}

  function setupMobileMenu() {{
    const menuBtn = document.querySelector('button[aria-label="Open menu"], button[aria-label="Close menu"]');
    if (!menuBtn) return;

    let drawer = document.getElementById('mobile-menu-drawer');
    if (!drawer) {{
      drawer = document.createElement('div');
      drawer.id = 'mobile-menu-drawer';
      drawer.className = 'fixed inset-0 z-50 flex flex-col bg-cream/95 backdrop-blur-lg p-6 transition-all duration-300 opacity-0 pointer-events-none md:hidden';
      drawer.style.backgroundColor = '#F7F5F0';
      drawer.innerHTML = `
        <div class="flex items-center justify-between border-b border-hairline pb-4">
          <a class="font-display text-2xl font-semibold text-ink" href="/">ilo<span class="text-coral">.</span><span class="ml-2 text-[10px] font-sans font-semibold uppercase tracking-[0.18em] text-muted">easymate</span></a>
          <button type="button" id="close-mobile-menu" class="inline-flex h-10 w-10 items-center justify-center rounded-full text-ink hover:bg-sand" aria-label="Close menu">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          </button>
        </div>
        <div class="mt-8 flex flex-col justify-between flex-1">
          <nav class="flex flex-col gap-6 text-3xl font-display font-semibold text-ink">
            <a href="/shop/" class="mobile-nav-link hover:text-coral transition-colors">Shop</a>
            <a href="/about/" class="mobile-nav-link hover:text-coral transition-colors">About</a>
            <a href="/wholesale/" class="mobile-nav-link hover:text-coral transition-colors">Wholesale</a>
          </nav>
          <div class="mt-auto border-t border-hairline pt-6 flex flex-col gap-5">
            <div class="flex items-center justify-between">
              <span class="mobile-lang-label text-xs font-semibold uppercase tracking-wider text-muted">Language</span>
              <div class="flex items-center rounded-full border border-hairline bg-white p-0.5" role="group" aria-label="Language">
                <button type="button" class="rounded-full px-3 py-1 text-xs font-semibold uppercase transition-colors bg-ink text-cream">en</button>
                <button type="button" class="rounded-full px-3 py-1 text-xs font-semibold uppercase transition-colors text-muted hover:text-ink">de</button>
                <button type="button" class="rounded-full px-3 py-1 text-xs font-semibold uppercase transition-colors text-muted hover:text-ink">fr</button>
              </div>
            </div>
            <div class="flex items-center justify-between">
              <span class="mobile-curr-label text-xs font-semibold uppercase tracking-wider text-muted">Currency</span>
              <div class="flex items-center rounded-full border border-hairline bg-white p-0.5" role="group" aria-label="Currency">
                <button type="button" class="rounded-full px-3 py-1 text-xs font-semibold transition-colors bg-ink text-cream">€</button>
                <button type="button" class="rounded-full px-3 py-1 text-xs font-semibold transition-colors text-muted hover:text-ink">CHF</button>
              </div>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(drawer);
    }}

    function openMenu() {{
      menuBtn.setAttribute('aria-expanded', 'true');
      drawer.classList.remove('opacity-0', 'pointer-events-none');
      drawer.classList.add('opacity-100', 'pointer-events-auto');
      document.body.style.overflow = 'hidden';
      setupEvents();
      applyState();
    }}

    function closeMenu() {{
      menuBtn.setAttribute('aria-expanded', 'false');
      drawer.classList.remove('opacity-100', 'pointer-events-auto');
      drawer.classList.add('opacity-0', 'pointer-events-none');
      document.body.style.overflow = '';
    }}

    menuBtn.onclick = (e) => {{
      e.preventDefault();
      const isOpen = menuBtn.getAttribute('aria-expanded') === 'true';
      if (isOpen) closeMenu();
      else openMenu();
    }};

    const closeBtn = drawer.querySelector('#close-mobile-menu');
    if (closeBtn) closeBtn.onclick = closeMenu;

    drawer.querySelectorAll('.mobile-nav-link').forEach(link => {{
      link.onclick = closeMenu;
    }});
  }}

  function init() {{
    setupMobileMenu();
    setupEvents();
    applyState();
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', init);
  }} else {{
    init();
  }}
}})();
"""

with open('store-switcher.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

with open('app/store-switcher.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Generated store-switcher.js with mobile menu successfully!")
