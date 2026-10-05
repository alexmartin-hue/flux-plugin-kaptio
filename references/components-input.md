# Flux — /components/input/

Source: https://flux.kaptio.com/components/input/

Component

# Input
Single-line text entry, with the label, help and error pattern that goes with it.

Plain-text source, for agents and clipboard use: [/components/source/input.txt](/components/source/input.txt)

## When to use it
Collects a short, free-form value. The field, its label, and its help or error text are one unit and should be built together — a bare input is almost always a bug.

Not thisFor a value from a known, closed set use Select. For a long-form value use Textarea. For a boolean use Switch or Checkbox.
## Examples

### Default

Booking reference

htmlCopy`
Booking reference

`
### With an info bubble
Explanatory text goes behind the info button, not below the field. The bubble opens on hover, focus or tap, stays open while the pointer is over it, and closes on Escape. Reference it from the control with aria-describedby so a screen reader announces it with the field.

Supplier invoice reference *

Enter it exactly as printed on the invoice. Kaptio and the AP extract keep it unchanged.

htmlCopy`

Supplier invoice reference *

Enter it exactly as printed on the invoice. Kaptio and the AP extract keep it unchanged.

`
### Error
Bind the message to the field with aria-describedby so a screen reader announces it, and set aria-invalid so the state is not conveyed by colour alone.

Email *

Add the part after the @, for example kaptio.com.

htmlCopy`

Email *

Add the part after the @, for example kaptio.com.
`
### Disabled

Currency

Set by the departure, and not editable here.

htmlCopy`

Currency

Set by the departure, and not editable here.

`
## Anatomy
PartDescriptionLabelAlways present and always visible, above the field. Bold, small.Control36px tall, 4px radius, border-strong outline so the boundary clears 3:1.Info bubbleAn info button beside the label. Explanation, format and constraints open in a bubble on hover, focus or tap, never as text below the field.Error textThe only message below the field. Says what to do, not that something failed.
## API
NameKindDescription`flux-field`classWrapper binding label, control and message into one unit.`flux-field__label`classThe visible label. Required on every field.`flux-input`classThe control. Also applies to type=email, number, search, tel, url.`flux-field__header`classRow holding the label and its info button. Use it only when the field has an info bubble.`flux-info`classWrapper positioning the info button and its bubble.`data-flux-info`attributeInitialises hover, focus, tap and Escape behaviour. Requires flux-components.js.`flux-info__trigger`classIcon-only button. Its aria-label names the field: "About <field label>".`flux-info__bubble`classrole="tooltip", hidden by default. The explanation, in one or two sentences.`flux-field__help`classError text below the field, with data-tone="error". Not for explanation.`aria-invalid`attributeMarks the field invalid. Drives the error border.
## States
StateTreatmentDefaultborder-strong outline on field-bg.Hoverborder-interactive.Focus2px teal outline at 2px offset, from the global focus rule.Invalidborder-error, plus error text bound with aria-describedby.Disabledsurface-disabled fill at 60% opacity.Info openBubble on layer-01 with a subtle border and shadow-md, above the label. The info icon turns icon-brand.
## Keyboard
KeysAction`Tab`Moves focus into and out of the field, and onto its info button. Focusing the info button opens the bubble.`Escape`Closes an open info bubble. Where the field is a search or filter, clears it.
## Accessibility

- Every input needs a programmatically associated label. A placeholder is not a label — it disappears on focus and fails 4.5:1 by design.
- Error text must be referenced by aria-describedby, or a screen reader user will hear the field is invalid without hearing why.
- Never signal validity with colour alone; pair the border with aria-invalid and a message.
- Reference the info bubble from both its button and the control with aria-describedby, so the explanation is announced with the field. With an error, list the error first: aria-describedby="ref-error ref-info".
- The bubble meets WCAG 1.4.13: it opens on focus as well as hover, stays open while the pointer is over it, and closes on Escape. A tap pins it open for touch.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-field-height
- --flux-field-radius
- --flux-field-padding-x
- --flux-field-border
- --flux-field-border-hover
- --flux-field-border-error
- --flux-field-placeholder
- --flux-field-info-size
- --flux-field-info-icon
- --flux-field-info-bg
- --flux-field-info-text
- --flux-field-info-max-width
## Do and don’t
Do

- Keep one field height and one radius across an entire form.
- Put explanation, format and constraints in the info bubble beside the label, so the form keeps one rhythm.
- Size the field to the expected content where it aids scanning — a postcode field need not be full width.Don’t

- Do not use the placeholder as the label.
- Do not use a blue focus ring. Focus is Flux teal in every theme.
- Do not mark a field required with colour alone; use the asterisk and the required attribute.
- Do not put explanatory text below the field. Only an error message sits there.
- Do not put an action, a link or the only copy of critical information inside the bubble. It holds explanation the user can do without once they know the form.[PreviousButton](/components/button/)[NextSelect](/components/select/)
