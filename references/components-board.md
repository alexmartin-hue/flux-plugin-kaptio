# Flux — /components/board/

Source: https://flux.kaptio.com/components/board/

Component

# Board
Records as cards in columns by stage, moved between stages by drag or keyboard.

Plain-text source, for agents and clipboard use: [/components/source/board.txt](/components/source/board.txt)

## When to use it
Shows how many records sit at each stage of a process and lets people move one forward by moving its card. Each column is a stage with a count, each card is a record with its reference, name and key facts. Cards move by their handle: drag it, or focus it and use the keyboard. Every move is announced, the counts update, and the board dispatches flux-board-move so the product can save the new stage.

Not thisNot for a long list that people sort, filter and scan; use a Table with a status column. Not for reordering one list; use Reorder. Not when a stage change needs a reason or a confirmation every time; open a Modal from the card instead of letting a drag commit it.
## Examples

### Quotes by stage
Drag a card by its handle, or focus the handle, press Space, use the arrow keys and press Space to drop.

### Enquiry

2

QT-2208

Golden Circle, Nordic Trails

Departs 14 Nov24 passengers

QT-2214

Ring Road self-drive, Lindqvist family

Departs 2 Dec4 passengers

### Quoted

3

QT-2190

Northern Lights, Polar Agency

Departs 21 Nov18 passengers

QT-2197

South Coast, Aurora Schools

Departs 9 Jan36 passengers

QT-2201

Snæfellsnes, private group

Departs 12 Dec8 passengers

### On request

1

QT-2176

Glacier walk, Nordic Trails

Departs 18 Nov12 passengers

### Confirmed

1

KB-104931

Golden Circle, Anna Lindqvist

Departs 14 Sep12 passengers

Press Space to pick the card up. The arrow keys move it within a column and between columns. Press Space to drop it, or Escape to put it back.

htmlCopy`

Enquiry
2

QT-2208

Golden Circle, Nordic Trails
Departs 14 Nov24 passengers

QT-2214

Ring Road self-drive, Lindqvist family
Departs 2 Dec4 passengers

Quoted
3

QT-2190

Northern Lights, Polar Agency
Departs 21 Nov18 passengers

QT-2197

South Coast, Aurora Schools
Departs 9 Jan36 passengers

QT-2201

Snæfellsnes, private group
Departs 12 Dec8 passengers

On request
1

QT-2176

Glacier walk, Nordic Trails
Departs 18 Nov12 passengers

Confirmed
1

KB-104931

Golden Circle, Anna Lindqvist
Departs 14 Sep12 passengers

Press Space to pick the card up. The arrow keys move it within a column and between columns. Press Space to drop it, or Escape to put it back.`
## Anatomy
PartDescriptionBoardA focusable horizontal scroll region of columns.ColumnA section named by its heading, with a mono count and an ordered list of cards on layer-02.CardA layer-01 list item with a hairline: mono reference, handle, name and meta.HandleA button named “Move” and the reference, described by the instructions.Lifted cardshadow-md and an interactive border while it is being moved.
## API
NameKindDescription`flux-board`classThe board. data-flux-board adds dragging, keyboard moves, announcements and counts. Give it role="region", a name and tabindex="0".`flux-board__column | __header | __title | __count`classA stage: its section, heading row, heading and count.`flux-board__cards`classThe ordered list of cards in a stage. It keeps a minimum height so an empty stage is still a drop target.`flux-board__card | __ref | __name | __meta`classA card and its reference, name and facts.`flux-board__handle`classThe move button. aria-pressed is true while the card is lifted.`flux-board-move`attributeEvent dispatched on the board after a move. detail holds card, from and to columns, and index.
## States
StateTreatmentRestinglayer-01 card with a hairline.Liftedshadow-md and border-interactive; the handle turns brand and aria-pressed is true.Empty stageThe column keeps its list ground so it can still be dropped into.
## Keyboard
KeysAction`Space / Enter`On a handle, picks the card up; pressed again, drops it.`Arrow Up / Arrow Down`Moves the lifted card within its column.`Arrow Left / Arrow Right`Moves the lifted card to the previous or next column.`Escape`Puts the lifted card back where it was.
## Accessibility

- Every pick-up, move and drop is announced with the column and position, through an assertive live region.
- The handle carries the instructions through aria-describedby.
- Columns are sections named by their headings, so a screen reader can jump between stages.
- Offer another way to change a stage too, such as a status select on the record, for people who cannot drag.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-board-column-width | -gap | -column-bg | -column-padding
- --flux-board-card-bg | -card-border | -card-padding | -card-gap
- --flux-board-lifted-shadow | -drop-border
## Do and don’t
Do

- Order columns the way records move, left to right.
- Save on flux-board-move and move the card back if the save fails, with an error toast.Don’t

- Do not put a status badge on a card; the column is the status.
- Do not colour columns. The stage name and count carry it.[PreviousReorderable list](/components/reorder/)[NextEditable cell](/components/editable-cell/)
