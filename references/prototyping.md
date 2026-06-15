# Flux — /prototyping

Source: https://flux.kaptio.com/prototyping

[Flux](/)
For Product Managers

# Prototyping with Flux + AI

A two-minute setup so prototypes you build in Cursor (or any AI tool) actually look
like Kaptio — not generic AI or Tailwind defaults. No code experience needed: you mostly
just paste a few lines and tell the agent to follow Flux.

## Quick start

In a hurry? Paste this into the agent at the start of a prototype. The steps below explain
each part.

Build this using the Kaptio Flux design system as the single source of truth.

1. Follow https://flux.kaptio.com/llms.txt (tokens, rules, component conventions).
2. In my global CSS, after the Tailwind import, add:
@import url("https://flux.kaptio.com/tokens/flux-tailwind.css");
(Not using Tailwind? Use https://flux.kaptio.com/tokens/flux.css instead.)
3. Use only --flux-* tokens — no raw hex, no gray-*/blue-* defaults.
Font: Lexend (300/700 only). Focus rings are Flux primary, never blue.
4. Clone real component markup from
https://flux.kaptio.com/components/source/<name>.txt (e.g. button, input, table).

Do not mix in Bootstrap, MUI, or Spotlight.
Stop the leaks

The Flux preset auto-corrects most generic styling, but ask the agent to avoid the two
things it can't catch: no “arbitrary” bracket values like
`bg-[#3b82f6]` or `text-[15px]`, and Lexend at 300 / 700 only
(no medium/semibold). Focus rings should be Flux teal, never blue — and the
`flux-tailwind.css` import must come last.

## 1. Point the AI at Flux

In your very first message to the agent, tell it to treat Flux as the single source of
truth. Paste this in:

Use the Kaptio Flux design system as the single source of truth: https://flux.kaptio.com/llms.txt — follow it strictly and do not use generic Tailwind defaults.
## 2. Import the Flux tokens

Paste this on the first line of your main CSS file. It defines every Flux color, spacing,
radius, shadow, and type value.

@import url("https://flux.kaptio.com/tokens/flux.css");
Not sure where that file is? Just ask Cursor: “Import the Flux tokens stylesheet at the
top of my global CSS.”

## 3. Add the Flux rule file

Ask Cursor to create `.cursor/rules/flux.mdc` using the ready-made rule on the
[For AI](/for-ai)
page. Once it's there, Cursor applies the brand rules automatically on every change — no
need to repeat yourself.

## 4. The golden rules

If something looks off-brand, it's almost always one of these. Hand them to the agent as-is.

- Use only `--flux-*` tokens — no raw hex, and no `gray-*`, `blue-*`, or `slate-*` Tailwind colors.
- Font is Lexend, weights 300 and 700 only (no 400/500/600).
- Text is Kaptio dark (`--flux-black`). No colored headings.
- Yellow (`--flux-yellow-400`) is for primary buttons and key highlights only.
- Don't mix in other UI kits (Bootstrap, MUI, and the like).
## 5. If it drifts off-brand

AI tools sometimes wander back to defaults. When that happens, paste this and let the agent
put it right:

Re-check this against https://flux.kaptio.com/for-ai and replace any non-Flux colors, fonts, radii, or spacing with the correct --flux-* tokens.
Everything for engineers and AI tools:
[For AI](/for-ai).
