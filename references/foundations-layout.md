# Flux — /foundations/layout/

Source: https://flux.kaptio.com/foundations/layout/

Foundations

# Layout & spacing
Everything sits on a 4px grid, and almost everything uses one of five steps from it. Consistent spacing is what makes a screen look designed rather than assembled, and it is the cheapest quality signal in the system.

## The 4px grid
Every spacing token is a multiple of 4px, expressed in rem so it scales with the fluid root.

A 4px base is small enough to describe dense product UI and large enough that arbitrary values stand out immediately. If a gap needs 14px, the answer is 12 or 16 — not a new token, and certainly not `14px`.

In practice most interfaces need five values. `space-2` between related items,`space-4` inside a component, `space-6` between components,`space-10` between groups, and the seam gap between sections. Reaching past those is a signal to look at the structure rather than the spacing.

## The spacing scale
TokenValueAt 16px root`--flux-space-0``0`0`--flux-space-px``1px`1px`--flux-space-1``0.25rem`4px`--flux-space-2``0.5rem`8px`--flux-space-3``0.75rem`12px`--flux-space-4``1rem`16px`--flux-space-5``1.25rem`20px`--flux-space-6``1.5rem`24px`--flux-space-8``2rem`32px`--flux-space-10``2.5rem`40px`--flux-space-12``3rem`48px`--flux-space-16``4rem`64px`--flux-space-20``5rem`80px`--flux-space-24``6rem`96px`--flux-space-32``8rem`128px
## Section rhythm
One value separates major sections, everywhere.

cssCopy`.section {
margin-top: var(--flux-seam-gap); /* 4.5rem */
}``--flux-seam-gap` is the distance between one idea and the next. It is deliberately larger than anything inside a section, so the eye can find a boundary without needing a rule or a background change to mark it.

Marketing surfaces may double it. Dense product UI may halve it. Nothing should invent a third value between them.

## Reflow, don’t scale
A viewport changes the arrangement, not the readable size of the interface.

Fitting the whole workflow above the fold is not a Flux goal. Never shrink type, row padding or the application shell until every section fits in one screenshot. Preserve the type scale and component rhythm, let sections continue down the page, and paginate long collections when the task benefits from it.

On a narrower viewport, columns reflow, controls wrap and a wide table scrolls inside its wrapper. Do not apply CSS `zoom` or a scaling transform to the page: both make the interface harder to read and leave its responsive structure unsolved.

NoteResponsive does not mean “show the same desktop canvas, smaller.” It means preserving legibility while changing the composition.
## Radius
Interface geometry is nearly square. 4px, and only 4px.

TokenValueUse`--flux-radius-none``0`Flush edges, full-bleed panels.`--flux-radius-xs``0.125rem``--flux-radius-sm``0.25rem`Every interface control: buttons, fields, cards, tables, notes.`--flux-radius-md``0.5rem`Modals and overlays.`--flux-radius-lg``0.75rem`Large marketing panels.`--flux-radius-xl``1rem`Display and imagery.`--flux-radius-2xl``1.5rem`Display and imagery.`--flux-radius-full``9999px`Pills and avatars only.Careful`radius-sm` covers almost all product work. A 12px or 16px radius on a button or a field is the single fastest way to make output stop looking like Kaptio.
## Measures and gutters
TokenValueUse`--flux-measure-prose`38remReading column.`--flux-measure-content`62remMixed content.`--flux-measure-wide`78remDashboards and full layouts.`--flux-gutter`clamp(1.25rem, 4vw, 3rem)Page inset. Fluid, so narrow screens are not wasteful and wide ones are not cramped.`--flux-hairline`1pxEvery border in the system. The one sanctioned px value.cssCopy`.page {
max-width: var(--flux-measure-wide);
margin-inline: auto;
padding-inline: var(--flux-gutter);
}`
## Do and don’t
Do

- Pick spacing from the scale, and reuse the same step for the same relationship.
- Use seam-gap between sections so every page has the same rhythm.
- Keep interface radius at radius-sm.
- Use the gutter token for page insets rather than a fixed padding.
- Reflow columns and wrap controls as the viewport narrows.Don’t

- Do not use an arbitrary px gap. If none of the steps fit, the structure is the problem.
- Do not mix two spacing steps for the same relationship on one screen.
- Do not shrink an application with CSS zoom or transform.
- Do not compress type or row spacing to put the whole workflow above the fold.
- Do not round product controls beyond 4px.
- Do not use radius-full on anything that is not a pill or an avatar.[PreviousTypography](/foundations/typography/)[NextElevation & layers](/foundations/elevation/)
