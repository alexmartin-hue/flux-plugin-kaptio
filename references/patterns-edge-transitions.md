# Flux — /patterns/edge-transitions

Source: https://flux.kaptio.com/patterns/edge-transitions

[Flux](/)       [Patterns](/patterns) /
Edge Transitions

# Salesforce ↔ Edge Transitions

When a user clicks "Send Proposal" on a booking, they're not thinking about
which system they're entering. They're focused on getting a proposal in front
of their client. This pattern defines how users move between Salesforce and
Edge apps — kept anchored to their outcome from start to finish, with the
technology boundary invisible.

Scope

This pattern applies to operator flows —
where a Salesforce user (sales rep, operations manager, call-centre agent)
steps into an Edge app to complete an outcome and then returns to their
Salesforce context.

Some Edge apps are also guest-facing —
used by the end traveller, not the operator. A traveller clicking "Pay Now"
from an email, viewing a published proposal, or filling in travel preferences
has no Salesforce context, no Outcome Header, and no "Back to Booking" action.
Guest-facing flows have their own entry and completion patterns and are not
covered here.

## Design Principles

### Outcome, not system

The UI reinforces the outcome — "Proposal for Smith Family Safari" — never
the system name. "Create Quote" is an action. "Edge Editor" is a system.
Neither belongs in the user's mental model. The outcome does.

### Continuous context

The booking name, client name, and outcome label persist throughout the
flow. When the user is choosing fonts for a document, they should still
see "Smith Family Safari" at the top of the screen. Context is the thread.

### Natural conclusion

Outcomes have a shape: begin, work, achieve. "Proposal sent to 3
recipients" is a conclusion. "Document saved successfully" is a system
confirmation — it doesn't tell the user they achieved what they set out to do.

### Invisible seams

The transition between systems should feel like zooming into a detail,
not teleporting. Visual continuity — shared design language, the outcome
label persisting, familiar typography — bridges any technical boundary.

## The Lifecycle
1. Arriving

"Opening your proposal..." — context is being resolved. The user sees a
branded loading state with an outcome-specific message. Never "Validating
token..." or "Loading editor..."

2. Working

The Outcome Header persists at the top: "Proposal for Smith Family
Safari" with a "Done" action always visible. The user works toward
their outcome with full context.

3. Achieved

"Proposal sent to 3 recipients" — the outcome is confirmed. Primary
action returns to context ("Back to Booking"), with logical next steps
offered alongside.

## Pattern Components

### Outcome Header

A persistent bar at the top of every outcome flow. It answers "what outcome
am I achieving?" and "how do I step back?" at a glance. The outcome label
should read like something you'd say to a colleague: "I'm working on the
proposal for Smith Family Safari."

### Full context
Back to SalesforceProposal for Smith Family Safari

Application content area
### Minimal (no return context)
Payment

DoneApplication content area
### Branded accent
Back to SalesforceQuote for Torres Family — Patagonia Circuit

Application content area
### Long label (truncates gracefully)
Back to SalesforceFinancial Summary for Andersen Anniversary Group — 14-Day New Zealand & Australia Explorer with Fiji Extension

Application content area
### Flow Entry

What the user sees during the first 1–3 seconds while context is resolved.
This is the most fragile moment — if it feels broken or slow, the seam
between systems becomes visible and the user's confidence drops.

### Interactive (cycles through states)
ArrivingReadyErrorOpening your proposal...

### Document editor (skeleton)
Opening your proposal...

### Payment form (skeleton)
Preparing payment...

### Preferences (skeleton)
Loading preferences...

### Error state (expired)

- This link has expired

Please go back to your booking and try again.

Go Back
### Error state (generic)

- Something went wrong

Please close this and try again from your booking.

Go Back
### Outcome Complete

The moment the user achieves their outcome. The confirmation is specific
and concrete — about what was accomplished, not about system state. The
user is guided back to their context or forward to their next likely step.

### Proposal sent
Achievement with next-step actions and auto-return countdown.

Proposal sent to 3 recipients

Smith Family Safari — Booking Quote v2

Back to Booking (5s)Cancel auto-returnOr continue with

Collect PaymentView Proposal
### Payment collected
Financial outcome with download and summary options.

Payment of $2,450.00 collected

Booking #4821 — Smith Family Safari

Back to ItineraryOr continue with

Download ReceiptView Financial Summary
### Preferences saved
Minimal success — no next steps, just a return action.

Preferences saved

Smith Family Safari — 3 traveller profiles updated

Back to Booking
### Minimal (no return context)
When no returnLabel is available, the action reads "Done".

Document published

Available at the viewer link

Done
## Copywriting Guide
The test: if the user would
need to know what Salesforce, Edge, JWT, a session, or any internal system name
is to understand the message, rewrite it. If the message describes an action or
system state instead of an outcome, rewrite it.

Instead of Write     "Return to Salesforce" "Back to Booking" / "Done"   "Create Quote" (as heading) "Proposal for Smith Family Safari"   "Validating token..." "Opening your proposal..."   "Edge Editor" / "Payment App" (Name the outcome, not the system)   "Session expired" "This link has expired. Go back and try again."   "Error: JWT malformed" "Something went wrong. Please close this and try again."   "Operation completed successfully" "Proposal sent to 3 recipients"   "Task: Collect Payment" "Payment for Booking #4821"
## Developer Contract

For the pattern to work, every Edge app must accept these fields in the JWT
payload or as query parameters.

returnUrl

Where "Done" / "Back to..." sends the user. Required for same-tab redirect flows; optional for new-tab flows (falls back to "You can close this tab").

outcomeLabel

Human-readable outcome phrase, e.g. "Proposal for Smith Family Safari". Shown in the Outcome Header and Flow Entry. Falls back to a generic label derived from context.

returnLabel

Human-readable return destination, e.g. "Booking", "Lead", "Itinerary". Used to construct "Back to {returnLabel}". Falls back to "Done".

### Minimum JWT Payload
{
"tenantId": "duvine",
"orgId": "00D...",
"userId": "005...",
"recordId": "a0B...",
"returnUrl": "https://org.lightning.force.com/lightning/r/.../view",
"outcomeLabel": "Proposal for Smith Family Safari",
"returnLabel": "Booking"
}
### Return Behaviour
returnUrl present Redirect to the URL. Works for both new-tab and same-tab launch modes.

no returnUrl + tab `window.close()`, with fallback message: "You can close this tab."

embedded iframe `postMessage({ type: "outcome-complete", payload })` to parent frame.

## Design Tokens
Token Value Purpose     --flux-flow-header-height 3rem (48px) Outcome header bar height   --flux-flow-header-bg #F5F5F5 Header background   --flux-flow-header-border #EBEBEB Header bottom border   --flux-flow-entry-duration 300ms Arriving-state fade-in   --flux-flow-achieved-duration 200ms Transition to achieved state   --flux-flow-return-countdown 5000ms Auto-return countdown default
