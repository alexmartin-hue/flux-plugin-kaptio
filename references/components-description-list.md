# Flux — /components/description-list/

Source: https://flux.kaptio.com/components/description-list/

Component

# Description list
Labelled values in a row or a stack. The summary block at the top of a record.

Plain-text source, for agents and clipboard use: [/components/source/description-list.txt](/components/source/description-list.txt)

## When to use it
Presents the fixed attributes of one object — a booking’s traveller, departure, nights and total — as label and value pairs. This is the most common block in a Kaptio operations screen, and the one most often rebuilt from scratch. Use it so that every record header in every product reads the same way.

Not thisNot for tabular data. If you have the same attributes across many objects, that is a table, and a reader needs to compare down a column. A description list describes exactly one thing.
## Examples

### Default
Values that are data — dates, counts, money, references — take mono. A person’s name is language, so it stays in Lexend.

Traveller
Marianne Hollis

Departure
14 March 2027

Nights
11

Total
EUR 8,420.00

htmlCopy`

Traveller
Marianne Hollis

Departure
14 March 2027

Nights
11

Total
EUR 8,420.00

`
### In a card
The usual placement: the summary block at the head of a record.

Reference
KB-104928

Status
Confirmed

Balance due
13 January 2027

htmlCopy`

Reference
KB-104928

Status
Confirmed

Balance due
13 January 2027

`
### Stacked
For a narrow column or a side panel. Label and value sit on one line, with the value aligned right.

Subtotal
EUR 7,890.00

Service fee
EUR 530.00

Total
EUR 8,420.00

htmlCopy`

Subtotal
EUR 7,890.00

Service fee
EUR 530.00

Total
EUR 8,420.00

`
## Anatomy
PartDescriptionListA dl. Horizontal by default, wrapping onto new rows as space runs out.TermA dt. The label: bold, small, secondary.DetailA dd. The value: mono when it is data, sans when it is language.
## API
NameKindDescription`flux-dl`classThe list. Horizontal, wrapping.`flux-dl--stacked`classLabel left, value right, one pair per line.`flux-dl__pair`classWraps one dt and dd. Required — dl children cannot be laid out directly.`flux-dl__term`classThe label.`flux-dl__detail`classThe value.`flux-dl__detail--data`classMono with tabular figures. For references, dates, counts and money.
## States
StateTreatmentDefaultNo fill and no border. The list takes the ground it is placed on.
## Keyboard
KeysAction`—`Not interactive. Any control inside a value keeps its own behaviour.
## Accessibility

- Use dl, dt and dd. A grid of divs conveys no relationship, so a screen reader reads eight unconnected strings instead of four labelled values.
- Each dt needs exactly one dd. If a value is genuinely absent, say so — an em dash or "Not set" — rather than leaving the dd empty.
- The wrapping div between dl and its pairs is valid HTML and does not break the association.
- Do not use a description list to fake a two-column table. A reader navigating a table expects row and column semantics that a dl does not provide.
## Tokens
The tier-3 and tier-2 tokens this component binds to. Change the token, not the component.

- --flux-dl-gap-x
- --flux-dl-gap-y
- --flux-dl-term-gap
- --flux-dl-term-color
- --flux-dl-term-size
- --flux-dl-detail-color
- --flux-dl-detail-size
## Do and don’t
Do

- Put the value in mono when it is data a reader will compare, copy or quote.
- Keep labels to one or two words so the pairs align down a wrapped row.
- Order the pairs by what the reader looks for first, not by what the database returns first.Don’t

- Do not put a person’s or place’s name in mono. Mono is for data, not language.
- Do not add vertical rules between pairs. The gap is the separator.
- Do not use it for more than one object.[PreviousCard](/components/card/)[NextBadge](/components/badge/)
