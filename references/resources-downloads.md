# Flux — /resources/downloads/

Source: https://flux.kaptio.com/resources/downloads/

Resources

# Downloads
Everything the system publishes, at a URL that will not move. Generated on every release from one source, so no two artifacts can disagree.

## Token artifacts
FileSizeContents`/tokens/v2/flux.css`25.7 kBFonts, all three tiers, all three themes, base rules. The usual import.`/tokens/v2/flux-tokens.css`23.9 kBThe same tokens without font imports or base rules.`/tokens/v2/flux.json`69.1 kBEvery token as structured data, grouped by tier and theme.`/tokens/v2/flux-tailwind.css`16.9 kBTailwind v4 theme block. Clears the defaults, remaps the names.`/tokens/v2/flux-components.css`25.7 kBThe twelve documented components, as framework-agnostic CSS.`/tokens/v2/flux-components.js`15.0 kBComponent behaviour for Select and Date picker, including keyboard handling and form-value syncing.`/tokens/v2/flux-deck.css`40.5 kBThe presentation layer. Slide canvas and layouts. Decks only — it overrides the fluid root.`/tokens/v2/flux-deck.js`7.1 kBDeck navigation: previous and next arrows, click to advance, and the keys. Optional — snapping is CSS.Direct links: [flux.css](/tokens/v2/flux.css) ·[flux-tokens.css](/tokens/v2/flux-tokens.css) ·[flux.json](/tokens/v2/flux.json) ·[flux-tailwind.css](/tokens/v2/flux-tailwind.css) ·[flux-components.css](/tokens/v2/flux-components.css) ·[flux-components.js](/tokens/v2/flux-components.js) ·[flux-deck.css](/tokens/v2/flux-deck.css) ·[flux-deck.js](/tokens/v2/flux-deck.js)

Not this path`/tokens/flux.css`, without the version, is Flux 1.x and stays that way. It is a live runtime dependency of applications that cannot redeploy to follow a change. Six tokens differ between the two — see [Upgrading](/get-started/upgrading/).
## Machine contract
FileFor`/llms.txt`The complete contract: tokens, rules, and every component’s markup.`/rules/flux.mdc`Cursor project rule. Drop into .cursor/rules/.`/rules/AGENTS.md`Portable agent brief. Works for Claude Code and Copilot.`/prototypes/brief.txt`Reusable product-prototype prompt with context fields, composition constraints and verification.`/decks/llms.txt`The deck contract. Separate on purpose — slide rules and product rules disagree.bashCopy`curl -o .cursor/rules/flux.mdc https://flux.kaptio.com/rules/flux.mdc
curl -o AGENTS.md                https://flux.kaptio.com/rules/AGENTS.md`
## Component sources
One plain-text file per component: markup, API, states, keyboard, accessibility and tokens.

- [button.txt

Triggers an action. Six variants, three sizes.](/components/source/button.txt)
- [input.txt

Single-line text entry, with the label, help and error pattern that goes with it.](/components/source/input.txt)
- [select.txt

Choice from a known, closed set of options.](/components/source/select.txt)
- [date-picker.txt

Single-date and date-range selection from a keyboard-operable calendar.](/components/source/date-picker.txt)
- [card.txt

Groups related content into one surface on the layer above.](/components/source/card.txt)
- [description-list.txt

Labelled values in a row or a stack. The summary block at the top of a record.](/components/source/description-list.txt)
- [badge.txt

A short status label. Four status colours, shared with tables.](/components/source/badge.txt)
- [table.txt

Quiet data table. Horizontal dividers only, tabular figures, badge status cells.](/components/source/table.txt)
- [modal.txt

A focused, interrupting dialog built on the native dialog element.](/components/source/modal.txt)
- [note.txt

Inline contextual message in one of four semantic tones.](/components/source/note.txt)
- [tabs.txt

Switches between sibling views within one context.](/components/source/tabs.txt)
- [avatar.txt

Represents a person or account, as an image or initials.](/components/source/avatar.txt)
## Package
bashCopy`npm config set @kaptio:registry https://gitlab.com/api/v4/packages/npm/
npm install @kaptio/flux-tokens`Published to the Kaptio GitLab registry. Pin it for anything you ship — see [Install](/get-started/install/).

## URL stability
GuaranteedEvery URL on this page is permanent. Artifacts are updated in place on each 2.x release, and no path will be moved or removed within the 2.x line. A 3.0 would take a new prefix rather than these.Hosted artifacts track the current release, which is right for prototypes and wrong for production. Pin the package where a change underneath you would matter.

[PreviousSlack teammates](/for-ai/slack/)[NextChangelog](/resources/changelog/)
