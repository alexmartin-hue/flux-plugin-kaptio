# Flux — /components/toast/

Source: https://flux.kaptio.com/components/toast/

Component

# Toast
A short confirmation that an action worked, with a way to undo it.

Plain-text source, for agents and clipboard use: [/components/source/toast.txt](/components/source/toast.txt)

## When to use it
Confirms an action whose result is not otherwise visible, such as a booking cancelled from a list or a manifest sent, and offers Undo while it is still cheap. It appears at the bottom corner, is announced politely, stays for a fixed time, and pauses while the pointer or focus is on it.

Not thisNot for errors; an error stays until it is resolved, so it goes in a Note or beside the field. Not for something the user must act on, or anything they must not miss; that is a Modal or a Note. Not to confirm what is already visible, such as a saved field that now shows its value.
## Examples

### Success with Undo
As rendered in the region. The static modifier only switches off the entrance for this page.

Booking KB-104933 cancelled.

Undo

htmlCopy`

Booking KB-104933 cancelled.

Undo

`
### Success without an action
When there is nothing to reverse, there is no action. The dismiss button stays.

Manifest sent to Anna Jónsdóttir.

htmlCopy`

Manifest sent to Anna Jónsdóttir.

`
### Information
Leave data-tone off for something that started rather than finished. The mark is the info icon in the brand colour.

Rates for Hotel Vík are being recalculated. This takes about a minute.

htmlCopy`

Rates for Hotel Vík are being recalculated. This takes about a minute.

`
### Long message
The message wraps; the icon and the actions stay on its first line. Two lines is the most a toast should need.

Departure KB-2026-09-14 moved to 21 September. Confirmations are resent to 14 passengers tonight.

Undo

htmlCopy`

Departure KB-2026-09-14 moved to 21 September. Confirmations are resent to 14 passengers tonight.

Undo

`
### Stacked
As the region shows them: the newest at the bottom, nearest the corner, and at most three. A fourth removes the oldest.

Rates for Hotel Vík are being recalculated. This takes about a minute.

Manifest sent to Anna Jónsdóttir.

Booking KB-104933 cancelled.

Undo

htmlCopy`

Rates for Hotel Vík are being recalculated. This takes about a minute.

Manifest sent to Anna Jónsdóttir.

Booking KB-104933 cancelled.

Undo

`
### Shown from a button
data-flux-toast shows a toast when the button is pressed. Undo dispatches flux-toast-action on the button. From script, dispatch a flux-toast event with the same fields. Press more than three to see the oldest leave.

Send manifest
Save itinerary
Recalculate rateshtmlCopy`Send manifest
Save itinerary
Recalculate rates`
## Anatomy
PartDescriptionRegionflux-toaster, a polite live region fixed to the bottom corner. Created by the script if the page has none.IconAn info mark, or a check for success.MessageOne sentence naming what happened and to what: "Booking KB-104933 cancelled."ActionOptional, at most one: usually Undo.DismissAn icon button with aria-label="Dismiss".
## API
NameKindDescription`flux-toaster`classThe region, with data-flux-toaster and aria-live="polite". Optional in markup; the script adds one.`flux-toast`classOne toast. data-tone="success" for a completed action; leave it off for neutral information.`data-flux-toast`attributeOn a button: the message to show when it is pressed. Pair with data-flux-toast-tone and data-flux-toast-action.`flux-toast event`elementdocument.dispatchEvent(new CustomEvent("flux-toast", { detail: { message, tone, action: { label, onSelect } } })).`flux-toast-action`elementEvent dispatched on a data-flux-toast button when its toast’s action is pressed.`flux-toast__actions`classHolds the action, a small ghost Button, and the dismiss button.`flux-toast--static, flux-toaster--static`classDraw a toast, or a stack, in the page flow without the entrance. For documentation only; a static region is not live.
## States
StateTreatmentEnteringFades in and rises by --flux-space-2 over --flux-duration-normal.WaitingStays for --flux-toast-duration, six seconds. The clock pauses while hovered or focused.LeavingFades out over --flux-duration-fast. At most three are shown; the oldest leaves first.
## Keyboard
KeysAction`Tab`Reaches the action and the dismiss button in the region, which pauses the timer.`Escape`Dismisses the focused toast.
## Accessibility

- The region is polite: the message is read after the current announcement, without moving focus.
- The region must be in the page before the first toast, or the first toast is not announced. The script creates it on load.
- Never put the only way to do something in a toast. Undo must also be reachable from the record, for anyone who misses it.
- Pausing on hover and focus gives time to read and to reach the action, as WCAG 2.2.1 asks.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-toast-width | -padding | -gap | -offset | -duration
- --flux-toast-bg | -border | -shadow | -icon | -icon-success | -icon-size
## Do and don’t
Do

- Name the record: "Booking KB-104933 cancelled", not "Done".
- Offer Undo for anything destructive that can still be reversed.
- Show one toast per action, after the action has succeeded.Don’t

- Do not use a toast for an error.
- Do not show a toast and a Note for the same event.
- Do not put links to elsewhere in a toast. It leaves before anyone gets there.[PreviousAccordion](/components/accordion/)[NextReorderable list](/components/reorder/)
