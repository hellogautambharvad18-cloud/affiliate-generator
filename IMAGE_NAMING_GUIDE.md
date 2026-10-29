# Image Naming Guide

When uploading your own product images (Image Source: Manual or Manual + SERP API), name each
file to match the slot you want it to fill. Any slot you upload a matching file for replaces the
template's own version of that image; anything you don't upload for is either left as a generic,
brand-agnostic default (badges, guarantee seal — never another product's own real photo) or
removed cleanly rather than filled with an unrelated image (bottle photos, checkout screenshot,
supplement-facts label, how-it-works diagram, favicon).

## Standard Filenames

| Filename | Section / content |
|---|---|
| `hero.jpg` | Main hero/product shot |
| `bottle-2.jpg` | 2-bottle pricing card photo |
| `bottle-3.jpg` | 3-bottle pricing card photo |
| `bottle-6.jpg` | 6-bottle pricing card photo |
| `badge-fda.jpg` | FDA-related trust badge |
| `badge-gmp.jpg` | GMP-certified badge |
| `badge-usa.jpg` | Made-in-USA badge |
| `badge-natural.jpg` | 100%-natural badge |
| `guarantee.jpg` | Money-back guarantee seal |
| `credit-cards.jpg` | Accepted payment method icons |
| `stars.jpg` | Star-rating graphic |
| `how-it-works.jpg` | How-it-works diagram/photo |
| `reviewer-1.jpg` | First customer review photo |
| `reviewer-2.jpg` | Second customer review photo |
| `reviewer-3.jpg` | Third customer review photo |
| `bonus-1.jpg` | First bonus/e-book cover |
| `bonus-2.jpg` | Second bonus/e-book cover |
| `favicon.png` | Browser-tab icon — square, used as-is. Not supplied? A brand-letter icon is generated automatically. |

(`1-bottles.jpg`/`3-bottles.jpg`/`6-bottles.jpg`-style names are also accepted for the bottle
slots and normalized automatically.)

## Extra / Theme-Specific Filenames

Some designs have extra one-off sections that don't exist in every template. Add a new name for
these as needed, but follow the same simple pattern (lowercase, hyphen-separated, `.png`):

| Filename | Section / content |
|---|---|
| `checkout.png` | Order/checkout page (timer, payment form) |
| `supplement-facts.png` | Ingredients/dosage/supplement-facts label |

## Rules

- All filenames must be lowercase.
- Use a hyphen (`-`) between words — no spaces or underscores.
- Extension is always `.png` (`.jpg`/`.jpeg`/`.webp`/`.gif` are also accepted).
- If there's a second copy of the same kind of slot (e.g. a duplicate reviewer card), add a
  number suffix: `reviewer-1.png`, `reviewer-2.png`.
- When adding a new theme, follow the standard list above as-is — the tool maps it automatically.
- If a new theme needs a section type that isn't in this list, give it a simple, descriptive name
  (like `checkout.png`, `supplement-facts.png`) and add it to this guide for future reference.
