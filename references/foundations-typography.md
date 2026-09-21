# Flux — /foundations/typography/

Source: https://flux.kaptio.com/foundations/typography/

Foundations

# Typography
Lexend Light carries everything Kaptio says. Lexend Bold carries what matters. JetBrains Mono carries what a machine produced. Three jobs, two families, and no weight in between.

## Two voices
A sans that speaks, and a mono that reports.

Flux 1.x had one family and two weights, which kept output consistent but left no way to distinguish a booking reference from a sentence. Everything looked like prose, including the things that were not.

2.0 promotes JetBrains Mono Variable from a code font to a documented second voice. It carries identifiers, metadata, structural labels and values — anything that is data rather than language. Look at the eyebrow above this page's title, or the column headers in any Flux table: that is the second voice doing its job.

## Lexend
Two weights. Nothing between them, and nothing outside them.

Lexend Light 300 — the default voice

Lexend Bold 700 — headings and emphasis

htmlCopy`
Lexend Light 300 — the default voice

Lexend Bold 700 — headings and emphasis
`Light is the default for everything, headings included. Bold is for headings that need to anchor a page, for emphasis inside a sentence, for labels, and for table headers.

There is no 400, 500 or 600. A request for a weight Flux does not load gets synthesised by the browser into something that is not Lexend, which is why the base layer forces every bold element back to 700.

cssCopy`/* From flux.css. This is enforced, not suggested. */
b, strong, h1, h2, h3, h4, h5, h6, th {
font-weight: var(--flux-weight-bold);
}`
## JetBrains Mono
Three weights, because the second voice has its own hierarchy.

400 Regular — code, values, raw output

500 Medium — inline metadata, badges, keyboard hints

700 Bold — structural labels, small and letter-spaced

htmlCopy`
400 Regular — code, values, raw output

500 Medium — inline metadata, badges, keyboard hints

700 Bold — structural labels, small and letter-spaced
`WeightTokenUse400 Regular`--flux-weight-mono-regular`Code blocks, raw values, identifiers in body copy.500 Medium`--flux-weight-mono-medium`Inline metadata, version numbers, keyboard hints, table figures.700 Bold`--flux-weight-mono-bold`Eyebrows, column headers, section labels. Always small, uppercase and letter-spaced.CarefulThe mono voice is for data, not for volume. Uppercase mono at`text-lg` or larger reads as a warning label. Keep the bold, letter-spaced form at`text-xs`.
## The scale
TokenSizeTypical use`--flux-text-xs``0.75rem`Short metadata, badges, help text`--flux-text-sm``0.875rem`Dense UI, table cells, secondary copy`--flux-text-base``1rem`Body`--flux-text-lg``1.125rem`Lede, card titles`--flux-text-xl``1.25rem`Subsection headings`--flux-text-2xl``1.5rem`Section headings`--flux-text-3xl``1.875rem`Page headings, dense layouts`--flux-text-4xl``2.25rem`Page headings`--flux-text-5xl``3rem`Marketing display`--flux-text-6xl``3.75rem`Slide displaySizes are in `rem`, and the root is fluid — see below. A`text-base` paragraph is 16px on a laptop and 19px on a large display, without a media query.

Careful`text-xs` is not a compact body size. Reserve it for badges, help text and short metadata. Controls, table cells and compact secondary copy start at `text-sm`; sentences intended to be read use `text-base`. If content does not fit, reflow or scroll it rather than shrinking the type.
## The fluid root
Every rem in Flux scales. This is the one place the system reaches past tokens into a base rule.

cssCopy`html {
font-size: clamp(16px, 0.875rem + 0.4vw, 19px);
}`Type, spacing and component heights all move together, because they are all expressed in`rem`. A dashboard on a 27-inch display gets a proportionally larger interface rather than the same 16px interface with more empty space around it.

The consequence to remember: never mix a `px` value into a layout built from Flux spacing. It will not scale with everything around it, and the gap will widen as the viewport does. The one sanctioned exception is`--flux-hairline`, which is 1px on purpose.

## Measure and leading
TokenValueUse`--flux-measure-prose`38remReading column. Roughly 70 characters.`--flux-measure-content`62remMixed content: tables, cards, specimens.`--flux-measure-wide`78remFull-bleed layouts and dashboards.`--flux-leading-tight`1.15Display headings.`--flux-leading-snug`1.3Headings and dense labels.`--flux-leading-normal`1.55Interface default.`--flux-leading-relaxed`1.7Body copy meant to be read.NoteLexend was drawn for reading proficiency, and it rewards air. Body copy at`leading-relaxed` inside `measure-prose` is the combination the rest of the system is tuned around.
## Do and don’t
Do

- Use Lexend 300 for everything, and 700 when something has to anchor.
- Reach for the mono voice when the content is data rather than language.
- Keep body copy inside measure-prose at leading-relaxed.
- Use at least text-sm for controls and table cells, and text-base for readable sentences.
- Use tracking-tight on headings at text-3xl and above.Don’t

- Do not request a Lexend weight other than 300 or 700.
- Do not set mono uppercase above text-xs.
- Do not use text-xs for paragraphs, table cells, controls or primary values.
- Do not shrink type to fit more content above the fold.
- Do not mix px into a layout built from rem tokens.
- Do not use a second sans-serif family. There is one.[PreviousColour](/foundations/color/)[NextLayout & spacing](/foundations/layout/)
