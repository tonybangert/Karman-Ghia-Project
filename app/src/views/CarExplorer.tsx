import { useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import type { SystemId } from '@/types/archive'
import { paidAmount } from '@/types/archive'
import { useArchive } from '@/lib/useArchive'
import { money } from '@/lib/format'
import { GhiaSilhouette } from '@/components/GhiaSilhouette'
import { TurntableViewer } from '@/components/TurntableViewer'
import { SystemPanel } from '@/components/SystemPanel'
import { SectionHeader } from '@/components/primitives'
import { cx } from '@/lib/cx'

// Hotspot anchors as % of the silhouette viewBox (1000 x 360). SYS-12 has no
// physical location, so it lives in the legend, not on the body.
const HOTSPOTS: { id: SystemId; x: number; y: number }[] = [
  { id: 'SYS-02', x: 12.0, y: 41.7 },
  { id: 'SYS-01', x: 15.0, y: 58.9 },
  { id: 'SYS-03', x: 22.2, y: 54.4 },
  { id: 'SYS-04', x: 7.8, y: 68.6 },
  { id: 'SYS-05', x: 34.5, y: 65.6 },
  { id: 'SYS-11', x: 25.0, y: 69.4 },
  { id: 'SYS-09', x: 38.5, y: 28.9 },
  { id: 'SYS-08', x: 50.0, y: 41.7 },
  { id: 'SYS-06', x: 68.8, y: 68.3 },
  { id: 'SYS-07', x: 76.2, y: 69.4 },
  { id: 'SYS-10', x: 90.5, y: 47.8 },
]

export function CarExplorer() {
  const a = useArchive()
  const [active, setActive] = useState<SystemId>('SYS-01')
  const [hover, setHover] = useState<SystemId | null>(null)
  const spendOf = (id: SystemId) => a.partsBySystem(id).reduce((s, e) => s + paidAmount(e), 0)
  const nameOf = (id: SystemId) => a.systemById.get(id)?.name ?? id

  return (
    <section id="explorer" className="scroll-mt-20 border-t border-line bg-surface-sunken/40">
      <div className="mx-auto max-w-content px-6 py-16">
        <SectionHeader
          kicker="The centerpiece"
          title="Explore the car by system"
          lead="Twelve systems, every one traceable to its parts and source documents. Hover a point on the car, or pick a system. Two systems carry build specs but no priced receipts, an honest gap the archive keeps rather than hides."
        />

        <div className="mt-10 grid gap-8 lg:grid-cols-[1.15fr_1fr]">
          {/* Left: turntable (if assets) + interactive silhouette + legend */}
          <div>
            <TurntableViewer />
            <div className="relative mt-4 hidden aspect-[1000/360] w-full rounded-lg border border-line bg-surface paper-grain md:block">
              <GhiaSilhouette className="absolute inset-0 h-full w-full text-brand-secondary/25" />
              <div className="absolute inset-0">
                {HOTSPOTS.map(({ id, x, y }) => {
                  const on = active === id || hover === id
                  return (
                    <button
                      key={id}
                      onClick={() => setActive(id)}
                      onMouseEnter={() => setHover(id)} onMouseLeave={() => setHover(null)}
                      onFocus={() => setHover(id)} onBlur={() => setHover(null)}
                      className="group absolute -translate-x-1/2 -translate-y-1/2"
                      style={{ left: `${x}%`, top: `${y}%` }}
                      aria-label={`${nameOf(id)}, ${money(spendOf(id))}`}
                    >
                      <span className={cx('absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 rounded-full transition-all',
                        on ? 'h-12 w-12 bg-brand-primary/25' : 'h-7 w-7 bg-brand-primary/0 group-hover:bg-brand-primary/15')} />
                      <span className={cx('relative block h-3 w-3 rounded-full border-2 transition-all',
                        active === id ? 'border-brand-primary bg-brand-primary' : 'border-brand-primary/80 bg-surface group-hover:bg-brand-primary')} />
                    </button>
                  )
                })}
                <AnimatePresence>
                  {hover && (
                    <motion.div
                      initial={{ opacity: 0, y: 4 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }}
                      className="mono pointer-events-none absolute left-1/2 top-3 -translate-x-1/2 whitespace-nowrap rounded-md border border-line bg-surface-elevated px-2.5 py-1 text-xs text-ink shadow-card"
                    >
                      {a.systemById.get(hover)?.system_id} &middot; {nameOf(hover)} &middot; <span className="text-brand-primary">{money(spendOf(hover))}</span>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            </div>

            {/* Legend: all 12 systems, including the non-physical SYS-12 */}
            <div className="mt-4 flex flex-wrap gap-1.5">
              {a.systems.map((s) => (
                <button
                  key={s.system_id}
                  onClick={() => setActive(s.system_id)}
                  onMouseEnter={() => setHover(s.system_id)} onMouseLeave={() => setHover(null)}
                  className={cx('rounded-full border px-2.5 py-1 text-xs transition-colors',
                    active === s.system_id ? 'border-brand-primary bg-brand-primary/15 text-ink' : 'border-line text-ink-muted hover:text-ink')}
                >
                  <span className="mono text-[10px] text-ink-faint">{s.system_id.replace('SYS-', '')}</span> {s.name}
                </button>
              ))}
            </div>
          </div>

          {/* Right (desktop): live system panel */}
          <div className="hidden lg:block">
            <div className="card sticky top-20 max-h-[80vh] overflow-y-auto p-5">
              <AnimatePresence mode="wait">
                <motion.div key={active} initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }} transition={{ duration: 0.2 }}>
                  <SystemPanel systemId={active} />
                </motion.div>
              </AnimatePresence>
            </div>
          </div>
        </div>

        {/* Mobile: tappable accordion of systems */}
        <div className="mt-8 space-y-2 lg:hidden">
          {a.systems.map((s) => (
            <details key={s.system_id} className="card overflow-hidden">
              <summary className="flex cursor-pointer list-none items-center justify-between gap-3 px-4 py-3">
                <span className="text-sm font-medium"><span className="mono text-[11px] text-ink-faint">{s.system_id}</span> {s.name}</span>
                <span className="mono text-sm text-ink-muted">{money(spendOf(s.system_id))}</span>
              </summary>
              <div className="border-t border-line px-4 py-4"><SystemPanel systemId={s.system_id} /></div>
            </details>
          ))}
        </div>
      </div>
    </section>
  )
}
