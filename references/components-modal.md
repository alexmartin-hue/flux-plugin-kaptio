# Flux — /components/modal/

Source: https://flux.kaptio.com/components/modal/

Component

# Modal
A focused, interrupting dialog built on the native dialog element.

Plain-text source, for agents and clipboard use: [/components/source/modal.txt](/components/source/modal.txt)

## When to use it
Use when a decision must be made before anything else can continue — confirming a destructive action, or completing a short, self-contained task.

Not thisDo not use a modal for content the user might want to keep beside the page, for long forms, or for non-urgent information. Stacked modals are always a design failure.
## Examples

### Confirmation
Built on <dialog>, so focus trapping, Escape to close, inertness of the page behind and the backdrop all come from the platform.

## Cancel booking KB-104928?

The supplier will be notified and the deposit refund will follow your cancellation policy. This cannot be undone.

Keep booking
Cancel booking

htmlCopy`

Cancel booking KB-104928?

The supplier will be notified and the deposit refund will follow your cancellation policy. This cannot be undone.

Keep booking
Cancel booking

`
## Anatomy
PartDescriptionBackdropsurface-backdrop, from the theme.HeaderTitle and a divider.BodySecondary text. Scrolls if it must.FooterRight-aligned. Cancel first, primary action last.
## API
NameKindDescription`dialog`elementUse the native element. Open with showModal(), never by toggling a class.`flux-modal`classThe dialog surface, including its ::backdrop.`flux-modal__header`classDivided title row.`flux-modal__body`classContent region.`flux-modal__footer`classRight-aligned action row.
## States
StateTreatmentClosedNot rendered and not focusable.OpenPage behind is inert; focus moves into the dialog.
## Keyboard
KeysAction`Escape`Closes the dialog. Native behaviour — do not prevent it.`Tab`Cycles within the dialog only.
## Accessibility

- showModal() gives focus trapping, page inertness and Escape for free. A div-based modal has to reimplement all three and usually reimplements none.
- Give the dialog an accessible name via aria-labelledby pointing at the title.
- Return focus to the control that opened the dialog when it closes.
- The title states the consequence, so a screen-reader user hears what is at stake before the buttons.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-modal-radius
- --flux-modal-bg
- --flux-modal-shadow
- --flux-modal-backdrop
- --flux-modal-width-sm | -md | -lg
## Do and don’t
Do

- Name the consequence in the title, not "Are you sure?".
- Label the confirm button with the action itself, so it reads correctly out of context.Don’t

- Do not tint the backdrop with a brand colour.
- Do not open a modal from a modal.
- Do not put a form longer than a few fields inside one.[PreviousTable](/components/table/)[NextNote](/components/note/)
