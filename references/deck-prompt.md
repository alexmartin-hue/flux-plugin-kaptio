# Flux — /deck-prompt

Source: https://flux.kaptio.com/deck-prompt

[Flux](/)
For Everyone

# Create a deck with Kai

Need a Kaptio-branded slide deck? Copy the prompt below, paste it into a Slack message to
Kai, and fill in your deck outline at the bottom. Kai does the rest — every slide is built
from the official Flux deck kit, so the result is on-brand by default.

Deck kit Slack + Kai Copy & paste flux.kaptio.com
## How to use it

- Copy the prompt — use the button below.
- Paste it into Slack in a message to Kai.
- Fill in the outline — replace the placeholders in the
`MY DECK` section at the bottom with your audience, goal, and slides.
## The prompt
Copy prompt    You are creating a Kaptio-branded slide deck using the Kaptio Flux design system. Follow these instructions exactly.

1. Fetch and follow https://flux.kaptio.com/llms.txt — it is the source of truth for all design rules. Import the Flux tokens exactly as its Setup section describes.

2. NEVER design a slide from scratch. For every slide: pick the matching template below, fetch its full source from the URL, clone the markup, and change ONLY copy, images, and data.

Routing table (slide content -> template -> source):
- Deck opener / title slide -> Cover -> https://flux.kaptio.com/slide-examples/source/cover.txt
- Section break / chapter divider -> Chapter -> https://flux.kaptio.com/slide-examples/source/chapter.txt
- One big idea / thesis / focus -> Statement -> https://flux.kaptio.com/slide-examples/source/statement.txt
- Explainer with supporting visual -> Content -> https://flux.kaptio.com/slide-examples/source/content.txt
- Customer / partner introduction -> Customer intro -> https://flux.kaptio.com/slide-examples/source/customer.txt
- Product status / progress / roadmap -> Status grid -> https://flux.kaptio.com/slide-examples/source/status-grid.txt
- Before vs after / two options -> Compare -> https://flux.kaptio.com/slide-examples/source/compare.txt
- Agenda / what we'll cover -> Agenda -> https://flux.kaptio.com/slide-examples/source/agenda.txt
- Single big number / KPI -> Big stat -> https://flux.kaptio.com/slide-examples/source/stat.txt
- Quote / testimonial -> Quote -> https://flux.kaptio.com/slide-examples/source/quote.txt
- Closing / thank-you / CTA -> Closing -> https://flux.kaptio.com/slide-examples/source/closing.txt
- Feature section opener -> Recap intro -> https://flux.kaptio.com/slide-examples/source/recap.txt
- Feature explainer (what/value) -> Feature detail -> https://flux.kaptio.com/slide-examples/source/feature.txt
- Feature impact + product fit -> Feature impact -> https://flux.kaptio.com/slide-examples/source/feature-impact.txt
- Customer intro with map -> Customer map -> https://flux.kaptio.com/slide-examples/source/customer-map.txt
- Two categorized lists / taxonomy -> Lists -> https://flux.kaptio.com/slide-examples/source/lists.txt
- Platform / product positioning panel -> Platform -> https://flux.kaptio.com/slide-examples/source/platform.txt
- Forward roadmap / timeline / horizons -> Roadmap -> https://flux.kaptio.com/slide-examples/source/roadmap.txt
- Customer logo strip / social proof -> Logo strip -> https://flux.kaptio.com/slide-examples/source/logos.txt
- Team / leadership -> Team -> https://flux.kaptio.com/slide-examples/source/team.txt
- Process / how it works / journey steps -> Journey -> https://flux.kaptio.com/slide-examples/source/journey.txt
- Q&A before close -> Q&A -> https://flux.kaptio.com/slide-examples/source/qa.txt
- Implementation / onboarding phases -> Implementation -> https://flux.kaptio.com/slide-examples/source/implementation.txt
- Security / trust / compliance -> Security -> https://flux.kaptio.com/slide-examples/source/security.txt
- Competitive feature matrix -> Matrix -> https://flux.kaptio.com/slide-examples/source/matrix.txt
- Growth chart / trend line -> Chart -> https://flux.kaptio.com/slide-examples/source/chart.txt
- Global footprint / regions -> Global presence -> https://flux.kaptio.com/slide-examples/source/global.txt

3. If no template matches, use the NEAREST template's structure — do not invent a new layout.

4. Self-check every slide:
- Headline on dark grounds is entirely white — never yellow/colored headline words.
- --flux-yellow-400 at most ONCE per slide, as a single small accent or CTA.
- One kicker/eyebrow per slide, maximum.
- Lexend weights 300 and 700 only.
- Only --flux-* tokens — no raw hex/rgb, no arbitrary values.
- Content slides are light; cover and chapter slides are dark.
- At most one emoji per slide — never in headings or as the icon system.
- No gradient text, no glow shadows, no coral accent eyebrows.

5. Output the deck as a single self-contained HTML file (or your closest supported format) using the cloned template markup, one 16:9 slide per section.

6. Asset paths: the deck must work as a standalone file. Rewrite every root-relative path from the templates to an absolute URL — /tokens/flux.css becomes https://flux.kaptio.com/tokens/flux.css, /images/... becomes https://flux.kaptio.com/images/... — and verify each URL resolves. Template photos are placeholders; swap in imagery relevant to the deck content where provided, otherwise keep the absolute placeholder URLs.

---
MY DECK:
Audience: [who it's for]
Goal: [what it should achieve]
Slides:
1. [slide content]
2. [slide content]
...
---
Curious what the templates look like? Preview them at
[Slide examples](/slide-examples).
Building decks with a coding tool instead? See
[For AI](/for-ai).
