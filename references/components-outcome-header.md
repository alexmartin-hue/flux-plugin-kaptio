# Flux — /components/outcome-header

Source: https://flux.kaptio.com/components/outcome-header

[Flux](/)       [Components](/components) / Outcome Patterns

# Outcome Header
Persistent bar anchoring the user to the outcome they are achieving, with a clear return action.

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

Application content area       Source  OutcomeHeaderDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/outcome-header.txt](/components/source/outcome-header.txt).

import React, { useState } from 'react';

function Section({ title, children }: { title: string; children: React.ReactNode }) {
return (
<div className="mb-8">
<h3 className="text-sm font-bold text-[var(--flux-heading)] mb-3">{title}</h3>
<div className="rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)] overflow-hidden">
{children}
</div>
</div>
);
}

function KaptioMark({ color = 'var(--flux-primary-400)' }: { color?: string }) {
return (
<svg width="20" height="20" viewBox="0 0 24 24" fill="none">
<circle cx="12" cy="12" r="10" stroke={color} strokeWidth="2" />
<circle cx="12" cy="12" r="3" fill={color} />
</svg>
);
}

function ArrowLeftIcon() {
return (
<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
<path d="M10 12L6 8l4-4" />
</svg>
);
}

interface OutcomeHeaderProps {
outcomeLabel: string;
returnLabel?: string;
accentColor?: string;
}

function OutcomeHeader({ outcomeLabel, returnLabel, accentColor }: OutcomeHeaderProps) {
const hasAccent = !!accentColor;
const [hovered, setHovered] = useState(false);

return (
<div
className="relative flex items-center px-4 gap-3"
style={{
height: 'var(--flux-flow-header-height, 3rem)',
backgroundColor: 'var(--flux-flow-header-bg, #F5F5F5)',
borderBottom: '1px solid var(--flux-flow-header-border, #EBEBEB)',
}}
>
{hasAccent && (
<div
className="absolute top-0 left-0 right-0 h-[2px]"
style={{ backgroundColor: accentColor }}
/>
)}

{returnLabel && (
<button
className="flex items-center gap-1.5 transition-colors flex-shrink-0"
style={{ color: hovered ? 'var(--flux-primary-400)' : 'var(--flux-grey-500)', background: 'none', border: 'none', cursor: 'pointer', padding: 0 }}
onMouseEnter={() => setHovered(true)}
onMouseLeave={() => setHovered(false)}
>
<ArrowLeftIcon />
<span
style={{
fontSize: '0.75rem',
fontWeight: 500,
maxWidth: hovered ? '160px' : '0px',
opacity: hovered ? 1 : 0,
overflow: 'hidden',
whiteSpace: 'nowrap',
transition: 'max-width 220ms ease, opacity 150ms ease',
}}
>
Back to Salesforce
</span>
</button>
)}

<div className="flex items-center gap-2.5 min-w-0 flex-1">
<p className="text-sm font-bold text-[var(--flux-heading)] truncate">
{outcomeLabel}
</p>
</div>

{!returnLabel && (
<button className="flex items-center gap-1 text-sm text-[var(--flux-grey-500)] hover:text-[var(--flux-primary-400)] transition-colors flex-shrink-0" style={{ background: 'none', border: 'none', cursor: 'pointer' }}>
<span>Done</span>
</button>
)}
</div>
);
}

export default function OutcomeHeaderDemo() {
return (
<div>
<Section title="Full context">
<OutcomeHeader
outcomeLabel="Proposal for Smith Family Safari"
returnLabel="Booking"
/>
<div className="p-6 flex items-center justify-center h-32 text-sm text-[var(--flux-grey-300)]">
Application content area
</div>
</Section>

<Section title="Minimal (no return context)">
<OutcomeHeader outcomeLabel="Payment" />
<div className="p-6 flex items-center justify-center h-32 text-sm text-[var(--flux-grey-300)]">
Application content area
</div>
</Section>

<Section title="Branded accent">
<OutcomeHeader
outcomeLabel="Quote for Torres Family — Patagonia Circuit"
returnLabel="Itinerary"
accentColor="#DE37A4"
/>
<div className="p-6 flex items-center justify-center h-32 text-sm text-[var(--flux-grey-300)]">
Application content area
</div>
</Section>

<Section title="Long label (truncates gracefully)">
<OutcomeHeader
outcomeLabel="Financial Summary for Andersen Anniversary Group — 14-Day New Zealand & Australia Explorer with Fiji Extension"
returnLabel="Lead"
accentColor="#4F46E5"
/>
<div className="p-6 flex items-center justify-center h-32 text-sm text-[var(--flux-grey-300)]">
Application content area
</div>
</Section>
</div>
);
}                  [← Tooltip](/components/tooltip) [Flow Entry →](/components/flow-entry)
