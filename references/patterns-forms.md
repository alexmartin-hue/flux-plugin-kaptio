# Flux — /patterns/forms/

Source: https://flux.kaptio.com/patterns/forms/

Patterns

# Forms
A form is the densest thing most Kaptio users interact with, and the place where small inconsistencies compound fastest. Everything here follows from one idea: a field, its label and its message are a single unit.

## Field anatomy
Label above with its info button, control, error below. Always in that order.

Departure name *

Shown to travellers on the booking page.

Sales channel

Direct B2C

- Direct B2C

- Trade partner

- Agent network

Capacity

Capacity cannot exceed the vehicle limit of 16.

Cancel
Save departure

htmlCopy`

Departure name *

Shown to travellers on the booking page.

Sales channel

Direct B2C

Direct B2C
Trade partner
Agent network

Capacity

Capacity cannot exceed the vehicle limit of 16.

Cancel
Save departure

`Labels sit above the control rather than beside it. Top-aligned labels are faster to scan down, survive translation into longer languages, and do not force a second column decision on every form in the product.

Explanation lives in the info bubble beside the label, never as text below the field. If a field has a format constraint, put it there so it is one hover, focus or tap away while it is still cheap to comply with. The space below the field is reserved for errors, so a message there always means something needs fixing.

## Form layout
One column, unless two fields genuinely belong on one line.

cssCopy`.form {
display: grid;
gap: var(--flux-space-5);
max-width: 32rem;
}

/* Two fields on one row, only when they are one idea. */
.form__row {
display: grid;
grid-template-columns: 1fr 1fr;
gap: var(--flux-space-4);
}`A single column has one path through it, and it is unambiguous on every screen size. Put two fields side by side only when they are halves of one value — a date range, a first and last name, an amount and its currency.

Size a field to its expected content where that helps: a postcode field that is 32rem wide is telling the user something untrue about what goes in it.

## Validation
Validate on blur, clear on input, and never surprise someone mid-keystroke.

htmlCopy`
Capacity

Capacity cannot exceed the vehicle limit of 16.

`
- On blur, not on keystroke. Telling someone their email is invalid while they are still typing it is a interruption, not help.
- Clear the error as soon as they start fixing it. A message that persists while the user corrects the field reads as though the correction is not working.
- Say what to do. "Capacity cannot exceed the vehicle limit of 16" is useful. "Invalid value" is not.
- Bind the message. `aria-describedby` plus`aria-invalid`, or a screen reader user hears that something is wrong without hearing what.NeverA red border with no message. Colour alone is not a validation state, and it is unreadable for anyone who cannot distinguish it.
## Actions
Right-aligned, cancel first, primary last.

htmlCopy`
Cancel
Save departure
`The primary action goes last, closest to where the eye finishes and where the cursor already is. Cancel is a ghost button — it needs to be reachable, not prominent.

Label the primary action with what it does. "Save departure" survives being read out of context; "Submit" does not.

CarefulNever disable the submit button until the form is valid. It gives no explanation, hides which field is the problem, and is unreachable by keyboard. Let it submit, then show the errors.
## Destructive actions
Name the consequence, and put it in the button.

## Delete the Golden Circle departure?

Four bookings are attached to this departure and will need to be moved manually. This cannot be undone.

Keep departure
Delete departure

htmlCopy`

Delete the Golden Circle departure?

Four bookings are attached to this departure and will need to be moved manually. This cannot be undone.

Keep departure
Delete departure

`The title states what will happen, the body states what it costs, and the button repeats the verb. "Are you sure?" with Yes and No asks someone to remember what they clicked thirty seconds ago — and reads as nothing at all to a screen reader landing on the buttons.

## Do and don’t
Do

- Keep the label, control and message together as one unit.
- Put explanatory text in the info bubble beside the label.
- Use one column unless two fields are halves of one value.
- Validate on blur and clear on input.
- Write errors that say what to do.
- Put the primary action last, and label it with the verb.Don’t

- Do not use a placeholder as a label.
- Do not put explanatory text below a field. Only errors go there.
- Do not disable submit until the form is valid.
- Do not show a red border without a message.
- Do not validate on every keystroke.
- Do not label a destructive confirmation “Yes”.[PreviousComposition discipline](/patterns/composition/)[NextDecks](/patterns/decks/)
