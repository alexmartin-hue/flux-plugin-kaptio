# Flux — /components/note

Source: https://flux.kaptio.com/components/note

[Flux](/)       [Components](/components) / Data Display

# Note
Contextual callouts for info, success, warning, and error states.

### Variants
Information

This itinerary includes a layover in Amsterdam. Allow at least 2 hours for the connection.

Booking Confirmed

Your reservation for the Northern Lights Tour has been confirmed. Check your email for details.

Visa Required

Travellers to this destination require a valid visa. Processing may take up to 15 business days.

Payment Failed

We were unable to process the payment. Please verify the card details and try again.

Source  NoteDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/note.txt](/components/source/note.txt).

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

function InfoIcon() {
return (
<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="10" cy="10" r="8" stroke="var(--flux-info)" strokeWidth="1.5" />
<path d="M10 9v4" stroke="var(--flux-info)" strokeWidth="1.5" strokeLinecap="round" />
<circle cx="10" cy="7" r="0.75" fill="var(--flux-info)" />
</svg>
);
}

function SuccessIcon() {
return (
<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="10" cy="10" r="8" stroke="var(--flux-success)" strokeWidth="1.5" />
<path d="M7 10l2 2 4-4" stroke="var(--flux-success)" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
</svg>
);
}

function WarningIcon() {
return (
<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M10 3l8 14H2L10 3z" stroke="var(--flux-warning)" strokeWidth="1.5" strokeLinejoin="round" />
<path d="M10 9v3" stroke="var(--flux-warning)" strokeWidth="1.5" strokeLinecap="round" />
<circle cx="10" cy="14.5" r="0.75" fill="var(--flux-warning)" />
</svg>
);
}

function ErrorIcon() {
return (
<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="10" cy="10" r="8" stroke="var(--flux-error)" strokeWidth="1.5" />
<path d="M7.5 7.5l5 5M12.5 7.5l-5 5" stroke="var(--flux-error)" strokeWidth="1.5" strokeLinecap="round" />
</svg>
);
}

interface NoteProps {
icon: React.ReactNode;
title: string;
description: string;
bgColor: string;
}

function Note({ icon, title, description, bgColor }: NoteProps) {
return (
<div
className="rounded p-4"
style={{ backgroundColor: bgColor }}
>
<div className="flex gap-3">
<div className="flex-shrink-0 mt-0.5">{icon}</div>
<div>
<p className="text-sm font-bold text-[var(--flux-black)]">{title}</p>
<p className="text-sm text-[var(--flux-black)] mt-1">{description}</p>
</div>
</div>
</div>
);
}

export default function NoteDemo() {
return (
<div>
<Section title="Variants">
<div className="flex flex-col gap-3">
<Note
icon={<InfoIcon />}
title="Information"
description="This itinerary includes a layover in Amsterdam. Allow at least 2 hours for the connection."
bgColor="var(--flux-primary-100)"
/>
<Note
icon={<SuccessIcon />}
title="Booking Confirmed"
description="Your reservation for the Northern Lights Tour has been confirmed. Check your email for details."
bgColor="var(--flux-green-100)"
/>
<Note
icon={<WarningIcon />}
title="Visa Required"
description="Travellers to this destination require a valid visa. Processing may take up to 15 business days."
bgColor="var(--flux-yellow-100)"
/>
<Note
icon={<ErrorIcon />}
title="Payment Failed"
description="We were unable to process the payment. Please verify the card details and try again."
bgColor="var(--flux-orange-100)"
/>
</div>
</Section>
</div>
);
}                  [← Modal](/components/modal) [Progress →](/components/progress)
