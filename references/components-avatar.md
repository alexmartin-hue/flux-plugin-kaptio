# Flux — /components/avatar/

Source: https://flux.kaptio.com/components/avatar/

Component

# Avatar
Represents a person or account, as an image or initials.

Plain-text source, for agents and clipboard use: [/components/source/avatar.txt](/components/source/avatar.txt)

## When to use it
Identifies who did something, or who is present. Always circular, in three sizes.

Not thisDo not use an avatar for a company, product or integration — those take a logo or a product mark. An avatar alone is never sufficient identification; pair it with a name wherever the person matters.
## Examples

### Sizes and group
OG
OG
OG

OG
AB
KA
htmlCopy`OG
OG
OG

OG
AB
KA
`
## Anatomy
PartDescriptionContainerCircle, filled with surface-brand-subtle when there is no image.InitialsMono, bold, so widths stay even across different letter pairs.ImageCover-fitted, clipped to the circle.
## API
NameKindDescription`flux-avatar`classBase class. Medium by default.`flux-avatar--sm | --lg`classSize modifiers.`flux-avatar-group`classOverlaps a set of avatars with a ring against the layer beneath.
## States
StateTreatmentStaticAn avatar has no interactive states of its own.
## Accessibility

- Initials are decorative to a screen reader unless labelled — give the element role="img" and an aria-label with the full name.
- When the avatar sits beside the person's visible name, mark it aria-hidden="true" instead, so the name is not announced twice.
- Never convey status by avatar colour alone.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-avatar-radius
- --flux-avatar-size-sm | -md | -lg
- --flux-avatar-bg
- --flux-avatar-text
## Do and don’t
Do

- Use two initials.
- Fall back to initials when an image fails to load.Don’t

- Do not use square avatars.
- Do not rely on an avatar alone to identify someone.[PreviousTabs](/components/tabs/)[NextComposition discipline](/patterns/composition/)
