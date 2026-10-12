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
- Component tokens. Tier 3 dimensions and role bindings for all 47 documented components.
- Component layer. flux-components.css — framework-agnostic CSS built entirely from tier-3 tokens.
- Date picker. Single-date and date-range calendars with ISO form values, hover range preview and the WAI-ARIA keyboard pattern.
- Deck layer. flux-deck.css — the presentation surface. A 16:9 canvas that scales as one piece, eighteen slide layouts, and per-slide theming so a deck varies its ground without leaving the contrast audit. Loosens scale, ground, asymmetry and bleed; holds tokens, type and contrast.
- Deck contract. A second agent contract at /decks/llms.txt. Separate from llms.txt on purpose: slide rules and product rules disagree, and an agent given both averages them.
- Deck navigation. flux-deck.js — previous and next arrows, click to advance, click the left quarter to go back, plus the arrow keys, space, Page Up and Down, and Home and End. Snapping stays in CSS, so a deck that never loads the script is still a working deck.
- Diagram vocabulary. flux-figure__frame, -panel, -link, -label, -note and -value, so an inline SVG carries roles instead of colours and re-themes with its slide. Wrap parts in flux-stage to reveal them in the order you explain them — six stages at most, and every stage shows if the script never loads.
- Data layouts. Chart, donut, timeline, journey, infographic and agenda. Charts are built from tokens and inline SVG rather than a library: a chart drawn by a library names its own colours, and cannot follow a per-slide theme.
- Split with photo. flux-slide--split-photo — copy and metrics beside an editorial photograph. The company-facts shape agents were missing.
- Image rhythm. Deck contract now requires at least three photographs per deck and forbids company-facts slides without an image.
- Metric and Dashboards. A Metric component for headline figures — label, value and a change coloured by consequence, aligned on one surface — and a Dashboards pattern: page header, one metric row, then the records that need action. In prototypes the value and change take the KPI type roles.
- Forest deck ground and deck loading checks. green-850 (#0C3403) joins the palette as the forest ground: data-ground="forest" on a deep slide, with every deep role contrast-audited against it. The deck contract now requires flux.css and flux-deck.css, forbids per-story and per-persona hues, and flux-check reports token fallbacks, raw slide grounds and Lexend loaded at extra weights.
- Prototype sizes match Lexend. flux-prototype.css now changes typefaces and weights only. Prototypes use the same type scale and component sizes as the Lexend product, instead of their own larger heading, KPI and label sizes.
- Timeline and Itinerary. A Timeline component for events in order — a booking history, or a day as a schedule with the time in its own column — and an Itinerary component that lays a trip out day by day, with each service’s supplier and status and the overnight.
- Empty state, Breadcrumbs, Pagination and Segmented control. An empty state that says what is missing and offers one action, in a card, a filtered result or a table cell. Breadcrumbs as a labelled ordered list. Pagination with range text, page links and disabled ends, or previous and next only for cursor results. A segmented control built on native radios.
- Stepper and wizard, List and detail. A numbered stepper with complete and error states, and a wizard recipe that validates each step, moves focus to each new step and ends on a review. A list and detail split view that swaps panes when its container is narrow.
- Slider. A slider on native range inputs for a duration, count or amount: one value, or a minimum and maximum on one track whose handles never cross. The value is shown with its unit beside the label and announced through aria-valuetext.
- Prototype composition check. flux-check --prototype fails a prototype that does not load Flux from the published URL or package, ships a copy of a Flux file, draws its own surfaces, sets a font family, restyles a Flux component or token, or names a class after a documented component. The prototype brief now states the composition contract, lists every component by job and requires the check before handoff.
- Shortcuts, Command palette, Calendar, Board, Walkthrough, Map and Flow diagram. Keyboard shortcut hints that name the platform’s keys, and a shortcut list. A command palette on the native dialog with a combobox, grouped options and an opt-in ⌘K. A month calendar of departures with an attention state. A board whose cards move between stages by drag or keyboard. Numbered walkthroughs beside real components, and storyboards. Map routes and markers, and flow diagrams with edges and a minimap, styled from tokens so a map or diagram library themes with the page.
- Switch, Action menu, Drawer and Chart. A switch on a native checkbox with role="switch", for settings that apply at once. The menu gets its own page, with separators, a destructive item and unavailable items. A drawer on the native dialog with a pinned action row, opened through invoker commands. Charts — columns, lines, ranked bars and a donut — built from lists and SVG, on new Tier 2 chart roles audited at 3:1 in every theme.
- File upload, Assistant panel and Rich text editor. A dropzone over a native file input, with a file list that shows progress, success and the reason for a failure. A panel for Runa with cited sources, suggestions and a working status. A rich text editor with a roving toolbar, and flux-prose for the saved text.
- Progress and meter. Segmented bars over native progress and meter elements. Progress is teal; a meter takes the pending or error colour from its low, high and optimum, and says the same thing in words.
- Skeleton. Flat placeholder shapes for a card, list or table whose layout is known. Text lines take the exact line box of the text they stand in for, so nothing moves when content arrives. A slow pulse, no shimmer.
- Checkbox and radio. The checkbox gets its own page, joined by a round radio, labelled choices and fieldset groups, stacked or inline, with a group error.
- Search. A Search component: magnifier, clear button, Escape to clear and a result count announced as it changes. The data table toolbar now uses it.
- Accordion. Collapsible page sections built on details and summary: hairline-separated, a chevron that turns, optional mono metadata, and no animated height.
- Toast. A Toast component and its polite live region: one sentence, an optional Undo, six seconds that pause on hover and focus. Shown from a data-flux-toast button or a flux-toast event.
- Reorderable list. Drag a handle or use the keyboard to reorder a list, with every pickup, move and drop announced and the neighbours settling into place.
- Editable cell. Table values edited in place, with view, editing, saving and error states, a flux-edit event for saving, and a rate matrix recipe.
- Tooltip and popover. A general tooltip for icon-only controls, shown on hover and focus, and a popover panel for one short decision, both in the top layer.
- Spinner. A Spinner component for loading states: an arc from the brand teal into the Edge pink that fades out and lengthens as it turns, always with a status label, and a teal-only brand modifier. It is the one documented exception to the 300ms motion ceiling, because it loops rather than transitions.
- App shell. An App shell component: a rail of destinations in labelled sections with the current page marked, which collapses to its icons and opens as a sheet on narrow screens, beside a top bar with a ⌘K search entry point and the session context. It replaces the per-product sidebars, each with its own width, colour and active state.
- Menu button chevron. Buttons that open a menu or panel, such as Columns and More filters, end in a chevron that flips while open, so they read as dropdowns rather than actions.
- Select variants. Select gains labelled option groups and a searchable variant for long lists. Multi-select is now scripted: its trigger names the checked options or their count, it closes on Escape or a click outside, and its checkboxes are drawn by Flux.
- Filter chips and More filters. The data table now shows one removable chip per active search or filter, with Clear all, and a More filters popover for filters used less often. Filters can match a data attribute on the row as well as a column.
- Prototype typography. flux-prototype.css retypes product prototypes in Google Sans Flex (titles, headings, KPI values) and Manrope (body, tables, inputs, labels, buttons, meta), with no mono voice. Component and pattern specimens on this site show the prototype type; decks and the surrounding documentation keep Lexend and JetBrains Mono.
- Agenda-only flower video. The deck contract reserves the blooming-flower video for the agenda slide. Cover, closing and every other slide use their own footage or a photograph.
- Field info bubble. Explanatory field text now opens from an info button beside the label, on hover, focus or tap, instead of sitting below the field. The space below a field is reserved for errors. flux-check reports field-help-below.
- No native dropdowns. The product contract and prototype brief now forbid native select, datalist and date inputs, and require flux-components.js wherever Select or Date picker appears. flux-check reports native-select and native-date.
- Eyebrows and numbering. Product, prototype and deck contracts now require eyebrows, kickers and numbering to be used sparingly: a label only when it adds context the heading lacks, and a number only when order is the meaning.
- Colour audit. Pairings checked against WCAG 2.2 AA on every build (body and primary held to AAA), plus a hue check that fails if a status surface drifts far enough from its own hue to stop reading as that status.
- Compliance check. flux-check — scans a repository for the hard-rule violations that can be detected mechanically, and exits non-zero. Ships with the package, so a consumer can gate its own build on the same rules.
- Link audit. Every internal link in the documentation resolved on every build.
- Machine contract. llms.txt, per-component plain-text sources, and drop-in rule files for Cursor, Claude Code and Copilot.
- Prototype brief. /prototypes/brief.txt — a reusable prompt that binds product prototypes to the Flux contract, documented components, readable density and verification.
- Cover and closing video. The deck contract now allows a muted looping background video under the deep-teal overlay on intro (cover) and outro (closing) slides, with the same pause control and reduced-motion behaviour as the agenda.
- Tailwind v4 preset. Clears Tailwind’s default palette, spacing, radius and font namespaces rather than sitting beside them.
- Fluid root. clamp(16px, 0.875rem + 0.4vw, 19px), so every rem in the system scales with the viewport.
- Data table. Table gains sortable headers, row selection with a bulk-action bar, expandable detail rows, one visible row action with an overflow menu, compact density, a sticky header and leading columns, a toolbar with search and filters, and column visibility. flux-components.js wires them together; the static table needs no script.
- Checkbox, menu and visually hidden. flux-checkbox, drawn from tokens so it follows every theme; flux-menu, a popover menu with keyboard navigation and checkable items; and flux-visually-hidden for captions and icon labels.
### Fixed

- Focus ring contrast. Flux 1.x used --flux-primary-300 for focus at 2.4:1 on white, failing WCAG 1.4.11. Now --flux-primary-400 at 5.8:1.
- Field borders. --flux-field-border now binds to border-strong rather than border-default, so a control’s boundary clears the 3:1 required of a non-text element carrying information.
- Synthesised bold. The base layer forces bold elements to 700, so a request for a weight Flux does not load no longer resolves to a browser-faked Lexend.
- Status hue on tinted themes. Subtle status surfaces were composed by mixing each hue into the layer beneath. On deep that averaged toward the teal ground, resolving warning to a green and error to a blue-grey — both passing contrast while meaning the wrong thing. They are now chosen values (--flux-yellow-900, --flux-orange-900, --flux-green-900), and the build fails if any of them drifts off its hue again.
- Prototype surface insets. The prototype brief now requires documented padding inside every bordered or filled surface, keeps action rows aligned to that inset, and wraps actions before they touch the container edge.
- Prototype badge mapping. The prototype brief now requires an explicit domain-to-badge mapping when sibling states have different consequences. The Badge reference includes Available, Assigned and Occupied inventory states, with a lighter unavailable ground that clears AA at 6.17:1.
- Status badge contrast. On request now uses yellow-900 text at 9.93:1, Awaiting supplier uses blue-800 text at 6.51:1, and Cancelled shares the lighter orange-200 treatment used by Occupied at 6.17:1. The contrast audit now checks every fixed badge pairing directly.
- Agenda video framing. Agenda video now uses the complete uncropped frame, aligns it to the bottom of a full-height media region, and retains two-fifths of the slide so it remains visually substantial.
- Small button text. --flux-button-font-size-sm now binds to text-sm. It was text-xs, which the rules forbid for controls, so every prototype following the component broke the rule.
- Table row headers. A th scope="row" was styled as a column header: mono, uppercase, extra-small. It now reads as the row’s name, in body type and bold. Rows are a fixed 48px, single-line by default, and the last divider no longer doubles with the wrapper border when rows are filtered.
- Unchecked control border. --flux-control-unchecked-border now binds to border-strong, as fields do, because the outline is the only sign of an unchecked box.
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
