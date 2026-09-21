# Flux — /components/button/

Source: https://flux.kaptio.com/components/button/

Component

# Button
Triggers an action. Six variants, three sizes.

Plain-text source, for agents and clipboard use: [/components/source/button.txt](/components/source/button.txt)

## When to use it
Use a button for an action the user takes on this page — submitting, confirming, opening a dialog. Exactly one primary button per view or section; everything else is secondary, outline or ghost.

Not thisNavigating to another page is a link, not a button, even when it looks like one. If the control changes location rather than state, use an anchor so it can be opened in a new tab and read correctly by assistive technology.
## Examples

### Variants
Primary carries the one action that matters. CTA yellow is reserved for a single conversion moment and never appears twice on a screen.

Save changes
Cancel
Export
Dismiss
Delete booking
Talk to ushtmlCopy`Save changes
Cancel
Export
Dismiss
Delete booking
Talk to us`
### Sizes
Small for toolbars and table rows, medium everywhere else, large only for a standalone page action.

Small
Medium
LargehtmlCopy`Small
Medium
Large`
### Disabled
Keep the button in the DOM and disabled rather than removing it, so the layout does not shift and the reason can be explained nearby.

Save changes
CancelhtmlCopy`Save changes
Cancel`
## Anatomy
PartDescriptionContainerFixed height from the size token, 4px radius, no shadow.LabelLexend Bold. Sentence case. A verb, and specific — "Save changes", not "Submit".Icon (optional)Leading or trailing, 16px, inheriting text colour via currentColor.
## API
NameKindDescription`flux-button`classBase class. Primary teal fill by default.`flux-button--secondary`classNeutral fill on layer-03. For the lesser of two actions.`flux-button--outline`classTeal border and text, transparent fill.`flux-button--ghost`classTeal text only. For tertiary actions in dense chrome.`flux-button--danger`classDestructive actions. Pair with a confirmation.`flux-button--cta`classBumble-Me Yellow. One per view, conversion only.`flux-button--sm | --lg`classSize modifiers. Medium is the default and needs no class.`disabled`attributeNative disabled. Do not simulate it with pointer-events.
## States
StateTreatmentDefaultsurface-brand fill, text-on-color label.Hoversurface-brand-hover. No lift, no shadow, no scale.Activesurface-brand-active.Focus2px focus-ring outline at 2px offset. Teal in every theme.Disabled50% opacity, not-allowed cursor. Colour is unchanged.
## Keyboard
KeysAction`Tab`Moves focus to the button.`Space, Enter`Activates the button.
## Accessibility

- A button with only an icon needs an accessible name — use aria-label, never a title attribute alone.
- Focus is a 2px teal outline offset by 2px, meeting WCAG 1.4.11 at 5.8:1 on white.
- Disabled buttons are removed from the tab order by the native attribute; if the reason is not obvious, state it in adjacent text rather than a tooltip.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-button-radius
- --flux-button-height-sm | -md | -lg
- --flux-button-padding-x-sm | -md | -lg
- --flux-button-font-size-sm | -md | -lg
- --flux-surface-brand
- --flux-surface-brand-hover
- --flux-text-on-color
## Do and don’t
Do

- Use one primary button per view. If two actions look equally important, one of them is not.
- Write labels as specific verbs: "Create departure", "Send evidence pack".
- Put the primary action last in a footer row, after Cancel.Don’t

- Do not use gradient fills, glow shadows, or a scale transform on hover.
- Do not use CTA yellow for anything but a single conversion action.
- Do not invent variants. Six exist; a seventh is a design decision, not a class name.[PreviousAccessibility](/foundations/accessibility/)[NextInput](/components/input/)
