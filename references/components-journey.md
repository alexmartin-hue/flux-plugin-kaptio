# Flux — /components/journey

Source: https://flux.kaptio.com/components/journey

[Flux](/)       [Components](/components) / Data Display

# Journey
Horizontal step-by-step flow for processes, onboarding, and architecture diagrams.

### Timeline
Operator Side

Quest Home

Lightning App

- Lead Capture

Salesforce Lead

- Convert

Quest Canvas + API

- Configure

Quest App

### Timeline
Guest Side

Browse

Web / App

- Search

Quest API

- Customise

Package Builder

- Confirm

Checkout

### Cards
Operator Journey

Entry PointQuest Home

Lightning App

The operator's command centre inside Salesforce. Quest Home surfaces active leads, recent searches, and pipeline health in a single dashboard — removing the need to navigate between tabs.

- CaptureLead Capture

Salesforce Lead

Every travel enquiry begins as a Salesforce Lead. This step captures traveller details, preferences, and source attribution — ensuring nothing falls through the cracks.

- BuildConvert

Quest Canvas + API

Quest Canvas transforms a lead into a bookable itinerary. Operators search live availability, drag-and-drop components, and see real-time pricing — all within a visual builder.

- FinaliseConfigure

Quest App

The final step before booking. Operators review the complete package, apply pricing adjustments, add optional services, and confirm the reservation with a single action.

TrackMonitor

Operations Dashboard

Active bookings are monitored through the operations dashboard. Operators track supplier confirmations, amendment requests, and upcoming departures.

- BookConfirm

Booking Engine

The booking is confirmed and payment is processed. The system generates all required documents and triggers downstream fulfilment workflows.

### Bidirectional
Steps connected both ways — showing how the first and last steps feed back into each other.

Iterative Flow

Entry PointQuest Home

Lightning App

The operator's command centre inside Salesforce. Quest Home surfaces active leads, recent searches, and pipeline health in a single dashboard — removing the need to navigate between tabs.

- CaptureLead Capture

Salesforce Lead

Every travel enquiry begins as a Salesforce Lead. This step captures traveller details, preferences, and source attribution — ensuring nothing falls through the cracks.

- BuildConvert

Quest Canvas + API

Quest Canvas transforms a lead into a bookable itinerary. Operators search live availability, drag-and-drop components, and see real-time pricing — all within a visual builder.

- FinaliseConfigure

Quest App

The final step before booking. Operators review the complete package, apply pricing adjustments, add optional services, and confirm the reservation with a single action.

Source  JourneyDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/journey.txt](/components/source/journey.txt).

import { useState } from 'react';

function Section({ title, children }: { title: string; children: React.ReactNode }) {
return (
<div className="mb-8">
<h3 className="text-sm font-bold text-[var(--flux-heading)] mb-3">{title}</h3>
{children}
</div>
);
}

interface JourneyStep {
icon: React.ReactNode;
iconBg: string;
title: string;
subtitle: string;
details: {
heading: string;
body: string;
bullets?: string[];
};
}

const ArrowIcon = () => (
<svg width="32" height="16" viewBox="0 0 32 16" fill="none" className="flex-shrink-0 text-[var(--flux-grey-200)]">
<line x1="0" y1="8" x2="22" y2="8" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" />
<path d="M20 3l7 5-7 5" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round" />
</svg>
);

function StepCard({
step,
onClick,
}: {
step: JourneyStep;
onClick: () => void;
}) {
return (
<button
onClick={onClick}
className="group flex flex-col items-center text-center transition-all duration-200 cursor-pointer"
style={{ minWidth: 140 }}
>
<div
className="w-14 h-14 rounded flex items-center justify-center mb-3 transition-all duration-200 group-hover:scale-110 group-hover:shadow-lg"
style={{ backgroundColor: step.iconBg }}
>
{step.icon}
</div>
<p className="text-sm font-bold text-[var(--flux-heading)] mb-0.5 group-hover:text-[var(--flux-primary-400)] transition-colors">
{step.title}
</p>
<p className="text-xs text-[var(--flux-black)] font-light leading-snug">
{step.subtitle}
</p>
</button>
);
}

