# Flux — /components/badge

Source: https://flux.kaptio.com/components/badge

[Flux](/)       [Components](/components) / Data Display

# Badge
Compact labels for status, categories, and counts.

### Solid
DefaultSuccessWarningError
### Outline
DefaultSuccessWarningError
### Sizes
Same solid “Default” fill as above (`--flux-primary-200` on `--flux-black` text) — only padding and type scale change.

SmallMediumLarge
### Status
Colour-coded status badges indicating required action or current state. Consistent across all system views.

Action RequiredUser needs to take actionPendingAwaiting user responseAwaiting SupplierWaiting on supplier confirmationConfirmedConfirmed and readyCompletedSuccessfully completedCancelledCancelled by user or systemRejectedRejected by supplier
### Quantity / Inventory
System colour codes for inventory and availability status pills. All colours meet WCAG AAA contrast on white backgrounds.

Live InventoryAPIvar(--flux-primary-200)AAA 10.25:1Allotment (8)AL (8)var(--flux-blue-200)AAA 11.4:1Free SaleFSvar(--flux-purple-200)AAA 10.88:1MixedMXvar(--flux-pink-200)AAA 11.41:1On RequestRQvar(--flux-yellow-300)AAA 11.77:1ClosedCvar(--flux-orange-300)AAA 8.74:1Not AvailableNAvar(--flux-orange-300)AAA 8.74:1Sold OutSOvar(--flux-orange-300)AAA 8.74:1PromotionsAAAvar(--flux-green-200)AAA 11.58:1       Source  BadgeDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/badge.txt](/components/source/badge.txt).

import React from "react";

function Section({ title, children }: { title: string; children: React.ReactNode }) {
return (
<div className="mb-8">
<h3 className="text-sm font-bold text-[var(--flux-heading)] mb-3">{title}</h3>
<div className="p-6 rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)]">
{children}
</div>
</div>
);
}

const solidBadge = "inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold";
const outlineBadge = "inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold bg-transparent border";
const pillBase = "inline-flex items-center justify-center px-3 py-1 rounded-full text-xs font-bold min-w-[110px]";
const pillCodeBase = "inline-flex items-center justify-center px-2.5 py-1 rounded-full text-xs font-bold min-w-[48px]";

interface InventoryPill {
label: string;
code: string;
bg: string;
text: string;
contrast: string;
}

interface StatusBadge {
label: string;
bg: string;
text: string;
dot: string;
meaning: string;
}

const statusBadges: StatusBadge[] = [
{ label: 'Action Required', bg: 'var(--flux-yellow-300)', text: 'var(--flux-black)', dot: 'var(--flux-yellow-300)', meaning: 'User needs to take action' },
{ label: 'Pending', bg: 'var(--flux-yellow-300)', text: 'var(--flux-black)', dot: 'var(--flux-yellow-300)', meaning: 'Awaiting user response' },
{ label: 'Awaiting Supplier', bg: 'var(--flux-blue-200)', text: 'var(--flux-black)', dot: 'var(--flux-blue-200)', meaning: 'Waiting on supplier confirmation' },
{ label: 'Confirmed', bg: 'var(--flux-green-200)', text: 'var(--flux-black)', dot: 'var(--flux-green-200)', meaning: 'Confirmed and ready' },
{ label: 'Completed', bg: 'var(--flux-green-200)', text: 'var(--flux-black)', dot: 'var(--flux-green-200)', meaning: 'Successfully completed' },
{ label: 'Cancelled', bg: 'var(--flux-orange-300)', text: 'var(--flux-black)', dot: 'var(--flux-orange-300)', meaning: 'Cancelled by user or system' },
{ label: 'Rejected', bg: 'var(--flux-orange-300)', text: 'var(--flux-black)', dot: 'var(--flux-orange-300)', meaning: 'Rejected by supplier' },
];

const inventoryPills: InventoryPill[] = [
{ label: 'Live Inventory', code: 'API', bg: 'var(--flux-primary-200)', text: 'var(--flux-black)', contrast: '10.25' },
{ label: 'Allotment (8)', code: 'AL (8)', bg: 'var(--flux-blue-200)', text: 'var(--flux-black)', contrast: '11.4' },
{ label: 'Free Sale', code: 'FS', bg: 'var(--flux-purple-200)', text: 'var(--flux-black)', contrast: '10.88' },
{ label: 'Mixed', code: 'MX', bg: 'var(--flux-pink-200)', text: 'var(--flux-black)', contrast: '11.41' },
{ label: 'On Request', code: 'RQ', bg: 'var(--flux-yellow-300)', text: 'var(--flux-black)', contrast: '11.77' },
{ label: 'Closed', code: 'C', bg: 'var(--flux-orange-300)', text: 'var(--flux-black)', contrast: '8.74' },
{ label: 'Not Available', code: 'NA', bg: 'var(--flux-orange-300)', text: 'var(--flux-black)', contrast: '8.74' },
{ label: 'Sold Out', code: 'SO', bg: 'var(--flux-orange-300)', text: 'var(--flux-black)', contrast: '8.74' },
{ label: 'Promotions', code: 'AAA', bg: 'var(--flux-green-200)', text: 'var(--flux-black)', contrast: '11.58' },
];

