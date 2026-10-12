# Flux — /components/menu/

Source: https://flux.kaptio.com/components/menu/

Component

# Action menu
A short list of actions behind one button, for a record or a toolbar.

Plain-text source, for agents and clipboard use: [/components/source/menu.txt](/components/source/menu.txt)

## When to use it
Gathers the less frequent actions for one thing — a booking, a row, an export — behind a single trigger, so the frequent action can stay a visible button beside it. It is a popover with role="menu": the platform gives it light dismiss, Escape and focus return, and flux-components.js places it below its trigger and moves through it with the arrow keys. Separators group related actions, and a destructive action sits last, in text-error.

Not thisNot for choosing a value; use a Select. Not for navigation between pages; use links. Not for the one action someone came to take; make that a button. Not for a single action; show it as a button.
## Examples

### Record actions
Edit is the frequent action, so it stays a button. The rest wait in the menu, with the destructive one last. Send manifest is unavailable until a guide is assigned, so it stays in place, focusable and announced as unavailable.

Edit booking
More actions

Duplicate
Send confirmation
Send manifest

Cancel booking
htmlCopy`Edit booking
More actions

Duplicate
Send confirmation
Send manifest

Cancel booking
`
### Icon trigger
In a row or a card header, an icon button opens the menu. Its accessible name says which record the actions belong to.

Send manifest
Export passenger list

Cancel departure
htmlCopy`

Send manifest
Export passenger list

Cancel departure
`
### Checkable items
menuitemcheckbox toggles in place and keeps the menu open, so several can be changed at once.

Show

Departures
Supplier deadlines
Public holidays
htmlCopy`Show

Departures
Supplier deadlines
Public holidays
`
## Anatomy
PartDescriptionTriggerA button with popovertarget, aria-haspopup="menu" and aria-expanded. A text trigger ends in a chevron; an icon trigger names the record.MenuA popover with role="menu" and an aria-label, on surface-overlay with shadow-md.ItemA button with role="menuitem", or menuitemcheckbox with a check for a setting.SeparatorA hairline with role="separator" between groups of actions.Destructive itemflux-menu__item--danger, last and after a separator. It opens a confirmation rather than acting.
## API
NameKindDescription`flux-menu`classOn the popover, with popover, role="menu" and an aria-label. Requires flux-components.js for placement and arrow keys.`flux-menu__item`classA button with role="menuitem", or role="menuitemcheckbox" with aria-checked and a flux-menu__check icon.`flux-menu__item--danger`classA destructive action, in text-error. Last, after a separator.`flux-menu__separator`classA div with role="separator" between groups.`aria-disabled="true"`attributeOn an item that is unavailable. It stays focusable and announced, and does nothing when chosen.`popovertarget`attributeOn the trigger, naming the menu’s id. Add aria-haspopup="menu" and aria-expanded="false".
## States
StateTreatmentClosedNot rendered. The trigger has aria-expanded="false".OpenPlaced below the trigger’s end edge, or above it when there is no room. Focus moves to the first item.Item hover and focuslayer-hover-01 behind the item.Unavailabletext-disabled, still focusable.Checkedmenuitemcheckbox with aria-checked="true" shows its check in icon-brand.
## Keyboard
KeysAction`Enter / Space`On the trigger, opens the menu. On an item, chooses it and closes the menu, returning focus to the trigger.`↓ ↑`Moves to the next or previous item, wrapping at the ends.`Home / End`Moves to the first or last item.`Escape`Closes the menu and returns focus to the trigger.`Tab`Closes the menu and moves on.
## Accessibility

- Give the menu an aria-label that names the record, and the icon trigger an accessible name that does the same.
- Use aria-disabled rather than disabled on an unavailable item, so it is still reached and announced.
- A destructive item opens a confirmation Modal that names the consequence; it never acts on its own.
- The menu closes when the page scrolls, so it never floats away from its trigger.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-menu-bg | -border | -shadow | -radius | -padding | -min-width
- --flux-menu-item-padding-x | -item-padding-y | -item-hover | -item-font-size
- --flux-menu-separator | -item-danger | -offset
## Do and don’t
Do

- Keep the frequent action as a visible button beside the menu.
- Order items by how often they are used, and group them with separators.
- Name each item with a verb and its object: "Send manifest".Don’t

- Do not put a single action in a menu.
- Do not nest menus.
- Do not let a destructive item act without a confirmation.
- Do not hide an unavailable action. Leave it in place and unavailable, so the menu keeps its shape.[PreviousTable](/components/table/)[NextKeyboard shortcut](/components/kbd/)
