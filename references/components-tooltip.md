# Flux — /components/tooltip/

Source: https://flux.kaptio.com/components/tooltip/

Component

# Tooltip and popover
A short label on hover or focus, and a small panel opened by a button.

Plain-text source, for agents and clipboard use: [/components/source/tooltip.txt](/components/source/tooltip.txt)

## When to use it
A tooltip names an icon-only control or adds a few words about it, on hover and on focus. A popover is a small panel anchored to its button, for a short task that should not leave the page: a confirmation with one choice, a quick setting. Both sit in the top layer, so no scroll container clips them, and both are placed beside their trigger by the script.

Not thisNot for explanation of a form field; that is the Input’s info bubble. Not for a list of actions; that is a menu. Not for anything with more than a couple of fields, or that needs the page to wait; that is a Modal. Not for content on something that cannot take focus, such as plain text.
## Examples

### Tooltips on icon-only buttons
The tooltip is the button’s name, so the button references it with aria-labelledby.

Export as CSV

Print manifesthtmlCopy`
Export as CSV

Print manifest`
### Popover
A short confirmation anchored to its button. Light dismiss, Escape and returning focus come from the platform.

Hold seats

### Hold 4 seats?

The seats are held for 48 hours, then released to sale.

Cancel
Hold seats

htmlCopy`Hold seats

Hold 4 seats?
The seats are held for 48 hours, then released to sale.

Cancel
Hold seats

`
## Anatomy
PartDescriptionTooltipA manual popover with role="tooltip": text-inverse on surface-inverse, one line where possible.TriggerA focusable control with data-flux-tooltip naming the tooltip’s id.PopoverA panel on surface-raised with a hairline and --flux-popover-shadow, opened with popovertarget.Popover partsAn optional title, a body in text-secondary, and actions aligned to the end.
## API
NameKindDescription`flux-tooltip`classOn an element with role="tooltip", an id and popover="manual".`data-flux-tooltip`attributeOn the trigger: the tooltip’s id. Opens it on hover and focus. Requires flux-components.js.`aria-labelledby / aria-describedby`attributelabelledby when the tooltip is the control’s name, describedby when it adds to a visible label.`flux-popover`classOn an element with popover, an id and role="dialog", opened by a button with popovertarget.`flux-popover__title`classOptional heading, referenced by aria-labelledby.`flux-popover__body`classThe text of the popover.`flux-popover__actions`classButtons, end-aligned. popovertargetaction="hide" closes without script.
## States
StateTreatmentTooltip openAbove the trigger, or below when there is no room; stays open while the pointer is over it.Popover openBelow the trigger, aligned to its end, flipped above when there is no room. aria-expanded follows.
## Keyboard
KeysAction`Tab`Focusing a trigger opens its tooltip; leaving it closes it.`Enter / Space`Opens or closes a popover. Focus moves to its first control.`Escape`Closes the tooltip or the popover; a popover returns focus to its button.
## Accessibility

- A tooltip opens on focus as well as hover, stays while the pointer is over it, and closes on Escape, as WCAG 1.4.13 requires.
- A tooltip holds text only. Anything interactive belongs in a popover.
- An icon-only button takes its name from its tooltip with aria-labelledby, so the name exists even when the tooltip is closed.
- Give a popover role="dialog" and a name, and keep it short enough that its controls are reached with a few Tabs.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-tooltip-bg | -text | -radius | -font-size | -padding-x | -padding-y | -max-width | -offset
- --flux-popover-width | -padding | -gap | -bg | -border | -shadow | -radius
## Do and don’t
Do

- Keep a tooltip to a few words: what the control does.
- Use a popover for one decision about the thing its button is on.Don’t

- Do not put the only copy of important information in a tooltip. It is invisible until someone looks for it.
- Do not open a popover on hover.
- Do not stack a popover on a popover.[PreviousEditable cell](/components/editable-cell/)[NextEmpty state](/components/empty-state/)
