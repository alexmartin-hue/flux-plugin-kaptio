# Flux — /components/command-palette/

Source: https://flux.kaptio.com/components/command-palette/

Component

# Command palette
A searchable list of actions, pages and records, opened over the page with ⌘K.

Plain-text source, for agents and clipboard use: [/components/source/command-palette.txt](/components/source/command-palette.txt)

## When to use it
Gets people to any action, page or record by typing a few letters. It is a native dialog holding a combobox and a listbox of grouped options. Focus stays in the input; the arrow keys move the active option and Enter chooses it. An option with data-href navigates; any other dispatches flux-command with its value and closes the palette. It resets when it closes.

Not thisNot as the only way to reach something; every command must also live in the interface. Not for searching within one list; use Search on the list. Not for choosing a form value; use Select.
## Examples

### Palette
Type “golden” to filter to the records. The arrow keys move, Enter chooses, Escape closes.

Open command palette

Actions
New booking
New quote
Assign a guide to a departure

Go to
Bookings
Departures
Suppliers
Reports

Records
Anna LindqvistKB-104931
Nordic TrailsKB-104877
Golden Circle, 14 SepDEP-0914

No commands or records match.

↑↓ to move
↵ to choose
Esc to close

htmlCopy`Open command palette

Actions
New booking
New quote
Assign a guide to a departure

Go to
Bookings
Departures
Suppliers
Reports

Records
Anna LindqvistKB-104931
Nordic TrailsKB-104877
Golden Circle, 14 SepDEP-0914

No commands or records match.

↑↓ to move
↵ to choose
Esc to close

`
## Anatomy
PartDescriptionDialogOn surface-overlay with shadow-xl, 40rem wide, set down from the top so it does not jump as results filter.SearchA combobox input at text-base with a search icon, above a hairline.GroupA mono uppercase label and its options. Groups with no matches hide.OptionAn icon, the label and optional mono meta such as a reference. The active option is surface-selected.Empty stateOne sentence when nothing matches.FooterThe keys that work in the palette.
## API
NameKindDescription`dialog`elementOpen with showModal() or a commandfor button.`flux-command`classOn the dialog. data-flux-command adds filtering, the active option and choosing. Name it with aria-label.`data-flux-command-shortcut`attributeOpens the palette on ⌘K or Ctrl K, and on the app shell’s flux-shell-search event. Put it on one palette per page.`flux-command__search | __input`classThe input row. The input has role="combobox", aria-controls naming the list and aria-expanded="true".`flux-command__list`classThe role="listbox" element.`flux-command__group | __group-label`classA role="group" labelled by its label.`flux-command__option | __meta`classA role="option" with a unique id. data-keywords adds search terms; data-href navigates; data-value is sent with flux-command.`flux-command__empty | __status | __footer`classThe no-results line, the visually hidden result count and the key hints.`flux-command event`attributeEvent dispatched on the dialog when an option without data-href is chosen. detail holds option and value.
## States
StateTreatmentOpenThe first matching option is active.FilteredOptions and groups that do not match every typed word hide; the count is announced.No resultsThe empty line shows and no option is active.ClosedThe query clears so the next open starts fresh.
## Keyboard
KeysAction`⌘K / Ctrl K`Opens the palette, with data-flux-command-shortcut.`Arrow Down / Arrow Up`Moves the active option, wrapping at the ends.`Enter`Chooses the active option.`Escape`Closes the palette and returns focus to where it was.
## Accessibility

- Focus never leaves the input. aria-activedescendant points at the active option, so typing and moving work together.
- The result count is announced through a status region as the list filters.
- showModal() makes the page inert; a click on the backdrop closes the palette.
- If the product already uses ⌘K, as this documentation site does, leave data-flux-command-shortcut off and open the palette from that handler.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-command-width | -list-height | -offset | -padding | -input-height
- --flux-command-bg | -shadow | -backdrop | -divider
- --flux-command-option-padding-x | -option-padding-y | -option-active | -option-icon | -group-label
## Do and don’t
Do

- Name options with the verb first for actions, and the record name for records.
- Match on references and synonyms through data-keywords.Don’t

- Do not put destructive actions in the palette without a confirmation.
- Do not show more than three groups before the user types; lead with the most used.[PreviousKeyboard shortcut](/components/kbd/)[NextModal](/components/modal/)