function DetailModal({
step,
onClose,
}: {
step: JourneyStep;
onClose: () => void;
}) {
return (
<div
className="fixed inset-0 z-50 flex items-center justify-center"
onClick={onClose}
>
<div className="absolute inset-0 bg-black/40 backdrop-blur-sm" />
<div
className="relative bg-[var(--flux-surface)] rounded shadow-xl max-w-md w-full mx-4 overflow-hidden"
onClick={(e) => e.stopPropagation()}
>
<div className="flex items-center gap-3 p-5 border-b border-[var(--flux-grey-100)]">
<div
className="w-10 h-10 rounded flex items-center justify-center flex-shrink-0"
style={{ backgroundColor: step.iconBg }}
>
{step.icon}
</div>
<div className="flex-1 min-w-0">
<h3 className="text-base font-bold text-[var(--flux-heading)]">{step.title}</h3>
<p className="text-xs text-[var(--flux-black)] font-light">{step.subtitle}</p>
</div>
<button
onClick={onClose}
className="w-8 h-8 flex items-center justify-center rounded text-[var(--flux-black)] hover:bg-[var(--flux-grey-50)] transition-colors"
>
<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
<path d="M1 1l12 12M13 1L1 13" />
</svg>
</button>
</div>
<div className="p-5">
<h4 className="text-sm font-bold text-[var(--flux-heading)] mb-2">{step.details.heading}</h4>
<p className="text-sm text-[var(--flux-black)] leading-relaxed mb-3">{step.details.body}</p>
{step.details.bullets && (
<ul className="space-y-1.5 list-disc pl-5 text-sm text-[var(--flux-black)]">
{step.details.bullets.map((b, i) => (
<li key={i}>{b}</li>
))}
</ul>
)}
</div>
</div>
</div>
);
}

const HomeIcon = () => (
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<path d="M3 12l9-8 9 8" />
<path d="M5 10v9a1 1 0 001 1h3v-5h6v5h3a1 1 0 001-1v-9" />
</svg>
);

const CaptureIcon = () => (
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<rect x="4" y="4" width="16" height="16" rx="2" />
<path d="M8 8h8M8 12h8M8 16h4" />
</svg>
);

const ConvertIcon = () => (
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
</svg>
);

const ConfigureIcon = () => (
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<circle cx="12" cy="12" r="3" />
<path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" />
</svg>
);

const operatorSteps: JourneyStep[] = [
{
icon: <HomeIcon />,
iconBg: '#056F82',
title: 'Quest Home',
subtitle: 'Lightning App',
details: {
heading: 'Entry point',
body: 'The Quest Home page is the operator\'s starting point inside Salesforce. It provides a dashboard overview of active leads, recent searches, and quick-access shortcuts.',
bullets: [
'Salesforce Lightning App',
'Dashboard with active pipeline',
'Quick search and recent activity',
],
},
},
{
icon: <CaptureIcon />,
iconBg: '#4285FF',
title: 'Lead Capture',
subtitle: 'Salesforce Lead',
details: {
heading: 'Capture enquiry',
body: 'Incoming travel enquiries are captured as Salesforce Leads. This step gathers traveller details, preferences, and initial requirements.',
bullets: [
'Standard Salesforce Lead object',
'Traveller preferences and requirements',
'Source tracking and attribution',
],
},
},
{
icon: <ConvertIcon />,
iconBg: '#FFBC42',
title: 'Convert',
subtitle: 'Quest Canvas + API',
details: {
heading: 'Build the itinerary',
body: 'The lead is converted into a bookable trip using Quest Canvas. Operators search availability, configure packages, and build a complete itinerary with real-time pricing.',
bullets: [
'Quest Canvas visual builder',
'Real-time availability and pricing via API',
'Multi-day itinerary configuration',
'Dynamic package assembly',
],
},
},
{
icon: <ConfigureIcon />,
iconBg: '#DE37A4',
title: 'Configure',
subtitle: 'Quest App',
details: {
heading: 'Finalise and book',
body: 'Final configuration, pricing adjustments, and booking confirmation happen in the Quest App. The operator reviews the complete package before submitting.',
bullets: [
'Pricing review and adjustments',
'Add-ons and optional services',
'Booking confirmation and payment',
'Automated confirmation emails',
],
},
},
];

