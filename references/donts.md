# Flux — /donts

Source: https://flux.kaptio.com/donts

[Flux](/)
Guidelines

# Don'ts

Flux documents what we do use. This page lists common mistakes, legacy ideas, and
invented details that sometimes appear in mockups, AI output, or ad hoc designs. If something
is not defined in Foundations, Components, or Patterns, treat it as out of scope unless
design explicitly adds it here or in Figma.

For implementations and tooling

Prefer tokens from [Token Reference](/foundations/tokens)
and documented components. Do not infer extra chrome (accent borders on one edge only, novel
colour names, or layout blocks that are not in this site) as part of Flux.

## Colours and tokens

Do not introduce colours that are not defined in
[Colours](/foundations/colors)
or the token source. No one-off hex or RGB values for brand UI unless they map to an existing token.

Do not use made-up token names (for example invented semantic keys) in code or copy. Use the
names and CSS variables from the published token list.

Do not assume product accents from marketing screenshots apply globally; product colours are
scoped per product in [Products](/products).

## Containers, cards, and borders

Do not add decorative treatments that are not described in Flux, such as a thick or coloured
border on only one edge of a box (for example a “stroke top” or top accent bar on
cards). Standard surfaces use the patterns in
[Card](/components/card)
and related components unless design ships an explicit pattern.

Do not use small solid coloured dots or circles beside headings or labels inside cards, panels,
or other boxed content (for example a teal marker next to a section title). Rely on typography
hierarchy and spacing from
[Typography](/foundations/typography)
instead of decorative bullets that look like ad hoc status indicators.

Do not stack multiple competing outlines, inner glows, and heavy shadows on the same container;
elevation should follow [Shadows](/foundations/shadows).

Do not use arbitrary corner radii or spacing; use the spacing scale and component specs in Foundations.

## Layout and page sections

Do not invent new section types, hero variants, or navigation models that are not documented
under Components or Patterns.

Do not treat the marketing Flux site layout (for example showcase sections on this documentation
site) as the default app shell for product UIs unless product design specifies it.

## Typography and iconography

Do not substitute typefaces outside the scale in
[Typography](/foundations/typography).

Do not mix ad hoc icon styles or emoji as the primary icon system in product UI; follow
[Iconography](/foundations/iconography).

Do not use light grey, yellow, or any colour other than Kaptio dark for text on light backgrounds.

## Keeping this list current

When review or tooling keeps proposing the same incorrect pattern, add a short bullet under the
right heading above so humans and assistants share one source of truth. For new allowed patterns,
add or update the relevant Foundations, Component, or Pattern page instead of only listing a
negative here.
