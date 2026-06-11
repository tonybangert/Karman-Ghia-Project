import { useMemo, useState } from 'react'
import { paidAmount } from '@/types/archive'
import type { Vendor } from '@/types/archive'
import { useArchive } from '@/lib/useArchive'
import { money } from '@/lib/format'
import { SectionHeader, Price, IdMono, EmptyState } from '@/components/primitives'
import { DocChip } from '@/components/DocChip'
import { USMap } from '@/components/USMap'
import { Modal } from '@/components/Modal'
import { geoForAddress } from '@/lib/geo'

export function Vendors() {
  const a = useArchive()
  const [activeId, setActiveId] = useState<string | null>(null)

  const cards = useMemo(() =>
    a.vendors.map((v) => {
      const entries = a.partsByVendor(v.vendor_id)
      const spend = entries.reduce((s, e) => s + paidAmount(e), 0)
      const docs = a.docsForVendor(v.vendor_id)
      return { v, spend, entryCount: entries.length, docCount: docs.length, geo: geoForAddress(v.address) }
    }).sort((x, y) => y.spend - x.spend)
  , [a])

  const active = activeId ? a.vendorById.get(activeId) : null

  return (
    <section id="vendors" className="scroll-mt-16 border-t border-line">
      <div className="mx-auto max-w-content px-6 py-16">
        <SectionHeader kicker="Who supplied it" title={`${a.totals.vendors} vendors`}
          lead="From Jake Raby in Georgia to a chrome shop in Henderson. Card size follows the money: a few specialists did the heavy lifting, with a long tail of counter receipts." />

        <div className="mt-8 grid gap-6 lg:grid-cols-[1fr_1.1fr]">
          <USMap />
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
            {cards.slice(0, 6).map(({ v, spend, entryCount, docCount }) => (
              <VendorCard key={v.vendor_id} v={v} spend={spend} entryCount={entryCount} docCount={docCount} onClick={() => setActiveId(v.vendor_id)} />
            ))}
          </div>
        </div>

        <div className="mt-3 grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {cards.slice(6).map(({ v, spend, entryCount, docCount }) => (
            <VendorCard key={v.vendor_id} v={v} spend={spend} entryCount={entryCount} docCount={docCount} onClick={() => setActiveId(v.vendor_id)} />
          ))}
        </div>
      </div>

      <VendorDrawer vendor={active ?? null} onClose={() => setActiveId(null)} />
    </section>
  )
}

function VendorCard({ v, spend, entryCount, docCount, onClick }: { v: Vendor; spend: number; entryCount: number; docCount: number; onClick: () => void }) {
  const geo = geoForAddress(v.address)
  return (
    <button onClick={onClick} className="card group flex h-full flex-col p-4 text-left transition-colors hover:border-brand-primary/50">
      <div className="flex items-start justify-between gap-2">
        <h3 className="font-display text-base font-bold leading-tight">{v.name}</h3>
        <IdMono className="shrink-0">{v.vendor_id}</IdMono>
      </div>
      <div className="mono mt-1 text-xs text-ink-muted">{geo?.place ?? 'location not on file'}</div>
      {v.specialty && <p className="mt-2 line-clamp-3 text-sm text-ink-muted/90">{v.specialty}</p>}
      <div className="mono mt-auto flex items-center gap-4 pt-3 text-xs text-ink-muted">
        <span className="text-brand-primary">{money(spend)}</span>
        <span>{entryCount} {entryCount === 1 ? 'line' : 'lines'}</span>
        <span>{docCount} {docCount === 1 ? 'doc' : 'docs'}</span>
      </div>
    </button>
  )
}

function VendorDrawer({ vendor, onClose }: { vendor: Vendor | null; onClose: () => void }) {
  const a = useArchive()
  const entries = vendor ? a.partsByVendor(vendor.vendor_id).slice().sort((x, y) => paidAmount(y) - paidAmount(x)) : []
  const docs = vendor ? a.docsForVendor(vendor.vendor_id) : []
  const spend = entries.reduce((s, e) => s + paidAmount(e), 0)

  return (
    <Modal open={!!vendor} onClose={onClose} label={vendor ? vendor.name : 'Vendor'} side>
      {vendor && (
        <div className="p-6 pt-12">
          <IdMono className="rounded bg-surface-sunken px-2 py-1 text-brand-primary">{vendor.vendor_id}</IdMono>
          <h3 className="mt-3 text-xl font-bold">{vendor.name}</h3>
          {vendor.address && <div className="mono mt-1 text-sm text-ink-muted">{vendor.address}</div>}

          <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1 text-sm text-ink-muted">
            {vendor.phones && Object.entries(vendor.phones).map(([k, v]) => (
              <span key={k}><span className="text-ink-faint">{k}</span> <span className="mono text-ink/90">{v}</span></span>
            ))}
          </div>
          {vendor.websites?.map((w) => <div key={w} className="mono mt-1 text-sm text-brand-secondary">{w}</div>)}

          {vendor.specialty && <p className="mt-3 text-sm leading-relaxed text-ink/90">{vendor.specialty}</p>}
          {vendor.current_status_note && <p className="mt-2 rounded-md border border-line bg-surface-sunken p-3 text-xs leading-relaxed text-ink-muted">{vendor.current_status_note}</p>}

          <div className="mono mt-4 flex items-center gap-4 border-y border-line py-3 text-sm">
            <span className="text-brand-primary">{money(spend)}</span>
            <span className="text-ink-muted">{entries.length} lines</span>
            <span className="text-ink-muted">{docs.length} documents</span>
          </div>

          {docs.length > 0 && (
            <div className="mt-4">
              <div className="mono text-xs uppercase tracking-wide text-ink-faint">Documents</div>
              <div className="mt-1.5 flex flex-wrap gap-1.5">{docs.map((d) => <DocChip key={d.doc_id} id={d.doc_id} />)}</div>
            </div>
          )}

          <div className="mt-4">
            <div className="mono text-xs uppercase tracking-wide text-ink-faint">Ledger lines</div>
            {entries.length === 0 ? (
              <div className="mt-2"><EmptyState>No priced ledger lines. This vendor is named on the build but carries no itemized receipts.</EmptyState></div>
            ) : (
              <ul className="mt-1.5 divide-y divide-line/60">
                {entries.map((e) => (
                  <li key={e.entry_id} className="flex items-baseline justify-between gap-3 py-1.5 text-sm">
                    <span className="min-w-0"><IdMono>{e.entry_id}</IdMono> <span className="text-ink/90">{e.item_name}</span></span>
                    <Price ext={e.ext_price} />
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      )}
    </Modal>
  )
}
