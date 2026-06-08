# Flux — /components/outcome-complete

Source: https://flux.kaptio.com/components/outcome-complete

[Flux](/)       [Components](/components) / Outcome Patterns

# Outcome Complete
Achievement confirmation with auto-return, next-step guidance, and outcome summary.

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

Done       Source  OutcomeCompleteDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/outcome-complete.txt](/components/source/outcome-complete.txt).

import React, { useState, useEffect, useRef } from 'react';

function Section({ title, description, children }: { title: string; description?: string; children: React.ReactNode }) {
return (
<div className="mb-8">
<h3 className="text-sm font-bold text-[var(--flux-heading)] mb-1">{title}</h3>
{description && (
<p className="text-xs text-[var(--flux-grey-500)] mb-3">{description}</p>
)}
<div className="rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)] overflow-hidden">
{children}
</div>
</div>
);
}

function CheckCircle() {
return (
<div className="w-14 h-14 rounded-full bg-[color:var(--flux-green-100)] flex items-center justify-center">
<svg width="28" height="28" viewBox="0 0 28 28" fill="none" stroke="var(--flux-green-400)" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
<polyline points="20 8 11 18 7 14" />
</svg>
</div>
);
}

interface OutcomeCompleteProps {
achievement: string;
detail?: string;
returnLabel?: string;
nextSteps?: { label: string; accent?: string }[];
autoReturn?: boolean;
countdownMs?: number;
}

function OutcomeComplete({
achievement,
detail,
returnLabel,
nextSteps,
autoReturn = false,
countdownMs = 5000,
}: OutcomeCompleteProps) {
const [countdown, setCountdown] = useState(Math.ceil(countdownMs / 1000));
const [cancelled, setCancelled] = useState(false);
const intervalRef = useRef<ReturnType<typeof setInterval>>();

useEffect(() => {
if (!autoReturn || cancelled) return;
intervalRef.current = setInterval(() => {
setCountdown((c) => {
if (c <= 1) {
clearInterval(intervalRef.current);
return 0;
}
return c - 1;
});
}, 1000);
return () => clearInterval(intervalRef.current);
}, [autoReturn, cancelled]);

const handleCancel = () => {
setCancelled(true);
clearInterval(intervalRef.current);
};

const returnText = returnLabel ? `Back to ${returnLabel}` : 'Done';

return (
<div className="flex flex-col items-center justify-center py-12 px-6 text-center gap-4">
<CheckCircle />

<div>
<p className="text-lg font-bold text-[var(--flux-heading)] mb-1">{achievement}</p>
{detail && (
<p className="text-sm text-[var(--flux-grey-500)]">{detail}</p>
)}
</div>

<div className="flex flex-col items-center gap-3 mt-2">
<button className="px-5 py-2.5 text-sm font-bold rounded bg-[var(--flux-primary-400)] text-white hover:opacity-90 transition-opacity">
{autoReturn && !cancelled && countdown > 0
? `${returnText} (${countdown}s)`
: returnText}
</button>

{autoReturn && !cancelled && countdown > 0 && (
<button
onClick={handleCancel}
className="text-xs text-[var(--flux-grey-300)] hover:text-[var(--flux-grey-500)] transition-colors"
>
Cancel auto-return
</button>
)}
</div>

{nextSteps && nextSteps.length > 0 && (
<div className="mt-4 pt-4 border-t border-[var(--flux-grey-100)] w-full max-w-sm">
<p className="text-xs text-[var(--flux-grey-300)] mb-3">Or continue with</p>
<div className="flex flex-wrap justify-center gap-2">
{nextSteps.map((step) => (
<button
key={step.label}
className="px-3 py-1.5 text-xs font-bold rounded border border-[var(--flux-grey-100)] text-[var(--flux-grey-500)] hover:border-[var(--flux-primary-300)] hover:text-[var(--flux-primary-400)] transition-colors"
>
{step.label}
</button>
))}
</div>
</div>
)}
</div>
);
}

export default function OutcomeCompleteDemo() {
return (
<div>
<Section
title="Proposal sent"
description="Achievement with next-step actions and auto-return countdown."
>
<OutcomeComplete
achievement="Proposal sent to 3 recipients"
detail="Smith Family Safari — Booking Quote v2"
returnLabel="Booking"
autoReturn
nextSteps={[
{ label: 'Collect Payment' },
{ label: 'View Proposal' },
]}
/>
</Section>

<Section
title="Payment collected"
description="Financial outcome with download and summary options."
>
<OutcomeComplete
achievement="Payment of $2,450.00 collected"
detail="Booking #4821 — Smith Family Safari"
returnLabel="Itinerary"
nextSteps={[
{ label: 'Download Receipt' },
{ label: 'View Financial Summary' },
]}
/>
</Section>

<Section
title="Preferences saved"
description="Minimal success — no next steps, just a return action."
>
<OutcomeComplete
achievement="Preferences saved"
detail="Smith Family Safari — 3 traveller profiles updated"
returnLabel="Booking"
/>
</Section>

<Section
title="Minimal (no return context)"
description='When no returnLabel is available, the action reads "Done".'
>
<OutcomeComplete
achievement="Document published"
detail="Available at the viewer link"
/>
</Section>
</div>
);
}                  [← Flow Entry](/components/flow-entry)
