# Flux — /components/accordion

Source: https://flux.kaptio.com/components/accordion

[Flux](/)       [Components](/components) / Layout & Overlay

# Accordion
Vertically stacked sections that expand and collapse to reveal content.

### Single item
What is Kaptio Travel?Kaptio Travel is an end-to-end travel management platform built for tour operators, wholesalers, and travel businesses that need to manage complex itineraries, inventory, and bookings at scale.
### Exclusive (one open at a time)
What is included in the booking?Each booking includes the core service, all applicable taxes, and standard support. Optional add-ons such as seat upgrades and travel insurance are available at checkout.How do I modify or cancel a reservation?Reservations can be modified or cancelled from the booking management screen up to 24 hours before departure. Cancellation policies vary by supplier and fare class.When will I receive my confirmation?Confirmations are sent to the email address on file within a few minutes of successful payment. Check your spam folder if you have not received it after 10 minutes.Is dynamic pricing applied at checkout?Yes. Prices shown reflect live inventory rates at the time of search. The final amount is confirmed at the point of payment and does not change after booking.
### Multiple (several can be open)
Expand allNotificationsConfigure email and in-app notification preferences per event type. Changes take effect immediately and apply to all connected channels.Data retentionBooking records are retained for 7 years by default in accordance with financial regulations. Contact your account manager to discuss custom retention policies.IntegrationsConnect third-party tools via the Integrations panel. OAuth tokens are stored encrypted and can be revoked at any time from the API settings page.
### Complex content
Booking BK-2024-03817 — Iceland Self-Drive, 5 nightsRefServiceNightsPaxUnit priceTotalStatusKT-00421Hotel — Reykjavik Natura32€189€1134ConfirmedKT-00422Northern Lights Tour12€95€190ConfirmedKT-00423Airport Transfer × 2—2€45€90PendingKT-00424Blue Lagoon Entry—2€79€158On RequestExport PDFAdd serviceSubtotal €1572VAT 20% €314Total  €1886Booking BK-2024-03651 — Lofoten Highlights, 7 nightsFull breakdown not yet loaded — click to fetch from supplier.

Booking BK-2024-03420 — Scottish Highlands Tour, 4 nightsFull breakdown not yet loaded — click to fetch from supplier.

### Disabled item
General settingsThese settings apply across the entire account and are inherited by all sub-users unless overridden.Enterprise-only settingsNot reachable.SupportContact your account manager or open a ticket via the help centre.       Source  AccordionDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/accordion.txt](/components/source/accordion.txt).

import { useState } from "react";

// ---------------------------------------------------------------------------
// Accordion primitives
// ---------------------------------------------------------------------------

interface AccordionItemProps {
title: string;
children: React.ReactNode;
open: boolean;
onToggle: () => void;
disabled?: boolean;
isLast?: boolean;
}

function AccordionItem({ title, children, open, onToggle, disabled = false, isLast = false }: AccordionItemProps) {
return (
<div
style={{
borderBottom: isLast ? "none" : "1px solid var(--flux-grey-100)",
}}
>
<button
type="button"
aria-expanded={open}
disabled={disabled}
onClick={onToggle}
style={{
width: "100%",
display: "flex",
alignItems: "center",
justifyContent: "space-between",
padding: "1rem 0",
background: "none",
border: "none",
cursor: disabled ? "not-allowed" : "pointer",
textAlign: "left",
gap: "1rem",
opacity: disabled ? 0.4 : 1,
}}
>
<span
style={{
fontSize: "0.9375rem",
fontWeight: 700,
color: "var(--flux-heading)",
fontFamily: "inherit",
}}
>
{title}
</span>
<ChevronIcon open={open} />
</button>

{/* Height animation via grid-template-rows */}
<div
style={{
display: "grid",
gridTemplateRows: open ? "1fr" : "0fr",
transition: "grid-template-rows 240ms cubic-bezier(0.23,1,0.32,1)",
}}
>
<div style={{ overflow: "hidden" }}>
<div
style={{
paddingBottom: "1.25rem",
fontSize: "0.9rem",
lineHeight: 1.65,
color: "var(--flux-black)",
}}
>
{children}
</div>
</div>
</div>
</div>
);
}

