# Flux — /components/editable-cell/

Source: https://flux.kaptio.com/components/editable-cell/

Component

# Editable cell
A table value that is edited where it is shown, with saving and error states.

Plain-text source, for agents and clipboard use: [/components/source/editable-cell.txt](/components/source/editable-cell.txt)

## When to use it
Lets someone correct many values without leaving the table: a rate matrix, allocations by date, prices by room type. The value is a button until it is activated, then an input; Enter saves, Escape cancels, and the cell shows that it is saving and, if the save fails, why, with the value still there to fix.

Not thisNot for values that depend on each other and must be saved together; use a form with one Save. Not for long text. Not for the only copy of a value that needs review before it changes; open a Modal with the field and its consequences.
## Examples

### Rate matrix
Each rate is one editable cell. Without a flux-edit listener a value saves at once; a listener calls event.detail.waitUntil(request) to show saving, and rejects with an Error to show its message.

Hotel Vík, rates per night in ISK. Select a rate to change it.

Room
12 Sep
13 Sep
14 Sep
15 Sep

Double
Edit Double, 12 Sep: 32,000
Edit Double, 13 Sep: 32,000
Edit Double, 14 Sep: 34,500
Edit Double, 15 Sep: 34,500

Twin
Edit Twin, 12 Sep: 30,500
Edit Twin, 13 Sep: 30,500
Edit Twin, 14 Sep: 33,000
Edit Twin, 15 Sep: 33,000

Single
Edit Single, 12 Sep: 24,000
Edit Single, 13 Sep: 24,000
Edit Single, 14 Sep: 26,000
Edit Single, 15 Sep: 26,000

htmlCopy`

Hotel Vík, rates per night in ISK. Select a rate to change it.

Room
12 Sep
13 Sep
14 Sep
15 Sep

Double
Edit Double, 12 Sep: 32,000
Edit Double, 13 Sep: 32,000
Edit Double, 14 Sep: 34,500
Edit Double, 15 Sep: 34,500

Twin
Edit Twin, 12 Sep: 30,500
Edit Twin, 13 Sep: 30,500
Edit Twin, 14 Sep: 33,000
Edit Twin, 15 Sep: 33,000

Single
Edit Single, 12 Sep: 24,000
Edit Single, 13 Sep: 24,000
Edit Single, 14 Sep: 26,000
Edit Single, 15 Sep: 26,000

`
### States
View, editing, saving and error, rendered as the script leaves them.

StateDouble, 12 Sep

View
Edit Double, 12 Sep: 32,000

Editing

Saving
Edit Double, 12 Sep: 34,000Saving

Error
Below the contracted minimum of 28,000.

htmlCopy`

StateDouble, 12 Sep

View
Edit Double, 12 Sep: 32,000

Editing

Saving
Edit Double, 12 Sep: 34,000Saving

Error
Below the contracted minimum of 28,000.

`
## Anatomy
PartDescriptionValueA button showing the value, with visually hidden text naming what it edits. Outlined in border-strong on hover.InputAn Input sized to the cell, labelled with the cell’s row and column.SavingThe new value in text-secondary with a small Spinner, announced as Saving.ErrorThe input stays open with the attempted value, aria-invalid, and the reason below it.
## API
NameKindDescription`flux-editable`classOn the td. data-state is view, editing, saving or error. Add data-numeric for figures.`data-flux-editable`attributeThe cell’s label, such as "Double, 12 Sep", used to name the input. Wires editing. Requires flux-components.js.`flux-editable__value`classThe button. Holds a flux-visually-hidden "Edit <label>: " span and the flux-editable__text span.`flux-editable__text`classThe displayed value. The script reads and writes it.`flux-editable__input`classAdded with flux-input while editing.`flux-edit event`elementCancelable, dispatched on the cell on save with detail.value, detail.previous and detail.waitUntil(promise). Cancel it to keep the field open.
## States
StateTreatmentViewThe value, outlined in border-strong on hover and focus.EditingAn input in place, with its text selected.SavingThe new value in text-secondary, the button disabled, a small Spinner at the start of the cell.ErrorThe input reopens with the attempted value, the reason below it, and focus in the field.
## Keyboard
KeysAction`Enter / Space`On a value, starts editing.`Enter`In the input, saves and returns focus to the value.`Escape`Cancels and returns focus to the value, unchanged.`Tab`Saves and moves to the next cell.
## Accessibility

- Each value is a button whose name says what it edits and what it holds: "Edit Double, 12 Sep: 32,000".
- The input is labelled with the cell’s row and column, so it makes sense on its own.
- Saving is announced through a status element; an error is bound to the input with aria-describedby.
- Keep row and column headers with scope, so a screen reader moving through the grid hears both.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-editable-padding-x | -radius | -border-hover | -saving-text
- All --flux-table-* tokens, for the cells.
## Do and don’t
Do

- Validate on the server and return a message that says what is allowed: "Below the contracted minimum of 28,000."
- Keep the attempted value in the field when a save fails, so it can be corrected rather than retyped.
- Format figures in the cell the same way before and after editing.Don’t

- Do not save on every keystroke.
- Do not show an input in every cell at once. A grid of inputs reads as a form and loses the row rhythm.
- Do not mark editable cells with a colour fill. The hover outline and the button are enough.[PreviousBoard](/components/board/)[NextTooltip and popover](/components/tooltip/)
