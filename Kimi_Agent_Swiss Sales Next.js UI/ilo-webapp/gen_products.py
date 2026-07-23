import json, os

cat = json.load(open('/mnt/agents/output/ilo-webapp/catalog.json'))

DESC = {
  "crossbody": {
    "en": [
      "Hands-free and featherlight, it keeps your phone, keys and cards exactly where you need them. Cut and sewn in our Hong Kong factory from durable nylon with smooth-glide zips.",
      "A compact everyday companion that wears crossbody or at the waist. The adjustable strap and sturdy nylon shell are made for years of daily miles."
    ],
    "de": [
      "Freihändig und federleicht: Handy, Schlüssel und Karten sind immer griffbereit. In unserer Hongkonger Manufaktur aus strapazierfähigem Nylon mit leichtläufigen Reissverschlüssen gefertigt.",
      "Ein kompakter Alltagsbegleiter – über der Schulter oder an der Hüfte tragbar. Verstellbarer Gurt und robustes Nylon, gemacht für viele Jahre täglicher Wege."
    ],
    "fr": [
      "Ultra-léger et mains libres, il garde téléphone, clés et cartes à portée de main. Cousu dans notre usine de Hong Kong en nylon résistant avec des zips fluides.",
      "Un compagnon compact à porter en bandoulière ou à la taille. Sangle réglable et nylon robuste, pensés pour des années d'usage quotidien."
    ]
  },
  "mesh": {
    "en": [
      "See everything at a glance through the airy mesh weave, with a zip that opens wide for easy packing. Lightweight, washable and made to be mixed, matched and colour-coded.",
      "Featherweight mesh keeps contents visible and ventilated, from cables to cosmetics. Double-stitched seams and a smooth zip, direct from our Hong Kong line."
    ],
    "de": [
      "Alles auf einen Blick: Das luftige Mesh-Gewebe zeigt den Inhalt, der Reissverschluss öffnet weit zum einfachen Packen. Leicht, waschbar und perfekt zum Farbcodieren.",
      "Federleichtes Mesh hält Kabel bis Kosmetik sichtbar und belüftet. Doppelt vernähte Säume und ein leichtläufiger Zip – direkt aus unserer Hongkonger Fertigung."
    ],
    "fr": [
      "Tout se voit d'un coup d'œil à travers le mesh aéré, et le zip s'ouvre en grand pour ranger facilement. Léger, lavable et parfait pour un rangement par couleurs.",
      "Un mesh plume qui garde câbles et cosmétiques visibles et aérés. Coutures doubles et zip fluide, directement de notre ligne de Hong Kong."
    ]
  },
  "accessories": {
    "en": [
      "The small detail that keeps a big bag tidy — keys, coins and cards in one grab-and-go spot. Finished with the same factory-direct hardware as our larger styles.",
      "A pocket-sized organiser for the bits that always go missing. Durable fabric, clean stitching and a zip that runs smooth, straight from the factory floor."
    ],
    "de": [
      "Das kleine Detail, das grosse Taschen ordentlich hält – Schlüssel, Münzen und Karten griffbereit an einem Platz. Mit denselben fabrikdirekten Beschlägen wie unsere grossen Modelle.",
      "Ein Organizer im Taschenformat für alles, was sonst verschwindet. Robustes Gewebe, saubere Nähte und ein leichtläufiger Zip – direkt ab Fabrik."
    ],
    "fr": [
      "Le petit détail qui garde un grand sac bien rangé — clés, monnaie et cartes réunies au même endroit. Mêmes finitions usine-directe que nos grands modèles.",
      "Un organiseur de poche pour tout ce qui se perd d'habitude. Tissu durable, coutures soignées et zip fluide, tout droit de l'usine."
    ]
  },
  "clear": {
    "en": [
      "Crystal-clear EVA shows exactly what's inside — no more digging for that one pen or cable. Water-resistant, wipe-clean and flexible enough to squeeze into any bag.",
      "Transparent, tough and airport-security friendly. The soft EVA shell wipes clean in seconds and keeps papers, pens and toiletries neatly on display."
    ],
    "de": [
      "Kristallklares EVA zeigt sofort, was drin ist – kein Suchen mehr nach Stift oder Kabel. Wasserabweisend, abwischbar und flexibel genug für jede Tasche.",
      "Transparent, robust und für die Sicherheitskontrolle geeignet. Die weiche EVA-Hülle lässt sich in Sekunden abwischen und hält Papiere, Stifte und Kosmetik sichtbar."
    ],
    "fr": [
      "L'EVA cristallin montre d'un coup d'œil ce qu'il contient — fini de fouiller pour un stylo ou un câble. Résistant à l'eau, il s'essuie et se glisse partout.",
      "Transparent, robuste et compatible avec le contrôle aéroportuaire. La coque en EVA souple se nettoie en un geste et garde papiers, stylos et accessoires bien visibles."
    ]
  },
  "storage": {
    "en": [
      "A proper home for the clutter — shelves, drawers and desks stay calm when everything has its pouch. Structured yet soft, and it folds flat when empty.",
      "Tidy drawers, happy desk: this organiser swallows the odds and ends of everyday life. Durable fabric body with a zip that opens wide for easy access."
    ],
    "de": [
      "Ein festes Zuhause für den Kleinkram – Regale, Schubladen und Schreibtische bleiben ruhig, wenn alles sein Etui hat. Formstabil und doch weich, flach faltbar wenn leer.",
      "Ordentliche Schubladen, glücklicher Schreibtisch: Dieser Organizer schluckt den Alltagskram. Robuster Stoffkörper mit weit öffnendem Reissverschluss."
    ],
    "fr": [
      "Une vraie maison pour le désordre — étagères, tiroirs et bureaux restent zen quand chaque chose a sa pochette. Structurée mais souple, elle se plie à plat une fois vide.",
      "Tiroirs nets, bureau serein : cet organisateur avale tout le petit bazar du quotidien. Corps en tissu durable avec zip à grande ouverture."
    ]
  },
  "work": {
    "en": [
      "Built for the commute and the meeting room — documents stay crisp and your essentials stay sorted. Clean lines, sturdy nylon and hardware from our own Hong Kong line.",
      "A professional silhouette without the bulk. Zips glide smoothly, pockets sit exactly where your hands expect them, and the fabric shrugs off daily wear."
    ],
    "de": [
      "Gemacht für Arbeitsweg und Meetingraum – Dokumente bleiben knitterfrei, das Wesentliche bleibt sortiert. Klare Linien, robustes Nylon und Beschläge aus eigener Hongkonger Fertigung.",
      "Eine professionelle Silhouette ohne Ballast. Zips gleiten sanft, Fächer sitzen genau da, wo die Hand sie erwartet, und das Gewebe steckt den Alltag locker weg."
    ],
    "fr": [
      "Pensé pour le trajet et la salle de réunion — documents impeccables, essentiels bien rangés. Lignes épurées, nylon robuste et finitions de notre propre ligne de Hong Kong.",
      "Une silhouette professionnelle sans le volume. Zips fluides, poches exactement où la main les attend, et un tissu qui encaisse le quotidien."
    ]
  },
  "travel": {
    "en": [
      "Packing, sorted: see-through panels and grab handles make airport security and hotel living painless. Lightweight nylon folds flat in your suitcase until you need it.",
      "From boarding gate to beach bag — a travel companion that keeps documents, chargers and toiletries in their lanes. Wipe-clean fabric, smooth zips, zero fuss."
    ],
    "de": [
      "Packen, erledigt: Sichtfenster und Griffe machen Sicherheitskontrolle und Hotelalltag mühelos. Leichtes Nylon liegt flach im Koffer, bis man es braucht.",
      "Vom Gate bis zum Strand – ein Reisebegleiter, der Dokumente, Ladekabel und Kosmetik sauber trennt. Abwischbarer Stoff, leichtläufige Zips, null Aufwand."
    ],
    "fr": [
      "Bagages bouclés : panneaux transparents et poignées rendent le contrôle et l'hôtel indolores. Le nylon léger se plie à plat dans la valise en attendant.",
      "De l'embarquement à la plage — un compagnon qui garde documents, chargeurs et produits chacun à sa place. Tissu essuyable, zips fluides, zéro prise de tête."
    ]
  },
  "laptop": {
    "en": [
      "A padded sleeve that hugs your laptop and shrugs off knocks, with room for charger and notebook. Soft-lined, water-repellent nylon — factory-direct quality at a friendly price.",
      "Slim protection for your daily machine: cushioned walls, a smooth zip and just enough extra space for the essentials. Sized for the commute, priced by the factory."
    ],
    "de": [
      "Ein gepolsterter Schutz, der dein Laptop sicher umhüllt und Stösse abfedert – mit Platz für Ladegerät und Notizbuch. Weich gefüttertes, wasserabweisendes Nylon in fabrikdirekter Qualität.",
      "Schlanker Schutz für dein tägliches Gerät: gepolsterte Wände, ein leichtläufiger Zip und genau genug Extra-Platz. Pendeltauglich geschnitten, zum Fabrikpreis."
    ],
    "fr": [
      "Une housse matelassée qui épouse votre ordinateur et absorbe les chocs, avec de la place pour chargeur et carnet. Nylon déperlant à doublure douce — qualité usine-directe à prix doux.",
      "Une protection fine pour votre machine de tous les jours : parois coussinées, zip fluide et juste l'espace qu'il faut. Pensée pour le trajet, tarifée par l'usine."
    ]
  }
}

