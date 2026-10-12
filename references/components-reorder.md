# Flux — /components/reorder/

Source: https://flux.kaptio.com/components/reorder/

Component

# Reorderable list
A list whose order is the meaning, rearranged by dragging a handle or with the keyboard.

Plain-text source, for agents and clipboard use: [/components/source/reorder.txt](/components/source/reorder.txt)

## When to use it
Lets someone put items in order where the order matters: the days of an itinerary, the priority of suppliers, the sequence of a manifest. Each item has a handle that can be dragged, or focused and moved with the arrow keys; every move is announced, and the rest of the list settles into place rather than jumping.

Not thisNot for sorting by a value, such as date or price; that is a sortable Table column. Not for moving items between lists; that needs its own pattern. Not for long lists, where dragging past the screen is slow; offer a position field instead.
## Examples

### Day order
Drag a handle, or focus it, press Space, move with the arrow keys and press Space again. Escape puts the day back.

Keflavík → Reykjavik
1 night

Reykjavik → Vík
2 nights

Vík → Jökulsárlón
1 night

Jökulsárlón → Höfn
1 night

Press Space to pick up. Use the arrow keys to move, Space to drop, Escape to cancel.

htmlCopy`

Keflavík → Reykjavik
1 night

Reykjavik → Vík
2 nights

Vík → Jökulsárlón
1 night

Jökulsárlón → Höfn
1 night

Press Space to pick up. Use the arrow keys to move, Space to drop, Escape to cancel.`
## Anatomy
PartDescriptionListAn ol, because the order is the meaning, labelled with aria-label.ItemA row separated from the next by a hairline.HandleA toggle button with a grip icon, named "Move <item>". The only part that drags.LabelThe item’s name, used in every announcement.MetaOptional mono detail that does not depend on position, such as "2 nights".
## API
NameKindDescription`flux-reorder`classThe ol.`data-flux-reorder`attributeWires dragging, keyboard moves, announcements and the settle. Requires flux-components.js.`flux-reorder__item`classAn li. Carries data-lifted while it is picked up.`flux-reorder__handle`classA button with aria-pressed and aria-describedby pointing at the instructions.`flux-reorder__label`classThe item name, read in announcements.`flux-reorder__meta`classOptional detail at the end of the row.`flux-reorder event`elementDispatched on the list after a drop that changed the order, with detail.item, detail.from and detail.to.
## States
StateTreatmentRestingRows on layer-01 with hairlines. The handle turns icon-brand on hover.LiftedThe item takes surface-raised and --flux-reorder-lifted-shadow, because it floats above the list.SettlingNeighbours slide into their new places over --flux-duration-fast, by transform only.
## Keyboard
KeysAction`Space / Enter`On a handle, picks the item up; again, drops it.`↑ ↓`While picked up, moves the item one place.`Escape`While picked up, returns the item to where it started.
## Accessibility

- Every pickup, move and drop is announced with the item’s name and position: "Reykjavik → Vík, position 3 of 4."
- The handle is a real button, reachable with Tab, with aria-pressed showing whether its item is picked up.
- Describe the keyboard controls once, in a visually hidden paragraph the handles reference.
- Dragging is never the only way: the keyboard moves the same items, and a long list should also offer a position field.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-reorder-divider | -padding-y | -gap
- --flux-reorder-handle-size | -handle-icon
- --flux-reorder-lifted-bg | -lifted-shadow
## Do and don’t
Do

- Save the new order as soon as it is dropped, and confirm with a Toast only if saving is not visible.
- Keep position-dependent text, such as "Day 2", out of the label, or update it after every drop.Don’t

- Do not make the whole row draggable. Text in it must stay selectable and its links clickable.
- Do not reorder on hover or animate the dragged item’s size. It lifts and moves; nothing grows.[PreviousToast](/components/toast/)[NextBoard](/components/board/)
