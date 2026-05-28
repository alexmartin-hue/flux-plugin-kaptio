# Flux — /foundations/iconography

Source: https://flux.kaptio.com/foundations/iconography

[Flux](/)
Foundations

# Iconography

Icons are a critical part of the Kaptio visual language. We use
[Streamline](https://www.streamlinehq.com)
as our official icon set across all products — over 100,000 icons in a consistent, professional system.

## Two weights. That's it.

Just like our typography, icons follow a two-weight system. Regular for default UI,
Bold for emphasis and active states. Constraint creates consistency.

Regular

Default
The standard weight for navigation, labels, toolbars, and general UI.
Clean, legible, and unobtrusive.

-         Bold

Emphasis
For active/selected states, high-visibility contexts, and moments
that need extra weight. Use sparingly.

-         Regular is the default. Only reach for Bold when an icon
needs to signal an active state, selected item, or high-importance action.

## Sizing on the 4px grid

Icons follow the same 4px base grid as all Flux spacing. Four standard sizes cover every use case.

-    16px

Inline text, badges, dense tables

-    20px

Form inputs, small buttons, labels

-    24px

Default UI, navigation, toolbars

-    32px

Feature icons, empty states, headers

## Color usage

Icons inherit their parent's text color by default. Use Flux tokens when
an icon needs to carry a specific meaning or accent.

Do

-   Inherit text color for general UI      Use accent color for active/success states
-   Use semantic color for error/warning       Avoid

-   Decorative color with no meaning      Too subtle to be functional
-      Mixing sizes in the same context
## Accessibility

Icons are powerful visual cues but should never be the only way to communicate meaning.

Pair icons with labels

Icons should accompany text labels by default. Standalone icons are acceptable only when
the meaning is universally understood (e.g. close, search).

Decorative icons get `aria-hidden="true"`

If an icon is purely decorative or redundant with adjacent text,
hide it from screen readers.

Interactive icons need accessible names

Icon-only buttons must have an `aria-label`
or visually hidden text describing the action.

Minimum touch target: 44 x 44px

Even if the icon itself is 24px, ensure the clickable area meets
WCAG minimum touch target guidelines.

## Access and tooling

The Streamline icon library is managed centrally and available to all team members.

IconJar

The full Streamline library is available in IconJar for quick drag-and-drop access in design and development workflows.

SVG export

Export icons as optimized SVGs. Use `currentColor` for stroke/fill
so icons inherit their parent's text color.

Streamline app

Browse, search, and copy icons directly from
[app.streamlinehq.com](https://app.streamlinehq.com).
