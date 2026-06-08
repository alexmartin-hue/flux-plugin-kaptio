# Flux — /components/flow-entry

Source: https://flux.kaptio.com/components/flow-entry

[Flux](/)       [Components](/components) / Outcome Patterns

# Flow Entry
The arriving state — what users see while their context resolves, with loading, error, and transition states.

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

Go Back       Source  FlowEntryDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/flow-entry.txt](/components/source/flow-entry.txt).

import React, { useState, useEffect, useCallback } from 'react';

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

const shimmerStyle: React.CSSProperties = {
background:
'linear-gradient(90deg, var(--flux-grey-100) 25%, var(--flux-grey-50, #f9fafb) 50%, var(--flux-grey-100) 75%)',
backgroundSize: '200% 100%',
animation: 'shimmer 1.5s infinite',
};

function Skeleton({ className }: { className: string }) {
return <div className={className} style={shimmerStyle} />;
}

function KaptioMark({ size = 32 }: { size?: number }) {
return (
<svg width={size} height={size} viewBox="0 0 24 24" fill="none">
<circle cx="12" cy="12" r="10" stroke="var(--flux-primary-400)" strokeWidth="1.5" />
<circle cx="12" cy="12" r="3" fill="var(--flux-primary-400)" />
</svg>
);
}

function SkeletonHeader() {
return (
<div
className="flex items-center justify-between px-4"
style={{
height: 'var(--flux-flow-header-height, 3rem)',
backgroundColor: 'var(--flux-flow-header-bg, #F5F5F5)',
borderBottom: '1px solid var(--flux-flow-header-border, #EBEBEB)',
}}
>
<div className="flex items-center gap-2.5">
<Skeleton className="w-5 h-5 rounded-full" />
<Skeleton className="h-3 w-48 rounded" />
</div>
<Skeleton className="h-3 w-20 rounded" />
</div>
);
}

function LoadingState({ message, variant = 'document' }: { message: string; variant?: 'document' | 'payment' | 'preferences' }) {
return (
<div>
<SkeletonHeader />
<div className="p-6">
<div className="flex items-center gap-3 mb-6">
<KaptioMark size={28} />
<p className="text-sm text-[var(--flux-grey-500)]">{message}</p>
</div>

{variant === 'document' && (
<div className="space-y-4 max-w-lg">
<Skeleton className="h-6 w-3/4 rounded" />
<Skeleton className="h-3 w-full rounded" />
<Skeleton className="h-3 w-5/6 rounded" />
<Skeleton className="h-3 w-2/3 rounded" />
<div className="pt-4 flex gap-3">
<Skeleton className="h-40 w-1/2 rounded" />
<Skeleton className="h-40 w-1/2 rounded" />
</div>
</div>
)}

{variant === 'payment' && (
<div className="space-y-4 max-w-sm">
<Skeleton className="h-5 w-1/2 rounded" />
<div className="space-y-3 pt-2">
<Skeleton className="h-10 w-full rounded" />
<Skeleton className="h-10 w-full rounded" />
<div className="flex gap-3">
<Skeleton className="h-10 w-1/2 rounded" />
<Skeleton className="h-10 w-1/2 rounded" />
</div>
</div>
<Skeleton className="h-11 w-full rounded mt-2" />
</div>
)}

{variant === 'preferences' && (
<div className="space-y-4 max-w-md">
<Skeleton className="h-5 w-2/5 rounded" />
<div className="space-y-3">
{[1, 2, 3].map((i) => (
<div key={i} className="flex items-center gap-3">
<Skeleton className="w-10 h-10 rounded-full shrink-0" />
<div className="flex-1 space-y-2">
<Skeleton className="h-3 w-3/4 rounded" />
<Skeleton className="h-3 w-1/2 rounded" />
</div>
</div>
))}
</div>
</div>
)}
</div>
</div>
);
}

