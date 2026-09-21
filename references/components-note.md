# Flux — /components/note/

Source: https://flux.kaptio.com/components/note/

Component

# Note
Inline contextual message in one of four semantic tones.

Plain-text source, for agents and clipboard use: [/components/source/note.txt](/components/source/note.txt)

## When to use it
Explains something about the region it sits in — a constraint, a consequence, a result. It stays in the layout rather than floating over it.

Not thisFor a transient confirmation of something the user just did, use a toast. For a blocking decision, use a modal. For per-field validation, use the field error text.
## Examples

### Tones

Read-only environment

Changes made here are not written back to Salesforce.

Evidence pack signed

Countersigned at close of trial and attached to the account record.

Three departures awaiting supplier

They will not appear on the site until the supplier confirms.

Price rule conflict

Two rules target the B2C channel for the same date range. Resolve one before publishing.

htmlCopy`

Read-only environment
Changes made here are not written back to Salesforce.

Evidence pack signed
Countersigned at close of trial and attached to the account record.

Three departures awaiting supplier
They will not appear on the site until the supplier confirms.

Price rule conflict
Two rules target the B2C channel for the same date range. Resolve one before publishing.

`
## Anatomy
PartDescriptionContainerTinted surface at 4px radius, no border.TitleOptional. Bold, one line.BodySecondary text. Body copy stays text-primary or text-secondary, never the tone colour.
## API
NameKindDescription`flux-note`classBase class. Informational tone by default.`flux-note--success`classA completed or verified outcome.`flux-note--warning`classSomething needs attention but nothing is broken.`flux-note--error`classSomething failed or blocks progress.`flux-note__title`classOptional bold lead line.
## States
StateTreatmentStaticNotes do not have interactive states.
## Accessibility

- Body text stays in a text token rather than the tone colour, which is what keeps every note at 4.5:1 on its tint.
- A note appearing in response to an action belongs in a live region — role="status" for informational, role="alert" for errors.
- The tone is reinforced by the wording; a note that only differs by tint is not accessible.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-note-radius
- --flux-note-padding
- --flux-note-gap
- --flux-surface-info-subtle
- --flux-surface-success-subtle
- --flux-surface-warning-subtle
- --flux-surface-error-subtle
## Do and don’t
Do

- Say what to do next, not only what happened.
- Keep a note beside the thing it describes.Don’t

- Do not colour the body text with the tone colour.
- Do not stack several notes at the top of a page as a substitute for fixing the flow.[PreviousModal](/components/modal/)[NextTabs](/components/tabs/)