const GuestIcon = () => (
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<circle cx="12" cy="8" r="4" />
<path d="M20 21a8 8 0 00-16 0" />
</svg>
);

const SearchIcon = () => (
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<circle cx="11" cy="11" r="7" />
<path d="M21 21l-4.35-4.35" />
</svg>
);

const CartIcon = () => (
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z" />
<line x1="3" y1="6" x2="21" y2="6" />
<path d="M16 10a4 4 0 01-8 0" />
</svg>
);

const ConfirmIcon = () => (
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
<path d="M22 11.08V12a10 10 0 11-5.93-9.14" />
<polyline points="22 4 12 14.01 9 11.01" />
</svg>
);

const guestSteps: JourneyStep[] = [
{
icon: <GuestIcon />,
iconBg: '#034955',
title: 'Browse',
subtitle: 'Web / App',
details: {
heading: 'Discovery',
body: 'The guest browses available travel packages through the operator\'s website or app, powered by Quest search.',
bullets: ['Curated package listings', 'Filter by destination, date, and budget', 'Responsive web and mobile experience'],
},
},
{
icon: <SearchIcon />,
iconBg: '#056F82',
title: 'Search',
subtitle: 'Quest API',
details: {
heading: 'Find availability',
body: 'Real-time search powered by Quest API returns available packages with pricing, availability, and options.',
bullets: ['Real-time availability', 'Dynamic pricing', 'Package comparison'],
},
},
{
icon: <CartIcon />,
iconBg: '#FFBC42',
title: 'Customise',
subtitle: 'Package Builder',
details: {
heading: 'Build your trip',
body: 'The guest selects options, adds extras, and customises their trip to their preferences before checkout.',
bullets: ['Room and cabin selection', 'Optional add-ons and upgrades', 'Traveller details and preferences'],
},
},
{
icon: <ConfirmIcon />,
iconBg: '#2BA711',
title: 'Confirm',
subtitle: 'Checkout',
details: {
heading: 'Book and pay',
body: 'Secure checkout with payment processing, booking confirmation, and automated communications.',
bullets: ['Secure payment processing', 'Instant booking confirmation', 'Email and SMS notifications'],
},
},
];

function JourneyFlow({
steps,
label,
labelColor,
}: {
steps: JourneyStep[];
label: string;
labelColor: string;
}) {
const [activeStep, setActiveStep] = useState<number | null>(null);

return (
<div className="p-6 rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)]">
<p
className="text-xs font-bold tracking-widest uppercase mb-6"
style={{ color: labelColor }}
>
{label}
</p>

<div className="flex items-start justify-center gap-3 sm:gap-4 overflow-x-auto pt-2 pb-2">
{steps.map((step, i) => (
<div key={step.title} className="flex items-center gap-3 sm:gap-4">
<StepCard step={step} onClick={() => setActiveStep(i)} />
{i < steps.length - 1 && <ArrowIcon />}
</div>
))}
</div>

{activeStep !== null && (
<DetailModal
step={steps[activeStep]}
onClose={() => setActiveStep(null)}
/>
)}
</div>
);
}

interface CardStep {
icon: React.ReactNode;
iconBg: string;
title: string;
subtitle: string;
image: string;
description: string;
features: string[];
tag?: string;
}

