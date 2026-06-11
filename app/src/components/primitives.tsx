import type { ReactNode } from 'react'
import { cx } from '@/lib/cx'
import { priceLabel } from '@/lib/format'

/** Document IDs, SKUs, gap IDs: always mono. */
export const IdMono = ({ children, className }: { children: ReactNode; className?: string }) => (
  <span className={cx('mono text-[0.9em] text-ink-muted', className)}>{children}</span>
)

/** Prices: mono, with honest "no price" styling for null/0. */
export function Price({ ext, className }: { ext: number | null | undefined; className?: string }) {
  const none = ext === null || ext === undefined || ext === 0
  return (
    <span className={cx('mono', none ? 'text-ink-faint' : 'text-ink', className)} title={none ? 'No priced amount on the source document' : undefined}>
      {priceLabel(ext)}
    </span>
  )
}

export function AttributionFlag({ reason = 'uncertain' }: { reason?: string }) {
  return (
    <span
      className="inline-flex items-center gap-1 rounded-[3px] border border-brand-primary/40 bg-brand-primary/10 px-1.5 py-0.5 font-mono text-[10px] uppercase tracking-wide text-brand-primary"
      title={`Attribution ${reason}: this entry may not belong to this car. Recorded, not hidden.`}
    >
      <span aria-hidden>?</span> attribution {reason}
    </span>
  )
}

export function Pill({ children, tone = 'muted' }: { children: ReactNode; tone?: 'muted' | 'accent' | 'blue' }) {
  const tones = {
    muted: 'border-line bg-surface-sunken text-ink-muted',
    accent: 'border-brand-primary/40 bg-brand-primary/10 text-brand-primary',
    blue: 'border-brand-secondary/40 bg-brand-secondary/10 text-brand-secondary',
  }
  return <span className={cx('inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium', tones[tone])}>{children}</span>
}

export function EmptyState({ children }: { children: ReactNode }) {
  return (
    <div className="rounded-md border border-dashed border-line/80 bg-surface-sunken/50 px-4 py-6 text-center text-sm text-ink-muted">
      {children}
    </div>
  )
}

export function SectionHeader({ kicker, title, lead, id }: { kicker: string; title: string; lead?: string; id?: string }) {
  return (
    <header id={id} className="scroll-mt-24">
      <div className="mono text-xs uppercase tracking-[0.2em] text-brand-primary">{kicker}</div>
      <h2 className="mt-2 text-3xl font-extrabold text-balance sm:text-4xl">{title}</h2>
      {lead && <p className="mt-3 max-w-2xl text-ink-muted">{lead}</p>}
    </header>
  )
}
