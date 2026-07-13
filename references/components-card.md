# Flux — /components/card

Source: https://flux.kaptio.com/components/card

[Flux](/)       [Components](/components) / Layout & Overlay

# Card
Contained surfaces for grouping related content and actions.

### Default

#### Iceland Explorer
7-day self-drive tour through the Golden Circle, south coast glaciers, and Reykjavik.

#### Northern Lights Chase
4-night winter adventure with guided aurora hunting and geothermal bathing.

### With header and footer

#### Departure Summary
ConfirmedPackageIceland ExplorerDate15 Jun 2026Guests12 / 16Revenue$48,600DetailsManage
### Interactive (hover)
Bookings

1,284

+12%

Revenue

$2.4M

+8%

Departures

47

+3

### With image

#### Midnight Sun Cruise
10-day coastal voyage along the Norwegian fjords under the midnight sun.

From $3,200New
### Muted / disabled

#### Archived Package
This package is no longer available for new bookings.

Source  CardDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/card.txt](/components/source/card.txt).

// Flux card hover — directional Flux-teal edge glow (see .flux-glow-card in global.css).
const cardHover = 'flux-glow-card';

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

function Badge({ children, color }: { children: React.ReactNode; color: string }) {
return (
<span
className="inline-flex px-2 py-0.5 rounded-full text-xs font-bold"
style={{ backgroundColor: color + '1a', color }}
>
{children}
</span>
);
}

export default function CardDemo() {
return (
<>
<Section title="Default">
<div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
<div className={`rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)] p-5 ${cardHover}`}>
<h4 className="text-sm font-bold text-[var(--flux-heading)] mb-1">Iceland Explorer</h4>
<p className="text-xs text-[var(--flux-black)] leading-relaxed">
7-day self-drive tour through the Golden Circle, south coast glaciers, and Reykjavik.
</p>
</div>
<div className={`rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)] p-5 ${cardHover}`}>
<h4 className="text-sm font-bold text-[var(--flux-heading)] mb-1">Northern Lights Chase</h4>
<p className="text-xs text-[var(--flux-black)] leading-relaxed">
4-night winter adventure with guided aurora hunting and geothermal bathing.
</p>
</div>
</div>
</Section>

<Section title="With header and footer">
<div className={`max-w-sm rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)] overflow-hidden ${cardHover}`}>
<div className="px-5 py-4 border-b border-[var(--flux-grey-100)] flex items-center justify-between">
<h4 className="text-sm font-bold text-[var(--flux-heading)]">Departure Summary</h4>
<Badge color="var(--flux-success)">Confirmed</Badge>
</div>
<div className="px-5 py-4">
<div className="space-y-2 text-sm">
<div className="flex justify-between">
<span className="text-[var(--flux-grey-300)]">Package</span>
<span className="text-[var(--flux-black)] font-bold">Iceland Explorer</span>
</div>
<div className="flex justify-between">
<span className="text-[var(--flux-grey-300)]">Date</span>
<span className="text-[var(--flux-black)]">15 Jun 2026</span>
</div>
<div className="flex justify-between">
<span className="text-[var(--flux-grey-300)]">Guests</span>
<span className="text-[var(--flux-black)]">12 / 16</span>
</div>
<div className="flex justify-between">
<span className="text-[var(--flux-grey-300)]">Revenue</span>
<span className="text-[var(--flux-black)] font-bold">$48,600</span>
</div>
</div>
</div>
<div className="px-5 py-3 border-t border-[var(--flux-grey-100)] flex justify-end gap-2">
<button className="px-3 py-1.5 text-xs font-bold rounded text-[var(--flux-black)] hover:bg-[var(--flux-grey-50)] transition-colors">
Details
</button>
<button className="px-3 py-1.5 text-xs font-bold rounded bg-[var(--flux-primary-400)] text-white hover:opacity-90 transition-opacity">
Manage
</button>
</div>
</div>
</Section>

<Section title="Interactive (hover)">
<div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
{[
{ title: 'Bookings', value: '1,284', change: '+12%' },
{ title: 'Revenue', value: '$2.4M', change: '+8%' },
{ title: 'Departures', value: '47', change: '+3' },
].map((stat) => (
<div
key={stat.title}
className={`rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)] p-5 cursor-pointer ${cardHover}`}
>
<p className="text-xs text-[var(--flux-grey-300)] mb-1">{stat.title}</p>
<p className="text-2xl font-bold text-[var(--flux-heading)]">{stat.value}</p>
<p className="text-xs font-bold mt-1" style={{ color: 'var(--flux-success)' }}>{stat.change}</p>
</div>
))}
</div>
</Section>

<Section title="With image">
<div className={`max-w-sm rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)] overflow-hidden ${cardHover}`}>
<img
src="/images/card-example.png"
alt="Card example"
className="h-40 w-full object-cover"
/>
<div className="p-5">
<h4 className="text-sm font-bold text-[var(--flux-heading)] mb-1">Midnight Sun Cruise</h4>
<p className="text-xs text-[var(--flux-black)] leading-relaxed mb-3">
10-day coastal voyage along the Norwegian fjords under the midnight sun.
</p>
<div className="flex items-center justify-between">
<span className="text-sm font-bold text-[var(--flux-heading)]">From $3,200</span>
<Badge color="var(--flux-primary-400)">New</Badge>
</div>
</div>
</div>
</Section>

<Section title="Muted / disabled">
<div className="max-w-sm rounded border border-[var(--flux-grey-100)] bg-[var(--flux-grey-50)] p-5 opacity-60">
<h4 className="text-sm font-bold text-[var(--flux-grey-300)] mb-1">Archived Package</h4>
<p className="text-xs text-[var(--flux-grey-200)] leading-relaxed">
This package is no longer available for new bookings.
</p>
</div>
</Section>
</>
);
}                  [← Button](/components/button) [Checkbox →](/components/checkbox)