def js(s):
    return json.dumps(s, ensure_ascii=False)

CAT_ORDER = ['crossbody', 'laptop', 'clear', 'mesh', 'travel', 'storage', 'work', 'accessories']

lines = []
lines.append("export type Lang = 'en' | 'de' | 'fr';")
lines.append("export type Currency = 'EUR' | 'CHF';")
lines.append("")
lines.append("export type Category = 'crossbody' | 'mesh' | 'accessories' | 'clear' | 'storage' | 'work' | 'travel' | 'laptop';")
lines.append("")
lines.append("export interface Product {")
lines.append("  id: number;")
lines.append("  sku: string;")
lines.append("  slug: string;")
lines.append("  nameZh: string;")
lines.append("  name: Record<Lang, string>;")
lines.append("  cat: Category;")
lines.append("  catLabels: [string, string, string];")
lines.append("  description: Record<Lang, string>;")
lines.append("  priceEur: number;")
lines.append("  priceChf: number;")
lines.append("  priceHkd: number;")
lines.append("  images: string[];")
lines.append("  accent: string;")
lines.append("}")
lines.append("")
lines.append("export const products: Product[] = [")

seen = {}
for p in cat:
    idx = seen.get(p['cat'], 0)
    seen[p['cat']] = idx + 1
    d = DESC[p['cat']]
    desc = {l: d[l][idx % 2] for l in ('en', 'de', 'fr')}
    lines.append("  {")
    lines.append("    id: %s," % p['id'])
    lines.append("    sku: %s," % js(p['sku']))
    lines.append("    slug: %s," % js(p['slug']))
    lines.append("    nameZh: %s," % js(p['nameZh']))
    lines.append("    name: { en: %s, de: %s, fr: %s }," % (js(p['name']['en']), js(p['name']['de']), js(p['name']['fr'])))
    lines.append("    cat: %s," % js(p['cat']))
    lines.append("    catLabels: [%s, %s, %s]," % (js(p['catLabels'][0]), js(p['catLabels'][1]), js(p['catLabels'][2])))
    lines.append("    description: { en: %s, de: %s, fr: %s }," % (js(desc['en']), js(desc['de']), js(desc['fr'])))
    lines.append("    priceEur: %s," % p['priceEur'])
    lines.append("    priceChf: %s," % p['priceChf'])
    lines.append("    priceHkd: %s," % p['priceHkd'])
    lines.append("    images: [%s]," % ", ".join(js(i) for i in p['images']))
    lines.append("    accent: %s," % js(p['accent']))
    lines.append("  },")
