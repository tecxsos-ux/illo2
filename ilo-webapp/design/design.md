# ilo — Europe Storefront · Design Document

## Concept
**ilo · easymate** — a Hong Kong factory-direct brand of colorful everyday bags & pouches,
now shipping to Switzerland & Europe. Editorial, warm, playful e-commerce. The products are
the color — the UI is a quiet warm canvas that lets them pop.

Tagline: "plan. do. life." / "Allplace Everywhere" · Factory-direct from Hong Kong since 1986.

## Tech
- Next.js 14 App Router + TypeScript + Tailwind CSS v3, `output: 'export'` (static), `images.unoptimized: true`
- framer-motion for scroll/hover micro-animations (no heavy 3D)
- Data: `/mnt/agents/output/ilo-webapp/catalog.json` → copy to `app/data/products.ts` (typed export).
  48 products: `{id, sku, slug, nameZh, name:{en,de,fr}, cat, catLabels:[en,de,fr], priceEur, priceChf, priceHkd, images:[/products/...], accent}`
- Images already in `app/public/products/*.webp` (900px) + `app/public/hero-collage.jpg`, `app/public/banner-strip.jpg`

## Design tokens
- Background: warm cream `#FAF7F2`; surface `#FFFFFF`; soft sand `#F1EBE2`
- Ink: `#211D19` (headings), `#5C554D` (body), `#8A8178` (muted)
- Accent (sparingly): deep coral `#E2583E` for CTAs; support hues pulled from products: teal `#2E8C8C`, mustard `#D9A521`, leaf `#7A9E5C`
- Lines: 1px `#E5DDD2` hairlines. Radius: cards 20px, buttons 999px (pill)
- Type: display serif **Fraunces** (Google, opsz) for headings; **Inter** for UI/body. Mono accents (SKU, prices labels): `IBM Plex Mono` optional
- NO gradients (esp. no blue-purple). Flat warm tones, generous whitespace, hairline dividers
- Buttons: pill, ink on hover invert. CTA primary = coral bg white text. Focus rings visible

## i18n & currency (client-side, React context)
- Languages: EN (default), DE, FR — pill switcher in navbar. All UI strings in a `lib/i18n.ts` dictionary; product names come from `name[lang]`
- Currency: EUR (€) default, CHF — toggle in navbar + cart. Prices from `priceEur/priceChf`, format `€ 6.90` / `CHF 6.50`
- Footer: "Ships from Hong Kong · EU VAT & duties calculated at checkout · 14-day returns (EU)"

## Pages (App Router)
### `/` Home
1. Announcement bar: "Free EU shipping over €49 · Factory-direct from Hong Kong"
2. Hero: split layout — left: Fraunces headline "Colorful organisation, made in Hong Kong." + sub + CTAs (Shop collection / Wholesale); right: `hero-collage.jpg` in a big rounded (28px) frame, slight parallax on scroll
3. Marquee strip: "Mesh Pouches · Crossbody · EVA Clear · Laptop · Travel ·" repeating, hairline top/bottom
4. Category tiles (6): Crossbody & Belt, Laptop & Work, Clear Pouches, Mesh Pouches, Travel, Storage — each tile = product image + label, hover zoom
5. Best sellers: horizontal scroll-snap row of 8 ProductCards
6. Story band: sand background, "Factory-direct since 1986" + 3 stats (48 SKUs · 100% factory QC · Ships to 27 EU countries) + link to /about
7. "Life scenes" grid: 3 lifestyle cards using banner-strip.jpg crops + copy (Work / Travel / Everyday)
8. Newsletter CTA + Footer

### `/shop`
- Filter bar: category chips (All + 8 cats), sort (Featured, Price ↑, Price ↓, Name), currency note
- Responsive grid 2/3/4 cols of ProductCard; empty state; count label
- ProductCard: square image on cream, hover: second-state lift + quick-add button slides up; name (current lang), category label, price; accent dot

### `/product/[slug]` (generateStaticParams for all 48)
- Breadcrumb; left: large image (rounded 24, cream bg); right: category label, Fraunces title, price (currency-aware), SKU mono, short description (generate 1-2 sentences per category in all 3 languages in products.ts), qty stepper, Add-to-cart (coral), accordion rows: Details / Shipping & returns / Factory notes
- "You may also like": 4 same-category cards

### `/about`
- Editorial page: banner-strip.jpg header, Hong Kong factory story (1986, direct-from-factory, EASYMATE & ilo lines), QC/materials section (EVA, mesh, nylon), Europe launch section. Warm serif pull-quotes

### `/wholesale`
- B2B page: value props (factory pricing, low MOQ, mixed-SKU cartons, EU shipping), tier table (Starter 100+ / Retail 500+ / Distributor 2000+ units with discount %), contact form (name, company, country select incl. CH/EU, message — client-side validation, success toast, no backend)

### Cart (global)
- Context + localStorage. Navbar bag icon with count badge → slide-over drawer from right: line items (thumb, name, qty stepper, remove), subtotal (currency-aware), free-shipping progress bar to €49/CHF 45, checkout button → mock checkout modal (3 steps: details → shipping → confirmation; purely client-side, order number generated)

## Shared components
`Navbar` (sticky, cream/translucent blur, logo = "ilo" Fraunces + deer-dot, links Shop/About/Wholesale, lang+currency pills, cart), `Footer` (ink bg, cream text: shop links, help, EU info, payments row as text badges Visa/Mastercard/TWINT/PayPal), `ProductCard`, `CartDrawer`, `Providers` (LangContext+CurrencyContext+CartContext), `Reveal` (framer-motion fade-up on scroll)

## Motion
- Reveal: 24px rise + fade, 0.6s ease-out, stagger 0.08
- Card hover: translateY -4px + soft shadow `0 20px 40px -20px rgba(33,29,25,.25)`
- Drawer/modals: spring. Respect prefers-reduced-motion

## Quality bar
- Fully responsive (mobile-first, hamburger menu), semantic HTML, alt text, no console errors,
  `npm run build` must pass cleanly, all 48 products reachable
