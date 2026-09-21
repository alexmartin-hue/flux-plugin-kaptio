# Flux — /resources/changelog/

Source: https://flux.kaptio.com/resources/changelog/

Resources

# Changelog
Flux 2.0 is almost entirely additive, and the six places where it is not are the reason it publishes at its own URL rather than over the top of 1.x.

## 2.0.0

### Added

- Three token tiers. Primitive, semantic and component, with a single generation pipeline and validation that fails the build on drift between them.
- Three themes. light, dark and deep, switched with data-flux-theme on any element. Light is byte-identical to Flux 1.x.
- Layer model. layer-00 through layer-03 plus hover states, so nested surfaces stay legible without hand-picked greys in any theme.
- JetBrains Mono as a second voice. Promoted from a code font to a documented voice at 400, 500 and 700, for data rather than language.
- Component tokens. Tier 3 dimensions and role bindings for all twelve documented components.
- Component layer. flux-components.css — framework-agnostic CSS built entirely from tier-3 tokens.
- Date picker. Single-date and date-range calendars with ISO form values, hover range preview and the WAI-ARIA keyboard pattern.
- Deck layer. flux-deck.css — the presentation surface. A 16:9 canvas that scales as one piece, 18 slide layouts, and per-slide theming so a deck varies its ground without leaving the contrast audit. Loosens scale, ground, asymmetry and bleed; holds tokens, type and contrast.
- Deck contract. A second agent contract at /decks/llms.txt. Separate from llms.txt on purpose: slide rules and product rules disagree, and an agent given both averages them.
- Deck navigation. flux-deck.js — previous and next arrows, click to advance, click the left quarter to go back, plus the arrow keys, space, Page Up and Down, and Home and End. Snapping stays in CSS, so a deck that never loads the script is still a working deck.
- Diagram vocabulary. flux-figure__frame, -panel, -link, -label, -note and -value, so an inline SVG carries roles instead of colours and re-themes with its slide. Wrap parts in flux-stage to reveal them in the order you explain them — six stages at most, and every stage shows if the script never loads.
- Data layouts. Chart, donut, timeline, journey, infographic and agenda. Charts are built from tokens and inline SVG rather than a library: a chart drawn by a library names its own colours, and cannot follow a per-slide theme.
- Split with photo. flux-slide--split-photo — copy and metrics beside an editorial photograph. The company-facts shape agents were missing.
- Image rhythm. Deck contract now requires at least three photographs per deck and forbids company-facts slides without an image.
- Colour audit. Pairings checked against WCAG 2.2 AA on every build (body and primary held to AAA), plus a hue check that fails if a status surface drifts far enough from its own hue to stop reading as that status.
- Compliance check. flux-check — scans a repository for the hard-rule violations that can be detected mechanically, and exits non-zero. Ships with the package, so a consumer can gate its own build on the same rules.
- Link audit. Every internal link in the documentation resolved on every build.
- Machine contract. llms.txt, per-component plain-text sources, and drop-in rule files for Cursor, Claude Code and Copilot.
- Prototype brief. /prototypes/brief.txt — a reusable prompt that binds product prototypes to the Flux contract, documented components, readable density and verification.
- Sidebar icons. Stroke glyphs on every sidebar item except Get started, inset one spacing step so they sit under the group heading rather than flush with it.
- Tailwind v4 preset. Clears Tailwind’s default palette, spacing, radius and font namespaces rather than sitting beside them.
- Fluid root. clamp(16px, 0.875rem + 0.4vw, 19px), so every rem in the system scales with the viewport.
### Fixed

