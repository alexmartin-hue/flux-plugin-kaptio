# Flux — /components/progress/

Source: https://flux.kaptio.com/components/progress/

Component

# Progress and meter
Segmented bars for how far a task has got, and where a measurement sits in its range.

Plain-text source, for agents and clipboard use: [/components/source/progress.txt](/components/source/progress.txt)

## When to use it
Progress shows a task that is under way and will finish, such as an import or a batch of confirmations, in brand teal. Meter shows a measurement within a known range, such as seats sold against what a departure needs to run, and takes a status colour from where the value sits. Both draw the value as a row of segments, and both are real progress and meter elements underneath, so the value is announced as a value.

Not thisNot when the amount of work is unknown; use a Spinner. Not for a value without a range, such as a booking total; write the number. Not as a chart of several values side by side; use a chart.
## Examples

### Progress
A percentage, written by the script from the progress element when the value span has data-flux-percent.

Importing rates
81%

81%

htmlCopy`

Importing rates
81%

81%

`
### Progress with a count
When the units mean something, say them. Set the value text yourself; the script still draws the segments.

Sending confirmations
120 of 480

120 of 480

htmlCopy`

Sending confirmations
120 of 480

120 of 480

`
### Meter, higher is better
Seats sold on a departure that runs at 20 and is safe above 40. Above high is teal; between low and high is pending; below low is an error.

KB-2026-09-14 seats sold
44 of 49, guaranteed

44 of 49, guaranteed

KB-2026-09-21 seats sold
30 of 49, 10 more to guarantee

30 of 49, 10 more to guarantee

KB-2026-09-28 seats sold
12 of 49, below the minimum of 20

12 of 49, below the minimum of 20

htmlCopy`

KB-2026-09-14 seats sold
44 of 49, guaranteed

44 of 49, guaranteed

KB-2026-09-21 seats sold
30 of 49, 10 more to guarantee

30 of 49, 10 more to guarantee

KB-2026-09-28 seats sold
12 of 49, below the minimum of 20

12 of 49, below the minimum of 20

`
### Meter, lower is better
Set optimum below low to reverse the scale: an agent’s credit used turns pending at 60% and an error past 90%.

Credit used, Nordic Trails
ISK 4,050,000 of 5,000,000

ISK 4,050,000 of 5,000,000

htmlCopy`

Credit used, Nordic Trails
ISK 4,050,000 of 5,000,000

ISK 4,050,000 of 5,000,000

`
### Small
flux-progress--sm halves the segment height, for a table cell or a dense list.

Content import
35%

35%

htmlCopy`

Content import
35%

35%

`
## Anatomy
PartDescriptionHeaderThe label, a label element bound to the progress or meter, and the value as text.ValueThe number in words or a percentage, in mono. It says what the colour says, so colour is never the only signal.ElementA visually hidden progress or meter. It holds the value; change it there and the segments follow.Segmentsflux-segments, aria-hidden. Twenty by default, or the count in data-segments; a segment fills once its whole share is reached.
## API
NameKindDescription`flux-progress`classA task under way. Holds a progress element and a flux-segments row.`flux-meter`classA measurement in a range. Holds a meter element with min, max, low, high and optimum.`flux-progress--sm`classThe small segment height, on either wrapper.`flux-segments`classThe segment row, aria-hidden. data-segments sets the count; twenty by default.`data-flux-percent`attributeOn the value span: the script writes the percentage into it.`data-tone`attributeOn flux-meter, set by the script from the meter’s region: warning when suboptimal, error when worse. Absent at optimum.
## States
StateTreatmentEmptyNo segment is filled until the value is above the minimum.PartialAny value above the minimum fills at least one segment, so started never reads as not started.CompleteEvery segment is filled only at the maximum.Meter regionsOptimum in brand teal, suboptimal in the pending colour, even less good in the error colour.
## Keyboard
KeysAction`—`Not interactive.
## Accessibility

- The progress or meter element is in the accessibility tree with its label, so assistive technology reads the value and the range.
- The value text says what the colour says. A meter in the error colour also says, in words, what is wrong.
- Progress changes are not announced as they happen. When a task finishes, say so in a status message or a Toast.
- Filled segments meet 3:1 against the ground and the empty segments in every theme.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-progress-segment-height | -height-sm | -gap | -radius | -empty
- --flux-progress-fill | -fill-warning | -fill-error
- --flux-progress-header-gap | -label | -value
## Do and don’t
Do

- Change the value on the progress or meter element, not on the segments.
- Pick low, high and optimum from what the value means to the business, and write that meaning in the value text.
- Use the count of the real units as data-segments when it is small, such as one segment per room.Don’t

- Do not colour a progress bar by status. Progress is not a warning; if a task fails, stop it and say why.
- Do not animate the segments filling in turn, or add a glow to the leading segment.
- Do not use a meter for completion over time, or a progress bar for a level.[PreviousSpinner](/components/spinner/)[NextSkeleton](/components/skeleton/)
