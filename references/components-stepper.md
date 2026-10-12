# Flux — /components/stepper/

Source: https://flux.kaptio.com/components/stepper/

Component

# Stepper and wizard
Numbered steps that show progress through a task, and the wizard recipe that validates each one.

Plain-text source, for agents and clipboard use: [/components/source/stepper.txt](/components/source/stepper.txt)

## When to use it
A Stepper shows where someone is in a task with a fixed order: which steps are done, which is current and which remain. The wizard recipe pairs it with one form section per step, validates each step with the platform’s constraint checks before the next one opens, moves focus to the new step’s heading, and ends on a review that reads back what was entered. Numbering is the meaning here, so the markers are numbered.

Not thisNot for a form short enough to fit on one screen. Not for steps that can be done in any order; use sections or Tabs. Not for showing location in a hierarchy; use Breadcrumbs.
## Examples

### Progress
Two steps done, the third current. Completed markers carry hidden text, so the tick is not the only signal.

- Completed: Lead traveller

- Completed: Departure

- 3Rooms

- 4Review
htmlCopy`
Completed: Lead traveller
Completed: Departure
3Rooms
4Review
`
### With an error
A step that was completed and then invalidated, such as by a supplier declining, returns with an error state and hidden text that says so.

- Completed: Lead traveller

- Needs attention: Departure

- 3Rooms

- 4Review
htmlCopy`
Completed: Lead traveller
Needs attention: Departure
3Rooms
4Review
`
### Wizard
Press Next with the fields empty to see each step validate. Focus moves to the first field with a problem, and to each new step’s heading. The review reads back the answers, and submitting dispatches flux-wizard-complete.

## New group booking

- 1Lead traveller

- 2Departure

- 3Review

### Lead traveller

Full name *

Email *

### Departure

Departure *
Golden Circle Classic, 14 Sep
South Coast Explorer, 19 Sep
Snæfellsnes Peninsula, 22 Sep

Travellers *

### Review

Lead traveller
Email
Departure
Travellers

Back
Next
Create booking

htmlCopy`
New group booking

1Lead traveller
2Departure
3Review

Lead traveller

Full name *

Email *

Departure

Departure *
Golden Circle Classic, 14 Sep
South Coast Explorer, 19 Sep
Snæfellsnes Peninsula, 22 Sep

Travellers *

Review

Lead traveller
Email
Departure
Travellers

Back
Next
Create booking

`
## Anatomy
PartDescriptionStepperAn ordered list labelled for the task.StepA marker and a label. aria-current="step" on the current one; data-state="complete" or "error" on others.MarkerA near-square box with the number in mono, a tick when complete, or an alert mark on error.ConnectorA hairline after each step that turns teal once the step is complete.Wizard stepA section with a heading per step. Only the current one is shown.ActionsBack on the left, Next or the final submit on the right, below a hairline.
## API
NameKindDescription`flux-stepper`classOn the ol. Label it for the task.`flux-stepper__step`classOn each li.`flux-stepper__marker`classThe number, or a tick or alert icon with hidden text.`flux-stepper__label`classThe step name. Below 48rem only the current step keeps its visible label.`aria-current="step"`attributeOn the current step.`data-state`attribute"complete" or "error" on a step that is not current.`data-flux-wizard`attributeOn the form. Wires the steps, the stepper, validation and the review.`flux-wizard__step`classOn each section. Hide all but the first in the markup.`flux-wizard__title`classThe step heading. Receives focus when its step opens.`flux-wizard__actions`classThe action row.`data-flux-wizard-back | -next | -submit`attributeOn the three buttons. The script shows the right ones for each step.`data-error`attributeOn a flux-field or choice group: the message shown when its control is invalid. Without it the browser’s message is used.`data-flux-review`attributeOn an element in the review: the name of the field whose value it shows. For radios, the checked option’s label.`flux-wizard-complete`elementCancelable event dispatched on the form when every step is valid and it is submitted. Call preventDefault to submit by script instead.
## States
StateTreatmentUpcomingA border-strong marker with the number in text-secondary.CurrentA teal filled marker with the number in text-on-color; the label is bold text-primary.CompleteA teal outlined marker with a tick, and a teal connector after it.ErrorAn error outlined marker with an alert mark, and the label in text-error.Invalid fieldaria-invalid on the control and an error message below it, bound with aria-describedby. The message clears once the value is valid.
## Keyboard
KeysAction`Tab`Moves through the fields of the current step, then Back and Next.`Enter`In a field, submits the form, which validates every step and opens the first one with a problem.
## Accessibility

- The stepper is a list, so its length and each position are announced; aria-current marks the current step.
- Completed and error markers carry hidden text, so the icon and colour are not the only signal.
- Moving to a step focuses its heading, so screen reader users hear where they are.
- An invalid step keeps focus on its first invalid field, with the message bound to it.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-stepper-marker-size | -gap
- --flux-stepper-connector | -connector-complete
- --flux-stepper-marker-border | -marker-text
- --flux-stepper-marker-current-bg | -marker-current-text
- --flux-stepper-marker-complete | -marker-error
- --flux-stepper-label | -label-current
## Do and don’t
Do

- Keep a wizard to three to six steps, each a coherent group of fields.
- End on a review that reads back what will be submitted.
- Keep answers when someone goes back a step.Don’t

- Do not make the steps clickable when they must be done in order.
- Do not validate a step before someone tries to leave it.
- Do not use a wizard for a form that fits on one screen.[PreviousSegmented control](/components/segmented-control/)[NextWalkthrough and storyboard](/components/walkthrough/)