export default function BadgeDemo() {
return (
<div>
<Section title="Solid">
<div className="flex flex-wrap gap-3">
<span className={solidBadge} style={{ backgroundColor: 'var(--flux-primary-200)', color: 'var(--flux-black)' }}>
Default
</span>
<span className={solidBadge} style={{ backgroundColor: 'var(--flux-green-200)', color: 'var(--flux-black)' }}>
Success
</span>
<span className={solidBadge} style={{ backgroundColor: 'var(--flux-yellow-300)', color: 'var(--flux-black)' }}>
Warning
</span>
<span className={solidBadge} style={{ backgroundColor: 'var(--flux-orange-300)', color: 'var(--flux-black)' }}>
Error
</span>
</div>
</Section>

<Section title="Outline">
<div className="flex flex-wrap gap-3">
<span className={`${outlineBadge} border-[var(--flux-primary-400)] text-[var(--flux-primary-400)]`}>
Default
</span>
<span className={`${outlineBadge} border-[var(--flux-green-400)] text-[var(--flux-green-600)]`}>
Success
</span>
<span className={`${outlineBadge} border-[var(--flux-yellow-800)] text-[var(--flux-yellow-800)]`}>
Warning
</span>
<span className={`${outlineBadge} border-[var(--flux-error)] text-[var(--flux-error)]`}>
Error
</span>
</div>
</Section>

<Section title="Sizes">
<p className="text-xs text-[var(--flux-black)] mb-3">
Same solid &ldquo;Default&rdquo; fill as above (<code>--flux-primary-200</code> on{' '}
<code>--flux-black</code> text) — only padding and type scale change.
</p>
<div className="flex flex-wrap items-center gap-3">
<span
className={solidBadge}
style={{ backgroundColor: 'var(--flux-primary-200)', color: 'var(--flux-black)' }}
>
Small
</span>
<span
className="inline-flex items-center px-3 py-1.5 rounded-full text-sm font-bold"
style={{ backgroundColor: 'var(--flux-primary-200)', color: 'var(--flux-black)' }}
>
Medium
</span>
<span
className="inline-flex items-center px-4 py-2 rounded-full text-base font-bold"
style={{ backgroundColor: 'var(--flux-primary-200)', color: 'var(--flux-black)' }}
>
Large
</span>
</div>
</Section>

<Section title="Status">
<p className="text-xs text-[var(--flux-black)] mb-4">
Colour-coded status badges indicating required action or current state. Consistent across all system views.
</p>
<div className="space-y-3">
{statusBadges.map(s => (
<div key={s.label} className="flex items-center gap-4">
<span className="flex items-center gap-2 min-w-[160px]">
<span className="w-0.5 h-3 rounded-sm flex-shrink-0" style={{ backgroundColor: s.dot }} />
<span className={`${solidBadge}`} style={{ backgroundColor: s.bg, color: s.text }}>{s.label}</span>
</span>
<span className="text-xs text-[var(--flux-black)]">{s.meaning}</span>
</div>
))}
</div>
</Section>

<Section title="Quantity / Inventory">
<p className="text-xs text-[var(--flux-black)] mb-4">
System colour codes for inventory and availability status pills. All colours meet WCAG AAA contrast on white backgrounds.
</p>
<div className="space-y-3">
{inventoryPills.map(pill => (
<div key={pill.label} className="flex items-center gap-4">
<span
className={pillBase}
style={{ backgroundColor: pill.bg, color: pill.text }}
>
{pill.label}
</span>
<span
className={pillCodeBase}
style={{ backgroundColor: pill.bg, color: pill.text }}
>
{pill.code}
</span>
<span className="text-xs font-mono text-[var(--flux-grey-300)] shrink-0 w-40 break-all" title={pill.bg}>
{pill.bg}
</span>
<span className="text-xs text-[var(--flux-grey-300)]">AAA {pill.contrast}:1</span>
</div>
))}
</div>
</Section>
</div>
);
}                  [← Avatar](/components/avatar) [Button →](/components/button)
