---
name: flux
description: >-
  Apply the Kaptio Flux design system when building or reviewing UI, themes,
  branding, or frontend components. Use when the user mentions Flux, design
  tokens, Kaptio brand colors, product accents (Core, Quest, Voyage, Circle,
  Edge, Agents), Lexend typography, or asks whether UI matches the design system.
---

# Flux design system

Flux is Kaptio's design system: https://flux.kaptio.com

**Version scraped:** v1.0 (May 2026). Full page snapshots live in `references/` beside this file.

## When to use this skill

- Building or reviewing React/MUI (or other) UI for Kaptio products
- Choosing colors, spacing, typography, shadows, or component patterns
- Scoping product-specific accent colors (Core vs Edge vs Agents, etc.)
- Reviewing AI-generated mockups for Flux compliance
- Implementing outcome flows (header, flow entry, outcome complete) or Salesforce ↔ Edge patterns

## Workflow

1. Read [quick-reference.md](references/quick-reference.md) for tokens, colors, typography, and don'ts.
2. For **don'ts** and anti-patterns, read [donts.md](references/donts.md) before proposing UI.
3. For the topic at hand, open the matching file from [references/index.md](references/index.md) (e.g. `foundations-colors.md`, `components-card.md`).
4. If a component page lacks variant detail (scraped pages are text-only), open the live URL from the reference `Source:` line or https://flux.kaptio.com/components/{name}.
5. For token values in code, prefer `flux.css` / `flux.json` from the [kaptio-flux](https://flux.kaptio.com/foundations/tokens) repo — do not guess CSS variable names.

## Design principles

- **Professional & approachable** — respect operators and travelers.
- **Clean & purposeful** — every element serves a function; no decorative noise.
- **Data-driven** — make dense operational data scannable.
- **Modern** — intentional, contemporary interactions.

## Implementation rules

### Tokens and color

- Use **CSS custom properties** (`--flux-*`) from `flux.json` / `flux.css`. Canonical source: GitLab `kaptio1/platform-and-services/edge/kaptio-flux`, path `src/tokens/flux.json`.
- Default **body text** on light backgrounds: `#212121` (`--flux` dark side / text token).
- Target **WCAG AA** minimum for text/background pairs; prefer documented shades on the Colors page.
- **Product accents** (Core teal, Edge pink, Agents purple, Product Experience orange) apply only in that product's UI — never globally.

### Typography

- **Lexend** for UI; **JetBrains Mono** for code and token display.
- Follow the type scale in [foundations-typography.md](references/foundations-typography.md) (Display → Small).
- Do not use colored heading text in product UI; use hierarchy, spacing, underline, or Seagreen for emphasis.

### Layout and components

- Use the **4px spacing scale** (`--flux-space-*`) — no arbitrary margins/padding.
- Elevation: `--flux-shadow-sm` through `--flux-shadow-xl`; border radius from the shadows/foundations page.
- Compose UI from **documented components** only (see [components.md](references/components.md)). If Flux does not define a pattern, flag it — do not invent chrome.
- **Outcome patterns** (Outcome Header, Flow Entry, Outcome Complete) apply to focused user journeys; see component reference files.

### MUI / React projects

When the repo uses Material UI:

- Map Flux tokens into the MUI theme (`palette`, `typography`, `spacing` multiplier aligned to 4px).
- Prefer `theme.palette` / `sx` with CSS variables where `flux.css` is loaded, e.g. `color: 'var(--flux-primary-400)'`.
- Use MUI components that correspond to Flux components (Button, Card, Dialog for Modal, etc.) and match Flux variants (primary, outline, danger) from [components-button.md](references/components-button.md) and siblings.
- Do not mix ad hoc Tailwind/Bootstrap colors alongside Flux tokens in the same app.

### Patterns

- **Salesforce ↔ Edge:** users cross a technology boundary invisibly; follow [patterns-edge-transitions.md](references/patterns-edge-transitions.md) for entry, loading, error, and return flows.

### Brand (marketing)

- Logo, voice, and story: [brand-logo.md](references/brand-logo.md), [brand-voice.md](references/brand-voice.md), [brand-story.md](references/brand-story.md).
- Wordmark accent dot: `#DE37A4`; do not recolor or distort the logo.

## Compliance checklist

Before shipping UI, verify:

- [ ] Colors map to Flux tokens (no invented hex or semantic names)
- [ ] Typography uses Lexend scale; body text is `#212121` on light backgrounds
- [ ] Spacing and radius use Flux scale
- [ ] Product accent used only for the correct product
- [ ] No items from the Don'ts list (decorative borders, heading dots, marketing-only layouts)
- [ ] Documented component or pattern exists, or design escalation is noted

## Refreshing this skill

Regenerate references after Flux site updates:

```bash
python scripts/scrape_flux.py
```

Then review [changelog.md](references/changelog.md) and update `quick-reference.md` if tokens or components changed materially.

## External links

- Site: https://flux.kaptio.com
- Token exports: https://flux.kaptio.com/assets
- Don'ts: https://flux.kaptio.com/donts
