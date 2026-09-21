# Flux — /for-ai/rules/

Source: https://flux.kaptio.com/for-ai/rules/

For AI

# Repository rules
Copy one file into a repository and every agent working in it builds in Flux by default. All of them are generated from the same source as llms.txt, so none of them can drift.

## Which file you need
ToolFilePath in your repoCursor`flux.mdc``.cursor/rules/flux.mdc`Claude Code`AGENTS.md``AGENTS.md`GitHub Copilot`AGENTS.md``.github/copilot-instructions.md`Anything else`llms.txt`Point the tool at the hosted URL.bashCopy`# Cursor
mkdir -p .cursor/rules
curl -o .cursor/rules/flux.mdc https://flux.kaptio.com/rules/flux.mdc

# Claude Code, or any agent that reads AGENTS.md
curl -o AGENTS.md https://flux.kaptio.com/rules/AGENTS.md

# Copilot
mkdir -p .github
curl -o .github/copilot-instructions.md https://flux.kaptio.com/rules/AGENTS.md`CarefulIf the repository already has an `AGENTS.md`, append the Flux section rather than replacing the file. Overwriting someone’s existing agent brief to install a design system is not a good trade.
## Cursor
Scoped to UI file types and always applied, so it is in context before the first line is written.

Published at [/rules/flux.mdc](/rules/flux.mdc).