- Focus ring contrast. Flux 1.x used --flux-primary-300 for focus at 2.4:1 on white, failing WCAG 1.4.11. Now --flux-primary-400 at 5.8:1.
- Field borders. --flux-field-border now binds to border-strong rather than border-default, so a control’s boundary clears the 3:1 required of a non-text element carrying information.
- Synthesised bold. The base layer forces bold elements to 700, so a request for a weight Flux does not load no longer resolves to a browser-faked Lexend.
- Status hue on tinted themes. Subtle status surfaces were composed by mixing each hue into the layer beneath. On deep that averaged toward the teal ground, resolving warning to a green and error to a blue-grey — both passing contrast while meaning the wrong thing. They are now chosen values (--flux-yellow-900, --flux-orange-900, --flux-green-900), and the build fails if any of them drifts off its hue again.
- Prototype surface insets. The prototype brief now requires documented padding inside every bordered or filled surface, keeps action rows aligned to that inset, and wraps actions before they touch the container edge.
- Prototype badge mapping. The prototype brief now requires an explicit domain-to-badge mapping when sibling states have different consequences. The Badge reference includes Available, Assigned and Occupied inventory states, with a lighter unavailable ground that clears AA at 6.17:1.
- Status badge contrast. On request now uses yellow-900 text at 9.93:1, Awaiting supplier uses blue-800 text at 6.51:1, and Cancelled shares the lighter orange-200 treatment used by Occupied at 6.17:1. The contrast audit now checks every fixed badge pairing directly.
### New primitives
Added because a real surface needed them and no existing token fit. Adding to tier 1 is safe — a name is never removed and a value never changes.

- `--flux-display-sm … -xl` — 4.5rem to 10.5rem. The presentation scale, named apart from text-* so the boundary is enforceable: a display size in product UI is a defect, not a bold heading.
- `--flux-leading-display` — 1. Display sizes set their own leading; 1.15 at 6rem opens a gap wide enough to read as two unrelated lines.
- `--flux-radius-xs` — 2px, for a radius nested inside a radius-sm container — a segmented control’s active pill, a chip inside a field. Concentric radii need the inner one smaller.
- `--flux-yellow-900, --flux-orange-900, --flux-green-900` — Dark-ground status surfaces. The existing ramps stopped at -800, which is a mid-tone and reads as a filled alert on a dark or teal layer.
- `--flux-blue-800` — Dark text for the blue-200 awaiting badge surface. Blue-600 measured 3.75:1; blue-800 raises the pairing to 6.51:1.
### Removed, and changed against 1.x
Six differences, five of them in the `--flux-flow-*` group. They are why 2.0 is served at `/tokens/v2/` and 1.x keeps `/tokens/` rather than being overwritten by it: applications import that URL at runtime and cannot redeploy to follow a change. [Upgrading from 1.x](/get-started/upgrading/) lists each one with what to do about it.

- `--flux-grey-400` and `--flux-flow-achieved-duration` are gone.
- `--flux-flow-return-countdown` moved from `5000` to`8s` — a unitless number to a time, which breaks anything reading it in JavaScript.
- `--flux-flow-header-height`, `--flux-flow-header-bg` and`--flux-flow-entry-duration` hold new values.
## Deliberately unchanged
Things that look like oversights and are not.

- The Flux 1.x neutral ramp. Its steps are uneven, which is why it cannot carry the layer model — but the values are in production across Kaptio, and changing them would silently reflow existing pages. It is retained verbatim, with the new ramp beside it.
- The `--flux-layer-*` product accent names. They now collide conceptually with the elevation tokens, and the honest fix would be a rename. Renaming would break every consumer, so both spellings are published and`--flux-product-*` is documented as the preferred one.
- Two Lexend weights. Adding 500 would solve real hierarchy problems and would also make every existing piece of Kaptio output look slightly wrong beside new output. The mono voice solves the same problem without that cost.
- Light as the default. Most Kaptio surfaces sit beside Salesforce, which is light. Following the system preference is a per-product decision, not a system-wide one.
## Versioning policy
GuaranteedNo token name published in 1.x or 2.0 will be removed in any 2.x release, and no published value will change except to fix a failure against a standard the token was documented as meeting.Patch releases fix defects. Minor releases add tokens, components or documentation. Neither removes anything. A change that would break a consumer is a major version, and there is no plan for one.

[PreviousDownloads](/resources/downloads/)
