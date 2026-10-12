# Flux — /components/drawer/

Source: https://flux.kaptio.com/components/drawer/

Component

# Drawer
A full-height panel over the page, from its end edge, to read or edit one record without leaving the list.

Plain-text source, for agents and clipboard use: [/components/source/drawer.txt](/components/source/drawer.txt)

## When to use it
Shows a record, or a short task on it, while the page it came from stays in place behind. It is a native dialog opened with showModal(), so focus moves into it, the page behind is inert, Escape or a click outside closes it and focus returns to the button that opened it. The header names the record, the body scrolls on its own, and the action row stays pinned at the bottom.

Not thisNot for a decision that must be made before anything else; use a Modal. Not for a list and its detail that people move through one after another; use the List and detail split view, which keeps both visible. Not for a long task with steps; give it its own page or a wizard. Never open a drawer from a drawer.
## Examples

### Record
Opens over a list to show one booking. A click outside the drawer, the close button, Close or Escape all close it.

View KB-104931

## KB-104931

Golden Circle, 14 Sep · 12 passengers

Guide not assigned

The manifest cannot be sent until a guide is confirmed.

Lead passengerAnna Lindqvist
AgentNordic Trails
StatusOn request
Balance due€4,860.00

Close
[Open booking](#)

htmlCopy`View KB-104931

KB-104931
Golden Circle, 14 Sep · 12 passengers

Guide not assigned
The manifest cannot be sent until a guide is confirmed.

Lead passengerAnna Lindqvist
AgentNordic Trails
StatusOn request
Balance due€4,860.00

Close
Open booking

`
### Task
A form inside the drawer, with method="dialog" so Save closes it. Closing it any other way leaves the fields as they were, so reopening the drawer returns to what was typed.

Assign guide

## Assign a guide

DEP-0914 · Golden Circle, 14 Sep

Guide

Meeting point

Note to the guide

Cancel
Assign guide

htmlCopy`Assign guide

Assign a guide
DEP-0914 · Golden Circle, 14 Sep

Guide

Meeting point

Note to the guide

Cancel
Assign guide

`
## Anatomy
PartDescriptionOpenerA button with commandfor naming the drawer and command="show-modal".DrawerA dialog on surface-overlay with shadow-xl, full height at the end edge, 32rem wide or 48rem with flux-drawer--lg.HeaderThe title, an optional line of context, and a close button.BodyScrolls on its own between the header and the action row.Action rowPinned at the bottom, right-aligned. Cancel or Close first, the primary action last.
## API
NameKindDescription`dialog`elementThe native element. Open it with showModal(), never by toggling a class or the open attribute.`flux-drawer`classOn the dialog. Give it an id and aria-labelledby pointing at the title.`flux-drawer--lg`classThe wide drawer, for a record with a table in it.`flux-drawer__header | __heading | __title | __meta | __close`classThe header row: the heading block, its title and context line, and the close button.`flux-drawer__body`classThe scrolling content.`flux-drawer__footer`classThe pinned action row.`flux-drawer__form`classA form wrapping header, body and footer, so a submit button in the footer submits the fields in the body.`commandfor | command`attributeOn a button: the drawer’s id, and show-modal or close. flux-components.js supplies them where the browser does not.
## States
StateTreatmentClosedNot rendered and not focusable.OpenSlides in from the end edge over surface-backdrop. The page behind is inert.Narrow viewportNever wider than the viewport; on a phone it covers the screen.
## Keyboard
KeysAction`Escape`Closes the drawer. Native behaviour — do not prevent it.`Tab`Cycles within the drawer only.`Click outside`Closes the drawer. Requires flux-components.js.
## Accessibility

- showModal() traps focus, makes the page inert and handles Escape; a div-based drawer reimplements all three.
- Name the drawer with aria-labelledby pointing at its title, and give the close button an accessible name.
- Focus returns to the opener when the drawer closes. If the opener is removed, for instance because the record was deleted, move focus to the list it was in.
- Reduced motion removes the slide; the base layer handles it.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-drawer-width | -width-lg | -padding | -duration
- --flux-drawer-bg | -shadow | -backdrop | -divider
## Do and don’t
Do

- Title the drawer with the record’s reference or the task it performs.
- Keep the page behind as it was, so closing the drawer returns to the same place in the list.Don’t

- Do not open a drawer from a drawer, or a modal from a drawer for anything but a confirmation.
- Do not use a drawer for content people need beside the page while they work. Use the List and detail split view.
- Do not round the drawer’s corners or give it a border; it is an edge of the window, not a card.[PreviousModal](/components/modal/)[NextNote](/components/note/)
