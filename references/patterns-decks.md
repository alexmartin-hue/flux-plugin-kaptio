# Flux — /patterns/decks/

Source: https://flux.kaptio.com/patterns/decks/

Patterns

# Decks
A slide is read in seconds, from the back of a room, while somebody talks over it. Product rules tuned for desk distance are what make a deck boring — so this surface loosens the ones that only make sense up close, and holds every one that carries the brand.

## Why decks differ
Same tokens. Different distance.

A slide is not a small web page. It is read in seconds, from the back of a
room, while somebody talks over it. The rules that keep a dense operational
interface legible — one ground, restrained colour, a bounded type scale, no
decoration — are the same rules that make a deck boring, because they are
tuned for a surface nobody is looking up at.

So the deck layer relaxes the rules that only make sense at desk distance, and
holds every rule that carries the brand. What loosens is scale, ground,
asymmetry and bleed. What never loosens is tokens, Lexend at two weights,
JetBrains Mono as the second voice, and contrast.

Separate contractDecks have their own agent contract at [/decks/llms.txt](/decks/llms.txt). Product rules and slide rules disagree deliberately, and an agent given both at once averages them into something that is neither.

## Setting one up
Two stylesheets and one wrapper. A deck is a standalone document.

htmlCopy`

Deck title

`The deck layer derives the root font size from the viewport, so the 80 × 45rem composition always fits and every rem token — spacing, type, radius — scales with it as one piece. Leftover viewport becomes the current slide’s ground, not a frame of the page behind it. That is the one place Flux overrides the fluid root, and it is safe only because a deck is a whole document. Never load `flux-deck.css` into product UI.

Slides advance to the right. Snapping is CSS, so a swipe, a trackpad and a presenter remote move one slide with no script at all; `flux-deck.js` adds the two things CSS cannot — previous and next arrows, clicking to advance, and the keys. Click anywhere to go forward, click the left quarter to go back, use the arrows at the edges, or the arrow keys, space, Page Up and Down, or Home and End.

Diagrams are inline SVG inside `flux-slide__figure`. Appearance comes from the`flux-figure__*` classes so the drawing re-themes with its slide; geometry stays in the markup as SVG attributes, because a `viewBox` is in user units and a rem token resolves to the wrong size inside one. Wrap the parts in`flux-stage` to reveal them in the order you explain them.

A deck with no script is still a working deck, which is why the navigation lives in a separate file rather than inside the stylesheet. The staged reveal degrades the same way: without it, every stage simply shows.[See a full deck](/decks/example/), or print one to PDF at 1280 × 720 — one slide per page.

## What loosens
Each product rule, and what replaces it on a slide.

Product ruleOn a slideThe type scale stops at --flux-text-6xl.Decks add --flux-display-sm through --flux-display-xl. These are deck-only: a display size in product UI is a defect, not a bold heading.A view has one ground.Every slide sets its own data-flux-theme. A deep teal statement between two light slides is the cheapest visual event in the system, and contrast is already audited for all three themes.Teal carries the system; other hues appear only when they carry meaning.A slide may take any product accent with data-accent. On a slide the accent is identity rather than status, so it needs no meaning — but it stays graphic.One yellow CTA element per view.Yellow is not a slide ground. The closing ask uses one full-bleed photograph under a deep-teal overlay.No centred body copy.Statement and quote slides centre. There is no body copy on them to centre.No three-column grid of icon, heading and paragraph as a default layout.The grid slide is exactly that, and it is right here — a taxonomy held on screen for twenty seconds is not a landing page.Constrain reading columns to --flux-measure-prose.Slides bleed to the edge. Images fill the canvas, and marks are cropped by it deliberately.Never exceed --flux-duration-slow.Content settles on arrival using a scroll-driven timeline, so it tracks the presenter rather than a clock. Still opacity and transform only.No decorative marks, bars or dots.A slide may carry one oversized typographic mark, or one hairline dot field. One. Two is decoration, and a coloured bar on the edge of anything is still banned.
## What holds
Unchanged from product UI. A slide is not an exemption.

