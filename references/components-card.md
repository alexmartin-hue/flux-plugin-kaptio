# Flux — /components/card/

Source: https://flux.kaptio.com/components/card/

Component

# Card
Groups related content into one surface on the layer above.

Plain-text source, for agents and clipboard use: [/components/source/card.txt](/components/source/card.txt)

## When to use it
Use to separate one coherent object — a booking, a departure, a summary — from its neighbours. A card sits on the next layer up from its container, which is what makes nesting legible without hand-picked greys.

Not thisDo not wrap a whole page in a card, and do not use one to add decoration to a paragraph. If everything on the screen is a card, nothing is grouped.
## Examples

### Default

### September departures

Twenty-four departures are published for September, with three awaiting supplier confirmation.

htmlCopy`
September departures
Twenty-four departures are published for September, with three awaiting supplier confirmation.
`
### With actions

### Deposit schedule

A 20% deposit is taken at booking, with the balance due 60 days before departure.

Edit schedule
View history

htmlCopy`
Deposit schedule
A 20% deposit is taken at booking, with the balance due 60 days before departure.

Edit schedule
View history

`
### Interactive
When the whole card is a link, the border warms on hover and elevation caps at shadow-md.

[### Orvis — Iceland 2026

Eight itineraries, two brands, live since March.](#)htmlCopy`
Orvis — Iceland 2026
Eight itineraries, two brands, live since March.
`
## Anatomy
PartDescriptionContainerlayer-01 fill, hairline border-subtle, 4px radius, 20px padding.TitleBold, base size. Optional.BodySmall, secondary text.FooterOptional divided row for actions.
## API
NameKindDescription`flux-card`classThe container.`flux-card--interactive`classAdds hover affordance. Use on an anchor or button element.`flux-card__title`classOptional heading. Use a real heading level for document order.`flux-card__body`classSecondary body copy.`flux-card__footer`classDivided action row.
## States
StateTreatmentDefaultcard-bg on layer-01, hairline border.Hover (interactive only)border-interactive plus shadow-md. Nothing moves.Focus (interactive only)Global teal focus outline on the anchor.
## Keyboard
KeysAction`Tab`Reaches an interactive card once, not once per element inside it.`Enter`Follows the card link.
## Accessibility

- An interactive card must be a single anchor or button. Nesting several links inside a clickable div creates a keyboard trap and an unreadable accessible name.
- Use a real heading element for the title so the page outline is navigable; the class only styles it.
- A card is not a landmark. Do not give it role="region" unless it genuinely needs its own labelled section.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-card-radius
- --flux-card-padding
- --flux-card-bg
- --flux-card-border
- --flux-card-border-hover
- --flux-card-shadow-hover
## Do and don’t
Do

- Let the card take its fill from the layer tokens so it works on every ground.
- Keep one padding value across a grid of cards.
- Keep the footer aligned to the card inset and let its actions wrap when they no longer fit.Don’t

- Do not remove the card padding or position nested notes and actions against its outer edge.
- Do not add a coloured bar along one edge as decoration.
- Do not put a coloured dot beside the title.
- Do not stack a border, an inner glow and a heavy shadow on the same container.[PreviousDate picker](/components/date-picker/)[NextDescription list](/components/description-list/)