function ChevronIcon({ open }: { open: boolean }) {
return (
<svg
width="16"
height="16"
viewBox="0 0 16 16"
fill="none"
aria-hidden="true"
style={{
flexShrink: 0,
transform: open ? "rotate(180deg)" : "rotate(0deg)",
transition: "transform 240ms cubic-bezier(0.23,1,0.32,1)",
color: "var(--flux-grey-300)",
}}
>
<path d="M4 6l4 4 4-4" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
</svg>
);
}

// Single-select accordion: only one item open at a time
function ExclusiveAccordion({ items }: { items: { title: string; body: string }[] }) {
const [open, setOpen] = useState<number | null>(0);
return (
<div>
{items.map((item, i) => (
<AccordionItem
key={i}
title={item.title}
open={open === i}
onToggle={() => setOpen(open === i ? null : i)}
isLast={i === items.length - 1}
>
{item.body}
</AccordionItem>
))}
</div>
);
}

// Multi-select accordion: multiple items can be open simultaneously.
// open / onToggle / onExpandAll / onCollapseAll are controlled externally
// so a parent can wire up "Expand all / Collapse all".
interface MultiAccordionProps {
items: { title: string; body: string }[];
open: Set<number>;
onToggle: (i: number) => void;
}
function MultiAccordion({ items, open, onToggle }: MultiAccordionProps) {
return (
<div>
{items.map((item, i) => (
<AccordionItem
key={i}
title={item.title}
open={open.has(i)}
onToggle={() => onToggle(i)}
isLast={i === items.length - 1}
>
{item.body}
</AccordionItem>
))}
</div>
);
}

// ---------------------------------------------------------------------------
// Demo
// ---------------------------------------------------------------------------

function Section({
title,
action,
children,
}: {
title: string;
action?: React.ReactNode;
children: React.ReactNode;
}) {
return (
<div className="mb-8">
<div className="flex items-center justify-between mb-3">
<h3 className="text-sm font-bold text-[var(--flux-heading)]">{title}</h3>
{action}
</div>
<div className="p-6 rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)]">
{children}
</div>
</div>
);
}

const BOOKING_ITEMS = [
{
title: "What is included in the booking?",
body: "Each booking includes the core service, all applicable taxes, and standard support. Optional add-ons such as seat upgrades and travel insurance are available at checkout.",
},
{
title: "How do I modify or cancel a reservation?",
body: "Reservations can be modified or cancelled from the booking management screen up to 24 hours before departure. Cancellation policies vary by supplier and fare class.",
},
{
title: "When will I receive my confirmation?",
body: "Confirmations are sent to the email address on file within a few minutes of successful payment. Check your spam folder if you have not received it after 10 minutes.",
},
{
title: "Is dynamic pricing applied at checkout?",
body: "Yes. Prices shown reflect live inventory rates at the time of search. The final amount is confirmed at the point of payment and does not change after booking.",
},
];

const SETTINGS_ITEMS = [
{
title: "Notifications",
body: "Configure email and in-app notification preferences per event type. Changes take effect immediately and apply to all connected channels.",
},
{
title: "Data retention",
body: "Booking records are retained for 7 years by default in accordance with financial regulations. Contact your account manager to discuss custom retention policies.",
},
{
title: "Integrations",
body: "Connect third-party tools via the Integrations panel. OAuth tokens are stored encrypted and can be revoked at any time from the API settings page.",
},
];

// ---------------------------------------------------------------------------
// Complex content demo
// ---------------------------------------------------------------------------

const BADGE: Record<string, { bg: string }> = {
confirmed:   { bg: "#BFE5B8" },
pending:     { bg: "#FFD78E" },
cancelled:   { bg: "#FFA99B" },
"on request": { bg: "#FFD78E" },
};

function StatusBadge({ label }: { label: string }) {
const { bg } = BADGE[label.toLowerCase()] ?? { bg: "#E5E7EB" };
return (
<span style={{
display: "inline-flex", alignItems: "center",
padding: "2px 10px", borderRadius: 9999,
fontSize: "0.7rem", fontWeight: 700,
backgroundColor: bg, color: "#1A1A1A", whiteSpace: "nowrap",
}}>
{label}
</span>
);
}

