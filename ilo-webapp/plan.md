# Plan — ilo (Hong Kong) Europe/Switzerland Next.js Storefront

## Goal
Premium Next.js (App Router) e-commerce web app to sell ilo/EASYMATE factory-direct
bags & pouches in Switzerland and Europe. Real product data + images scraped from
ilo.com.hk (48 products, 100 images — already downloaded to assets_src/images/).

## Brand facts (from ilo.com.hk)
- Brand: ilo / EASYMATE — "plan. do. life" / "Allplace Everywhere"
- Hong Kong daily bag brand: colorful mesh zip pouches, EVA pouches, crossbody bags,
  camo collection, laptop bags, travel storage, transparent storage, mesh bags
- HKD pricing on source site → convert to EUR + CHF display for EU/CH market
- Aesthetic: bright, colorful, playful, clean product shots on white

## Stages

### Stage 1 — Data pipeline (done by orchestrator)
- [x] Scrape WooCommerce store API: products.json (48 SKUs, names ZH, prices HKD)
- [x] Download 100 product images → assets_src/images/
- [ ] Generate enriched catalog JSON: English + German + French names/descriptions,
      EUR/CHF prices, EU-friendly categories (Crossbody, Laptop, Travel, Storage,
      Pouches, Transparent), hero/featured picks
- [ ] Optimize images → Next.js public/ folder (webp, consistent)

### Stage 2 — Build (load vibecoding-webapp-swarm)
- Next.js 14 App Router + TypeScript + Tailwind, premium storefront:
  - Home: hero, brand story (factory-direct HK → Europe), featured scenes, best sellers
  - Shop: filterable product grid (category, color), EUR/CHF currency toggle
  - Product detail: gallery, specs, multilingual content
  - Cart (client state) + checkout mock
  - About/factory page, wholesale B2B contact, footer with EU info (VAT, shipping)
  - i18n: EN default, DE + FR (Switzerland)
- Design: low-saturation warm base + product-color accents, generous whitespace,
  no blue-purple gradients, editorial e-commerce look

### Stage 3 — Validate & deliver
- Build passes (next build), screenshots review
- Save website version via mshtools-website_version_manager (type: static)
