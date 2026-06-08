# Flux — /components/skeleton

Source: https://flux.kaptio.com/components/skeleton

[Flux](/)       [Components](/components) / Feedback

# Skeleton
Placeholder shapes while content loads.

### Text

### Card
Source  SkeletonDemo.tsx
The exact code behind the live demo above. Fetch it raw at
[/components/source/skeleton.txt](/components/source/skeleton.txt).

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

const shimmerStyle: React.CSSProperties = {
background:
"linear-gradient(90deg, var(--flux-grey-100) 25%, var(--flux-grey-50, #f9fafb) 50%, var(--flux-grey-100) 75%)",
backgroundSize: "200% 100%",
animation: "shimmer 1.5s infinite",
};

function Skeleton({ className }: { className: string }) {
return <div className={className} style={shimmerStyle} />;
}

export default function SkeletonDemo() {
return (
<div>
<style>{`
@keyframes shimmer {
0% { background-position: -200% 0; }
100% { background-position: 200% 0; }
}
`}</style>

<Section title="Text">
<div className="space-y-3 max-w-md">
<Skeleton className="h-3 w-full rounded" />
<Skeleton className="h-3 w-4/5 rounded" />
<Skeleton className="h-3 w-3/5 rounded" />
</div>
</Section>

<Section title="Card">
<div className="max-w-sm space-y-4">
<div className="flex items-center gap-3">
<Skeleton className="h-12 w-12 rounded-full shrink-0" />
<div className="flex-1 space-y-2">
<Skeleton className="h-3 w-3/4 rounded" />
<Skeleton className="h-3 w-1/2 rounded" />
</div>
</div>
<Skeleton className="h-32 w-full rounded" />
</div>
</Section>
</div>
);
}                  [← Select](/components/select) [Spinner →](/components/spinner)