const BOOKING_LINES = [
{ ref: "KT-00421", service: "Hotel — Reykjavik Natura", nights: 3, pax: 2, unit: 189, status: "Confirmed" },
{ ref: "KT-00422", service: "Northern Lights Tour", nights: 1, pax: 2, unit: 95, status: "Confirmed" },
{ ref: "KT-00423", service: "Airport Transfer × 2",  nights: 0, pax: 2, unit: 45, status: "Pending" },
{ ref: "KT-00424", service: "Blue Lagoon Entry",     nights: 0, pax: 2, unit: 79, status: "On Request" },
];

function HoverButton({ variant, children }: { variant: "primary" | "ghost"; children: React.ReactNode }) {
const [hovered, setHovered] = useState(false);
const isPrimary = variant === "primary";
return (
<button
type="button"
onMouseEnter={() => setHovered(true)}
onMouseLeave={() => setHovered(false)}
style={{
padding: "6px 14px", borderRadius: 6, fontSize: "0.78rem", fontWeight: 700,
cursor: "pointer", border: "1px solid var(--flux-grey-100)",
transition: "background 160ms cubic-bezier(0.23,1,0.32,1), color 160ms ease, border-color 160ms ease, transform 160ms cubic-bezier(0.23,1,0.32,1), box-shadow 160ms ease",
transform: hovered ? "translateY(-1px)" : "translateY(0)",
...(isPrimary ? {
background: hovered ? "#0A4A56" : "var(--flux-primary-800)",
color: "#FFFFFF",
borderColor: "transparent",
boxShadow: hovered ? "0 4px 12px rgba(3,46,54,0.35)" : "none",
} : {
background: hovered ? "var(--flux-grey-100, #F3F4F6)" : "transparent",
color: hovered ? "var(--flux-heading)" : "var(--flux-grey-300)",
borderColor: hovered ? "var(--flux-grey-200, #E5E7EB)" : "var(--flux-grey-100)",
boxShadow: "none",
}),
}}
>
{children}
</button>
);
}

function BookingRow({ line: l, total, isLast }: { line: typeof BOOKING_LINES[0]; total: number; isLast?: boolean }) {
const [hovered, setHovered] = useState(false);
const [removed, setRemoved] = useState(false);

if (removed) return null;

return (
<tr
onMouseEnter={() => setHovered(true)}
onMouseLeave={() => setHovered(false)}
style={{
borderBottom: isLast ? "none" : "1px solid var(--flux-grey-100)",
backgroundColor: hovered ? "var(--flux-grey-50, #F8FAFB)" : "transparent",
transition: "background-color 120ms ease",
}}
>
<td style={{ padding: "0.65rem 0.75rem", fontFamily: "'Lexend', sans-serif", fontWeight: 300, fontSize: "0.78rem", color: "var(--flux-heading)" }}>{l.ref}</td>
<td style={{ padding: "0.65rem 0.75rem", fontWeight: 600, color: "var(--flux-heading)" }}>{l.service}</td>
<td style={{ padding: "0.65rem 0.75rem", textAlign: "center" }}>{l.nights || "—"}</td>
<td style={{ padding: "0.65rem 0.75rem", textAlign: "center" }}>{l.pax}</td>
<td style={{ padding: "0.65rem 0.75rem", textAlign: "right", fontVariantNumeric: "tabular-nums" }}>€{l.unit}</td>
<td style={{ padding: "0.65rem 0.75rem", textAlign: "right", fontWeight: 700, fontVariantNumeric: "tabular-nums" }}>€{total}</td>
<td style={{ padding: "0.65rem 0.75rem" }}><StatusBadge label={l.status} /></td>

{/* Inline actions — fade in on row hover */}
<td style={{ padding: "0.65rem 0.75rem", textAlign: "right", whiteSpace: "nowrap" }}>
<span style={{
display: "inline-flex", alignItems: "center", gap: "0.15rem",
opacity: hovered ? 1 : 0,
transition: "opacity 150ms ease",
}}>
<IconBtn title="Edit" onClick={() => alert(`Edit ${l.ref}`)}>
<svg width="16" height="16" viewBox="0 0 14 14" fill="none" aria-hidden="true">
<path d="M9.5 2.5l2 2L4 12H2v-2L9.5 2.5z" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round"/>
</svg>
</IconBtn>
<IconBtn title="Duplicate" onClick={() => alert(`Duplicate ${l.ref}`)}>
<svg width="16" height="16" viewBox="0 0 14 14" fill="none" aria-hidden="true">
<rect x="4" y="4" width="8" height="8" rx="1.5" stroke="currentColor" strokeWidth="1.3"/>
<path d="M2 10V2.5A.5.5 0 012.5 2H10" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round"/>
</svg>
</IconBtn>
<IconBtn title="Remove" danger onClick={() => setRemoved(true)}>
<svg width="16" height="16" viewBox="0 0 14 14" fill="none" aria-hidden="true">
<path d="M2 4h10M5 4V2.5h4V4M5.5 6.5v4M8.5 6.5v4M3.5 4l.5 7.5h6l.5-7.5" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round"/>
</svg>
</IconBtn>
</span>
</td>
</tr>
);
}

