import json, os

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

js_code = """
(function() {
  const PRODUCTS = {
  "fc201520": {
    "en": "Ultra-Light Shoulder Belt Bag",
    "de": "Ultraleichte Schulter-G\u00fcrteltasche",
    "fr": "Sac banane ultral\u00e9ger",
    "eur": 6.5,
    "chf": 6.0,
    "catLabels": [
      "Crossbody & Belt",
      "Umh\u00e4ngetaschen",
      "Bandouli\u00e8re"
    ]
  },
  "fc9660": {
    "en": "Jet-Black Double-Zip Mesh Pouch",
    "de": "Tiefschwarzes Mesh-Etui mit Doppelzip",
    "fr": "Pochette mesh noir double zip",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc9490": {
    "en": "Airy Mesh Handle Storage Bag",
    "de": "Leichter Mesh-Aufbewahrungsbeutel mit Griff",
    "fr": "Sac de rangement mesh \u00e0 anse",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc8244-p": {
    "en": "Camo Triple-Zip Crossbody \u00b7 205\u00d7130",
    "de": "Camo Umh\u00e4ngetasche 3 Zip \u00b7 205\u00d7130",
    "fr": "Sac bandouli\u00e8re camo 3 zips \u00b7 205\u00d7130",
    "eur": 7.5,
    "chf": 7.0,
    "catLabels": [
      "Crossbody & Belt",
      "Umh\u00e4ngetaschen",
      "Bandouli\u00e8re"
    ]
  },
  "fc8243-s": {
    "en": "Camo 3-Compartment Crossbody \u00b7 160\u00d7205",
    "de": "Camo Umh\u00e4ngetasche 3 F\u00e4cher \u00b7 160\u00d7205",
    "fr": "Sac bandouli\u00e8re camo 3 compartiments \u00b7 160\u00d7205",
    "eur": 7.5,
    "chf": 7.0,
    "catLabels": [
      "Crossbody & Belt",
      "Umh\u00e4ngetaschen",
      "Bandouli\u00e8re"
    ]
  },
  "fc8223-k": {
    "en": "Camo Card, Key & Coin Pouch",
    "de": "Camo Karten- & Schl\u00fcsseletui",
    "fr": "Porte-cartes et cl\u00e9s camo",
    "eur": 5.0,
    "chf": 4.5,
    "catLabels": [
      "Small Accessories",
      "Kleinaccessoires",
      "Petits accessoires"
    ]
  },
  "fc8222-p": {
    "en": "Camo Double-Zip Crossbody \u00b7 200\u00d7120",
    "de": "Camo Umh\u00e4ngetasche Doppelzip \u00b7 200\u00d7120",
    "fr": "Sac bandouli\u00e8re camo double zip \u00b7 200\u00d7120",
    "eur": 6.5,
    "chf": 6.0,
    "catLabels": [
      "Crossbody & Belt",
      "Umh\u00e4ngetaschen",
      "Bandouli\u00e8re"
    ]
  },
  "fc8221-s": {
    "en": "Camo Double-Zip Crossbody \u00b7 150\u00d7200",
    "de": "Camo Umh\u00e4ngetasche Doppelzip \u00b7 150\u00d7200",
    "fr": "Sac bandouli\u00e8re camo double zip \u00b7 150\u00d7200",
    "eur": 6.5,
    "chf": 6.0,
    "catLabels": [
      "Crossbody & Belt",
      "Umh\u00e4ngetaschen",
      "Bandouli\u00e8re"
    ]
  },
  "fc8220-m": {
    "en": "Camo Double-Zip Crossbody \u00b7 250\u00d7180",
    "de": "Camo Umh\u00e4ngetasche Doppelzip \u00b7 250\u00d7180",
    "fr": "Sac bandouli\u00e8re camo double zip \u00b7 250\u00d7180",
    "eur": 7.5,
    "chf": 7.0,
    "catLabels": [
      "Crossbody & Belt",
      "Umh\u00e4ngetaschen",
      "Bandouli\u00e8re"
    ]
  },
  "fc7550-a4_2_0": {
    "en": "ilo Frosted Grid Tote A4 2.0",
    "de": "ilo A4 Tragetasche Frosted Grid 2.0",
    "fr": "Tote A4 ilo Frosted Grid 2.0",
    "eur": 3.5,
    "chf": 3.5,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc7550-a4": {
    "en": "Frosted Grid Mesh Handle Tote A4",
    "de": "A4 Mesh-Tragetasche Frosted Grid",
    "fr": "Tote A4 mesh givr\u00e9 \u00e0 anse",
    "eur": 3.5,
    "chf": 3.5,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc6891-4": {
    "en": "Artist Portfolio Carry Bag",
    "de": "K\u00fcnstler-Portfolio Tragetasche",
    "fr": "Sac portfolio pour artiste",
    "eur": 11.5,
    "chf": 11.0,
    "catLabels": [
      "Storage",
      "Aufbewahrung",
      "Rangement"
    ]
  },
  "fc6489-m": {
    "en": "Everyday Double-Zip Crossbody M",
    "de": "Alltags-Umh\u00e4ngetasche Doppelzip M",
    "fr": "Sac bandouli\u00e8re quotidien M",
    "eur": 8.5,
    "chf": 8.0,
    "catLabels": [
      "Crossbody & Belt",
      "Umh\u00e4ngetaschen",
      "Bandouli\u00e8re"
    ]
  },
  "fc5200": {
    "en": "Frosted Weave Double-Zip Pouch",
    "de": "Mattes Doppelzip-Etui Weboptik",
    "fr": "Pochette double zip tiss\u00e9 givr\u00e9",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc4400-a4_2_0": {
    "en": "ilo Frosted Grid Homework Tote A4 2.0",
    "de": "ilo A4 Arbeitsmappe Frosted Grid 2.0",
    "fr": "Tote devoirs A4 ilo 2.0",
    "eur": 3.5,
    "chf": 3.5,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc4400-a4": {
    "en": "Frosted Grid Homework Tote A4",
    "de": "A4 Arbeitsmappe Frosted Grid",
    "fr": "Tote devoirs A4 givr\u00e9",
    "eur": 3.5,
    "chf": 3.5,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc4300": {
    "en": "EVA Grid Zip Pouch",
    "de": "EVA Zip-Etui Rastermuster",
    "fr": "Pochette zip EVA quadrill\u00e9e",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc4100": {
    "en": "Tinted Clear Mesh Zip Pouch",
    "de": "Get\u00f6ntes Clear-Mesh Zip-Etui",
    "fr": "Pochette mesh transparent teint\u00e9",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc3871-79": {
    "en": "Crystal Clear Storage Pouch",
    "de": "Transparentes Aufbewahrungsetui",
    "fr": "Pochette de rangement transparente",
    "eur": 3.0,
    "chf": 3.0,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc3867-9": {
    "en": "Ultra-Clear Pouch 3-Piece Set",
    "de": "Ultra-Clear Etui 3er-Set",
    "fr": "Set de 3 pochettes ultra-claires",
    "eur": 5.0,
    "chf": 4.5,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc3860-a5": {
    "en": "A5 High-Clarity Zip Tote",
    "de": "A5 Zip-Tasche hochtransparent",
    "fr": "Tote A5 zip ultra-transparent",
    "eur": 2.5,
    "chf": 2.5,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc3840": {
    "en": "Macaron Clear Mini Pouch",
    "de": "Macaron Clear Mini-Etui",
    "fr": "Mini pochette transparente macaron",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fc3570-m": {
    "en": "Feather Mesh Crossbody 25\u00d718",
    "de": "Federleichte Mesh-Umh\u00e4ngetasche 25\u00d718",
    "fr": "Sac bandouli\u00e8re mesh 25\u00d718",
    "eur": 5.5,
    "chf": 5.0,
    "catLabels": [
      "Crossbody & Belt",
      "Umh\u00e4ngetaschen",
      "Bandouli\u00e8re"
    ]
  },
  "fc2910": {
    "en": "3-Ring Binder Zip Pouch",
    "de": "Zip-Etui f\u00fcr 3-Ring-Ordner",
    "fr": "Pochette zip pour classeur 3 anneaux",
    "eur": 3.5,
    "chf": 3.5,
    "catLabels": [
      "Storage",
      "Aufbewahrung",
      "Rangement"
    ]
  },
  "fc2780": {
    "en": "Hand-Carry Double-Zip Pouch",
    "de": "Hand-Etui mit Doppelzip",
    "fr": "Pochette main double zip",
    "eur": 3.5,
    "chf": 3.5,
    "catLabels": [
      "Work & Portfolio",
      "Arbeit & Portfolio",
      "Travail & portfolio"
    ]
  },
  "fc2655": {
    "en": "Multi-Purpose Triple-Zip Pouch",
    "de": "Mehrzweck-Etui 3 Zip",
    "fr": "Pochette multi-usage 3 zips",
    "eur": 3.5,
    "chf": 3.5,
    "catLabels": [
      "Storage",
      "Aufbewahrung",
      "Rangement"
    ]
  },
  "fc2500": {
    "en": "Multi-Purpose Double-Zip Pouch",
    "de": "Mehrzweck-Etui Doppelzip",
    "fr": "Pochette multi-usage double zip",
    "eur": 3.5,
    "chf": 3.5,
    "catLabels": [
      "Storage",
      "Aufbewahrung",
      "Rangement"
    ]
  },
  "fc2338": {
    "en": "Double-Zip Utility Mesh Pouch",
    "de": "Mesh-Universaletui Doppelzip",
    "fr": "Pochette mesh utilitaire double zip",
    "eur": 3.0,
    "chf": 3.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc2330": {
    "en": "Featherlight Triangle Mesh Pouch",
    "de": "Ultraleichtes Mesh-Dreiecksetui",
    "fr": "Pochette triangle mesh ultral\u00e9g\u00e8re",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc2110": {
    "en": "Double-Layer Zip Pouch",
    "de": "Zweilagiges Zip-Etui",
    "fr": "Pochette zip double couche",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Storage",
      "Aufbewahrung",
      "Rangement"
    ]
  },
  "fc2076": {
    "en": "Portable Organizer with Zip Pocket",
    "de": "Mobiler Organizer mit Zipfach",
    "fr": "Organisateur portable avec poche zip",
    "eur": 5.5,
    "chf": 5.0,
    "catLabels": [
      "Work & Portfolio",
      "Arbeit & Portfolio",
      "Travail & portfolio"
    ]
  },
  "fc2064": {
    "en": "Everyday Double-Zip Pouch",
    "de": "Alltags-Etui Doppelzip",
    "fr": "Pochette quotidienne double zip",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Storage",
      "Aufbewahrung",
      "Rangement"
    ]
  },
  "fc2042": {
    "en": "Everyday Zip Pouch",
    "de": "Alltags Zip-Etui",
    "fr": "Pochette zip quotidienne",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Storage",
      "Aufbewahrung",
      "Rangement"
    ]
  },
  "fc1143": {
    "en": "Light Carry Triple-Zip Bag",
    "de": "Leichte Tragetasche 3 Zip",
    "fr": "Sac \u00e0 main l\u00e9ger 3 zips",
    "eur": 4.5,
    "chf": 4.0,
    "catLabels": [
      "Work & Portfolio",
      "Arbeit & Portfolio",
      "Travail & portfolio"
    ]
  },
  "fc1138": {
    "en": "Compact Double-Zip Pouch",
    "de": "Kompaktes Doppelzip-Etui",
    "fr": "Pochette compacte double zip",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Storage",
      "Aufbewahrung",
      "Rangement"
    ]
  },
  "fc1080": {
    "en": "EVA U-Shape Double-Zip Mesh Pouch",
    "de": "EVA U-Shape Mesh-Etui Doppelzip",
    "fr": "Pochette mesh EVA double zip forme U",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc9424-26": {
    "en": "Light Mesh Handle Study Bag",
    "de": "Leichter Mesh-Lernbeutel mit Griff",
    "fr": "Sac d\u2019\u00e9tude mesh \u00e0 anse",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc3540-47": {
    "en": "Woven Mesh Stand-Up Pouch",
    "de": "Gewebtes Mesh Stand-Up Etui",
    "fr": "Pochette mesh tiss\u00e9 autoportante",
    "eur": 3.0,
    "chf": 3.0,
    "catLabels": [
      "Travel",
      "Reisen",
      "Voyage"
    ]
  },
  "fc721-8": {
    "en": "EVA Grid Contrast Zip Pouch",
    "de": "EVA Zip-Etui Kontrast-Raster",
    "fr": "Pochette zip EVA contraste",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc6910-16": {
    "en": "Urban Laptop Commuter Briefcase",
    "de": "Urban Laptop-Business-Tasche",
    "fr": "Sacoche ordinateur urbaine",
    "eur": 17.0,
    "chf": 16.0,
    "catLabels": [
      "Laptop & Work",
      "Laptop & Arbeit",
      "Ordinateur & travail"
    ]
  },
  "fc6921-27": {
    "en": "Feelfree Light Laptop Tote",
    "de": "Feelfree Leichte Laptop-Tote",
    "fr": "Tote ordinateur l\u00e9g\u00e8re Feelfree",
    "eur": 18.0,
    "chf": 17.0,
    "catLabels": [
      "Laptop & Work",
      "Laptop & Arbeit",
      "Ordinateur & travail"
    ]
  },
  "fc392-5": {
    "en": "Grid Double-Zip Pouch + Card Pocket",
    "de": "Raster-Etui Doppelzip mit Kartenfach",
    "fr": "Pochette quadrill\u00e9e + porte-cartes",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc360-9": {
    "en": "Mesh Zip Pouch + Card Pocket",
    "de": "Mesh Zip-Etui mit Kartenfach",
    "fr": "Pochette mesh zip + porte-cartes",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc351-5": {
    "en": "Classic Double-Zip Mesh Pouch",
    "de": "Klassisches Mesh-Etui Doppelzip",
    "fr": "Pochette mesh classique double zip",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc9xx": {
    "en": "Double-Zip Gauze Storage Pouch",
    "de": "Doppelzip-Aufbewahrungsetui Gaze",
    "fr": "Pochette de rangement gaze double zip",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Mesh Pouches",
      "Mesh-Etuis",
      "Pochettes mesh"
    ]
  },
  "fc5": {
    "en": "Matte Waterproof EVA Zip Pouch",
    "de": "Mattes wasserdichtes EVA Zip-Etui",
    "fr": "Pochette zip EVA mate imperm\u00e9able",
    "eur": 2.0,
    "chf": 2.0,
    "catLabels": [
      "Travel",
      "Reisen",
      "Voyage"
    ]
  },
  "fb2803": {
    "en": "See-Through Multi-Function Pouch",
    "de": "Transparentes Multifunktions-Etui",
    "fr": "Pochette multifonction transparente",
    "eur": 3.0,
    "chf": 3.0,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  },
  "fb2803_mt": {
    "en": "See-Through Pouch \u00b7 Milk Tea",
    "de": "Transparentes Etui \u00b7 Milk Tea",
    "fr": "Pochette transparente \u00b7 Milk Tea",
    "eur": 3.0,
    "chf": 3.0,
    "catLabels": [
      "Clear Pouches",
      "Transparent",
      "Transparent"
    ]
  }
};

  const TRANSLATIONS = {
    en: {
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
    },
    de: {
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
    },
    fr: {
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
    }
  };

  function getLang() {
    return localStorage.getItem('ilo_lang') || 'en';
  }

  function getCurrency() {
    return localStorage.getItem('ilo_currency') || 'EUR';
  }

  function setLang(lang) {
    localStorage.setItem('ilo_lang', lang);
    applyState();
  }

  function setCurrency(curr) {
    localStorage.setItem('ilo_currency', curr);
    applyState();
  }

  function formatPrice(eur, chf, curr) {
    if (curr === 'CHF') {
      return 'CHF ' + (chf || eur).toFixed(2);
    }
    return '€ ' + (eur).toFixed(2);
  }

  function applyState() {
    const lang = getLang();
    const curr = getCurrency();
    const t = TRANSLATIONS[lang] || TRANSLATIONS.en;
    const langIdx = lang === 'de' ? 1 : (lang === 'fr' ? 2 : 0);

    // 1. Language buttons UI
    document.querySelectorAll('[aria-label="Language"] button').forEach(btn => {
      const bLang = btn.textContent.trim().toLowerCase();
      const isActive = bLang === lang;
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      btn.className = isActive
        ? 'rounded-full px-2.5 py-1 text-xs font-semibold uppercase transition-colors bg-ink text-cream'
        : 'rounded-full px-2.5 py-1 text-xs font-semibold uppercase transition-colors text-muted hover:text-ink';
    });

    // 2. Currency buttons UI
    document.querySelectorAll('[aria-label="Currency"] button').forEach(btn => {
      const bText = btn.textContent.trim();
      const isEur = bText === '€' || bText === 'EUR';
      const isActive = (isEur && curr === 'EUR') || (!isEur && curr === 'CHF');
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      btn.className = isActive
        ? 'rounded-full px-2.5 py-1 text-xs font-semibold transition-colors bg-ink text-cream'
        : 'rounded-full px-2.5 py-1 text-xs font-semibold transition-colors text-muted hover:text-ink';
    });

    // 3. Update shipping header text
    const shipText = document.querySelector('header .bg-ink p');
    if (shipText) {
      shipText.textContent = curr === 'CHF' ? t.shippingChf : t.shippingEur;
    }

    // 4. Update Nav links text (header + mobile drawer)
    const navLinks = document.querySelectorAll('header nav[aria-label="Main"] ul li a');
    if (navLinks.length >= 3) {
      if (navLinks[0]) navLinks[0].textContent = t.navShop;
      if (navLinks[1]) navLinks[1].textContent = t.navAbout;
      if (navLinks[2]) navLinks[2].textContent = t.navWholesale;
    }

    const drawerNavLinks = document.querySelectorAll('#mobile-menu-drawer .mobile-nav-link');
    if (drawerNavLinks.length >= 3) {
      drawerNavLinks[0].textContent = t.navShop;
      drawerNavLinks[1].textContent = t.navAbout;
      drawerNavLinks[2].textContent = t.navWholesale;
    }

    const drawerLangLabel = document.querySelector('#mobile-menu-drawer .mobile-lang-label');
    if (drawerLangLabel) drawerLangLabel.textContent = t.langLabel;

    const drawerCurrLabel = document.querySelector('#mobile-menu-drawer .mobile-curr-label');
    if (drawerCurrLabel) drawerCurrLabel.textContent = t.currLabel;

    // 5. Update Add to cart buttons
    document.querySelectorAll('button').forEach(btn => {
      const txt = btn.textContent;
      if (txt.includes('Add to cart') || txt.includes('In den Warenkorb') || txt.includes('Ajouter au panier')) {
        btn.textContent = t.addToCart;
      }
    });

    // 6. Update Product Cards (Titles, Category labels, Prices)
    document.querySelectorAll('a[href*="/product/"]').forEach(link => {
      const href = link.getAttribute('href') || '';
      const parts = href.split('/').filter(Boolean);
      const slug = parts[parts.length - 1] ? parts[parts.length - 1].toLowerCase() : '';
      const product = PRODUCTS[slug];
      if (!product) return;

      const pTitle = link.querySelector('h3');
      if (pTitle) {
        pTitle.textContent = product[lang] || product.en;
      }

      const pImg = link.querySelector('img');
      if (pImg) {
        pImg.alt = product[lang] || product.en;
      }

      // Category label inside card
      const pCat = link.querySelector('p.text-muted');
      if (pCat && product.catLabels) {
        const catSpan = pCat.querySelector('span');
        const catName = product.catLabels[langIdx] || product.catLabels[0];
        if (catSpan) {
          pCat.innerHTML = catSpan.outerHTML + ' ' + catName;
        } else {
          pCat.textContent = catName;
        }
      }

      // Price tag inside card
      const priceEls = link.querySelectorAll('p');
      priceEls.forEach(p => {
        if (p.textContent.includes('€') || p.textContent.includes('CHF')) {
          p.textContent = formatPrice(product.eur, product.chf, curr);
        }
      });
    });

    // 7. Update main text on Home page if present
    const heroTitle = document.querySelector('main h1');
    if (heroTitle && heroTitle.textContent.includes('organisation')) {
      heroTitle.textContent = t.heroTitle;
    }
  }

  let eventsSet = false;
  function setupEvents() {
    document.querySelectorAll('[aria-label="Language"] button').forEach(btn => {
      btn.onclick = (e) => {
        e.preventDefault();
        const l = btn.textContent.trim().toLowerCase();
        setLang(l);
      };
    });

    document.querySelectorAll('[aria-label="Currency"] button').forEach(btn => {
      btn.onclick = (e) => {
        e.preventDefault();
        const bText = btn.textContent.trim();
        const c = (bText === '€' || bText === 'EUR') ? 'EUR' : 'CHF';
        setCurrency(c);
      };
    });
  }

  function setupMobileMenu() {
    const menuBtn = document.querySelector('button[aria-label="Open menu"], button[aria-label="Close menu"]');
    if (!menuBtn) return;

    let drawer = document.getElementById('mobile-menu-drawer');
    if (!drawer) {
      drawer = document.createElement('div');
      drawer.id = 'mobile-menu-drawer';
      drawer.className = 'fixed inset-0 z-50 flex flex-col bg-cream/95 backdrop-blur-lg p-6 transition-all duration-300 opacity-0 pointer-events-none md:hidden';
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
    }

    function openMenu() {
      menuBtn.setAttribute('aria-expanded', 'true');
      drawer.classList.remove('opacity-0', 'pointer-events-none');
      drawer.classList.add('opacity-100', 'pointer-events-auto');
      document.body.style.overflow = 'hidden';
      setupEvents();
      applyState();
    }

    function closeMenu() {
      menuBtn.setAttribute('aria-expanded', 'false');
      drawer.classList.remove('opacity-100', 'pointer-events-auto');
      drawer.classList.add('opacity-0', 'pointer-events-none');
      document.body.style.overflow = '';
    }

    menuBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const isOpen = menuBtn.getAttribute('aria-expanded') === 'true';
      if (isOpen) closeMenu();
      else openMenu();
    });

    const closeBtn = drawer.querySelector('#close-mobile-menu');
    if (closeBtn) closeBtn.addEventListener('click', closeMenu);

    drawer.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', closeMenu);
    });
  }

  function init() {
    setupMobileMenu();
    setupEvents();
    applyState();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
"""

with open('store-switcher.js', 'w') as f:
    f.write(js_code)

with open('app/store-switcher.js', 'w') as f:
    f.write(js_code)

print("Generated store-switcher.js with mobile menu successfully!")