const cardSteps: CardStep[] = [
{
icon: <HomeIcon />,
iconBg: '#056F82',
title: 'Quest Home',
subtitle: 'Lightning App',
image: '/images/hero-quest.png',
tag: 'Entry Point',
description: 'The operator\'s command centre inside Salesforce. Quest Home surfaces active leads, recent searches, and pipeline health in a single dashboard — removing the need to navigate between tabs.',
features: [
'Dashboard with pipeline overview and KPIs',
'Quick-access shortcuts to active itineraries',
'Recent search history and saved filters',
'Role-based views for agents and managers',
],
},
{
icon: <CaptureIcon />,
iconBg: '#4285FF',
title: 'Lead Capture',
subtitle: 'Salesforce Lead',
image: '/images/hero-circle.png',
tag: 'Capture',
description: 'Every travel enquiry begins as a Salesforce Lead. This step captures traveller details, preferences, and source attribution — ensuring nothing falls through the cracks.',
features: [
'Standard Salesforce Lead object integration',
'Traveller preferences and special requirements',
'Source tracking, UTM attribution, and referral data',
'Automated lead assignment and routing rules',
],
},
{
icon: <ConvertIcon />,
iconBg: '#FFBC42',
title: 'Convert',
subtitle: 'Quest Canvas + API',
image: '/images/hero-travel.png',
tag: 'Build',
description: 'Quest Canvas transforms a lead into a bookable itinerary. Operators search live availability, drag-and-drop components, and see real-time pricing — all within a visual builder.',
features: [
'Visual drag-and-drop itinerary builder',
'Real-time availability and pricing via Quest API',
'Multi-day, multi-destination configuration',
'Dynamic package assembly with optional add-ons',
],
},
{
icon: <ConfigureIcon />,
iconBg: '#034955',
title: 'Configure',
subtitle: 'Quest App',
image: '/images/card-example.png',
tag: 'Finalise',
description: 'The final step before booking. Operators review the complete package, apply pricing adjustments, add optional services, and confirm the reservation with a single action.',
features: [
'Full pricing review with margin controls',
'Add-on services and experience upgrades',
'Payment processing and deposit management',
'Automated confirmation emails and documentation',
],
},
{
icon: <ConfirmIcon />,
iconBg: '#2BA711',
title: 'Confirm',
subtitle: 'Booking Engine',
image: '/images/hero-travel.png',
tag: 'Book',
description: 'The booking is confirmed and payment is processed. The system generates all required documents and triggers downstream fulfilment workflows.',
features: [
'Secure payment capture and receipts',
'Booking reference generation',
'Supplier notifications and allocations',
'Traveller confirmation and documents',
],
},
{
icon: <SearchIcon />,
iconBg: '#056F82',
title: 'Monitor',
subtitle: 'Operations Dashboard',
image: '/images/hero-quest.png',
tag: 'Track',
description: 'Active bookings are monitored through the operations dashboard. Operators track supplier confirmations, amendment requests, and upcoming departures.',
features: [
'Real-time booking status tracking',
'Supplier confirmation management',
'Amendment and cancellation workflows',
'Departure countdown and readiness checks',
],
},
];