function IconBtn({ title, danger, onClick, children }: {
title: string; danger?: boolean; onClick: () => void; children: React.ReactNode;
}) {
const [hovered, setHovered] = useState(false);
return (
<button
type="button"
title={title}
onClick={onClick}
onMouseEnter={() => setHovered(true)}
onMouseLeave={() => setHovered(false)}
style={{
display: "inline-flex", alignItems: "center", justifyContent: "center",
width: 32, height: 32, borderRadius: 7,
background: hovered ? (danger ? "#FEE2E2" : "var(--flux-grey-100, #F3F4F6)") : "none",
border: "none", cursor: "pointer",
color: hovered ? (danger ? "#E05252" : "var(--flux-heading)") : (danger ? "#E05252" : "var(--flux-grey-300)"),
transition: "background 120ms ease, color 120ms ease",
transform: hovered ? "translateY(-1px)" : "translateY(0)",
}}
>
{children}
</button>
);
}

const iconBtnStyle: React.CSSProperties = {};

function BookingBreakdown() {
const subtotal = BOOKING_LINES.reduce((s, l) => s + l.unit * l.pax * Math.max(l.nights, 1), 0);
const tax = Math.round(subtotal * 0.2);
return (
<div style={{ fontSize: "0.82rem", color: "var(--flux-black)" }}>
{/* Line items */}
<div style={{ overflowX: "auto" }}>
<table style={{ width: "100%", borderCollapse: "collapse", whiteSpace: "nowrap", marginBottom: "0.75rem" }}>
<thead>
<tr style={{ borderBottom: "1px solid var(--flux-grey-100)" }}>
{["Ref", "Service", "Nights", "Pax", "Unit price", "Total", "Status", ""].map(h => (
<th key={h} style={{
padding: "0.4rem 0.75rem 0.6rem",
textAlign: ["Unit price", "Total"].includes(h) ? "right" : "left",
fontWeight: 700, fontSize: "0.7rem",
color: "var(--flux-grey-300)", textTransform: "uppercase", letterSpacing: "0.06em",
}}>{h}</th>
))}
</tr>
</thead>
<tbody>
{BOOKING_LINES.map((l, i) => {
const total = l.unit * l.pax * Math.max(l.nights, 1);
return (
<BookingRow key={i} line={l} total={total} isLast={i === BOOKING_LINES.length - 1} />
);
})}
</tbody>
</table>
</div>

{/* Totals + actions */}
<div style={{
display: "flex", alignItems: "flex-end", justifyContent: "space-between",
gap: "1rem", flexWrap: "wrap", paddingTop: "1rem", marginTop: "0.25rem",
}}>
<div style={{ display: "flex", gap: "0.5rem" }}>
<HoverButton variant="ghost">Export PDF</HoverButton>
<HoverButton variant="primary">Add service</HoverButton>

</div>
<div style={{ textAlign: "right", lineHeight: 1.8 }}>
<div style={{ color: "var(--flux-grey-300)", fontSize: "0.78rem" }}>
Subtotal <span style={{ color: "var(--flux-black)", fontWeight: 600, marginLeft: 8 }}>€{subtotal}</span>
</div>
<div style={{ color: "var(--flux-grey-300)", fontSize: "0.78rem" }}>
VAT 20% <span style={{ color: "var(--flux-black)", fontWeight: 600, marginLeft: 8 }}>€{tax}</span>
</div>
<div style={{ fontWeight: 700, fontSize: "0.9rem", color: "var(--flux-heading)", marginTop: 4 }}>
Total&nbsp;&nbsp;€{subtotal + tax}
</div>
</div>
</div>
</div>
);
}

