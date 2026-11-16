# Flux — /components/quantity/

Source: https://flux.kaptio.com/components/quantity/

Component

# Quantity
A small whole number set with minus and plus buttons, or typed: travellers, rooms, nights.

Plain-text source, for agents and clipboard use: [/components/source/quantity.txt](/components/source/quantity.txt)

## When to use it
A quantity sets a count that is usually small and usually changes by one: adults and children in a room, the number of rooms, extra nights. Minus and plus buttons step it within its bounds, and the number between them is a text field with role="spinbutton", so it can also be typed, and the arrow keys step it. A button turns disabled at its bound, so the limit is visible rather than discovered.

Not thisNot for a large or exact number such as a price or an allocation of 120 seats; use an Input with inputmode="numeric", which is faster to type. Not where the position within a range matters more than the figure; use a Slider. Not for a choice between a few named options; use a Segmented control.
## Examples

### Default

Adults

htmlCopy`
Adults

`
### With an explanation
What counts and the limits go in the info bubble beside the label. At its minimum the minus button is disabled, so the bound is visible.

Children

Ages 2 to 11 on the day of departure. A room takes up to four children.

htmlCopy`

Children

Ages 2 to 11 on the day of departure. A room takes up to four children.

`
### Disabled

Rooms

htmlCopy`
Rooms

`
## Anatomy
PartDescriptionLabelVisible, above the control, naming what is counted: "Adults", not "Number".Minus and plusIcon buttons in icon-brand on either side of the value, each a field-height square. Each names its action with the noun: "Fewer adults".ValueA narrow field with the border-strong outline, the number centred in tabular figures. Typing replaces it; leaving the field brings it back within bounds.Info bubbleThe bounds and what counts, such as the ages a child covers, beside the label, never as text below.
## API
NameKindDescription`flux-quantity`classThe row holding the two buttons and the value field, inside a flux-field with its label.`data-flux-quantity`attributeWires the buttons, the arrow keys and the bounds to the field. Requires flux-components.js.`flux-quantity__input`classOn an input type="text" with inputmode="numeric" and role="spinbutton". Write value and aria-valuenow, plus aria-valuemin and aria-valuemax for the bounds.`flux-quantity__button`classOn each button type="button", with tabindex="-1", aria-controls naming the field, and an aria-label that names the action and the noun.`data-flux-quantity-step`attribute"down" on the minus button, "up" on the plus button.`data-flux-quantity-step-size`attributeOptional, on the wrapper. The amount one press adds or removes. Defaults to 1.
## States
StateTreatmentDefaultIcons in icon-brand; the value field in border-strong on field-bg.HoverA button fills with surface-brand-subtle; the field outline turns border-interactive.FocusThe Flux focus ring around the value field, from the global focus rule.At a boundThe button that would leave the range is disabled and its icon turns icon-disabled.DisabledThe field takes the disabled field style and both buttons are disabled.
## Keyboard
KeysAction`Arrow Up / Arrow Down`Adds or removes one step.`Page Up / Page Down`Adds or removes ten steps, within the bounds.`Home / End`Sets the minimum or the maximum.`Digits`Type a value. Leaving the field, or pressing Enter, brings it back within bounds.`Tab`Moves to the value field and on. The buttons are not tab stops, because the arrow keys do what they do.
## Accessibility

- The value is a text field with role="spinbutton", aria-valuenow, aria-valuemin and aria-valuemax, so it is announced as a number in a range and keeps its label. flux-components.js keeps aria-valuenow current.
- Do not use input type="number". Its spin arrows draw in the operating system style, and a scroll wheel over it changes the value by accident.
- The buttons stay reachable by pointer, touch and screen reader. They leave the tab order because the field already steps on the arrow keys, as the ARIA spinbutton pattern recommends.
- Each button names its action with the noun, "Fewer adults" and "More adults", so it makes sense out of context.
- On a coarse pointer the buttons and the field grow to the touch target with the field height.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-quantity-gap | -input-width | -icon-size
- --flux-quantity-icon | -icon-disabled | -button-bg-hover
- --flux-field-height | -border | -border-hover | -radius
## Do and don’t
Do

- Set bounds that match the business rule, and say them in the info bubble when they are not obvious.
- Write value and aria-valuenow into the markup, so the page reads correctly before the script runs.
- Group related counts, such as adults, children and infants, under one heading for the room they fill.Don’t

- Do not use a quantity for a number people usually type, such as a price or a large allocation.
- Do not hide the bounds and let a press silently do nothing. The button at a bound is disabled.
- Do not explain the count in text below the control. Use the info bubble.[PreviousSlider](/components/slider/)[NextSearch](/components/search/)
