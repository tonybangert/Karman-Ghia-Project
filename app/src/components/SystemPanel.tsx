import { useMemo } from 'react'
import type { SystemId } from '@/types/archive'
import { paidAmount } from '@/types/archive'
import { useArchive } from '@/lib/useArchive'
import { money } from '@/lib/format'
import { DocChip } from './DocChip'
import { SpecCardView } from './SpecCardView'
import { Price, IdMono, AttributionFlag, EmptyState } from './primitives'
import { cx } from '@/lib/cx'

export function SystemPanel({ systemId }: { systemId: SystemId }) {
  const a = useArchive()
  const system = a.systemById.get(systemId)!
  const cards = a.cardsForSystem(systemId)
  const parts = useMemo(() => a.partsBySystem(systemId).slice().sort((x, y) => paidAmount(y) - paidAmount(x)), [a, systemId])
  const spend = parts.reduce((s, e) => s + paidAmount(e), 0)
  const srcDocs = useMemo(() => {
    const set = new Set<string>()
    cards.forEach(({ card }) => (card.sources ?? []).forEach((d) => set.add(d)))
    parts.forEach((e) => set.add(e.doc_id))
    return [...set].sort()
  }, [cards, parts])

  return (
    <div>
      <div className="flex items-baseline justify-between gap-3">
        <div>
          <div className="mono text-xs text-brand-primary">{system.system_id}</div>
          <h3 className="font-display text-2xl font-extrabold">{system.name}</h3>
        </div>
        <div className="text-right">
          <div className="mono text-xl text-ink">{money(spend)}</div>
          <div className="text-xs text-ink-muted">{parts.length} {parts.length === 1 ? 'entry' : 'entries'}</div>
        </div>
      </div>

      <div className="mt-4 space-y-3">
        {cards.length > 0
          ? cards.map(({ key, card }) => <SpecCardView key={key} areaKey={key} card={card} />)
          : <EmptyState>No build spec card for this system. Its parts are documented in the ledger below.</EmptyState>}
      </div>

      <div className="mt-5">
        <div className="mono mb-2 text-xs uppercase tracking-wide text-ink-faint">Ledger ({parts.length})</div>
        {parts.length === 0 ? (
          <EmptyState>No priced ledger lines yet. This system is documented through build notes and literature.</EmptyState>
        ) : (
          <ul className="divide-y divide-line/60">
            {parts.map((e) => {
              const vendor = a.vendorById.get(e.vendor_id)
              const service = e.entry_id.startsWith('S')
              return (
                <li key={e.entry_id} className="py-2.5">
                  <div className="flex items-baseline justify-between gap-3">
                    <div className="min-w-0">
                      <span className={cx('mono text-[11px]', service ? 'text-brand-secondary' : 'text-ink-faint')}>{e.entry_id}</span>{' '}
                      <span className="text-sm text-ink/90">{e.item_name}</span>
                      {service && <span className="ml-2 rounded-[3px] border border-brand-secondary/40 px-1 py-0.5 align-middle font-mono text-[9px] uppercase text-brand-secondary">service</span>}
                    </div>
                    <Price ext={e.ext_price} className="shrink-0 text-sm" />
                  </div>
                  <div className="mt-1 flex flex-wrap items-center gap-x-2 gap-y-1 text-xs text-ink-muted">
                    {e.vendor_sku && <IdMono>{e.vendor_sku}</IdMono>}
                    {vendor && <span>{vendor.name}</span>}
                    <DocChip id={e.doc_id} />
                    {e.attribution && <AttributionFlag reason={e.attribution} />}
                  </div>
                  {e.notes && <p className="mt-1 text-xs leading-relaxed text-ink-muted/90">{e.notes}</p>}
                </li>
              )
            })}
          </ul>
        )}
      </div>

      {srcDocs.length > 0 && (
        <div className="mt-5 flex flex-wrap items-center gap-1.5 border-t border-line/60 pt-4">
          <span className="mono text-[11px] uppercase tracking-wide text-ink-faint">Source documents</span>
          {srcDocs.map((d) => <DocChip key={d} id={d} />)}
        </div>
      )}
    </div>
  )
}