- Every value comes from a token. No raw hex, no raw dimension, no Tailwind arbitrary value.
- Lexend at 300 or 700. JetBrains Mono at 400, 500 or 700. Never a third family.
- Grounds are Flux themes. Contrast is WCAG 2.2 AA at minimum (4.5:1 text, 3:1 non-text) and stays audited. Never a hand-picked colour.
- Product accents colour type and data: the oversized mark, the list numerals, chart bars, a donut arc. Never decoration — no bar on the edge of a card, no rule beside a label — and never a word you are meant to read.
- Interface radius stays --flux-radius-sm. A slide is not a reason for a soft corner.
- No gradient fills, no glassmorphism, no glow, no neon, no blur behind content, no gradient mesh.
- No emoji as an icon system.
- Animate opacity and transform. Never width, height, top, left, margin or padding.
- The agenda video is decorative and muted. It pauses off-slide, respects reduced motion, and always has the Flux pause control.
- Real text in real elements. A slide is not an image of a slide.
- One idea per slide. If it needs two sentences to state, it is two slides.AccentsA product accent colours type and data: the oversized mark on a section slide, the numerals on a list, the bars of a chart, the filled arc of a donut. It never draws decoration — no bar on the edge of a card, no rule beside a label — and it never carries a word, because it has no guaranteed contrast on any ground. Colour behind text comes from a theme. The closing slide uses the deep theme over a full-bleed photograph, with the built-in teal overlay preserving contrast.

## Pacing
This is what makes a deck interesting. Not more colour.

A boring deck is almost always a deck where every slide is the same shape. Variety of rhythm does more than variety of decoration, and it costs nothing.

- Pick the layout from the sentence, not the sentence from the layout. Write the line first, then choose the slide that fits it.
- Never two consecutive slides of the same layout. If two facts want the same shape, one of them is the wrong shape.
- Change ground at least every third slide. Light, dark and deep in rotation is the rhythm.
- Give the audience a beat every four to six slides: a section divider, or a statement with nothing else on it.
- Twenty-five words per slide, counting every visible word — kickers, labels and numerals included. Twelve on a statement slide.
- The data layouts — chart, donut, timeline, journey, infographic — and the agenda are outside that count, because their repeated text is labels rather than prose. They get their own budget: one label and at most one line of explanation per item, and nothing else.
- A labelled diagram earns its words by taking them off the slide. If the lede still explains what the figure already shows, cut the lede, not the labels.
- An agenda belongs near the front of a deck long enough to have parts, and again before each part with aria-current on the item you are reaching. In a deck of eight slides it is a slide nobody needed.
- When an agenda is needed, use the agenda-video layout. There is no text-only agenda alternative: the quiet looping visual gives the room a paced opening without competing with the list.
- Five items in a list, eight words each. A sixth item is a second slide.
- At most one accent per slide. None is fine — a statement carries itself. A second accent on the same slide is a defect.
- The final ask uses a full-bleed photograph with the deep-theme overlay. Never a flat yellow closing ground.
- Open on a cover and close on the ask. Everything between is yours.
- A number worth saying out loud is worth a metric slide of its own.
- Every third slide carries a photograph, screenshot, or portrait. Three consecutive text-only slides is a defect.
- A founding, scale, or company-facts slide is never metrics alone. Pair it with an editorial image — use split-photo.
## Images
Photography is part of the argument, not decoration you add if there is room.

Decks go dull when every slide is type on a flat ground. The image and split-photo layouts exist so agents reach for a photograph when the slide mentions a place, a product, or people in context — not only when the photo is the entire point.

- Every deck needs at least three photographs: one on the cover or opening beat, one grounding a company or product claim, one showing people or customers in context.
- Portraits for people. Photography for place and product. If the slide mentions where you are or what you do, show it.
- Use flux-slide--image when the photograph carries the point on its own. Use flux-slide--split-photo when copy and metrics share the slide with it.
- The closing ask always uses a meaningful full-bleed photograph beneath the deep-teal overlay. The image supports the action; it is not generic texture.
- The agenda uses the video-backed agenda archetype. Keep its visual quiet, decorative and dark enough that the list remains the point.
- src may be a URL or a path under /decks/assets/. Alt text is mandatory and must describe what is in the frame, not repeat the slide title.
- Never leave a slide that mentions a place, product, or team without a visual of that thing.
## The layouts
18 shapes. Pick the one that fits the sentence you have already written.

