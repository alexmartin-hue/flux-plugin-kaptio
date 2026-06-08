# Flux — /components/table

Source: https://flux.kaptio.com/components/table

[Flux](/)       [Components](/components) / Data Display

# Table
Structured data in rows and columns.

### Default
NameDestinationStatusPriceNorthern Lights TourReykjavik, IcelandConfirmed$2,450Amalfi Coast EscapeNaples, ItalyPending$3,800Safari AdventureNairobi, KenyaConfirmed$5,200Patagonia TrekEl Calafate, ArgentinaCancelled$4,100Kyoto Heritage WalkKyoto, JapanConfirmed$3,150
### Striped
NameDestinationStatusPriceNorthern Lights TourReykjavik, IcelandConfirmed$2,450Amalfi Coast EscapeNaples, ItalyPending$3,800Safari AdventureNairobi, KenyaConfirmed$5,200Patagonia TrekEl Calafate, ArgentinaCancelled$4,100Kyoto Heritage WalkKyoto, JapanConfirmed$3,150       Source  TableDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/table.txt](/components/source/table.txt).

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

const columns = ["Name", "Destination", "Status", "Price"] as const;

interface Row {
name: string;
destination: string;
status: string;
price: string;
}

// Flux badge colours — matches flux.kaptio.com/components/badge/
const BADGE_COLORS: Record<string, { bg: string }> = {
confirmed:           { bg: "#BFE5B8" },
completed:           { bg: "#BFE5B8" },
pending:             { bg: "#FFD78E" },
"action required":   { bg: "#FFD78E" },
"on request":        { bg: "#FFD78E" },
"awaiting supplier": { bg: "#C6DAFF" },
cancelled:           { bg: "#FFA99B" },
rejected:            { bg: "#FFA99B" },
expired:             { bg: "#FFA99B" },
};

function StatusBadge({ status }: { status: string }) {
const { bg } = BADGE_COLORS[status.toLowerCase()] ?? { bg: "#B4D4DA" };
return (
<span
className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold"
style={{ backgroundColor: bg, color: "#1A1A1A" }}
>
{status}
</span>
);
}

const rows: Row[] = [
{ name: "Northern Lights Tour",    destination: "Reykjavik, Iceland",       status: "Confirmed", price: "$2,450" },
{ name: "Amalfi Coast Escape",     destination: "Naples, Italy",            status: "Pending",   price: "$3,800" },
{ name: "Safari Adventure",        destination: "Nairobi, Kenya",           status: "Confirmed", price: "$5,200" },
{ name: "Patagonia Trek",          destination: "El Calafate, Argentina",   status: "Cancelled", price: "$4,100" },
{ name: "Kyoto Heritage Walk",     destination: "Kyoto, Japan",             status: "Confirmed", price: "$3,150" },
];

const thClass =
"text-xs font-bold uppercase tracking-wider text-[var(--flux-grey-300)] border-b border-[var(--flux-grey-100)] pb-3 text-left";
const tdClass = "py-3 border-b border-[var(--flux-grey-100)] text-[var(--flux-black)] font-light";

export default function TableDemo() {
return (
<div>
<Section title="Default">
<table className="w-full text-left text-sm">
<thead>
<tr>
{columns.map((col) => (
<th key={col} className={thClass}>
{col}
</th>
))}
</tr>
</thead>
<tbody>
{rows.map((row) => (
<tr key={row.name}>
<td className={tdClass}>{row.name}</td>
<td className={tdClass}>{row.destination}</td>
<td className={tdClass}>
<StatusBadge status={row.status} />
</td>
<td className={tdClass}>{row.price}</td>
</tr>
))}
</tbody>
</table>
</Section>

<Section title="Striped">
<table className="w-full text-left text-sm">
<thead>
<tr>
{columns.map((col) => (
<th key={col} className={thClass}>
{col}
</th>
))}
</tr>
</thead>
<tbody>
{rows.map((row, i) => (
<tr
key={row.name}
className={i % 2 === 1 ? "bg-[var(--flux-background)]" : ""}
>
<td className={tdClass}>{row.name}</td>
<td className={tdClass}>{row.destination}</td>
<td className={tdClass}>
<StatusBadge status={row.status} />
</td>
<td className={tdClass}>{row.price}</td>
</tr>
))}
</tbody>
</table>
</Section>
</div>
);
}                  [← Switch](/components/switch) [Tabs →](/components/tabs)