markdownCopy`---
description: Kaptio Flux 2.0 design system. Applies to all UI, CSS, markup and design output.
globs: ["**/*.css","**/*.scss","**/*.html","**/*.astro","**/*.tsx","**/*.jsx","**/*.vue","**/*.svelte","**/*.cmp","**/*.md"]
alwaysApply: true
---

# Flux 2.0 — Kaptio design system

All visual output in this repository uses Flux 2.0. This is a constraint, not a
default. Reference: https://flux.kaptio.com · Contract: https://flux.kaptio.com/llms.txt

## Before writing UI

1. Import Flux: `@import url("https://flux.kaptio.com/tokens/v2/flux.css");` or the pinned
package `@kaptio/flux-tokens`.
2. Reference Tier 2 semantic tokens. They are the only tier that themes.
3. If a token you need does not exist, say so and propose one. Do not invent a value.

## Hard rules

### Tokens

A raw value is invisible to every theme and to every future change. The token layer is the only mechanism by which a change propagates.

- Never write a raw colour. No hex, rgb(), hsl() or named colour in any component or page.
- Never write a raw dimension where a token exists. Spacing, radius, font size, line height, duration and easing all come from tokens. The only sanctioned literal is --flux-hairline (1px).
- Reference Tier 2 semantic tokens for anything with an interface role: text-*, layer-*, surface-*, border-*, icon-*, focus-*.
- Reference Tier 1 primitives only inside a semantic token definition, or for graphic content with no interface role (chart series, illustration fill, product accent mark).
- Never use Tailwind arbitrary values: bg-[#056F82], p-[14px], text-[15px]. They bypass the token layer entirely.
- If no token fits, say so and propose one. Do not invent a value.

### Typography

Flux loads two Lexend weights and three JetBrains Mono weights. A request for anything else is synthesised by the browser into a font that is not Lexend.

- Lexend at 300 or 700 only. Never 400, 500 or 600.
- Lexend Light (300) is the default for all copy, including headings.
- Lexend Bold (700) for headings that anchor, emphasis, labels and table headers.
- JetBrains Mono is the second voice, for data rather than language: identifiers, references, metadata, values, structural labels, keyboard hints.
- Mono at 400 for code and values, 500 for inline metadata, 700 for small uppercase structural labels.
- Uppercase letter-spaced mono only at --flux-text-xs. Larger reads as a warning label.
- --flux-text-xs is reserved for badges, help text and short metadata. Never use it for paragraph copy, table cells, controls or primary values.
- Use at least --flux-text-sm for controls, table cells and compact secondary copy. Use --flux-text-base for sentences intended to be read. Never reduce type to fit more content in a viewport.
- Never introduce a second sans-serif family.
- Set sizes from the scale (--flux-text-xs through -6xl). Never a literal rem or px.

### Colour

Most of the palette cannot carry text. Treating a mid-tone accent as a text colour is the most common way Flux output goes wrong.

- WCAG 2.2 AA is the contrast floor for the whole system: 4.5:1 for every text pairing, 3:1 for icons, control borders and the focus ring. Body and primary text still target AAA (7:1). Disabled is exempt per 1.4.3. Never invent a colour pairing the contrast audit does not already check.
- Teal carries the system. Other hues appear only when they carry meaning.
- Bumble-Me Yellow (--flux-surface-cta) is for one conversion action per view, and never for navigation. A second yellow element on a view is a defect.
- Yellow never carries white text. Pair --flux-surface-cta with --flux-text-on-cta, which is black.
- Never use a 400-weight accent as text on a light ground. Use a text-* role.
- Status colours are the four documented pairings. Map a new status onto the nearest existing one rather than introducing a hue.
- Map every domain status deliberately before rendering it. When sibling states have materially different consequences, leaving every badge on the neutral base style is a defect.
- A workflow stage is not automatically a warning. Use the yellow pending status only when waiting, delay or required attention is part of the meaning; otherwise use the neutral badge.
- Product accents (--flux-product-*) are graphic only: fills, marks, diagram keys. Never text, never a global theme.
- Never use colour as the only signal for a state.

### Layout and geometry

Consistent spacing and near-square geometry are what make output read as Kaptio rather than as generic.

- All spacing comes from the 4px scale. If none of the steps fit, the structure is wrong, not the scale.
- Interface radius is --flux-radius-sm (4px): buttons, fields, cards, tables, notes. --flux-radius-md for modals only.
- --flux-radius-full is for pills and avatars, nothing else.
- Separate sections with --flux-seam-gap.
- Constrain reading columns to --flux-measure-prose.
- Text and controls never sit directly against the edge of a bordered or filled surface. Use the component padding token; tables apply inset through their cells, and intentional edge-to-edge media is the exception.
- Action rows keep the same inline inset as the content above and use a spacing token between actions. Wrap or stack the actions before a control touches the container edge.
- Do not scale an application with CSS zoom or transform, and do not compress type or spacing to make the whole workflow fit above the fold. Reflow the layout, wrap controls and let the page scroll; wrap wide tables in their horizontal scroll container.
- Never mix px into a layout built from rem tokens. The root size is fluid, so they diverge as the viewport grows.

### Elevation

Flux is a flat system. Depth is reserved for things that genuinely float, so that when it appears it means something.

- Separate nested surfaces with a layer step (--flux-layer-01 → -02 → -03) and a hairline. Never hand-pick a grey.
- Shadow is for overlays, popovers and modals. --flux-shadow-md is the ceiling for anything in normal flow.
- Never use a coloured shadow or a glow.
- Never stack a border, an inner glow and a heavy shadow on the same container.
- Never nest three layer levels on the deep theme; layer-03 aliases layer-02 there.

### Motion

Motion in Flux confirms that something happened. Anything that draws attention to itself is describing the animation rather than the change.

- Default to --flux-duration-fast with --flux-ease-productive.
- Name the properties being transitioned. Never use transition: all.
- Animate opacity, transform and colour. Never width, height, top, left, margin or padding.
- Never scale, lift or grow on hover. Flux buttons change colour and nothing else.
- Never exceed --flux-duration-slow (300ms) in product UI.
- Do not write your own prefers-reduced-motion reset. The base layer handles it globally.

### Accessibility

Flux guarantees contrast and focus. Everything structural is the implementer’s responsibility, and it is where generated UI code fails most often.

- Do not ship a text or control pairing below WCAG 2.2 AA. Use a semantic text-*, icon-* or border-strong role on a documented ground so the audited pairings apply. A raw colour, or a primitive used as text, is already a defect.
- Never remove the focus outline. Focus is teal, 2px, offset 2px, in every theme, applied by the base layer.
- Use native elements before ARIA: button, a, dialog, select, table, input. A div with a click handler is not a button.
- Open modals with dialog.showModal(), never by toggling a class. Focus trapping, page inertness and Escape come from the platform.
- Every input needs a visible, programmatically associated label. A placeholder is not a label.
- Bind error text to its field with aria-describedby, and set aria-invalid.
- Every icon-only control needs an accessible name.
- Tabs need roving tabindex: the selected tab is tabindex="0", the rest are tabindex="-1".
- Table headers need scope. Numeric columns are right-aligned with tabular figures.
- Choose heading levels for document structure, and size them with tokens.

### Themes

A component that references roles works in three themes for free. A component that references colours works in one.

- Never write theme-specific CSS inside a component. If you need to, a semantic token is missing — say which.
- Test new work in light, dark and deep before considering it done.
- A scoped theme region must set its own background from --flux-surface-page or a layer-* token.
- Deep is a brand ground for slides and marketing, not a dark mode for dense UI.

## Composition discipline

These are not token violations. They are the habits that make output look
generic even when every value is correct.

- No gradient fills on interface surfaces. Flat colour, or nothing.
- No decorative coloured bar along the edge of a card.
- No coloured dot beside a heading.
- No emoji as an icon system. Use a consistent icon set.
- No glow, no neon, no glassmorphism, no heavy blur behind content.
- No centred body copy. Centre a heading and a lede at most.
- No three-column feature grid of icon-plus-heading-plus-paragraph as a default layout.
- No badge on something that is not a status.
- No hero section with a gradient mesh background.
- Do not stack decoration: pick one of border, shadow, or fill change to signal a state.
- Do not add a container just to add a container. If it holds one thing, it is not grouping anything.
- Do not remove a documented component’s internal padding. A parent inset does not replace the inset inside a card, note, table cell or action row.
- Do not turn every value into a card. Group related metrics on one surface and let the important exception carry the emphasis.
- Do not shrink the interface to show everything at once. Preserve readable type and row rhythm, then use scrolling, pagination or progressive disclosure for the remainder.
- Prefer one strong element over three competing ones. Density is not hierarchy.

## Components

Twelve components are documented with live specimens, markup, states, keyboard
behaviour and token bindings. Read the plain-text source before building one
from scratch:

https://flux.kaptio.com/components/source/.txt

Available: button, input, select, date-picker, card, description-list, badge, table, modal, note, tabs, avatar.

If the repository already has a component for the job, extend it. Do not create
a second implementation of a documented component.

## Slide decks

Decks are a different surface with a different contract. If you are asked for a
presentation, stop reading this file and read that one instead:

https://flux.kaptio.com/decks/llms.txt

The two disagree deliberately — a slide relaxes scale, ground and bleed in ways
a dashboard cannot. Do not average them. Never load flux-deck.css into product
UI: it overrides the fluid root, which is correct for a deck and wrong for an
application. Never use --flux-display-* sizes outside a deck.

## Verify

Run the compliance check before you consider UI work finished:

npx flux-check src/

It reports the violations that can be detected mechanically — raw colours,
arbitrary Tailwind values, synthesised font weights, transition: all, removed
focus outlines, gradients, raw dimensions, divs with click handlers, table
headers without scope — each with the rule name and the fix. It exits non-zero,
so it also works as a CI gate.

Fix every finding. If one is genuinely correct, annotate the line above it with
the reason and the rule name:

/* Glyph, not a surface: gradients inherit currentColor, an SVG cannot.
flux-ignore-next-line gradient */

## Self-check before returning UI code

- No raw hex, rgb() or named colour anywhere.
- No raw px, rem or ms where a token exists (--flux-hairline excepted).
- No Tailwind arbitrary values.
- Lexend at 300 or 700 only.
- No paragraph, table cell, control or primary value set at --flux-text-xs.
- No CSS zoom, scaled application shell or fit-to-viewport compression.
- Radius is --flux-radius-sm on every control.
- At most one yellow CTA element.
- Text and control pairings meet WCAG 2.2 AA (4.5:1 text, 3:1 non-text). Use semantic roles, not a colour that looks dark enough.
- Focus outline present and not overridden.
- Native elements used for buttons, links, dialogs, selects and tables.
- No transition: all, and no scale or lift on hover.
- Would this render correctly with data-flux-theme="dark" on the root? If any
part would not, that part is referencing a primitive or a raw value.`
## AGENTS.md
The portable form. Same rules, no tool-specific frontmatter.