Each is a live slide at full size, framed to 16:9. If none of them fits what you are trying to say, say so and propose one — inventing a layout in a deck is the same defect as inventing a component in product UI.

One is already known to be missing: there is no layout for a command or a code snippet. A deck about tooling or adoption wants one, and until it exists, carry the command as a list item or a `flux-slide__note` rather than building a slide for it.

### Cover
Use when The deck opens. Once, at the front.

Not when Never for a section break — that is the section layout, and it looks different on purpose.

htmlCopy`
Platform review · Q3
Connect ships to every tenant
Vera Lindqvist · 18 August 2026
`
### Agenda
Use when Near the front, to tell the room the shape of the next twenty minutes. This video-backed layout is the agenda type for every deck. Repeat it before a part begins, with aria-current on the item you are reaching.

Not when For content. An agenda names the parts of the deck; a list of arguments is the list layout. A four-slide deck does not need one.

htmlCopy`

Agenda
What we’ll cover

Where we are today
Product status, go-lives, and key milestones from the year.

What customers told us
Themes from advisory boards, support, and the field.

The roadmap ahead
Priorities and innovation themes for the next four quarters.

How we get there
Teams, timelines, and what we need from each other.

Pause video

`
### Section
Use when A divider between parts of the argument. It exists to give the room a beat.

Not when For a slide that carries content. A section slide says where you are, nothing else.

htmlCopy`
02
Part two
What the migration cost
`
### Statement
Use when One sentence that deserves the whole room. The most underused slide in any deck.

Not when For a sentence that needs support. If it needs a caption, it is a split.

htmlCopy`
Every booking now clears in under four seconds.
`
### Metric
Use when A number worth saying out loud. One, or up to three abreast.

Not when For four or more numbers. That is a table. For founding year, headcount, revenue, or scale — use split-photo, not metric alone. Metrics without a photograph read as a spreadsheet.

htmlCopy`
Throughput

3.9s
Median clear time
Down from twenty-one seconds at the start of the quarter.

99.98%
Availability
Two minutes of degradation, all of it planned.

`
### Chart
Use when One series, four to seven bars, where the shape of the change is the point. Each bar carries its value as --flux-bar, a percentage of the plot.

Not when For two series, or for a trend with many points. A deck bar chart compares a handful of things; anything denser belongs in the document behind it.

htmlCopy`
Median clear time · seconds
Every release took time out

21.4

16.2

9.8

5.1

3.9

Q2 '25
Q3 '25
Q4 '25
Q1 '26
Q2 '26

`
### Donut
Use when One proportion, stated next to what it means. The ring is drawn on a circumference of exactly 100, so a segment is written as its percentage.

Not when For four or more segments, or for anything that is not a share of a whole. A donut sliced five ways is a table nobody can read.

htmlCopy`

Migration
68% of tenants are on the new engine
The rest are scheduled before the end of the quarter.

`
### Infographic
Use when One figure that carries the claim, with two or three that support it. The hierarchy is the point.

Not when For figures of equal weight — that is the metric layout. If you cannot say which number leads, you have a metric slide.

htmlCopy`
Twelve months of Connect

1.2M
Bookings cleared
Through one engine, on one contract, in one currency model.

41
Tenants live

0
Rollbacks

`
### Split
Use when An argument on one side and its evidence on the other. Use --split-wide when the text outweighs the figure.

Not when For two competing positions. That is compare, and the seam between them matters.

htmlCopy`

Before
Six systems, one booking
Every handoff was a place a reservation could quietly stop existing.

`
### Split with photo
Use when Copy on one side and an editorial photograph on the other. The company-facts shape: founding story, scale metrics, or product context beside a place, landscape, or operators in the field.

Not when For a diagram or annotated screenshot — that is split with an inline SVG. For a photograph that carries the whole point alone — that is image.

htmlCopy`

About Kaptio
Built for multi-day travel. Nothing else.
Founded in Reykjavík to give multi-day travel brands software that fits the industry.

2014
Founded in Iceland

100
People · 17 nationalities

20+
Travel brands

€1.6B
2025 booking volume

`
### List
Use when Genuinely sequential or enumerable points. Five at most.

Not when As the default slide. If every slide is a list, the deck is a document read aloud.

