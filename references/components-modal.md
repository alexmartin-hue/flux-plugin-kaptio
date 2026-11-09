# Flux — /components/modal/

Source: https://flux.kaptio.com/components/modal/

Component

# Modal
A focused, interrupting dialog built on the native dialog element.

Plain-text source, for agents and clipboard use: [/components/source/modal.txt](/components/source/modal.txt)

## When to use it
Use when a decision must be made before anything else can continue — confirming a destructive action, or completing a short, self-contained task.

Not thisNever for a task that needs information outside the modal: creating or editing complex bookings, multi-step workflows, searching and selecting inventory, comparing products, services or prices, assigning passengers to rooms or cabins, editing pricing structures, configuring departures or services, large forms or editable tables. Use inline editing, a Drawer, the List and detail split view or a page — see Interaction architecture. Not for non-urgent information. A modal never opens another modal.
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
NameKindDescription`dialog`elementUse the native element. Open with showModal(), never by toggling a class.`flux-modal`classThe dialog surface, including its ::backdrop.`flux-modal--wide`classWidens the dialog to --flux-modal-width-max, 90% of the window, when a permitted decision must show what it affects, such as the read-only summary of an irreversible change. Never for a table, a comparison or a form.`flux-modal__header`classDivided title row.`flux-modal__body`classContent region.`flux-modal__footer`classRight-aligned action row.
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
- --flux-modal-width-max
## Do and don’t
Do

- Name the consequence in the title, not "Are you sure?".
- Label the confirm button with the action itself, so it reads correctly out of context.
- Leave the underlying data exactly as it was when the modal is cancelled.Don’t

- Do not tint the backdrop with a brand colour.
- Do not open a modal from a modal.
- Do not put a form longer than a few fields inside one.
- Do not use a modal to reduce visual clutter, or to avoid navigating to a page.[PreviousCommand palette](/components/command-palette/)[NextDrawer](/components/drawer/)