Published at [/rules/AGENTS.md](/rules/AGENTS.md).

markdownCopy`# Flux 2.0 — design system contract

This repository uses the Kaptio Flux 2.0 design system for all visual output.

- Reference: https://flux.kaptio.com
- Machine contract: https://flux.kaptio.com/llms.txt
- Component sources: https://flux.kaptio.com/components/source/.txt

## Setup

```css
@import url("https://flux.kaptio.com/tokens/v2/flux.css");
/* optional: working components, built from Flux tokens */
@import url("https://flux.kaptio.com/tokens/v2/flux-components.css");
```

## The one rule everything else follows from

Reference Tier 2 semantic tokens — `text-*`, `layer-*`, `surface-*`,
`border-*`, `icon-*`, `focus-*`. They resolve per theme. Primitives and raw
values do not, so anything built on them works in exactly one theme and breaks
silently in the others.

## Tokens

A raw value is invisible to every theme and to every future change. The token layer is the only mechanism by which a change propagates.

- Never write a raw colour. No hex, rgb(), hsl() or named colour in any component or page.
- Never write a raw dimension where a token exists. Spacing, radius, font size, line height, duration and easing all come from tokens. The only sanctioned literal is --flux-hairline (1px).
- Reference Tier 2 semantic tokens for anything with an interface role: text-*, layer-*, surface-*, border-*, icon-*, focus-*.
- Reference Tier 1 primitives only inside a semantic token definition, or for graphic content with no interface role (chart series, illustration fill, product accent mark).
- Never use Tailwind arbitrary values: bg-[#056F82], p-[14px], text-[15px]. They bypass the token layer entirely.
- If no token fits, say so and propose one. Do not invent a value.

## Typography

Flux loads two Lexend weights and three JetBrains Mono weights. A request for anything else is synthesised by the browser into a font that is not Lexend.

- Lexend at 300 or 700 only. Never 400, 500 or 600.
- Lexend Light (300) is the default for all copy, including headings.
- Lexend Bold (700) for headings that anchor, emphasis, labels and table headers.
- JetBrains Mono is the second voice, for data rather than language: identifiers, references, metadata, values, structural labels, keyboard hints.
- Mono at 400 for code and values, 500 for inline metadata, 700 for small uppercase structural labels.
- Uppercase letter-spaced mono only at --flux-text-xs. Larger reads as a warning label.
- --flux-text-xs is reserved for badges, help text and short metadata. Never use it for paragraph copy, table cells, controls or primary values.
- Use at least --flux-text-sm for controls, table cells and compact secondary copy. Use --flux-text-base for sentences intended to be read. Never reduce type to fit more content in a viewport.
- Never introduce a second sans-serif family.
- Set sizes from the scale (--flux-text-xs through -6xl). Never a literal rem or px.

## Colour

Most of the palette cannot carry text. Treating a mid-tone accent as a text colour is the most common way Flux output goes wrong.

- WCAG 2.2 AA is the contrast floor for the whole system: 4.5:1 for every text pairing, 3:1 for icons, control borders and the focus ring. Body and primary text still target AAA (7:1). Disabled is exempt per 1.4.3. Never invent a colour pairing the contrast audit does not already check.
- Teal carries the system. Other hues appear only when they carry meaning.
- Bumble-Me Yellow (--flux-surface-cta) is for one conversion action per view, and never for navigation. A second yellow element on a view is a defect.
- Yellow never carries white text. Pair --flux-surface-cta with --flux-text-on-cta, which is black.
- Never use a 400-weight accent as text on a light ground. Use a text-* role.
- Status colours are the four documented pairings. Map a new status onto the nearest existing one rather than introducing a hue.
- Map every domain status deliberately before rendering it. When sibling states have materially different consequences, leaving every badge on the neutral base style is a defect.
- A workflow stage is not automatically a warning. Use the yellow pending status only when waiting, delay or required attention is part of the meaning; otherwise use the neutral badge.
- Product accents (--flux-product-*) are graphic only: fills, marks, diagram keys. Never text, never a global theme.
- Never use colour as the only signal for a state.

## Layout and geometry

Consistent spacing and near-square geometry are what make output read as Kaptio rather than as generic.

- All spacing comes from the 4px scale. If none of the steps fit, the structure is wrong, not the scale.
- Interface radius is --flux-radius-sm (4px): buttons, fields, cards, tables, notes. --flux-radius-md for modals only.
- --flux-radius-full is for pills and avatars, nothing else.
- Separate sections with --flux-seam-gap.
- Constrain reading columns to --flux-measure-prose.
- Text and controls never sit directly against the edge of a bordered or filled surface. Use the component padding token; tables apply inset through their cells, and intentional edge-to-edge media is the exception.
- Action rows keep the same inline inset as the content above and use a spacing token between actions. Wrap or stack the actions before a control touches the container edge.
- Do not scale an application with CSS zoom or transform, and do not compress type or spacing to make the whole workflow fit above the fold. Reflow the layout, wrap controls and let the page scroll; wrap wide tables in their horizontal scroll container.
- Never mix px into a layout built from rem tokens. The root size is fluid, so they diverge as the viewport grows.

## Elevation

Flux is a flat system. Depth is reserved for things that genuinely float, so that when it appears it means something.

- Separate nested surfaces with a layer step (--flux-layer-01 → -02 → -03) and a hairline. Never hand-pick a grey.
- Shadow is for overlays, popovers and modals. --flux-shadow-md is the ceiling for anything in normal flow.
- Never use a coloured shadow or a glow.
- Never stack a border, an inner glow and a heavy shadow on the same container.
- Never nest three layer levels on the deep theme; layer-03 aliases layer-02 there.

## Motion

Motion in Flux confirms that something happened. Anything that draws attention to itself is describing the animation rather than the change.

- Default to --flux-duration-fast with --flux-ease-productive.
- Name the properties being transitioned. Never use transition: all.
- Animate opacity, transform and colour. Never width, height, top, left, margin or padding.
- Never scale, lift or grow on hover. Flux buttons change colour and nothing else.
- Never exceed --flux-duration-slow (300ms) in product UI.
- Do not write your own prefers-reduced-motion reset. The base layer handles it globally.

## Accessibility

Flux guarantees contrast and focus. Everything structural is the implementer’s responsibility, and it is where generated UI code fails most often.

- Do not ship a text or control pairing below WCAG 2.2 AA. Use a semantic text-*, icon-* or border-strong role on a documented ground so the audited pairings apply. A raw colour, or a primitive used as text, is already a defect.
- Never remove the focus outline. Focus is teal, 2px, offset 2px, in every theme, applied by the base layer.
- Use native elements before ARIA: button, a, dialog, select, table, input. A div with a click handler is not a button.
- Open modals with dialog.showModal(), never by toggling a class. Focus trapping, page inertness and Escape come from the platform.
- Every input needs a visible, programmatically associated label. A placeholder is not a label.
- Bind error text to its field with aria-describedby, and set aria-invalid.
- Every icon-only control needs an accessible name.
- Tabs need roving tabindex: the selected tab is tabindex="0", the rest are tabindex="-1".
- Table headers need scope. Numeric columns are right-aligned with tabular figures.
- Choose heading levels for document structure, and size them with tokens.

## Themes

A component that references roles works in three themes for free. A component that references colours works in one.

- Never write theme-specific CSS inside a component. If you need to, a semantic token is missing — say which.
- Test new work in light, dark and deep before considering it done.
- A scoped theme region must set its own background from --flux-surface-page or a layer-* token.
- Deep is a brand ground for slides and marketing, not a dark mode for dense UI.

## Composition discipline

- No gradient fills on interface surfaces. Flat colour, or nothing.
- No decorative coloured bar along the edge of a card.
- No coloured dot beside a heading.
- No emoji as an icon system. Use a consistent icon set.
- No glow, no neon, no glassmorphism, no heavy blur behind content.
- No centred body copy. Centre a heading and a lede at most.
- No three-column feature grid of icon-plus-heading-plus-paragraph as a default layout.
- No badge on something that is not a status.
- No hero section with a gradient mesh background.
- Do not stack decoration: pick one of border, shadow, or fill change to signal a state.
- Do not add a container just to add a container. If it holds one thing, it is not grouping anything.
- Do not remove a documented component’s internal padding. A parent inset does not replace the inset inside a card, note, table cell or action row.
- Do not turn every value into a card. Group related metrics on one surface and let the important exception carry the emphasis.
- Do not shrink the interface to show everything at once. Preserve readable type and row rhythm, then use scrolling, pagination or progressive disclosure for the remainder.
- Prefer one strong element over three competing ones. Density is not hierarchy.

## Slide decks

Presentations are a different surface with a different contract. If you are
asked for a deck, read https://flux.kaptio.com/decks/llms.txt instead of this file. The two
disagree deliberately; do not average them. Never load flux-deck.css into
product UI, and never use `--flux-display-*` sizes outside a deck.

## Before returning UI code

Ask: would this render correctly with `data-flux-theme="dark"` on the root
element? If any part would not, that part is referencing a primitive or a raw
value, and it is a defect.

## Verify

Run the compliance check before you consider UI work finished:

npx flux-check src/

It reports the violations that can be detected mechanically — raw colours,
arbitrary Tailwind values, synthesised font weights, transition: all, removed
focus outlines, gradients, raw dimensions, divs with click handlers, table
headers without scope — each with the rule name and the fix. It exits non-zero,
so it also works as a CI gate.

Fix every finding. If one is genuinely correct, annotate the line above it with
the reason and the rule name:

/* Glyph, not a surface: gradients inherit currentColor, an SVG cannot.
flux-ignore-next-line gradient */`
## Copilot
Copilot reads .github/copilot-instructions.md. The AGENTS.md content works unmodified.

