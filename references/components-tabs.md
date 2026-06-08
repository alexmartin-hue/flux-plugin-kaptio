# Flux — /components/tabs

Source: https://flux.kaptio.com/components/tabs

[Flux](/)       [Components](/components) / Layout & Overlay

# Tabs
Horizontal navigation between related content panels.

### Default
OverviewItineraryPricingThis trip covers the highlights of the region with curated experiences, premium accommodations, and guided excursions throughout the journey.
### With Icons
Overview
- Itinerary
- PricingThis trip covers the highlights of the region with curated experiences, premium accommodations, and guided excursions throughout the journey.       Source  TabsDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/tabs.txt](/components/source/tabs.txt).

import React, { useState } from "react";

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

const tabs = [
{ id: "overview", label: "Overview" },
{ id: "itinerary", label: "Itinerary" },
{ id: "pricing", label: "Pricing" },
];

const tabContent: Record<string, string> = {
overview:
"This trip covers the highlights of the region with curated experiences, premium accommodations, and guided excursions throughout the journey.",
itinerary:
"Day 1: Arrival and welcome dinner. Day 2: Guided city tour and museum visit. Day 3: Coastal excursion with lunch. Day 4: Free day for exploration. Day 5: Departure.",
pricing:
"Standard package starts at $2,450 per person. Premium upgrade with private transfers and suite accommodation available at $3,200 per person.",
};

function GlobeIcon() {
return (
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<circle cx="12" cy="12" r="10" />
<path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10A15.3 15.3 0 0 1 12 2z" />
</svg>
);
}

function ListIcon() {
return (
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<line x1="8" y1="6" x2="21" y2="6" />
<line x1="8" y1="12" x2="21" y2="12" />
<line x1="8" y1="18" x2="21" y2="18" />
<line x1="3" y1="6" x2="3.01" y2="6" />
<line x1="3" y1="12" x2="3.01" y2="12" />
<line x1="3" y1="18" x2="3.01" y2="18" />
</svg>
);
}

function CurrencyIcon() {
return (
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<line x1="12" y1="1" x2="12" y2="23" />
<path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
</svg>
);
}

const tabIcons: Record<string, React.ReactNode> = {
overview: <GlobeIcon />,
itinerary: <ListIcon />,
pricing: <CurrencyIcon />,
};

function TabBar({
activeTab,
onSelect,
withIcons = false,
}: {
activeTab: string;
onSelect: (id: string) => void;
withIcons?: boolean;
}) {
return (
<div className="flex border-b border-[var(--flux-grey-100)]">
{tabs.map((tab) => {
const isActive = tab.id === activeTab;
return (
<button
key={tab.id}
onClick={() => onSelect(tab.id)}
className={`px-4 py-2.5 text-sm font-bold transition-colors flex items-center gap-1.5 ${
isActive
? "text-[var(--flux-primary-800)] border-b-2 border-[var(--flux-primary-800)]"
: "text-[var(--flux-grey-300)] hover:text-[var(--flux-black)]"
}`}
>
{withIcons && tabIcons[tab.id]}
{tab.label}
</button>
);
})}
</div>
);
}

export default function TabsDemo() {
const [activeTab, setActiveTab] = useState("overview");
const [activeIconTab, setActiveIconTab] = useState("overview");

return (
<div>
<Section title="Default">
<TabBar activeTab={activeTab} onSelect={setActiveTab} />
<div className="p-4 text-sm text-[var(--flux-black)] leading-relaxed">
{tabContent[activeTab]}
</div>
</Section>

<Section title="With Icons">
<TabBar activeTab={activeIconTab} onSelect={setActiveIconTab} withIcons />
<div className="p-4 text-sm text-[var(--flux-black)] leading-relaxed">
{tabContent[activeIconTab]}
</div>
</Section>
</div>
);
}                  [← Table](/components/table) [Textarea →](/components/textarea)
