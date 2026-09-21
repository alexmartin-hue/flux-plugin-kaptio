# Flux — /for-ai/prototypes/

Source: https://flux.kaptio.com/for-ai/prototypes/

For AI

# Prototype prompt
Importing the stylesheet gives a prototype Flux values. Giving the agent this brief makes it use those values as a system: documented components, readable density, one hierarchy and a check before handoff.

## Set up the repository
Persistent rules carry more authority than a paragraph pasted once.

Add the Flux rule file from [Repository rules](/for-ai/rules/) to the prototype repository first. It is always applied to UI files, so later prompts cannot silently drop the design contract when the conversation grows.

If the repository already has agent instructions, append the Flux contract rather than replacing them. Product context and engineering conventions still apply.

CarefulA CSS import supplies tokens; it does not choose hierarchy, density or component semantics. The repository rule and prototype brief are both required for consistent generated work.
## Copy the prompt
Fill the five context fields, then give the whole prompt to the agent.

Also available as plain text at [/prototypes/brief.txt](/prototypes/brief.txt).

textCopy`Build a Kaptio product prototype using Flux 2.0.

Before writing UI:
1. Read and follow https://flux.kaptio.com/llms.txt.
2. Read documented component markup from https://flux.kaptio.com/components/source/.txt.
3. Reuse existing repository components when they already solve the job.
4. This is product UI, not a presentation. Never import flux-deck.css.

Prototype context:
- Product or feature: [name]
- Primary user: [user]
- Task they must complete: [task]
- Required screens and states: [screens and states]
- Data and business constraints: [constraints]

Design requirements:
- Import https://flux.kaptio.com/tokens/v2/flux.css and https://flux.kaptio.com/tokens/v2/flux-components.css.
- Reference Tier 2 semantic tokens for every interface role.
- Use documented Flux components instead of recreating them.
- Use at least --flux-text-sm for controls, table cells and compact secondary copy.
- Use --flux-text-base for sentences intended to be read.
- Reserve --flux-text-xs for badges, help text and short metadata.
- Preserve readable type and spacing. Let the page scroll.
- Keep text, notes and controls inside the documented padding of their surface. Never let content touch a card or panel edge.
- Keep action rows inside the same inline inset as the content above, with a token gap between actions; wrap or stack them on narrow screens.
- Reflow layouts on narrow screens; never use CSS zoom or transform to scale the application.
- Wrap wide tables in their horizontal scrolling container.
- Group related metrics on one surface instead of making every value a card.
- Establish one clear primary action and use at most one yellow CTA per view.
- Map each domain status to the documented Badge semantics before rendering it. Do not leave every status on the neutral base style when the states have different consequences.
- Use yellow status styling only when waiting, delay or required attention is part of the meaning.
- Use native semantic elements, visible labels and documented keyboard behaviour.
- Support light and dark themes. Do not use deep for dense product UI.
- Do not invent colours, dimensions, components, statuses or interactions.

Workflow:
1. Inspect the repository and its existing components.
2. State the proposed screen hierarchy briefly.
3. Implement only the requested workflow.
4. Verify responsive reflow and keyboard interaction.
5. Test light and dark themes.
6. Run npx flux-check src/ and fix every finding.

Do not optimise the prototype to fit into one screenshot. Optimise it for the user completing the task.`
## Fill the context
Flux controls the interface language. These fields tell the agent what the interface must accomplish.

Do

- Name one primary user and the task they need to complete.
- List required empty, loading, error and success states when they matter.
- Provide representative data shapes and real business constraints.
- Keep the requested workflow narrow enough to verify.Don’t

- Do not ask for a generic dashboard without naming the user’s task.
- Do not use a screenshot as the only statement of hierarchy.
- Do not ask the agent to fit the whole workflow into one viewport.
- Do not add a second visual taste system on top of Flux.
## Product or deck
Choose one contract. The two surfaces deliberately use different composition rules.

This prompt is for product interfaces and operational prototypes. For a presentation, use the [deck brief](/decks/brief.txt) instead. Never paste both contracts into the same request: the agent will average rules that are intentionally different.

[PreviousRepository rules](/for-ai/rules/)[NextSlack teammates](/for-ai/slack/)
