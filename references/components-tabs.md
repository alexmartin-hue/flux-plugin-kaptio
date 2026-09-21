# Flux — /components/tabs/

Source: https://flux.kaptio.com/components/tabs/

Component

# Tabs
Switches between sibling views within one context.

Plain-text source, for agents and clipboard use: [/components/source/tabs.txt](/components/source/tabs.txt)

## When to use it
Use for a handful of peer views of the same object, where the user will move between them and only one is relevant at a time.

Not thisTabs are not navigation between pages, and not a wizard. If the views are steps in a sequence, or if content in a hidden tab needs to be found by search or print, do not use tabs.
## Examples

### Default

Overview
Pricing
Suppliers

Twenty-four departures published, three awaiting supplier confirmation.

htmlCopy`
Overview
Pricing
Suppliers

Twenty-four departures published, three awaiting supplier confirmation.
`
## Anatomy
PartDescriptionTab listRow of tabs above a hairline divider.TabBold, small. Inactive in text-subtle.Indicator2px underline in border-interactive on the selected tab.PanelThe content region, labelled by its tab.
## API
NameKindDescription`flux-tabs`classThe tab list. Needs role="tablist" and an aria-label.`flux-tab`classA tab. Use a button with role="tab".`aria-selected`attributeDrives the active style. Exactly one tab is true.`aria-controls`attributePoints at the panel id.
## States
StateTreatmentInactivetab-text, transparent underline.Hovertext-primary.Selectedtab-text-active plus a 2px indicator.FocusGlobal teal focus outline.
## Keyboard
KeysAction`Tab`Moves to the tab list, then to the panel. Only the selected tab is a tab stop.`Left, Right`Moves between tabs.`Home, End`Jumps to the first or last tab.
## Accessibility

- Roving tabindex is required: the selected tab is tabindex="0", the rest are tabindex="-1". Without it, keyboard users must tab through every tab to reach the panel.
- The indicator is a 2px underline plus a colour change, so selection is not signalled by colour alone.
- Each panel is labelled by its tab through aria-labelledby.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-tab-height
- --flux-tab-padding-x
- --flux-tab-indicator
- --flux-tab-indicator-width
- --flux-tab-text
- --flux-tab-text-active
## Do and don’t
Do

- Keep tab labels to one or two words.
- Preserve the selected tab across a page reload where the view is shareable.Don’t

- Do not use more than about five tabs; beyond that, use navigation.
- Do not hide required form fields inside an unselected tab.[PreviousNote](/components/note/)[NextAvatar](/components/avatar/)
