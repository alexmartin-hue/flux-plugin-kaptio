# Flux — /patterns/interaction/

Source: https://flux.kaptio.com/patterns/interaction/

Patterns

# Interaction architecture
Kaptio should behave like a connected operational workspace, not a collection of disconnected dialogs.

## Core principle
Keep users in context. Do not interrupt workflows unnecessarily.

Kaptio is a complex operational platform where users frequently need to reference, compare and modify interconnected information. The interface must prioritise persistent context, predictable navigation and uninterrupted workflows.

Default ruleNever use a modal for a task that requires users to reference, compare or modify information outside that modal. Modals are exceptions, not the default interaction pattern.StatusMandatory for all new features, redesigned screens and shared UI components.
## Approved interaction patterns
Use this hierarchy when designing an interaction. Each pattern has a Flux component; use it rather than building another.

PriorityPatternUse forFlux component1Inline editingSimple changes to existing information[Editable cell](/components/editable-cell/)2Expandable sectionsRevealing additional information in context[Accordion](/components/accordion/)3Contextual side panelsFocused editing and secondary tasks[Drawer](/components/drawer/)4Split-view workspacesComparing, selecting and configuring information[List and detail](/components/split-view/)5Dedicated pagesComplex or multi-step workflows[App shell](/components/app-shell/)ExceptionModal dialogsCritical confirmations and short blocking decisions[Modal](/components/modal/)Choose the least disruptive pattern that provides sufficient space, context and clarity for the task.

Do not force complex interactions into small containers simply to avoid navigating to another page.

## Modal usage
Modals are exceptions. A modal that fails any condition below is a defect.

### Permitted only when all of these hold

- The interaction requires immediate attention or an explicit decision.
- The task is short and self-contained.
- The user does not need to reference underlying content.
- The interaction contains no complex navigation.
- The dialog has a clear primary action and a clear way to dismiss or cancel.Acceptable examples:

- Confirm deleting a booking.
- Confirm discarding unsaved changes.
- Confirm an irreversible financial action.
- Resolve a short, blocking decision.
### Prohibited
Modals must not be used for:

- Creating or editing complex bookings.
- Multi-step workflows.
- Searching and selecting inventory.
- Comparing products, services or prices.
- Assigning passengers to rooms or cabins.
- Editing complex pricing structures.
- Configuring departures or services.
- Large forms or editable data tables.
- Tasks requiring information from another screen.NeverNested modals are strictly prohibited. A modal must never open another modal.
### Behaviour
When a modal is justified:

- Provide a descriptive title.
- State the consequences of the action clearly.
- Use explicit button labels such as “Delete booking” instead of “OK”.
- Preserve underlying data when cancelled.
- Return focus to the triggering element when closed, where possible.
- Trap keyboard focus while open.
- Support Escape to dismiss when safe.
- Never allow backdrop dismissal to silently discard changes.The [Modal](/components/modal/) is built on the native dialog, so focus trapping, Escape and returning focus come from the platform. It is never wider than 90% of the window, and that width never makes it suitable for a table, a comparison or a form.

## Contextual side panels
The preferred pattern for focused secondary tasks. In Flux, the Drawer.

### Use a side panel when

- The user needs to inspect or edit details without leaving the current workspace.
- The underlying information remains relevant.
- The task is relatively short.
- The user benefits from seeing the result of changes in context.
### Requirements

- Panels must have consistent widths and positioning.
- Panels must have clear titles and close controls.
- The underlying workspace should remain accessible when the workflow requires it.
- Unsaved changes must be handled explicitly.
- Opening a panel must not unexpectedly reset the main workspace.
- Panels must support keyboard navigation and appropriate focus management.The [Drawer](/components/drawer/) covers these: two widths, a title and close button, focus that returns to its opener, and fields that keep what was typed when it closes. Once a field has been edited, a click outside no longer closes it. At 48rem and narrower it becomes a full-screen view by itself, so a page never needs to override it. When the workspace behind must stay usable while the panel is open, use the [List and detail](/components/split-view/)split view instead.

### Do not use a side panel for

- Complex multi-step workflows.
- Large configuration interfaces.
- Tasks requiring extensive horizontal space.
- Interactions that require multiple nested panels.When a side panel becomes too complex, promote the task to a dedicated page.

