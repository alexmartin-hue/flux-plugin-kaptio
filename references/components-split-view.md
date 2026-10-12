# Flux — /components/split-view/

Source: https://flux.kaptio.com/components/split-view/

Component

# List and detail
A list of records beside the detail of the selected one, each pane scrolling on its own.

Plain-text source, for agents and clipboard use: [/components/source/split-view.txt](/components/source/split-view.txt)

## When to use it
For working through a queue: supplier requests, messages, tasks. The list stays in view while the detail changes, so moving to the next record is one click. Selecting an item marks it current and shows its panel. The split view responds to its own width rather than the viewport: below 32rem the list and the detail take turns, the detail gains a Back button, and focus follows the change of view.

Not thisNot when each record needs the full width or a URL of its own that people share; link to a detail page. Not for comparing two records side by side.
## Examples

### Supplier requests
Select a request to show it. Make the window narrow to see the panes take turns.

Hotel Rangá On request
KB-104931 · 6 rooms, 14 Sep

Fosshótel Glacier Lagoon Awaiting supplier
KB-104940 · 2 rooms, 19 Sep

Hótel Búðir Confirmed
KB-104957 · 8 rooms, 22 Sep

All requests

### Hotel Rangá

BookingKB-104931
Rooms6 double, 14–16 Sep
Requested3 days ago

Mark confirmed
Send reminder

All requests

### Fosshótel Glacier Lagoon

BookingKB-104940
Rooms2 twin, 19–20 Sep
RequestedYesterday

All requests

### Hótel Búðir

BookingKB-104957
Rooms8 double, 22–23 Sep
ConfirmedToday, 09:12

htmlCopy`

Hotel Rangá On request
KB-104931 · 6 rooms, 14 Sep

Fosshótel Glacier Lagoon Awaiting supplier
KB-104940 · 2 rooms, 19 Sep

Hótel Búðir Confirmed
KB-104957 · 8 rooms, 22 Sep

All requests
Hotel Rangá

BookingKB-104931
Rooms6 double, 14–16 Sep
Requested3 days ago

Mark confirmed
Send reminder

All requests
Fosshótel Glacier Lagoon

BookingKB-104940
Rooms2 twin, 19–20 Sep
RequestedYesterday

All requests
Hótel Búðir

BookingKB-104957
Rooms8 double, 22–23 Sep
ConfirmedToday, 09:12

`
## Anatomy
PartDescriptionContainerOne bordered surface with a fixed height. Each pane scrolls inside it.ListA labelled ul of item buttons, each with a title line and a line of metadata.ItemA button with aria-controls naming its panel and aria-current="true" when selected.DetailThe pane holding one panel per item. Only the selected one is shown.PanelA section with a heading, the record and its actions, plus a Back button that only appears when narrow.
## API
NameKindDescription`flux-split`classThe container. Its height is --flux-split-height.`data-flux-split`attributeWires selection, panels and the narrow view.`flux-split__list | __items`classThe list pane and its ul. Label the ul.`flux-split__item`classOn each button. Set aria-controls to its panel’s id.`flux-split__item-title | __item-meta | __ref`classThe title line, the metadata line and a mono reference inside it.`flux-split__detail | __panel`classThe detail pane and each panel. Hide all but the selected panel.`flux-split__back`classOn a button in each panel. Only shown when the container is narrow.`flux-split__title`classThe panel heading. Receives focus when the narrow view switches to it.`flux-split__actions`classThe record’s actions, below a hairline at the end of the panel.`data-view`attribute"list" or "detail", set by the script. Decides which pane shows when narrow.
## States
StateTreatmentItem hoverlayer-hover-01 fill.Item selectedsurface-selected fill that continues past the divider as a pointer at the detail, with aria-current="true".Narrow, listBelow 32rem of container width, only the list shows.Narrow, detailOnly the detail shows, with a Back button above its heading.
## Keyboard
KeysAction`Tab`Moves through the items, then into the detail.`Enter, Space`Selects the item and shows its panel. When narrow, focus moves to the panel heading.`Back button`Returns to the list and focuses the selected item.
## Accessibility

- Items are buttons, with aria-current="true" marking the selection so it is not conveyed by fill alone.
- Each panel is a section labelled by its heading.
- When the view switches in a narrow container, focus follows the switch so it is never left on a hidden element.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-split-list-width | -height | -bg | -border
- --flux-split-item-padding-y | -item-padding-x | -item-hover | -item-meta
- --flux-split-item-selected | -item-pointer-size
- --flux-split-detail-padding
## Do and don’t
Do

- Keep each item to a title line and a metadata line.
- Select the first item when the view opens, so the detail is never blank.
- Put the record’s actions in its panel, not in the list.Don’t

- Do not nest another bordered surface inside the detail; group with headings and hairlines.
- Do not use a split view for records people need to link to.[PreviousWalkthrough and storyboard](/components/walkthrough/)[NextFile upload](/components/file-upload/)
