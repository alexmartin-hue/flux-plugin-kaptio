# Flux — /for-ai/

Source: https://flux.kaptio.com/for-ai/

For AI

# Flux for AI
Most Kaptio interface work now passes through an agent before it reaches a person. Flux 2.0 treats that as the primary consumption path rather than an afterthought, so the system is published as a machine contract as well as a website.

## Why this exists
A design system that only a human can read gets applied by whoever remembers it.

Showcase, Spotlight and the rest of the Kaptio agent surfaces generate interface code continuously. An agent reaching for its defaults produces something that is competent, generic, and not Kaptio: a blue focus ring, a 12px radius, a gradient hero, Inter at 500. Every one of those is a reasonable default somewhere. None of them is Flux.

So the rules are published where an agent will actually read them — one plain-text file, no HTML to parse, with the reason for each rule stated alongside it. Models comply far more reliably with a constraint they understand than with a list they were handed.

## The contract
One file. Every token, every rule, every component's markup.

textCopy`https://flux.kaptio.com/llms.txt`It is generated from the same sources as this site, so it cannot describe a system the site does not implement. Point an agent at it once and it has the complete system: 822 tokens across three tiers and three themes, the hard rules with their reasoning, the composition habits to avoid, and copyable markup for all 48 components.

NoteIndividual components are also published as plain text at`/components/source/.txt` — useful when you want one component in context rather than the whole system.
## The hard rules
Each of these is a defect if violated, not a preference. The premise is part of the rule.

### Tokens
A raw value is invisible to every theme and to every future change. The token layer is the only mechanism by which a change propagates.