function ErrorState({ message, detail }: { message: string; detail: string }) {
return (
<div className="flex flex-col items-center justify-center py-16 gap-4 text-center px-6">
<div className="w-12 h-12 rounded-full bg-[color:var(--flux-orange-100)] flex items-center justify-center">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--flux-orange-400)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<circle cx="12" cy="12" r="10" />
<line x1="12" y1="8" x2="12" y2="12" />
<line x1="12" y1="16" x2="12.01" y2="16" />
</svg>
</div>
<div>
<p className="text-sm font-bold text-[var(--flux-heading)] mb-1">{message}</p>
<p className="text-xs text-[var(--flux-grey-500)]">{detail}</p>
</div>
<button className="mt-2 px-4 py-2 text-sm font-bold rounded bg-[var(--flux-primary-400)] text-white hover:opacity-90 transition-opacity">
Go Back
</button>
</div>
);
}

function ResolvedState() {
return (
<div
className="flex flex-col items-center justify-center py-16 gap-2"
style={{
animation: 'fadeIn var(--flux-flow-entry-duration, 300ms) var(--flux-ease, ease) forwards',
}}
>
<div className="w-10 h-10 rounded-full bg-[color:var(--flux-green-100)] flex items-center justify-center">
<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="var(--flux-green-400)" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<polyline points="16 6 8 14 4 10" />
</svg>
</div>
<p className="text-sm text-[var(--flux-grey-500)]">Ready</p>
</div>
);
}

type DemoState = 'loading' | 'resolved' | 'error';

function InteractiveDemo() {
const [state, setState] = useState<DemoState>('loading');

const cycle = useCallback(() => {
setState('loading');
const t1 = setTimeout(() => setState('resolved'), 2500);
const t2 = setTimeout(() => setState('loading'), 4500);
return () => { clearTimeout(t1); clearTimeout(t2); };
}, []);

useEffect(() => {
const cleanup = cycle();
return cleanup;
}, [cycle]);

return (
<div>
<div className="flex gap-2 p-3 border-b border-[var(--flux-grey-100)]">
{(['loading', 'resolved', 'error'] as const).map((s) => (
<button
key={s}
onClick={() => setState(s)}
className={`px-3 py-1 text-xs font-bold rounded transition-colors capitalize ${
state === s
? 'bg-[var(--flux-primary-400)] text-white'
: 'text-[var(--flux-grey-500)] hover:bg-[var(--flux-grey-100)]'
}`}
>
{s === 'loading' ? 'Arriving' : s === 'resolved' ? 'Ready' : 'Error'}
</button>
))}
</div>
{state === 'loading' && <LoadingState message="Opening your proposal..." variant="document" />}
{state === 'resolved' && <ResolvedState />}
{state === 'error' && (
<ErrorState
message="This link has expired"
detail="Please go back to your booking and try again."
/>
)}
</div>
);
}

export default function FlowEntryDemo() {
return (
<div>
<style>{`
@keyframes shimmer {
0% { background-position: -200% 0; }
100% { background-position: 200% 0; }
}
@keyframes fadeIn {
from { opacity: 0; transform: translateY(8px); }
to { opacity: 1; transform: translateY(0); }
}
`}</style>

<Section title="Interactive (cycles through states)">
<InteractiveDemo />
</Section>

<Section title="Document editor (skeleton)">
<LoadingState message="Opening your proposal..." variant="document" />
</Section>

<Section title="Payment form (skeleton)">
<LoadingState message="Preparing payment..." variant="payment" />
</Section>

<Section title="Preferences (skeleton)">
<LoadingState message="Loading preferences..." variant="preferences" />
</Section>

<Section title="Error state (expired)">
<ErrorState
message="This link has expired"
detail="Please go back to your booking and try again."
/>
</Section>

<Section title="Error state (generic)">
<ErrorState
message="Something went wrong"
detail="Please close this and try again from your booking."
/>
</Section>
</div>
);
}                  [← Outcome Header](/components/outcome-header) [Outcome Complete →](/components/outcome-complete)
