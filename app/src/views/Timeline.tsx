import { lazy, Suspense, useMemo, useState } from 'react'
import { motion } from 'framer-motion'
import { useArchive } from '@/lib/useArchive'
import { PHASES, phaseForDate } from '@/lib/archive'
import { fmtDate, money, moneyCompact } from '@/lib/format'
import { SectionHeader } from '@/components/primitives'
import { DocChip } from '@/components/DocChip'
import { cx } from '@/lib/cx'
const Sparkline = lazy(() => import('@/components/Sparkline'))

export function Timeline() {
  const a = useArchive()
  const [activeDate, setActiveDate] = useState<string>(a.totals.firstDate ?? '2013-06-29')

  const groups = useMemo(() => {
    const byPhase = PHASES.map((p) => ({
      phase: p,
      events: a.timeline.filter((e) => e.date && phaseForDate(e.date)?.id === p.id),
    }))
    const undated = a.timeline.filter((e) => !e.date)
    return { byPhase, undated }
  }, [a.timeline])

  const activePhaseId = phaseForDate(activeDate)?.id ?? PHASES[0].id

  // cumulative-spend sparkline data; "fill" is null past the active date
  const spark = useMemo(() => {
    return a.cumulativeSpend.map((p, i) => ({
      i, c: p.cumulative,
      fill: p.date <= activeDate ? p.cumulative : null,
    }))
  }, [a.cumulativeSpend, activeDate])
  const cumAtActive = useMemo(() => {
    let v = 0
    for (const p of a.cumulativeSpend) { if (p.date <= activeDate) v = p.cumulative; else break }
    return v
  }, [a.cumulativeSpend, activeDate])

  const phaseSpend = (startYear: number, endYear: number) =>
    a.cumulativeSpend.filter((p) => { const y = +p.date.slice(0, 4); return y >= startYear && y <= endYear })
      .reduce((s, p) => s + p.amount, 0)

  return (
    <section id="timeline" className="scroll-mt-16 border-t border-line">
      <div className="mx-auto max-w-content px-6 py-16">
        <SectionHeader kicker="2013 to 2018" title="The build, in order"
          lead="Four phases across five years, from a Las Vegas engine program to a finished car in Henderson. The line tracks documented spend as it accumulates. Undated records sort last." />
      </div>

      {/* Sticky scrubber + cumulative sparkline */}
      <div className="sticky top-14 z-30 border-y border-line bg-surface/90 backdrop-blur-md">
        <div className="mx-auto flex max-w-content flex-col gap-3 px-6 py-3 sm:flex-row sm:items-center">
          <div className="flex flex-wrap gap-1.5">
            {PHASES.map((p) => (
              <a key={p.id} href={`#phase-${p.id}`}
                className={cx('rounded-full border px-3 py-1 text-xs transition-colors',
                  activePhaseId === p.id ? 'border-brand-primary bg-brand-primary/15 text-ink' : 'border-line text-ink-muted hover:text-ink')}>
                {p.label}
              </a>
            ))}
          </div>
          <div className="flex flex-1 items-center gap-3 sm:justify-end">
            <div className="h-10 w-full max-w-[260px]">
<Suspense fallback={<div className="h-full w-full" />}><Sparkline data={spark} /></Suspense>
            </div>
            <div className="whitespace-nowrap text-right">
              <div className="mono text-sm text-brand-primary">{money(cumAtActive)}</div>
              <div className="text-[10px] uppercase tracking-wide text-ink-faint">by {fmtDate(activeDate)}</div>
            </div>
          </div>
        </div>
      </div>

      {/* Timeline rail */}
      <div className="mx-auto max-w-content px-6 py-10">
        <ol className="relative ml-3 border-l border-line">
          {groups.byPhase.map(({ phase, events }) => (
            <li key={phase.id} id={`phase-${phase.id}`} className="scroll-mt-32">
              <div className="mb-4 mt-8 flex flex-wrap items-baseline gap-x-3 gap-y-1 pl-6 first:mt-0">
                <span className="-ml-[1.65rem] grid h-3 w-3 place-items-center rounded-full bg-brand-primary ring-4 ring-surface" aria-hidden />
                <h3 className="font-display text-xl font-extrabold">{phase.label}</h3>
                <span className="mono text-xs text-ink-muted">{phase.startYear}{phase.endYear !== phase.startYear ? `–${phase.endYear}` : ''} &middot; {phase.place}</span>
                <span className="mono text-xs text-brand-primary">{moneyCompact(phaseSpend(phase.startYear, phase.endYear))}</span>
              </div>
              <div className="space-y-3 pb-2">
                {events.map((e, idx) => (
                  <motion.article
                    key={`${phase.id}-${idx}`}
                    className="relative ml-6 card p-4"
                    initial={{ opacity: 0, y: 10 }} whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, margin: '0px 0px -55% 0px' }}
                    onViewportEnter={() => e.date && setActiveDate(e.date)}
                    transition={{ duration: 0.35 }}
                  >
                    <span className="absolute -left-[1.92rem] top-5 h-2 w-2 rounded-full bg-line ring-4 ring-surface" aria-hidden />
                    <div className="mono text-xs text-ink-muted">{fmtDate(e.date)}</div>
                    <p className="mt-1 text-sm leading-relaxed text-ink/90">{e.event}</p>
                    {e.doc_id && (
                      <div className="mt-2 flex flex-wrap gap-1.5">
                        {e.doc_id.split(',').map((d) => d.trim()).filter(Boolean).map((d) => <DocChip key={d} id={d} />)}
                      </div>
                    )}
                  </motion.article>
                ))}
              </div>
            </li>
          ))}

          {groups.undated.length > 0 && (
            <li className="scroll-mt-32">
              <div className="mb-4 mt-8 flex items-baseline gap-3 pl-6">
                <span className="-ml-[1.65rem] grid h-3 w-3 place-items-center rounded-full bg-ink-faint ring-4 ring-surface" aria-hidden />
                <h3 className="font-display text-xl font-extrabold text-ink-muted">Undated</h3>
                <span className="mono text-xs text-ink-faint">records without a date on the document</span>
              </div>
              <div className="space-y-3 pb-2">
                {groups.undated.map((e, idx) => (
                  <article key={idx} className="relative ml-6 card border-dashed p-4">
                    <span className="absolute -left-[1.92rem] top-5 h-2 w-2 rounded-full bg-ink-faint ring-4 ring-surface" aria-hidden />
                    <div className="mono text-xs text-ink-faint">undated</div>
                    <p className="mt-1 text-sm leading-relaxed text-ink/90">{e.event}</p>
                    {e.doc_id && <div className="mt-2 flex flex-wrap gap-1.5">{e.doc_id.split(',').map((d) => d.trim()).map((d) => <DocChip key={d} id={d} />)}</div>}
                  </article>
                ))}
              </div>
            </li>
          )}
        </ol>
      </div>
    </section>
  )
}