function JourneyCard({ step, index, onClick }: { step: CardStep; index: number; onClick: () => void }) {
return (
<button
onClick={onClick}
className="group rounded border border-[var(--flux-grey-100)] bg-[var(--flux-surface)] overflow-hidden transition-shadow duration-300 hover:shadow-lg text-left cursor-pointer w-full"
>
<div className="relative h-28 overflow-hidden">
<img
src={step.image}
alt={step.title}
className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
/>
<div className="absolute inset-0" style={{ background: 'linear-gradient(to top, rgba(3,46,54,0.7) 0%, transparent 60%)' }} />
<div className="absolute top-2 left-2">
<span
className="text-[9px] font-bold tracking-widest uppercase px-2 py-0.5 rounded text-white"
style={{ backgroundColor: step.iconBg }}
>
{step.tag || `Step ${index + 1}`}
</span>
</div>
<div className="absolute bottom-2 left-2 flex items-center gap-2">
<div
className="w-7 h-7 rounded flex items-center justify-center flex-shrink-0"
style={{ backgroundColor: step.iconBg }}
>
<span className="scale-75">{step.icon}</span>
</div>
<div>
<p className="text-xs font-bold text-white leading-tight">{step.title}</p>
<p className="text-[10px] text-white/70 font-light">{step.subtitle}</p>
</div>
</div>
</div>

<div className="p-3">
<p className="text-xs text-[var(--flux-black)] leading-relaxed" style={{ display: '-webkit-box', WebkitLineClamp: 3, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>
{step.description}
</p>
</div>
</button>
);
}

function CardDetailModal({ step, onClose }: { step: CardStep; onClose: () => void }) {
return (
<div className="fixed inset-0 z-50 flex items-center justify-center" onClick={onClose}>
<div className="absolute inset-0 bg-black/40 backdrop-blur-sm" />
<div
className="relative bg-[var(--flux-surface)] rounded shadow-xl max-w-lg w-full mx-4 overflow-hidden"
onClick={(e) => e.stopPropagation()}
>
<div className="relative h-44 overflow-hidden">
<img src={step.image} alt={step.title} className="w-full h-full object-cover" />
<div className="absolute inset-0" style={{ background: 'linear-gradient(to top, rgba(3,46,54,0.85) 0%, rgba(3,46,54,0.2) 60%)' }} />
<button
onClick={onClose}
className="absolute top-3 right-3 w-8 h-8 flex items-center justify-center rounded bg-black/30 text-white hover:bg-black/50 transition-colors"
>
<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
<path d="M1 1l12 12M13 1L1 13" />
</svg>
</button>
<div className="absolute bottom-3 left-4 flex items-center gap-3">
<div
className="w-10 h-10 rounded flex items-center justify-center flex-shrink-0"
style={{ backgroundColor: step.iconBg }}
>
{step.icon}
</div>
<div>
<p className="text-base font-bold text-white">{step.title}</p>
<p className="text-xs text-white/70 font-light">{step.subtitle}</p>
</div>
</div>
</div>
<div className="p-5">
<p className="text-sm text-[var(--flux-black)] leading-relaxed mb-4">{step.description}</p>
<ul className="space-y-2 list-disc pl-5 text-sm text-[var(--flux-black)]">
{step.features.map((f, i) => (
<li key={i}>{f}</li>
))}
</ul>
</div>
</div>
</div>
);
}

const LeftArrowIcon = () => (
<svg width="32" height="16" viewBox="0 0 32 16" fill="none" className="flex-shrink-0 text-[var(--flux-grey-200)]">
<line x1="32" y1="8" x2="10" y2="8" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" />
<path d="M12 3l-7 5 7 5" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round" />
</svg>
);

function ReturnArrow({ side }: { side: 'right' | 'left' }) {
return (
<div className={`flex ${side === 'right' ? 'justify-end pr-[92px]' : 'justify-start pl-[92px]'} py-1`}>
<svg width="32" height="40" viewBox="0 0 32 40" fill="none" className="text-[var(--flux-grey-200)]">
<path d="M16 0 C16 14 16 16 6 16 C16 16 16 18 16 32" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round" />
<path d="M12 28l4 6 4-6" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round" />
</svg>
</div>
);
}

function CardFlow({ steps, label }: { steps: CardStep[]; label: string }) {
const [activeStep, setActiveStep] = useState<number | null>(null);
const perRow = 4;
const rows: CardStep[][] = [];
for (let i = 0; i < steps.length; i += perRow) {
rows.push(steps.slice(i, i + perRow));
}

return (
<div>
<p className="text-xs font-bold tracking-widest uppercase mb-4" style={{ color: '#056F82' }}>
{label}
</p>
{rows.map((row, rowIdx) => {
const reversed = rowIdx % 2 === 1;
const displayRow = reversed ? [...row].reverse() : row;
const startIdx = rowIdx * perRow;
const hasNextRow = rowIdx < rows.length - 1;

return (
<div key={rowIdx}>
<div className={`flex items-start gap-3 pt-2 pb-2 ${reversed ? 'justify-end' : ''}`}>
{displayRow.map((step, colIdx) => {
const actualIdx = reversed
? startIdx + (row.length - 1 - colIdx)
: startIdx + colIdx;
const isLastInRow = colIdx === displayRow.length - 1;

return (
<div key={step.title} className="flex items-center gap-3 flex-shrink-0" style={{ width: 200 }}>
<div className="w-full">
<JourneyCard step={step} index={actualIdx} onClick={() => setActiveStep(actualIdx)} />
</div>
{!isLastInRow && (
<div className="flex-shrink-0">
{reversed ? <LeftArrowIcon /> : <ArrowIcon />}
</div>
)}
</div>
);
})}
</div>
{hasNextRow && (
<ReturnArrow side={reversed ? 'left' : 'right'} />
)}
</div>
);
})}
{activeStep !== null && (
<CardDetailModal step={steps[activeStep]} onClose={() => setActiveStep(null)} />
)}
</div>
);
}

const BiArrowIcon = () => (
<svg width="32" height="20" viewBox="0 0 32 20" fill="none" className="flex-shrink-0 text-[var(--flux-grey-200)]">
<line x1="6" y1="7" x2="26" y2="7" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" />
<path d="M24 3l5 4-5 4" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round" />
<line x1="26" y1="14" x2="6" y2="14" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" />
<path d="M8 10l-5 4 5 4" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round" />
</svg>
);

function BidirectionalFlow({ steps, label }: { steps: CardStep[]; label: string }) {
const [activeStep, setActiveStep] = useState<number | null>(null);
const display = steps.slice(0, 4);

return (
<div>
<p className="text-xs font-bold tracking-widest uppercase mb-4" style={{ color: '#056F82' }}>
{label}
</p>
<div className="relative pb-8">
<div className="flex items-start gap-3 pt-2 pb-2">
{display.map((step, i) => (
<div key={step.title} className="flex items-center gap-3 flex-shrink-0" style={{ width: 200 }}>
<div className="w-full">
<JourneyCard step={step} index={i} onClick={() => setActiveStep(i)} />
</div>
{i < display.length - 1 && (
<div className="flex-shrink-0">
{i === 0 || i === display.length - 2
? <BiArrowIcon />
: <ArrowIcon />
}
</div>
)}
</div>
))}
</div>

<svg
className="absolute bottom-0 left-0 w-full text-[var(--flux-grey-200)]"
height="32"
viewBox="0 0 900 32"
fill="none"
preserveAspectRatio="none"
style={{ overflow: 'visible' }}
>
<path
d="M 100 0 C 100 24, 200 30, 450 30 C 700 30, 800 24, 800 0"
stroke="currentColor"
strokeWidth="2.5"
fill="none"
strokeLinecap="round"
/>
<path d="M 96 6 L 100 0 L 106 5" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round" />
<path d="M 794 5 L 800 0 L 804 6" stroke="currentColor" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round" />
</svg>
</div>
{activeStep !== null && (
<CardDetailModal step={display[activeStep]} onClose={() => setActiveStep(null)} />
)}
</div>
);
}

export default function JourneyDemo() {
return (
<div>
<Section title="Timeline">
<JourneyFlow
steps={operatorSteps}
label="Operator Side"
labelColor="#056F82"
/>
</Section>

<Section title="Timeline">
<JourneyFlow
steps={guestSteps}
label="Guest Side"
labelColor="#056F82"
/>
</Section>

<Section title="Cards">
<CardFlow steps={cardSteps} label="Operator Journey" />
</Section>

<Section title="Bidirectional">
<p className="text-xs text-[var(--flux-black)] mb-3">
Steps connected both ways — showing how the first and last steps feed back into each other.
</p>
<BidirectionalFlow steps={cardSteps} label="Iterative Flow" />
</Section>
</div>
);
}                  [← Input](/components/input) [Modal →](/components/modal)