function ComplexAccordion() {
const [open, setOpen] = useState<number | null>(0);
const items = [
{ title: "Booking BK-2024-03817 — Iceland Self-Drive, 5 nights", content: <BookingBreakdown /> },
{ title: "Booking BK-2024-03651 — Lofoten Highlights, 7 nights", content: <p style={{ fontSize: "0.85rem", color: "var(--flux-grey-300)" }}>Full breakdown not yet loaded — click to fetch from supplier.</p> },
{ title: "Booking BK-2024-03420 — Scottish Highlands Tour, 4 nights", content: <p style={{ fontSize: "0.85rem", color: "var(--flux-grey-300)" }}>Full breakdown not yet loaded — click to fetch from supplier.</p> },
];
return (
<div>
{items.map((item, i) => (
<AccordionItem key={i} title={item.title} open={open === i} onToggle={() => setOpen(open === i ? null : i)} isLast={i === items.length - 1}>
{item.content}
</AccordionItem>
))}
</div>
);
}

export default function AccordionDemo() {
const [singleOpen, setSingleOpen] = useState<boolean>(true);

// Controlled state for the "Multiple" section so the expand/collapse all
// button can act on all items at once.
const [multiOpen, setMultiOpen] = useState<Set<number>>(new Set([0]));
const allExpanded = multiOpen.size === SETTINGS_ITEMS.length;

const toggleMulti = (i: number) => {
const next = new Set(multiOpen);
next.has(i) ? next.delete(i) : next.add(i);
setMultiOpen(next);
};

const expandAll = () => setMultiOpen(new Set(SETTINGS_ITEMS.map((_, i) => i)));
const collapseAll = () => setMultiOpen(new Set());

return (
<div>
<Section title="Single item">
<AccordionItem
title="What is Kaptio Travel?"
open={singleOpen}
onToggle={() => setSingleOpen(!singleOpen)}
isLast
>
Kaptio Travel is an end-to-end travel management platform built for tour operators, wholesalers, and travel businesses that need to manage complex itineraries, inventory, and bookings at scale.
</AccordionItem>
</Section>

<Section title="Exclusive (one open at a time)">
<ExclusiveAccordion items={BOOKING_ITEMS} />
</Section>

<Section
title="Multiple (several can be open)"
action={
<button
type="button"
onClick={allExpanded ? collapseAll : expandAll}
style={{
display: "inline-flex",
alignItems: "center",
gap: "0.35rem",
fontSize: "0.75rem",
fontWeight: 700,
color: "var(--flux-primary-800)",
background: "none",
border: "none",
cursor: "pointer",
padding: "2px 0",
letterSpacing: "0.01em",
}}
>
{allExpanded ? (
<>
<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
<path d="M12 5H9V2M2 9H5V12M12 2L8 6M2 12L6 8" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"/>
</svg>
Collapse all
</>
) : (
<>
<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
<path d="M9 2H12V5M5 12H2V9M12 2L7 7M2 12L7 7" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"/>
</svg>
Expand all
</>
)}
</button>
}
>
<MultiAccordion
items={SETTINGS_ITEMS}
open={multiOpen}
onToggle={toggleMulti}
/>
</Section>

<Section title="Complex content">
<ComplexAccordion />
</Section>

<Section title="Disabled item">
<div>
<AccordionItem
title="General settings"
open={true}
onToggle={() => {}}
>
These settings apply across the entire account and are inherited by all sub-users unless overridden.
</AccordionItem>
<AccordionItem
title="Enterprise-only settings"
open={false}
onToggle={() => {}}
disabled
>
Not reachable.
</AccordionItem>
<AccordionItem
title="Support"
open={false}
onToggle={() => {}}
isLast
>
Contact your account manager or open a ticket via the help centre.
</AccordionItem>
</div>
</Section>
</div>
);
}                   [Avatar →](/components/avatar)
