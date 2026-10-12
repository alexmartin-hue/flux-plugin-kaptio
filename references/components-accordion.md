# Flux — /components/accordion/

Source: https://flux.kaptio.com/components/accordion/

Component

# Accordion
Page sections that open and close under their own headings.

Plain-text source, for agents and clipboard use: [/components/source/accordion.txt](/components/source/accordion.txt)

## When to use it
Lets a long page of reference material show its outline first and its detail on demand: supplier terms, policy sections, setup steps someone returns to. Built on details and summary, so it opens without the script, works with find-in-page, and needs no ARIA.

Not thisNot for content everyone needs to read; leave it open on the page. Not for switching between views of one thing; that is Tabs. Not for a row of a table; the Table has its own expandable rows. Not for steps that must be done in order; that is a Flow.
## Examples

### Supplier terms
The first section opens by default because it is the one most people come for. Give the details elements the same name to let only one open at a time.

Cancellation3 rules

Free cancellation up to 30 days before arrival. 50% of the stay is charged from 29 to 8 days, and the full stay from 7 days.

Payment2 rules

A 30% deposit secures the allocation. The balance is due 45 days before arrival, by bank transfer.

Release dates1 rule

Unsold rooms in the allocation return to the hotel 21 days before arrival.

htmlCopy`

Cancellation3 rules

Free cancellation up to 30 days before arrival. 50% of the stay is charged from 29 to 8 days, and the full stay from 7 days.

Payment2 rules

A 30% deposit secures the allocation. The balance is due 45 days before arrival, by bank transfer.

Release dates1 rule

Unsold rooms in the allocation return to the hotel 21 days before arrival.

`
## Anatomy
PartDescriptionAccordionThe list of sections, with a hairline above the first and below each one. No box around it.SummaryThe always-visible line: the title, optional mono metadata, and a chevron that turns when open.PanelThe content, in text-secondary, indented by nothing so it aligns with the title.
## API
NameKindDescription`flux-accordion`classThe wrapper around the sections.`flux-accordion__item`classA details element. Add open to start it open, and a shared name to make the group exclusive.`flux-accordion__summary`classThe summary element.`flux-accordion__title`classThe section title, in bold.`flux-accordion__meta`classOptional mono metadata such as a count, in text-secondary.`flux-accordion__icon`classThe chevron svg, aria-hidden. Turns 180° when the section is open.`flux-accordion__panel`classThe content of the section.
## States
StateTreatmentClosedTitle and metadata only.HoverThe title turns text-brand. Colour only; nothing moves.OpenThe chevron turns and the panel shows. The height does not animate.
## Keyboard
KeysAction`Tab`Moves between summaries, then into an open panel’s links and controls.`Enter / Space`Opens or closes the focused section.
## Accessibility

- details and summary give the expanded state and the keyboard behaviour without ARIA. Do not add role or aria-expanded.
- Put the accordion under a real heading for the page outline. A summary is a button to assistive technology, so a heading inside it is not announced as one.
- Closed content is still found by find-in-page, which opens its section.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-accordion-divider | -padding-y | -panel-padding
- --flux-accordion-title-size | -title-hover | -icon | -meta
## Do and don’t
Do

- Write titles that let someone find their section without opening the others.
- Open the section most people come for.
- Keep each panel short. If a panel needs its own headings, it is a page.Don’t

- Do not put a form inside a closed section that must be completed. Required fields cannot hide.
- Do not put each section in a card. Hairlines separate them.
- Do not nest an accordion inside an accordion.[PreviousSkeleton](/components/skeleton/)[NextToast](/components/toast/)