htmlCopy`
What changed

One reservation record, owned by Connect.
Every price resolved at write time.
Failures surface in the channel, not the log.

`
### Compare
Use when Two positions held against each other. The seam is the point.

Not when For three or more options. Three columns of prose is a table nobody will read.

htmlCopy`

Today
Each tenant runs its own pricing rules, and no two agree on rounding.

September
One engine, one rounding rule, and a tenant override that has to be justified.

`
### Timeline
Use when When. Three to five dated milestones on one axis. Mark the one you are standing on with aria-current.

Not when For stages without dates — that is the journey layout. For more than five milestones: a timeline read from the back of a room holds about four.

htmlCopy`
Rollout
Every tenant by March

Sep 2026
Pilot
Four tenants, both currency models, one region.

Nov 2026
General availability
Opt-in for everyone already on Connect.

Jan 2027
Default
New tenants provision on the engine automatically.

Mar 2027
Legacy off
The old pricing path stops accepting writes.

`
### Journey
Use when Who, in order. Stages of a process and the hand-off between them. The seams are where the work changes hands.

Not when For dated milestones — that is the timeline. For a set of points with no order, use list or grid.

htmlCopy`
One booking, end to end

Quote
Prices resolve once, against the live rate card.
Connect

Hold
Inventory is reserved for the length of the quote.
Connect

Confirm
One record, written once, owned by one system.
Salesforce

Settle
Payment clears against the same record it quoted.
Kaptio Pay

`
### Quote
Use when Somebody else’s words, where whose words they are matters.

Not when To dress up your own point. A quote from nobody is a statement slide with extra punctuation.

htmlCopy`
We stopped reconciling bookings by hand in week three, and nobody has asked to go back.
Operations lead, Tauck
`
### Image
Use when A photograph or screenshot that carries the point on its own.

Not when As background texture behind unrelated text. If the image is decoration, drop it.

htmlCopy`

One timeline
Every state change, in order, with the actor who caused it.

`
### Grid
Use when A taxonomy: four to six things of the same kind, held on screen together.

Not when For a sequence. Order in a grid is ambiguous — use the list.

htmlCopy`
The shape of it

Ingest
Supplier feeds land once, and are versioned on arrival.

Resolve
Price and availability settle before anything is written.

Publish
One record, one shape, every channel.

`
### Closing
Use when The ask. One per deck, at the end. A full-bleed photograph makes the action tangible.

Not when Anywhere else. This is a closing action, not a reusable image treatment.

htmlCopy`

Pilot it with two tenants in September.
Decision needed by 29 August.

`
## For agents
The check to run before a deck is finished.

- Every slide uses one of the layouts. An invented layout is a missing one — say which.
- No two consecutive slides share a layout.
- The ground changes at least every third slide.
- There is a beat — a section or statement slide — every four to six slides.
- The last slide is the ask, over a full-bleed image with the deep-teal overlay.
- No slide exceeds twenty-five words, the data layouts aside.
- One accent per slide, and no accent carries text.
- Every chart bar carries a --flux-bar percentage, and a donut’s two dash values add up to 100.
- A chart, a donut or a timeline has a caption saying what it shows. A figure without a claim is decoration.
- No raw hex, no raw dimension, no font weight outside 300 and 700.
- Every readable pairing uses a theme ground, so contrast stays at WCAG 2.2 AA.
- Every image has real alt text, and no slide is a picture of text.
- At least three slides carry a photograph or screenshot.
- If the deck needs an agenda, it uses flux-slide--agenda-video with a muted video and its pause control.
- No company-facts slide without an accompanying image — use split-photo.
- The deck reads correctly with the browser at any window size, because the composition scales as one piece and leftover viewport takes the slide’s ground.The full machine contract — premise, layouts, markup and all of the above — is at[/decks/llms.txt](/decks/llms.txt). It is written to be sufficient on its own: an agent should be able to build a correct deck from that file without fetching anything else.

For a Slack teammate whose configuration is a single text box and cannot fetch a URL,[/decks/brief.txt](/decks/brief.txt) is the same contract condensed to fit a system prompt. It is generated from the same source, so it is a shorter statement of these rules and never a different one.

[PreviousForms](/patterns/forms/)[NextOverview](/for-ai/)
