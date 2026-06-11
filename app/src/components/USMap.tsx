import { useState } from 'react'
import { useArchive } from '@/lib/useArchive'
import { geoForAddress } from '@/lib/geo'
import { paidAmount } from '@/types/archive'
import { money } from '@/lib/format'

// Simplified continental US outline (stylized, single path) on a 100 x 62 box.
const US =
  'M3,17 L20,12 L33,9 L40,11 L52,8 L63,9 L72,7 L86,10 L95,15 L97,20 L93,24 ' +
  'L96,30 L92,36 L84,40 L80,47 L74,50 L70,47 L64,49 L55,46 L46,49 L38,47 ' +
  'L30,42 L22,40 L15,34 L8,30 L5,24 Z'

export function USMap() {
  const a = useArchive()
  const [hover, setHover] = useState<string | null>(null)

  const points = a.vendors.map((v) => {
    const g = geoForAddress(v.address)
    if (!g) return null
    const spend = a.partsByVendor(v.vendor_id).reduce((s, e) => s + paidAmount(e), 0)
    return { v, g, spend }
  }).filter(Boolean) as { v: any; g: { x: number; y: number; place: string }; spend: number }[]

  return (
    <figure className="card overflow-hidden p-4">
      <figcaption className="mono mb-2 text-xs uppercase tracking-wide text-ink-faint">Supply geography</figcaption>
      <svg viewBox="0 0 100 62" className="w-full" role="img" aria-label="Map of vendor locations across the United States">
        <path d={US} className="fill-surface-sunken stroke-line" strokeWidth={0.4} />
        {points.map(({ v, g, spend }) => {
          const r = spend > 0 ? Math.max(1.1, Math.min(3.4, Math.sqrt(spend) / 16)) : 1
          const on = hover === v.vendor_id
          return (
            <g key={v.vendor_id} onMouseEnter={() => setHover(v.vendor_id)} onMouseLeave={() => setHover(null)}>
              <circle cx={g.x} cy={g.y} r={r + 1.5} className="fill-brand-primary/20" />
              <circle cx={g.x} cy={g.y} r={r} className="fill-brand-primary" />
              {on && (
                <g>
                  <rect x={g.x + 2} y={g.y - 5} width={Math.max(28, v.name.length * 1.05)} height={7} rx={1} className="fill-surface-elevated stroke-line" strokeWidth={0.3} />
                  <text x={g.x + 3.2} y={g.y - 1.4} className="fill-ink" style={{ fontSize: 2.4 }}>{v.name}</text>
                  <text x={g.x + 3.2} y={g.y + 1.1} className="fill-brand-primary" style={{ fontSize: 2.2 }}>{g.place} &middot; {money(spend)}</text>
                </g>
              )}
            </g>
          )
        })}
      </svg>
      <p className="mt-1 text-xs text-ink-muted">Dot size scales with documented spend. A Nevada and Utah hub, a Southern California cluster, and two mail-order sources in Illinois and Georgia.</p>
    </figure>
  )
}