- Never write a raw colour. No hex, rgb(), hsl() or named colour in any component or page.
- Never write a raw dimension where a token exists. Spacing, radius, font size, line height, duration and easing all come from tokens. The only sanctioned literal is --flux-hairline (1px).
- Reference Tier 2 semantic tokens for anything with an interface role: text-*, layer-*, surface-*, border-*, icon-*, focus-*.
- Reference Tier 1 primitives only inside a semantic token definition, or for graphic content with no interface role (illustration fill, product accent mark).
- Never use Tailwind arbitrary values: bg-[#056F82], p-[14px], text-[15px]. They bypass the token layer entirely.
- If no token fits, say so and propose one. Do not invent a value.
### Typography
Flux loads two Lexend weights and three JetBrains Mono weights. A request for anything else is synthesised by the browser into a font that is not Lexend.

- Product prototypes are the one exception to the Lexend rules below. A prototype loads flux-prototype.css after flux.css and flux-components.css, and that layer sets its type. Never load it in a deck.
- In a prototype: Google Sans Flex Medium for headings and card titles; Google Sans Flex Bold for KPI values (.flux-kpi, and the Metric component’s value), in text-brand. Manrope Regular for body, tables, inputs, descriptions (.flux-description) and meta (.flux-meta); Manrope Medium for labels; Manrope Semi Bold for buttons and KPI change (.flux-kpi-change). Prototypes have no mono voice.
- flux-prototype.css changes typefaces and weights, never sizes. Size a prototype exactly as you would the Lexend product: the same scale tokens for headings, and the sizes each component already sets.
- Set prototype weights through --flux-prototype-weight-regular, -medium, -semibold and -bold, never as literal numbers.
- Outside prototypes, Lexend at 300 or 700 only. Never 400, 500 or 600.
- Lexend Light (300) is the default for all copy, including headings.
- Lexend Bold (700) for headings that anchor, emphasis, labels and table headers.
- JetBrains Mono is the second voice, for data rather than language: identifiers, references, metadata, values, structural labels, keyboard hints.
- Mono at 400 for code and values, 500 for inline metadata, 700 for small uppercase structural labels.
- Uppercase letter-spaced mono only at --flux-text-xs. Larger reads as a warning label.
- --flux-text-xs is reserved for badges, help text and short metadata. Never use it for paragraph copy, table cells, controls or primary values.
- Use at least --flux-text-sm for controls, table cells and compact secondary copy. Use --flux-text-base for sentences intended to be read. Never reduce type to fit more content in a viewport.
- Never introduce a family Flux does not load. Prototypes use exactly the two that flux-prototype.css loads; everything else uses Lexend.
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
- Chart series take --flux-chart-1 to -4 in order, and --flux-chart-muted for a comparison such as last year. A heatmap takes the --flux-chart-sequential-1 to -5 ramp. Never a chart library’s palette, a product accent or a status colour.
- Never use colour as the only signal for a state.
### Layout and geometry
Consistent spacing and near-square geometry are what make output read as Kaptio rather than as generic.

- All spacing comes from the 4px scale. If none of the steps fit, the structure is wrong, not the scale.
- Interface radius is --flux-radius-sm (4px): buttons, fields, cards, tables, notes. --flux-radius-md for modals only.
- --flux-radius-full is for pills, avatars, radio buttons, switches and the spinner ring, nothing else.
- Separate sections with --flux-seam-gap.
- A modal is never wider than --flux-modal-width-max, 90% of the window. Add flux-modal--wide only when a permitted modal must show what a decision affects, such as the read-only summary of an irreversible change. Width never makes a modal suitable for a table, a comparison or a form; those belong in a side panel, a split view or a page.
- Constrain reading columns to --flux-measure-prose.
- Text and controls never sit directly against the edge of a bordered or filled surface. Use the component padding token; tables apply inset through their cells, and intentional edge-to-edge media is the exception.
- Action rows keep the same inline inset as the content above and use a spacing token between actions. Wrap or stack the actions before a control touches the container edge.
- Do not scale an application with CSS zoom or transform, and do not compress type or spacing to make the whole workflow fit above the fold. Reflow the layout, wrap controls and let the page scroll; wrap wide tables in their horizontal scroll container.
- Never cut a value off silently. When a value does not fit its column, truncate it with data-truncate, which caps a table cell at --flux-table-truncate-width and, with flux-components.js loaded, shows the full value on hover; never write your own ellipsis or max-width. Never truncate a reference, an amount or a date: let those columns size to their content.
- Never mix px into a layout built from rem tokens. The root size is fluid, so they diverge as the viewport grows.
### Elevation
Flux is a flat system. Depth is reserved for things that genuinely float, so that when it appears it means something.

- Separate nested surfaces with a layer step (--flux-layer-01 → -02 → -03) and a hairline. Never hand-pick a grey. Nest a surface only when it is a different kind of thing, such as a note or a table inside a card, never to group content that spacing could group.
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
- Never exceed --flux-duration-slow (300ms) in product UI. The Spinner and the Skeleton pulse are the exceptions: they are loops, not transitions, and run at --flux-spinner-duration and --flux-skeleton-duration.
- Do not write your own prefers-reduced-motion reset. The base layer handles it globally.
### Accessibility
Flux guarantees contrast and focus. Everything structural is the implementer’s responsibility, and it is where generated UI code fails most often.

- Do not ship a text or control pairing below WCAG 2.2 AA. Use a semantic text-*, icon-* or border-strong role on a documented ground so the audited pairings apply. A raw colour, or a primitive used as text, is already a defect.
- Never remove the focus outline. Focus is teal, 2px, offset 2px, in every theme, applied by the base layer.
- Use native elements before ARIA: button, a, dialog, table, input. A div with a click handler is not a button.
- Select and Date picker are the exception: never render a native select element or a date-type input, because their menus and calendars draw in the operating system style. Copy the documented Flux markup and load flux-components.js.
- Open modals with dialog.showModal(), never by toggling a class. Focus trapping, page inertness and Escape come from the platform.
- Every input needs a visible, programmatically associated label. A placeholder is not a label.
- Bind error text to its field with aria-describedby, and set aria-invalid.
- Explanatory field text — what a field means, its format, its constraints — goes in the documented info bubble beside the label, never as text below the field. Only an error message sits below a field. Reference the bubble from the control with aria-describedby.
- Every icon-only control needs an accessible name.
- On a coarse pointer every control is at least --flux-touch-target (44px) tall. Flux components do this themselves; a custom control sizes from the component tokens or sets min-block-size: var(--flux-touch-target) under @media (pointer: coarse).
- Tabs need roving tabindex: the selected tab is tabindex="0", the rest are tabindex="-1".
- Table headers need scope. Numeric columns are right-aligned with tabular figures.
- Choose heading levels for document structure, and size them with tokens.
### Interaction architecture
Kaptio users reference, compare and modify interconnected information. Keep them in context: modals are exceptions, not the default interaction pattern. Mandatory for all new features, redesigned screens and shared components.

- Never use a modal for a task that requires users to reference, compare or modify information outside that modal.
- Choose the least disruptive pattern that gives the task enough space, context and clarity, in this order: inline editing (Editable cell), expandable sections (Accordion), a contextual side panel (Drawer), a split-view workspace (List and detail), a dedicated page. A modal is the exception.
- A modal is permitted only when all of these hold: the interaction needs immediate attention or an explicit decision, it is short and self-contained, the user does not need the content behind it, it has no complex navigation, and it has a clear primary action and a clear way to cancel. Examples: confirm deleting a booking, discarding unsaved changes or an irreversible financial action.
- Never use a modal for creating or editing complex bookings, multi-step workflows, searching and selecting inventory, comparing products, services or prices, assigning passengers to rooms or cabins, editing pricing structures, configuring departures or services, large forms, editable data tables, or anything that needs information from another screen.
- A modal never opens another modal, and a side panel never opens another side panel.
- A modal has a descriptive title that states the consequence and an explicit action label such as “Delete booking”, never “OK”. Cancelling preserves the underlying data, and neither a backdrop click nor Escape silently discards changes.
- Never compress a complex workflow into a modal or side panel to avoid page navigation. When a side panel becomes too complex, promote the task to a dedicated page.
- Inline edits show validation beside the field, keep the entered value with a clear error when a save fails, and confirm visibly when a save succeeds. Use explicit Save and Cancel when a change is consequential or spans related fields, and never silently save an irreversible or high-impact change.
- Navigation preserves filters, sorting, selection, draft data and scroll position, and warns before discarding unsaved changes. Represent important workspace state in the URL where practical, so Back behaves predictably.
- Use progressive disclosure to reduce load, never to hide frequently used primary actions, and never use a modal to reduce visual clutter.
- On narrow screens a split view stacks and a side panel becomes a full-screen view — never a modal.
- The same type of task uses the same pattern in every module. A modal outside the permitted uses needs a documented exception approved by the design owner.
### Themes
A component that references roles works in three themes for free. A component that references colours works in one.

- Never write theme-specific CSS inside a component. If you need to, a semantic token is missing — say which.
- Test new work in light, dark and deep before considering it done.
- A scoped theme region must set its own background from --flux-surface-page or a layer-* token.
- Deep is a brand ground for slides and marketing, not a dark mode for dense UI.
## Composition discipline
No linter catches any of these. They are what makes correct output still look wrong.

Every value can come from a token and the result can still be visibly not-Kaptio. These are the specific habits that do it — the moves a model reaches for when it has been asked to make something look designed.

- No gradient fills on interface surfaces. Flat colour, or nothing.
- No decorative coloured bar along the edge of a card.
- No coloured dot beside a heading.
- No emoji as an icon system. Use a consistent icon set.
- No glow, no neon, no glassmorphism, no heavy blur behind content.
- No centred body copy. Centre a heading and a lede at most.
- No three-column feature grid of icon-plus-heading-plus-paragraph as a default layout.
- No badge on something that is not a status.
- Use eyebrows — the small uppercase label above a heading — and numbering sparingly. An eyebrow must add context the heading does not, so never put one above every heading or section. Number items only when order is the meaning, such as steps or a sequence, and never as section decoration like 01, 02, 03.
- No hero section with a gradient mesh background.
- Do not stack decoration: pick one of border, shadow, or fill change to signal a state.
- Do not add a container just to add a container. If it holds one thing, it is not grouping anything.
- Build every prototype view from documented Flux components. Prototype CSS places them — grid, flex, gap, spacing and size — and never draws a background, box border, radius or shadow, sets a font family, or restyles a .flux-* class. A class named like a component (booking-card, status-pill) is a hand-built copy of one. Run npx flux-check --prototype . before handoff.
- Do not nest boxes. A region has one bordered or filled surface, and everything inside it is grouped by spacing, a heading or a hairline divider — never by another bordered box. A Metric row inside a card drops its own surface automatically; do not rebuild one with borders. Count the outlines between the page edge and a value: more than one inside the page content means remove the inner ones.
- Do not remove a documented component’s internal padding. A parent inset does not replace the inset inside a card, note, table cell or action row.
- Do not turn every value into a card. Group related metrics on one surface with the Metric component and let the important exception carry the emphasis.
- Do not shrink the interface to show everything at once. Preserve readable type and row rhythm, then use scrolling, pagination or progressive disclosure for the remainder.
- Prefer one strong element over three competing ones. Density is not hierarchy.
## The self-check
One question catches most of it.

AskWould this render correctly with `data-flux-theme="dark"` on the root element?If any part would not, that part is referencing a primitive or a raw value, which is the underlying cause of most Flux violations. The theme question finds them without needing to audit line by line.

CheckWhy it failsNo raw hex, rgb() or named colourInvisible to every theme.No raw px, rem or ms where a token existsDiverges from the fluid root as the viewport grows.No Tailwind arbitrary valuesBypasses the token layer entirely.Lexend at 300 or 700 onlyAny other weight is synthesised into a font that is not Lexend.Interface radius is --flux-radius-smA 12px radius is the fastest way to stop looking like Kaptio.At most one yellow CTAA second one halves the value of the first.Focus outline presentRemoving it makes the interface unusable by keyboard.Native elements for controlsA styled div has none of a button’s behaviour.No transition: all, no scale on hoverAnimates properties nobody chose, and performs rather than confirms.
## Enforcing it
A rule that cannot fail a build is a suggestion.

The contract tells an agent what to do. The compliance check tells it when it did not, which is the half that actually changes behaviour — an agent that gets a failing exit code with a named rule and a fix will correct itself without being asked.

bashCopy`npx flux-check src/`It scans CSS, markup and component files for the violations that can be detected mechanically: raw colours, arbitrary Tailwind values, synthesised font weights,`transition: all`, removed focus outlines, gradients on interface surfaces, raw dimensions where a token exists, divs with click handlers, native selects and date inputs, help text below fields, and table headers without `scope`.

Rules are scoped to the context they can apply to, so prose that quotes a hex code in order to ban it is not reported. A linter that cries wolf gets switched off in a week. Where a violation is genuinely correct — a caret drawn with gradients so it can inherit`currentColor` — annotate it and say why:

cssCopy`/* Glyph, not a surface: gradients are the only way to inherit currentColor.
flux-ignore-next-line gradient */
background-image: linear-gradient(45deg, transparent 50%, currentColor 50%);`In CIThe check exits non-zero on any finding, so it works unchanged as a pipeline gate or a pre-commit hook. Flux runs it against its own source on every build.
## Machine sources
URLContents`https://flux.kaptio.com/llms.txt`This contract, complete, as plain text.`https://flux.kaptio.com/tokens/v2/flux.json`Every token as structured data.`https://flux.kaptio.com/tokens/v2/flux.css`The stylesheet to import.`https://flux.kaptio.com/components/source/.txt`Per-component markup, API, accessibility and tokens, as plain text.`https://flux.kaptio.com/components/`The human-readable component reference.`https://flux.kaptio.com/prototypes/brief.txt`A copyable product-prototype prompt that binds an agent to this contract.`https://flux.kaptio.com/decks/llms.txt`The deck contract. A separate surface with rules that deliberately differ. Read it instead of this file when building a presentation, never alongside it.Drop-in rule files for Cursor, Claude Code and Copilot are on [Repository rules](/for-ai/rules/).

[PreviousDecks](/patterns/decks/)[NextRepository rules](/for-ai/rules/)
