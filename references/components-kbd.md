# Flux — /components/kbd/

Source: https://flux.kaptio.com/components/kbd/

Component

# Keyboard shortcut
A key or key combination, shown inline, in a control, or in a list of shortcuts.

Plain-text source, for agents and clipboard use: [/components/source/kbd.txt](/components/source/kbd.txt)

## When to use it
Tells people which keys do something. It is the kbd element in mono on layer-02 with a hairline. Write shortcuts with Apple symbols and add data-flux-keys: on other platforms flux-components.js rewrites ⌘ as Ctrl and ⌥ as Alt, so the hint matches the keyboard in front of the reader.

Not thisNot for a shortcut that does not exist; a hint promises behaviour. Not for code or identifiers; use mono text or code. Not as a button.
## Examples

### Inline
Press ⌘K to search, or ? to see every shortcut.

htmlCopy`Press ⌘K to search, or ? to see every shortcut.`
### In a button
The hint is hidden from assistive technology and the shortcut is declared with aria-keyshortcuts instead.

Save draft ⌘ShtmlCopy`Save draft ⌘S`
### Shortcut list

Search⌘K
Save changes⌘S
Next recordJ
Previous recordK
Show shortcuts?
htmlCopy`
Search⌘K
Save changes⌘S
Next recordJ
Previous recordK
Show shortcuts?
`
## Anatomy
PartDescriptionKeyA kbd at text-xs mono 500, not uppercase, on layer-02 with a hairline and 4px radius.Shortcut listA dl.flux-shortcuts: the action as the term, its keys as the detail, divided by hairlines.
## API
NameKindDescription`kbd`elementThe native element for keyboard input.`flux-kbd`classOn the kbd. Inside a menu item or command option it aligns to the end.`data-flux-keys`attributeRewrites ⌘ as Ctrl, ⌥ as Alt, ⌃ as Ctrl and ⇧ as Shift on platforms other than Apple’s.`flux-shortcuts`classOn a dl listing shortcuts, one div per action.`aria-keyshortcuts`attributeOn the control the shortcut triggers, e.g. Meta+S.
## States
StateTreatmentApple platformsSymbols as written.Other platformsModifier names, e.g. Ctrl K.
## Keyboard
KeysAction`None`A hint is not focusable. The shortcut itself is handled by the product.
## Accessibility

- Declare a control’s shortcut with aria-keyshortcuts and hide the visual hint inside it, so the accessible name stays “Save draft”.
- Never bind a single printable key without a way to turn it off or remap it (WCAG 2.1.4); J and K only apply when focus is not in a field.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-kbd-bg | -border | -text | -padding-x | -gap
## Do and don’t
Do

- Show the shortcut where the action is, in its menu item or button.
- Keep one list of every shortcut, opened with ?.Don’t

- Do not uppercase keys or letter-space them; a kbd is not a structural label.
- Do not override a browser or screen-reader shortcut.[PreviousAction menu](/components/menu/)[NextCommand palette](/components/command-palette/)
