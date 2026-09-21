# Flux — /patterns/composition/

Source: https://flux.kaptio.com/patterns/composition/

Patterns

# Composition discipline
Every value can come from a token and the result can still be visibly not Kaptio. This page is about that gap — the moves that get reached for when something needs to look designed, and why each one costs more than it returns.

## Correct and still wrong
Token compliance is necessary, not sufficient.

A card with `--flux-card-bg`, `--flux-card-radius` and`--flux-space-5` padding passes every check in the system. Add a gradient header, a coloured left edge and a dot beside the title, and it still passes — while looking like it came from somewhere else entirely.

None of these are catchable by a linter, which is exactly why they need to be written down. They are the difference between output that uses Flux and output that looks like Flux.

## The list
Each of these is a defect in Kaptio output.

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
## Stacked decoration
Pick one signal. Three signals for one state is noise, not emphasis.

cssCopy`/* Wrong. Four treatments competing to say the same thing. */
.card--selected {
border: 2px solid var(--flux-primary-400);
box-shadow: 0 0 0 4px var(--flux-primary-100);
background: linear-gradient(180deg, var(--flux-primary-50), var(--flux-white));
transform: translateY(-2px);
}

/* Right. One signal, stated once. */
.card--selected {
border-color: var(--flux-border-interactive);
background: var(--flux-surface-selected);
}`The instinct behind the first block is that a state should be obvious. But when every state shouts, none of them reads, and the interface starts to feel anxious. A selected card in Flux changes its border and its fill. That is enough, and it stays legible when twenty of them are on screen.

## Density is not hierarchy
One strong element beats three competing ones.

A common failure in generated layouts is treating every piece of content as equally important and then trying to make all of it prominent. The result is a page where the eye has nowhere to land: three headings at the same size, four cards with the same weight, two primary buttons.

Hierarchy is created by difference. If everything on a screen is bold, nothing is. Decide what the one thing is, give it the weight, and let everything else be quiet.

NoteA useful test: squint at the screen. You should be able to name the single most important element. If two or three compete, the hierarchy has not been decided yet.
## Preserve scanability
More visible data is not useful when the reader has to zoom in to identify it.

Generated operational screens often optimize for a screenshot: every summary, warning, metric and table is compressed into one viewport. That is not information density. It removes the type size, row rhythm and section boundaries that make dense information scannable.

Start with the documented component sizes. Keep table cells and controls at`text-sm` or larger, keep readable sentences at `text-base`, and use the seam gap between major sections. Let the page scroll. For long collections, use pagination or bounded disclosure; for wide tables, preserve the columns and scroll the wrapper horizontally.

Metrics do not each need a card. Put related values on one surface, align them for comparison, and reserve a fill change for the exception that needs attention.

CarefulNever scale the application shell with CSS `zoom` or`transform: scale()`. Responsive layout changes arrangement; it does not make the whole desktop interface smaller.
## Insets define containment
A surface begins at its edge. Its content begins one documented padding step inside.

Text, notes and controls touching a card or panel edge make separate regions collapse into one another. Use the documented component class and keep its padding token intact. A parent page gutter does not replace the inset inside a card, and a card inset does not replace the padding inside a nested note.

Tables are the structured exception: the wrapper reaches the surface edge while each header and data cell supplies its own inset. Intentional edge-to-edge media is the visual exception. Ordinary copy and controls are neither.

An action row uses the same inline inset as the content above and a spacing token between controls. If the actions do not fit, wrap or stack them; never remove the inset or push a button against the outer edge to keep one row.

NoteTrace the outer edge of a surface. No text or control should touch that line.
## Containers that hold one thing
A card around a single paragraph is not grouping anything.

htmlCopy`

Info
Deposits are taken at 20% of the total.

Deposits are taken at 20% of the total.

`Every container is a claim that the things inside it belong together and apart from everything else. When there is only one thing inside, the claim is empty, and the border just adds a line for the reader to process.

## Do and don’t
Do

- Decide what the one important element on a screen is, and give it the weight.
- Use one signal per state.
- Let quiet things be quiet. Most of an interface should recede.
- Preserve readable type and row rhythm, then let the page scroll.
- Keep every surface’s documented inset and align its action row to the content above.
- Group related metrics on one surface and emphasize only the exception.
- Group things in a container only when there is something to group.Don’t

- Do not add decoration to make something look designed.
- Do not use a gradient on an interface surface.
- Do not put a coloured bar or a dot on a card.
- Do not centre body copy.
- Do not reach for a three-column icon grid as a default layout.
- Do not shrink the whole interface to make every section visible at once.
- Do not remove component padding to make a layout fit.
- Do not put every metric in its own card.[PreviousAvatar](/components/avatar/)[NextForms](/patterns/forms/)