Copilot's context window for instructions is smaller than most, and it weights the opening lines heavily. If you need to trim, keep the setup block, the semantic-tier rule and the self-check, and drop the per-category premises — they are the most valuable part for larger models and the first thing Copilot will lose anyway.

## Inline, for a one-off prompt
When you cannot add a file, this paragraph does most of the work.

textCopy`Use the Kaptio Flux 2.0 design system: https://flux.kaptio.com/llms.txt

Import https://flux.kaptio.com/tokens/v2/flux.css and reference Tier 2 semantic
tokens only (--flux-text-*, --flux-layer-*, --flux-surface-*, --flux-border-*).
No raw hex, px or rem values. Lexend at weight 300 or 700 only; JetBrains Mono
for identifiers and labels. Radius --flux-radius-sm on every control. One yellow
CTA per view, maximum. Never remove the focus outline. Native elements for
buttons, dialogs, selects and tables. Before you finish: would this render
correctly with data-flux-theme="dark" on the root element?`
## Verifying an agent is complying
Four greps and one attribute find nearly everything.

bashCopy`# Raw colours
rg -n '#[0-9a-fA-F]{3,8}\b|rgb\(|hsl\(' --glob '!**/flux*.css' src/

# Raw dimensions outside tokens
rg -n ':\s*\d+px' --glob '!**/flux*.css' src/

# Tailwind arbitrary values
rg -n '\[[#0-9]' src/

# Focus removal and unscoped transitions
rg -n 'outline:\s*none|transition:\s*all' src/`Then set `data-flux-theme="dark"` on the root and look at the result. Anything that stays light is referencing a primitive or a raw value, and the greps above will usually tell you exactly where.

VerifiedThese same checks run in this repository’s own build. The system holds itself to the contract it publishes.[PreviousOverview](/for-ai/)[NextPrototype prompt](/for-ai/prototypes/)