## Inline editing
The preferred method for modifying simple values. In Flux, the Editable cell.

Suitable fields include prices, quantities, dates, names, statuses, allotments, simple configuration values.

### Requirements

- Editable values must be clearly identifiable.
- Editing must not unexpectedly change the surrounding layout.
- Validation must appear close to the affected field.
- Save behaviour must be predictable.
- Failed saves must preserve the entered value and display a clear error.
- Users must receive visible feedback when changes are saved.Use explicit Save and Cancel actions when changes are consequential or involve multiple related fields. Never silently save irreversible or high-impact changes.

## Dedicated workspaces
Complex Kaptio workflows use dedicated pages or persistent workspaces.

For example: Package Builder, Booking Management, Cabin Assignment, Departure Configuration, Inventory Management, Complex Pricing Configuration.

### Requirements

- Preserve the user’s position and working context.
- Keep relevant information visible whenever practical.
- Support navigation between related tasks.
- Avoid unnecessary page resets.
- Preserve filters, selections and scroll positions where appropriate.
- Provide clear loading, saving, success and error states.
- Allow users to return to previous steps without losing valid work.Where useful, a workspace supports:

- Split-view layouts
- Persistent detail panels
- Contextual actions
- Expandable sections
- Inline editing
- Sticky summaries or action barsCarefulA complex workflow must never be compressed into a modal solely to avoid page navigation.
## Navigation and state preservation
Navigation must not destroy user context.

When users navigate between related views:

- Preserve active filters and sorting.
- Preserve selected records where appropriate.
- Maintain draft data.
- Restore relevant scroll positions.
- Provide a predictable return path.
- Warn before discarding unsaved changes.Where practical, represent important workspace states in the URL to support bookmarking, browser history and direct navigation. Browser Back must behave predictably.

## Progressive disclosure
Do not display every available control by default. Reveal complexity progressively based on the user’s current task.

- Show essential information first.
- Group related controls logically.
- Place advanced settings in expandable sections.
- Reveal contextual actions when relevant.
- Avoid hiding frequently used primary actions.
- Do not use modals merely to reduce visual clutter.Progressive disclosure must reduce cognitive load without making functionality difficult to discover.

## Responsive behaviour
Interaction patterns adapt to the available space without losing the task or its state.

DesktopNarrow screensSplit-view workspaceStacked or sequential viewsContextual side panelFull-screen detail viewInline editingInline or focused edit viewMulti-column configurationSingle-column layoutResponsive behaviour must preserve task functionality and user state.

A side panel may become a full-screen view on smaller screens without becoming a modal dialog.

## Interaction consistency
The same type of task must use the same interaction pattern across Kaptio unless a documented exception is justified.

- Editing a simple field behaves consistently across modules.
- Opening record details follows a consistent pattern.
- Saving and cancelling follow shared conventions.
- Destructive actions use consistent confirmation behaviour.
- Side panels use shared components and interaction rules.Do not introduce a new interaction pattern when an approved design-system pattern already solves the problem.

## Design review checklist
Verify each item before approving a new feature or interaction.

- Can the user complete the task without an unnecessary modal?
- Does the interaction preserve relevant context?
- Is the selected pattern appropriate for the task’s complexity?
- Can users reference related information when necessary?
- Are editing and save behaviours predictable?
- Are navigation and workspace states preserved appropriately?
- Is the interaction consistent with other Kaptio modules?
- Does the design support keyboard and accessible interaction?
- Does the layout work across supported screen sizes?
- Are errors, loading states and unsaved changes handled?CarefulAny failed item must be resolved or documented as an approved exception before implementation.
## Exceptions and enforcement
Any proposed modal outside the permitted use cases requires design review. The proposal must explain:

- Why the interaction must interrupt the current workflow.
- Why inline editing, a side panel or a dedicated page is unsuitable.
- How user context and unsaved changes will be preserved.
- How accessibility and keyboard interaction will be supported.Exceptions must be documented and approved by the design owner.

Existing modal-based workflows should be assessed and prioritised for replacement when redesigned. They do not require immediate migration solely because these rules have been introduced.

Guiding principleKeep the workspace visible. Keep the user in control. Keep the workflow moving.[PreviousComposition discipline](/patterns/composition/)[NextForms](/patterns/forms/)
