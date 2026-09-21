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

textCopy`https://flux.kaptio.com/llms.txt`It is generated from the same sources as this site, so it cannot describe a system the site does not implement. Point an agent at it once and it has the complete system: 345 tokens across three tiers and three themes, the hard rules with their reasoning, the composition habits to avoid, and copyable markup for all twelve components.

NoteIndividual components are also published as plain text at`/components/source/.txt` — useful when you want one component in context rather than the whole system.
## The hard rules
Each of these is a defect if violated, not a preference. The premise is part of the rule.

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
- No hero section with a gradient mesh background.
- Do not stack decoration: pick one of border, shadow, or fill change to signal a state.
- Do not add a container just to add a container. If it holds one thing, it is not grouping anything.
- Do not remove a documented component’s internal padding. A parent inset does not replace the inset inside a card, note, table cell or action row.
- Do not turn every value into a card. Group related metrics on one surface and let the important exception carry the emphasis.
- Do not shrink the interface to show everything at once. Preserve readable type and row rhythm, then use scrolling, pagination or progressive disclosure for the remainder.
- Prefer one strong element over three competing ones. Density is not hierarchy.
## The self-check
One question catches most of it.

AskWould this render correctly with `data-flux-theme="dark"` on the root element?If any part would not, that part is referencing a primitive or a raw value, which is the underlying cause of most Flux violations. The theme question finds them without needing to audit line by line.

CheckWhy it failsNo raw hex, rgb() or named colourInvisible to every theme.No raw px, rem or ms where a token existsDiverges from the fluid root as the viewport grows.No Tailwind arbitrary valuesBypasses the token layer entirely.Lexend at 300 or 700 onlyAny other weight is synthesised into a font that is not Lexend.Interface radius is --flux-radius-smA 12px radius is the fastest way to stop looking like Kaptio.At most one yellow CTAA second one halves the value of the first.Focus outline presentRemoving it makes the interface unusable by keyboard.Native elements for controlsA styled div has none of a button’s behaviour.No transition: all, no scale on hoverAnimates properties nobody chose, and performs rather than confirms.
## Enforcing it
A rule that cannot fail a build is a suggestion.

The contract tells an agent what to do. The compliance check tells it when it did not, which is the half that actually changes behaviour — an agent that gets a failing exit code with a named rule and a fix will correct itself without being asked.

bashCopy`npx flux-check src/`It scans CSS, markup and component files for the violations that can be detected mechanically: raw colours, arbitrary Tailwind values, synthesised font weights,`transition: all`, removed focus outlines, gradients on interface surfaces, raw dimensions where a token exists, divs with click handlers, and table headers without `scope`.

Rules are scoped to the context they can apply to, so prose that quotes a hex code in order to ban it is not reported. A linter that cries wolf gets switched off in a week. Where a violation is genuinely correct — a caret drawn with gradients so it can inherit`currentColor` — annotate it and say why:

cssCopy`/* Glyph, not a surface: gradients are the only way to inherit currentColor.
flux-ignore-next-line gradient */
background-image: linear-gradient(45deg, transparent 50%, currentColor 50%);`In CIThe check exits non-zero on any finding, so it works unchanged as a pipeline gate or a pre-commit hook. Flux runs it against its own source on every build.
## Machine sources
URLContents`https://flux.kaptio.com/llms.txt`This contract, complete, as plain text.`https://flux.kaptio.com/tokens/v2/flux.json`Every token as structured data.`https://flux.kaptio.com/tokens/v2/flux.css`The stylesheet to import.`https://flux.kaptio.com/components/source/.txt`Per-component markup, API, accessibility and tokens, as plain text.`https://flux.kaptio.com/components/`The human-readable component reference.`https://flux.kaptio.com/prototypes/brief.txt`A copyable product-prototype prompt that binds an agent to this contract.`https://flux.kaptio.com/decks/llms.txt`The deck contract. A separate surface with rules that deliberately differ. Read it instead of this file when building a presentation, never alongside it.Drop-in rule files for Cursor, Claude Code and Copilot are on [Repository rules](/for-ai/rules/).

[PreviousDecks](/patterns/decks/)[NextRepository rules](/for-ai/rules/)
