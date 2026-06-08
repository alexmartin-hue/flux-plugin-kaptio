# Flux — /components/textarea

Source: https://flux.kaptio.com/components/textarea

[Flux](/)       [Components](/components) / Inputs & Forms

# Textarea
Multi-line text input with optional character count.

### Default
DescriptionA brief overview of the itinerary.
### With character count
Notes0 / 500

### Error state
FeedbackThis field is required.

Source  TextareaDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/textarea.txt](/components/source/textarea.txt).

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

const labelClass = "block text-sm font-medium text-[var(--flux-black)] mb-1";
const textareaBase =
"w-full px-3 py-2 rounded border border-[var(--flux-grey-200)] bg-[var(--flux-surface)] text-sm text-[var(--flux-black)] min-h-[100px] resize-y focus:border-[var(--flux-primary-400)] focus:ring-1 focus:ring-[var(--flux-primary-300)] outline-none transition-colors";

const MAX_CHARS = 500;

export default function TextareaDemo() {
const [charCount, setCharCount] = useState(0);

return (
<div>
<Section title="Default">
<div className="max-w-md">
<label className={labelClass}>Description</label>
<textarea
className={textareaBase}
defaultValue="A brief overview of the itinerary."
/>
</div>
</Section>

<Section title="With character count">
<div className="max-w-md">
<label className={labelClass}>Notes</label>
<textarea
className={textareaBase}
maxLength={MAX_CHARS}
onChange={(e) => setCharCount(e.target.value.length)}
/>
<p className="mt-1 text-xs text-[var(--flux-black)] text-right">
{charCount} / {MAX_CHARS}
</p>
</div>
</Section>

<Section title="Error state">
<div className="max-w-md">
<label className={labelClass}>Feedback</label>
<textarea
className={`${textareaBase} !border-[var(--flux-error)] focus:!ring-[var(--flux-error)]`}
defaultValue=""
/>
<p className="mt-1 text-xs text-[var(--flux-error)]">
This field is required.
</p>
</div>
</Section>
</div>
);
}                  [← Tabs](/components/tabs) [Tooltip →](/components/tooltip)
