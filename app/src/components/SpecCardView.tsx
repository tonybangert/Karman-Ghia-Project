import type { SpecCard } from '@/types/archive'
import { DocChip } from './DocChip'

const TITLE = (k: string) => k.replace(/_/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase())

export function SpecCardView({ areaKey, card }: { areaKey: string; card: SpecCard }) {
  const rows = Object.entries(card).filter(([k]) => k !== 'card_id' && k !== 'sources')
  return (
    <div className="rounded-lg border border-line bg-surface-sunken/60 p-4">
      <div className="flex items-center justify-between">
        <h4 className="font-display text-sm font-bold uppercase tracking-wide text-ink">{TITLE(areaKey)}</h4>
        <span className="mono text-[11px] text-ink-faint">{card.card_id}</span>
      </div>
      <dl className="mt-3 space-y-2">
        {rows.map(([k, v]) => (
          <div key={k} className="grid grid-cols-[8.5rem_1fr] gap-3 text-sm">
            <dt className="text-ink-muted">{TITLE(k)}</dt>
            <dd className="text-ink/90">{Array.isArray(v) ? v.join(', ') : String(v)}</dd>
          </div>
        ))}
      </dl>
      {Array.isArray(card.sources) && card.sources.length > 0 && (
        <div className="mt-3 flex flex-wrap items-center gap-1.5 border-t border-line/60 pt-3">
          <span className="mono text-[11px] uppercase tracking-wide text-ink-faint">Sources</span>
          {card.sources.map((d) => <DocChip key={d} id={d} />)}
        </div>
      )}
    </div>
  )
}
