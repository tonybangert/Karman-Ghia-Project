import { useMemo, useState } from 'react'
import type { DataGap } from '@/types/archive'
import { useArchive } from '@/lib/useArchive'
import { SectionHeader, Pill } from '@/components/primitives'
import { DocChip } from '@/components/DocChip'
import { cx } from '@/lib/cx'

type Bucket = 'open' | 'progress' | 'resolved'
const bucketOf = (g: DataGap): Bucket => {
  const s = (g.status ?? '').toUpperCase()
  if (s.startsWith('RESOLVED')) return 'resolved'
  if (s.startsWith('PARTIALLY') || s.startsWith('SUBSTANTIALLY')) return 'progress'
  return 'open'
}
const LABEL: Record<Bucket, string> = { open: 'Open', progress: 'In progress', resolved: 'Solved' }

function DocRefs({ text }: { text?: string }) {
  const ids = text ? [...new Set(text.match(/DOC-\d{3}/g) ?? [])] : []
  if (!ids.length) return null
  return <div className="mt-2 flex flex-wrap gap-1.5">{ids.map((d) => <DocChip key={d} id={d} />)}</div>
}

export function Mysteries() {
  const a = useArchive()
  const [filter, setFilter] = useState<Bucket | 'all'>('all')

  const counts = useMemo(() => {
    const c = { open: 0, progress: 0, resolved: 0 }
    a.gaps.forEach((g) => { c[bucketOf(g)]++ })
    return c
  }, [a.gaps])

  const order: Record<Bucket, number> = { open: 0, progress: 1, resolved: 2 }
  const prio: Record<string, number> = { high: 0, medium: 1, low: 2 }
  const shown = useMemo(() =>
    a.gaps
      .filter((g) => filter === 'all' || bucketOf(g) === filter)
      .slice()
      .sort((x, y) => order[bucketOf(x)] - order[bucketOf(y)] || (prio[x.priority] ?? 9) - (prio[y.priority] ?? 9))
  , [a.gaps, filter])

  return (
    <section id="mysteries" className="scroll-mt-16 border-t border-line">
      <div className="mx-auto max-w-content px-6 py-16">
        <SectionHeader kicker="What we still do not know" title="Open mysteries"
          lead="An archive is honest about its edges. These are the tracked unknowns and the ones already cracked: a machine shop named from a fax number, a purchase date pushed back a month, a paint formula chased across two counters." />

        <div className="mt-6 flex flex-wrap gap-1.5">
          {([['all', a.gaps.length], ['open', counts.open], ['progress', counts.progress], ['resolved', counts.resolved]] as const).map(([k, n]) => (
            <button key={k} onClick={() => setFilter(k as Bucket | 'all')}
              className={cx('rounded-full border px-3 py-1 text-xs transition-colors',
                filter === k ? 'border-brand-primary bg-brand-primary/15 text-ink' : 'border-line text-ink-muted hover:text-ink')}>
              {k === 'all' ? 'All' : LABEL[k as Bucket]} <span className="mono text-ink-faint">{n}</span>
            </button>
          ))}
        </div>

        <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {shown.map((g) => {
            const b = bucketOf(g)
            return (
              <article key={g.gap_id}
                className={cx('flex flex-col rounded-lg border p-4',
                  b === 'resolved' ? 'border-brand-secondary/40 bg-brand-secondary/5'
                  : b === 'progress' ? 'border-line bg-surface-elevated'
                  : 'border-dashed border-line bg-surface-elevated/60')}>
                <div className="flex items-center justify-between gap-2">
                  <span className="mono text-xs text-ink-faint">{g.gap_id}</span>
                  <div className="flex items-center gap-1.5">
                    <Pill tone={g.priority === 'high' ? 'accent' : g.priority === 'medium' ? 'blue' : 'muted'}>{g.priority}</Pill>
                    <span className={cx('rounded-full px-2 py-0.5 text-[10px] font-medium uppercase tracking-wide',
                      b === 'resolved' ? 'bg-brand-secondary/20 text-brand-secondary'
                      : b === 'progress' ? 'bg-brand-primary/15 text-brand-primary'
                      : 'bg-surface-sunken text-ink-muted')}>
                      {b === 'open' ? 'unsolved' : b === 'progress' ? 'in progress' : 'solved'}
                    </span>
                  </div>
                </div>

                <p className={cx('mt-2 text-sm leading-relaxed', b === 'open' ? 'text-ink' : 'text-ink/90')}>{g.item}</p>

                {g.resolution && (
                  <div className="mt-3 border-t border-line/60 pt-3">
                    <div className="mono text-[11px] uppercase tracking-wide text-brand-secondary">What we learned</div>
                    <p className="mt-1 text-sm leading-relaxed text-ink/90">{g.resolution}</p>
                    <DocRefs text={g.resolution} />
                  </div>
                )}
                {g.note && <p className="mt-2 text-xs leading-relaxed text-ink-muted">{g.note}</p>}
              </article>
            )
          })}
        </div>
      </div>
    </section>
  )
}
