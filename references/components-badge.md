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
SmallLarge
### Status
Colour-coded status badges indicating required action or current state. Consistent across all system views.

Action RequiredUser needs to take actionPendingAwaiting user responseAwaiting SupplierWaiting on supplier confirmationConfirmedConfirmed and readyCompletedSuccessfully completedCancelledCancelled by user or systemRejectedRejected by supplier
### Quantity / Inventory
System colour codes for inventory and availability status pills. All colours meet WCAG AAA contrast on white backgrounds.

Live InventoryAPI#B4D4DAAAA 10.25:1Allotment (8)AL (8)#C6DAFFAAA 11.4:1Free SaleFS#D5CFFFAAA 10.88:1MixedMX#F5C3E4AAA 11.41:1On RequestRQ#FFD78EAAA 11.77:1ClosedC#FFA99BAAA 8.74:1Not AvailableNA#FFA99BAAA 8.74:1Sold OutSO#FFA99BAAA 8.74:1PromotionsAAA#BFE5B8AAA 11.58:1       Source  BadgeDemo.tsx
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
{ label: 'Action Required', bg: '#FFD78E', text: '#1A1A1A', dot: '#FFD78E', meaning: 'User needs to take action' },
{ label: 'Pending', bg: '#FFD78E', text: '#1A1A1A', dot: '#FFD78E', meaning: 'Awaiting user response' },
{ label: 'Awaiting Supplier', bg: '#C6DAFF', text: '#1A1A1A', dot: '#C6DAFF', meaning: 'Waiting on supplier confirmation' },
{ label: 'Confirmed', bg: '#BFE5B8', text: '#1A1A1A', dot: '#BFE5B8', meaning: 'Confirmed and ready' },
{ label: 'Completed', bg: '#BFE5B8', text: '#1A1A1A', dot: '#BFE5B8', meaning: 'Successfully completed' },
{ label: 'Cancelled', bg: '#FFA99B', text: '#1A1A1A', dot: '#FFA99B', meaning: 'Cancelled by user or system' },
{ label: 'Rejected', bg: '#FFA99B', text: '#1A1A1A', dot: '#FFA99B', meaning: 'Rejected by supplier' },
];

const inventoryPills: InventoryPill[] = [
{ label: 'Live Inventory', code: 'API', bg: '#B4D4DA', text: '#1A1A1A', contrast: '10.25' },
{ label: 'Allotment (8)', code: 'AL (8)', bg: '#C6DAFF', text: '#1A1A1A', contrast: '11.4' },
{ label: 'Free Sale', code: 'FS', bg: '#D5CFFF', text: '#1A1A1A', contrast: '10.88' },
{ label: 'Mixed', code: 'MX', bg: '#F5C3E4', text: '#1A1A1A', contrast: '11.41' },
{ label: 'On Request', code: 'RQ', bg: '#FFD78E', text: '#1A1A1A', contrast: '11.77' },
{ label: 'Closed', code: 'C', bg: '#FFA99B', text: '#1A1A1A', contrast: '8.74' },
{ label: 'Not Available', code: 'NA', bg: '#FFA99B', text: '#1A1A1A', contrast: '8.74' },
{ label: 'Sold Out', code: 'SO', bg: '#FFA99B', text: '#1A1A1A', contrast: '8.74' },
{ label: 'Promotions', code: 'AAA', bg: '#BFE5B8', text: '#1A1A1A', contrast: '11.58' },
];

export default function BadgeDemo() {
return (
<div>
<Section title="Solid">
<div className="flex flex-wrap gap-3">
<span className={solidBadge} style={{ backgroundColor: '#B4D4DA', color: '#1A1A1A' }}>
Default
</span>
<span className={solidBadge} style={{ backgroundColor: '#BFE5B8', color: '#1A1A1A' }}>
Success
</span>
<span className={solidBadge} style={{ backgroundColor: '#FFD78E', color: '#1A1A1A' }}>
Warning
</span>
<span className={solidBadge} style={{ backgroundColor: '#FFA99B', color: '#1A1A1A' }}>
Error
</span>
</div>
</Section>

<Section title="Outline">
<div className="flex flex-wrap gap-3">
<span className={`${outlineBadge} border-[var(--flux-primary-400)] text-[var(--flux-primary-400)]`}>
Default
</span>
<span className={`${outlineBadge} border-[var(--flux-green-400)] text-[var(--flux-green-400)]`}>
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
<div className="flex flex-wrap items-center gap-3">
<span className="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-bold bg-[var(--flux-primary-100)] text-[var(--flux-primary-400)]">
Small
</span>
<span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-bold bg-[var(--flux-primary-100)] text-[var(--flux-primary-400)]">
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
<span className="text-xs font-mono text-[var(--flux-grey-300)] w-16">{pill.bg}</span>
<span className="text-xs text-[var(--flux-grey-300)]">AAA {pill.contrast}:1</span>
</div>
))}
</div>
</Section>
</div>
);
}                  [← Avatar](/components/avatar) [Button →](/components/button)
