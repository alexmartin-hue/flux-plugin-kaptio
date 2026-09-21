# Flux — /components/badge/

Source: https://flux.kaptio.com/components/badge/

Component

# Badge
A short status label. Four status colours, shared with tables.

Plain-text source, for agents and clipboard use: [/components/source/badge.txt](/components/source/badge.txt)

## When to use it
Labels the state of the row or object beside it. The four status colours are fixed, and mean the same thing in a table cell as in a card.

Not thisA badge is not a button and not a filter. If it can be clicked, it is a control and needs a control's affordances. Do not use badges for counts.
## Examples

### Status semantics
These four mappings are the whole set. A fifth status reuses the nearest of these rather than introducing a colour.

Confirmed
On request
Awaiting supplier
Cancelled
DrafthtmlCopy`Confirmed
On request
Awaiting supplier
Cancelled
Draft`
### Inventory availability
Map domain labels by consequence: ready is positive, the current allocation is neutral, and unavailable blocks selection.

Available
Assigned
OccupiedhtmlCopy`Available
Assigned
Occupied`
## Anatomy
PartDescriptionContainerPill, 20px tall, extra-small bold text.LabelOne or two words. Sentence case.
## API
NameKindDescription`flux-badge`classBase class. Neutral teal tint by default.`flux-badge--confirmed`classConfirmed, completed, verified, live.`flux-badge--pending`classPending, on request, action required.`flux-badge--awaiting`classAwaiting supplier, awaiting third party.`flux-badge--cancelled`classCancelled, rejected, expired, failed.`flux-badge--unavailable`classUnavailable or blocked from selection. Uses a lighter orange ground than cancelled so normal occupancy does not read as an error.
## States
StateTreatmentStaticA badge has no interactive states. It reflects state; it does not change it.
## Accessibility

- Colour never carries the meaning on its own — the word in the badge is the status, and the tint reinforces it.
- Where a badge updates without a page load, put it in a live region so the change is announced.
- Every badge pairing meets 4.5:1: dark status text on a light tint of the same hue.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-badge-radius
- --flux-badge-height
- --flux-badge-padding-x
- --flux-badge-font-size
## Do and don’t
Do

- Reuse the four status colours across tables, cards and detail views.
- Write down the domain-to-badge mapping before rendering a set of sibling statuses.
- Keep labels to one or two words.Don’t

- Do not invent a per-status hex. Map every new status onto one of the four.
- Do not leave every status neutral when the states have materially different consequences.
- Do not make a badge clickable.
- Do not use a badge where a full sentence would be clearer.[PreviousDescription list](/components/description-list/)[NextTable](/components/table/)