lines.append("];")
lines.append("")
lines.append("export const categories: Category[] = ['crossbody', 'laptop', 'clear', 'mesh', 'travel', 'storage', 'work', 'accessories'];")
lines.append("")
lines.append("const catLabelMap: Record<Category, [string, string, string]> = {")
for c in CAT_ORDER:
    lbl = next(p['catLabels'] for p in cat if p['cat'] == c)
    lines.append("  %s: [%s, %s, %s]," % (c, js(lbl[0]), js(lbl[1]), js(lbl[2])))
lines.append("};")
lines.append("")
lines.append("const langIdx: Record<Lang, number> = { en: 0, de: 1, fr: 2 };")
lines.append("")
lines.append("export function categoryLabel(cat: Category, lang: Lang): string {")
lines.append("  return catLabelMap[cat][langIdx[lang]];")
lines.append("}")
lines.append("")
lines.append("export function getProduct(slug: string): Product | undefined {")
lines.append("  return products.find((p) => p.slug === slug);")
lines.append("}")
lines.append("")
lines.append("export function relatedProducts(product: Product, count = 4): Product[] {")
lines.append("  const same = products.filter((p) => p.cat === product.cat && p.slug !== product.slug);")
lines.append("  const rest = products.filter((p) => p.cat !== product.cat);")
lines.append("  return [...same, ...rest].slice(0, count);")
lines.append("}")
lines.append("")
lines.append("export function formatAmount(value: number, currency: Currency): string {")
lines.append("  return currency === 'EUR' ? `\\u20AC ${value.toFixed(2)}` : `CHF ${value.toFixed(2)}`;")
lines.append("}")
lines.append("")
lines.append("export function productPrice(product: Pick<Product, 'priceEur' | 'priceChf'>, currency: Currency): string {")
lines.append("  return formatAmount(currency === 'EUR' ? product.priceEur : product.priceChf, currency);")
lines.append("}")
lines.append("")
lines.append("export function unitPrice(product: Pick<Product, 'priceEur' | 'priceChf'>, currency: Currency): number {")
lines.append("  return currency === 'EUR' ? product.priceEur : product.priceChf;")
lines.append("}")

src = "\n".join(lines) + "\n"
out = '/mnt/agents/output/ilo-webapp/app/src/data/products.ts'
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w').write(src)
print(len(src), "bytes written to", out)
