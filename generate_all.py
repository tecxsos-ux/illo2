import os
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
      shippingEur: "Free EU & Swiss shipping over € 49.00 · Factory-direct from Hong Kong",
      shippingChf: "Free shipping over CHF 49.00 · Factory-direct from Hong Kong",
      navShop: "Shop",
      navIndustry: "Swiss Industry",
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
      shippingEur: "Kostenloser Versand in die Schweiz & EU ab € 49.00 · Direkt ab Manufaktur",
      shippingChf: "Kostenloser Versand ab CHF 49.00 · Direkt ab Hongkonger Manufaktur",
      navShop: "Shop",
      navIndustry: "Schweizer Industrie",
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
      shippingEur: "Livraison Suisse & UE offerte dès € 49.00 · Direct d'usine à Hong Kong",
      shippingChf: "Livraison offerte dès CHF 49.00 · Direct d'usine à Hong Kong",
      navShop: "Boutique",
      navIndustry: "Industrie Suisse",
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

  function createMobileDrawer() {{
    if (document.getElementById('mobile-menu-drawer')) return;
    const drawerEl = document.createElement('div');
    drawerEl.id = 'mobile-menu-drawer';
    drawerEl.style.cssText = 'display:none; position:fixed; top:0; left:0; right:0; bottom:0; width:100vw; height:100vh; z-index:99999; background-color:#FFFFFF; padding:24px; box-sizing:border-box; flex-direction:column; justify-content:space-between; overflow-y:auto; font-family:sans-serif;';
    drawerEl.innerHTML = `
      <div>
        <div style="display:flex; align-items:center; justify-content:space-between; border-bottom:1px solid rgba(0,0,0,0.1); padding-bottom:16px;">
          <a href="/" style="text-decoration:none; color:#2E1065; font-size:24px; font-weight:700;">ilo<span style="color:#9333EA;">.</span><span style="font-size:10px; text-transform:uppercase; letter-spacing:0.18em; color:#8B5CF6; margin-left:8px;">easymate</span></a>
          <button type="button" id="close-mobile-menu" aria-label="Close menu" style="background:none; border:none; padding:8px; cursor:pointer; font-size:24px; color:#2E1065; font-weight:bold;">✕</button>
        </div>
        <nav style="display:flex; flex-direction:column; gap:20px; margin-top:32px; font-size:24px; font-weight:600;">
          <a href="/shop/" class="mobile-nav-link" style="text-decoration:none; color:#2E1065;">Shop</a>
          <a href="/industry/" class="mobile-nav-link" style="text-decoration:none; color:#9333EA;">Swiss Industry</a>
          <a href="/about/" class="mobile-nav-link" style="text-decoration:none; color:#2E1065;">About</a>
          <a href="/wholesale/" class="mobile-nav-link" style="text-decoration:none; color:#2E1065;">Wholesale</a>
        </nav>
      </div>
      <div style="border-top:1px solid rgba(0,0,0,0.1); padding-top:20px; display:flex; flex-direction:column; gap:16px; margin-top: auto;">
        <div style="display:flex; align-items:center; justify-content:space-between;">
          <span class="mobile-lang-label" style="font-size:12px; font-weight:600; text-transform:uppercase; color:#8B5CF6; letter-spacing: 0.1em;">Language</span>
          <div role="group" aria-label="Language" style="display:flex; background:#FFF; border:1px solid #E9D5FF; border-radius:999px; padding:2px;">
            <button type="button" style="border:none; border-radius:999px; padding:6px 14px; font-size:12px; font-weight:600; text-transform:uppercase; cursor:pointer;">en</button>
            <button type="button" style="border:none; border-radius:999px; padding:6px 14px; font-size:12px; font-weight:600; text-transform:uppercase; cursor:pointer;">de</button>
            <button type="button" style="border:none; border-radius:999px; padding:6px 14px; font-size:12px; font-weight:600; text-transform:uppercase; cursor:pointer;">fr</button>
          </div>
        </div>
        <div style="display:flex; align-items:center; justify-content:space-between;">
          <span class="mobile-curr-label" style="font-size:12px; font-weight:600; text-transform:uppercase; color:#8B5CF6; letter-spacing: 0.1em;">Currency</span>
          <div role="group" aria-label="Currency" style="display:flex; background:#FFF; border:1px solid #E9D5FF; border-radius:999px; padding:2px;">
            <button type="button" style="border:none; border-radius:999px; padding:6px 14px; font-size:12px; font-weight:600; cursor:pointer;">€</button>
            <button type="button" style="border:none; border-radius:999px; padding:6px 14px; font-size:12px; font-weight:600; cursor:pointer;">CHF</button>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(drawerEl);
  }}

  function toggleMobileMenu(forceClose) {{
    createMobileDrawer();
    const drawer = document.getElementById('mobile-menu-drawer');
    if (!drawer) return;
    const isVisible = drawer.style.display === 'flex';
    if (isVisible || forceClose) {{
      drawer.style.display = 'none';
      document.body.style.overflow = '';
    }} else {{
      drawer.style.display = 'flex';
      document.body.style.overflow = 'hidden';
      applyState();
    }}
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
      btn.style.backgroundColor = isActive ? '#2E1065' : 'transparent';
      btn.style.color = isActive ? '#FFFFFF' : '#8B5CF6';
    }});

    // 2. Currency buttons UI
    document.querySelectorAll('[aria-label="Currency"] button').forEach(btn => {{
      const bText = btn.textContent.trim();
      const isEur = bText === '€' || bText === 'EUR';
      const isActive = (isEur && curr === 'EUR') || (!isEur && curr === 'CHF');
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      btn.style.backgroundColor = isActive ? '#2E1065' : 'transparent';
      btn.style.color = isActive ? '#FFFFFF' : '#8B5CF6';
    }});

    // 3. Update shipping header text
    const shipText = document.querySelector('header .bg-ink p');
    if (shipText) {{
      shipText.textContent = curr === 'CHF' ? t.shippingChf : t.shippingEur;
    }}

    // 4. Update Nav links text (header + mobile drawer)
    const drawerNavLinks = document.querySelectorAll('#mobile-menu-drawer .mobile-nav-link');
    if (drawerNavLinks.length >= 4) {{
      drawerNavLinks[0].textContent = t.navShop;
      drawerNavLinks[1].textContent = t.navIndustry;
      drawerNavLinks[2].textContent = t.navAbout;
      drawerNavLinks[3].textContent = t.navWholesale;
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
  }}

  document.addEventListener('click', function(e) {{
    const btn = e.target.closest('button[aria-label="Open menu"], button[aria-label="Close menu"], #close-mobile-menu');
    if (btn) {{
      e.preventDefault();
      e.stopPropagation();
      toggleMobileMenu();
      return;
    }}

    const langBtn = e.target.closest('[aria-label="Language"] button');
    if (langBtn) {{
      e.preventDefault();
      const l = langBtn.textContent.trim().toLowerCase();
      setLang(l);
      return;
    }}

    const currBtn = e.target.closest('[aria-label="Currency"] button');
    if (currBtn) {{
      e.preventDefault();
      const bText = currBtn.textContent.trim();
      const c = (bText === '€' || bText === 'EUR') ? 'EUR' : 'CHF';
      setCurrency(c);
      return;
    }}

    const navLink = e.target.closest('.mobile-nav-link');
    if (navLink) {{
      toggleMobileMenu(true);
      return;
    }}
  }});

  function init() {{
    createMobileDrawer();
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

if os.path.exists('app'):
    with open('app/store-switcher.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

print("Updated generate_all.py and store-switcher.js with Swiss Industry nav!")
