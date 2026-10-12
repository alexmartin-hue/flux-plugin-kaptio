# Flux — /components/empty-state/

Source: https://flux.kaptio.com/components/empty-state/

Component

# Empty state
What a region shows when it has nothing in it: why, and the one thing to do next.

Plain-text source, for agents and clipboard use: [/components/source/empty-state.txt](/components/source/empty-state.txt)

## When to use it
Replaces a blank table, list or panel with a short heading that says what is missing, one sentence on why or what fills it, and at most one action. It sits inside the surface that would have held the content, so the page keeps its structure. A first-use state invites the first record; a filtered state offers to clear the filters; a table keeps its headers and spans the empty state across every column.

Not thisNot for an error: say what failed and offer a retry in a Note. Not while content is loading; use a Skeleton or a Spinner. Not as an illustration-led marketing panel.
## Examples

### First use, in a card
The card keeps its title, so the page still reads as the same page. The body says what fills the region and the button does it.

## Departures

### No departures yet

Add the first departure for Golden Circle Classic, and it will appear here with its allocation and guide.

Add departure

htmlCopy`
Departures

No departures yet
Add the first departure for Golden Circle Classic, and it will appear here with its allocation and guide.

Add departure

`
### Filtered to nothing
When filters hide every row, say so and offer to clear them. The action is secondary: nothing is being created.

### No bookings match these filters

Nothing departs in October with the status Awaiting supplier.

Clear filters

htmlCopy`

No bookings match these filters
Nothing departs in October with the status Awaiting supplier.

Clear filters

`
### In a table
The headers stay, so the shape of the data is still clear. One cell spans every column and holds a compact empty state.

Supplier requests

Reference
Supplier
Status
Rooms

No open requests

Every supplier has answered. New requests appear here when a booking needs space confirmed.

htmlCopy`

Supplier requests

Reference
Supplier
Status
Rooms

No open requests
Every supplier has answered. New requests appear here when a booking needs space confirmed.

`
## Anatomy
PartDescriptionIconOptional. A 32px line icon in icon-secondary that names the kind of thing missing. Never an illustration.TitleA heading at the level the region needs, or a paragraph inside a table cell. States what is missing.BodyOne sentence, held to the reading measure.ActionsAt most one primary action, or a secondary action for a filtered state.
## API
NameKindDescription`flux-empty`classThe empty state. Place it inside the surface that would have held the content.`flux-empty__icon`classOn the svg. Optional.`flux-empty__title`classOn a heading, or a p inside a table cell.`flux-empty__body`classOne sentence.`flux-empty__actions`classThe action row.`flux-empty--compact`classLess vertical padding, for table cells, panels and filtered results.
## States
StateTreatmentFirst useNothing has been created. One primary action creates the first record.FilteredRecords exist but are hidden. A secondary action clears the filters.DoneNothing is waiting, which is good news. No action, and a sentence saying what would bring something back.
## Keyboard
KeysAction`Tab`Reaches the action, if there is one. The rest is not interactive.
## Accessibility

- Use a heading for the title when the region has headings of its own, at the next level down.
- When a search or filter empties the results, announce it through the live result count that the table or search already has.
- The icon is decorative and carries aria-hidden.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-empty-padding | -gap | -measure
- --flux-empty-icon | -icon-size
- --flux-empty-title-size | -body
## Do and don’t
Do

- Say what is missing in the title and what fills it in the body.
- Keep the region’s own heading, headers and toolbar in place.
- Offer the action that ends the empty state: create the first one, or clear the filters.Don’t

- Do not add an illustration, a mascot or a gradient panel.
- Do not offer more than one primary action.
- Do not centre more than the title and the one sentence below it.[PreviousTooltip and popover](/components/tooltip/)[NextBreadcrumbs](/components/breadcrumbs/)
