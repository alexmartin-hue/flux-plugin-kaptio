# Flux — /components/skeleton/

Source: https://flux.kaptio.com/components/skeleton/

Component

# Skeleton
Flat placeholder shapes that hold the layout of content that is still loading.

Plain-text source, for agents and clipboard use: [/components/source/skeleton.txt](/components/source/skeleton.txt)

## When to use it
Shows the shape of what is coming when its layout is already known: a card, a list, the rows of a table. Each text line occupies exactly the line box of the text it stands in for, so the content replaces it without the page moving. The shapes pulse slowly in a layer fill, with no shimmer and no gradient, and the region says in words what is loading.

Not thisNot when the layout is not known in advance, such as search results that may be one row or none; use a Spinner. Not for a single value or control; use a small Spinner inside it. Not for anything that loads in under half a second.
## Examples

### Text
One flux-skeleton--text per line of the text that is coming. The last line of a paragraph runs short, so it reads as prose.

htmlCopy`

`
### Card
The card is the region. The title slot takes flux-card__title, so the line is the height of the heading that replaces it.

Loading departure

htmlCopy`
Loading departure

`
### List with avatars
flux-skeleton-row sets an avatar beside its lines: a name and a line of metadata.

Loading guides

htmlCopy`
Loading guides

`
### Table rows
The headers are real, because the columns are known; only the body waits. A cell’s line is inline, so it follows the cell’s alignment, including numeric columns.

Loading bookings

Bookings departing in September

Reference
Departure
Status
Pax
Total

htmlCopy`
Loading bookings

Bookings departing in September

Reference
Departure
Status
Pax
Total

`
### Block
flux-skeleton--block holds the place of a chart, a map or an image. To match what is coming, set --flux-skeleton-block-size on the region to another spacing token.

Loading occupancy chart

htmlCopy`
Loading occupancy chart

`
## Anatomy
PartDescriptionRegionThe element that will hold the content, with aria-busy="true" until it arrives.StatusA role="status" element naming what is loading, usually flux-visually-hidden.SlotAn aria-hidden element carrying the class of the text it replaces, such as flux-card__title, so the line takes that text’s size and line height.Shapeflux-skeleton with a modifier: a text line, an avatar or a block.
## API
NameKindDescription`flux-skeleton`classA shape. Always inside an aria-hidden element: the status carries the meaning.`flux-skeleton--text`classOne line, at cap height in the line box of the surrounding text. The last of several runs short.`flux-skeleton--short`classA short line, for a title or a name.`flux-skeleton--avatar`classA circle the size of a medium Avatar.`flux-skeleton--block`classA rectangle --flux-skeleton-block-size tall, for a chart, map or image.`flux-skeleton-row`classAn avatar beside a group of lines.`aria-busy="true"`attributeOn the region, removed when the content replaces the skeleton.
## States
StateTreatmentLoadingThe shapes pulse to half strength and back once every --flux-skeleton-duration.Reduced motionThe base layer runs the pulse once and it ends at full strength, so the shapes rest as still fills.LoadedThe content replaces the skeleton in place, and aria-busy is removed.
## Keyboard
KeysAction`—`Not interactive. Nothing inside a skeleton takes focus.
## Accessibility

- Put aria-busy="true" on the region and a role="status" element inside it that names what is loading.
- Mark every slot and shape aria-hidden. Empty headings or cells announced one by one say nothing useful.
- Keep real column headers in a loading table, so the structure is announced and only the data waits.
- The fill is a graphic with no text, so it relies on the status for meaning rather than on its contrast.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-skeleton-bg | -radius
- --flux-skeleton-block-size | -avatar-size
- --flux-skeleton-duration | -ease | -dim
## Do and don’t
Do

- Draw the layout that is actually coming: the same number of columns, a believable number of rows.
- Wait about half a second before showing a skeleton, so a fast response never flashes one.
- Replace the skeleton with a message and a retry action if loading fails.Don’t

- Do not add a shimmer, a gradient sweep or a glow.
- Do not show a skeleton and a Spinner for the same region.
- Do not skeleton what is already known, such as section headings, field labels and column headers.[PreviousProgress and meter](/components/progress/)[NextAccordion](/components/accordion/)
