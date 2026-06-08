# Flux — /components/modal

Source: https://flux.kaptio.com/components/modal

[Flux](/)       [Components](/components) / Layout & Overlay

# Modal
Overlay dialogs for focused tasks and confirmations.

### Default
Open Modal       Source  ModalDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/modal.txt](/components/source/modal.txt).

import React, { useState, useCallback } from "react";

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

export default function ModalDemo() {
const [open, setOpen] = useState(false);

const handleBackdropClick = useCallback(
(e: React.MouseEvent<HTMLDivElement>) => {
if (e.target === e.currentTarget) {
setOpen(false);
}
},
[],
);

return (
<div>
<Section title="Default">
<button
onClick={() => setOpen(true)}
className="px-4 py-2 text-sm font-bold rounded bg-[var(--flux-primary-400)] text-white hover:opacity-90 transition-opacity"
>
Open Modal
</button>
</Section>

{open && (
<div
className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center"
onClick={handleBackdropClick}
>
<div className="bg-[var(--flux-surface)] rounded shadow-xl max-w-md w-full mx-4">
<div className="p-5 border-b border-[var(--flux-grey-100)] flex items-center justify-between">
<h4 className="text-base font-bold text-[var(--flux-heading)]">
Confirm Action
</h4>
<button
onClick={() => setOpen(false)}
className="text-[var(--flux-grey-300)] hover:text-[var(--flux-black)] transition-colors"
>
<svg width="20" height="20" viewBox="0 0 20 20" fill="none">
<path
d="M15 5L5 15M5 5l10 10"
stroke="currentColor"
strokeWidth="1.5"
strokeLinecap="round"
strokeLinejoin="round"
/>
</svg>
</button>
</div>

<div className="p-5">
<p className="text-sm text-[var(--flux-black)] leading-relaxed">
Are you sure you want to proceed with this action? This operation
cannot be undone and will apply changes immediately.
</p>
</div>

<div className="p-5 border-t border-[var(--flux-grey-100)] flex justify-end gap-3">
<button
onClick={() => setOpen(false)}
className="px-4 py-2 text-sm font-bold rounded text-[var(--flux-black)] hover:bg-[var(--flux-grey-100)] transition-colors"
>
Cancel
</button>
<button
onClick={() => setOpen(false)}
className="px-4 py-2 text-sm font-bold rounded bg-[var(--flux-primary-400)] text-white hover:opacity-90 transition-opacity"
>
Confirm
</button>
</div>
</div>
</div>
)}
</div>
);
}                  [← Journey](/components/journey) [Note →](/components/note)
