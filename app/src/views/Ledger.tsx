import { useMemo, useState } from 'react'
import type { LedgerEntry, SystemId } from '@/types/archive'
import { paidAmount } from '@/types/archive'
import { useArchive } from '@/lib/useArchive'
import { money, fmtDate, yearOf } from '@/lib/format'
import { SectionHeader, Price, IdMono, AttributionFlag, EmptyState } from '@/components/primitives'
import { SpendBySystemBar, SpendByVendorDonut } from '@/components/SpendCharts'
import { DocChip } from '@/components/DocChip'
import { Modal } from '@/components/Modal'
import { cx } from '@/lib/cx'

type Sort = 'date-desc' | 'date-asc' | 'price-desc' | 'price-asc'

export function Ledger() {
  const a = useArchive()
  const [q, setQ] = useState('')
  const [sys, setSys] = useState<SystemId | ''>('')
  const [ven, setVen] = useState('')
  const [year, setYear] = useState('')
  const [sort, setSort] = useState<Sort>('date-desc')
  const [activeId, setActiveId] = useState<string | null>(null)

  const years = useMemo(() => {
    const s = new Set<string>()
    a.ledger.forEach((e) => s.add(yearOf(e.date) ?? 'undated'))
    return [...s].sort()
  }, [a.ledger])

  const rows = useMemo(() => {
    const needle = q.trim().toLowerCase()
    let r = a.ledger.filter((e) => {
      if (sys && e.system_id !== sys) return false
      if (ven && e.vendor_id !== ven) return false
      if (year && (yearOf(e.date) ?? 'undated') !== year) return false
      if (needle) {
        const hay = `${e.item_name} ${e.vendor_sku ?? ''} ${e.entry_id}`.toLowerCase()
        if (!hay.includes(needle)) return false
      }
      return true
    })
    const cmp: Record<Sort, (x: LedgerEntry, y: LedgerEntry) => number> = {
      'date-desc': (x, y) => (y.date ?? '').localeCompare(x.date ?? ''),
      'date-asc': (x, y) => (x.date ?? '').localeCompare(y.date ?? ''),
      'price-desc': (x, y) => paidAmount(y) - paidAmount(x),
      'price-asc': (x, y) => paidAmount(x) - paidAmount(y),
    }
    return r.slice().sort(cmp[sort])
  }, [a.ledger, q, sys, ven, year, sort])

  const filteredSpend = rows.reduce((s, e) => s + paidAmount(e), 0)
  const active = activeId ? a.entryById.get(activeId) : null

  const selectCls = 'rounded-md border border-line bg-surface-elevated px-2.5 py-1.5 text-sm text-ink focus:border-brand-primary'

  return (
    <section id="ledger" className="scroll-mt-16 border-t border-line bg-surface-sunken/40">
      <div className="mx-auto max-w-content px-6 py-16">
        <SectionHeader kicker="Every line item" title="The parts ledger"
          lead={`All ${a.totals.entries} entries, ${a.totals.parts} parts and ${a.totals.services} services, each tied to a document and a vendor. Filter, search, and sort. Entries at no charge (kit headers, backorders, warranty work) are kept and shown honestly.`} />

        <div className="mt-8 grid gap-6 rounded-xl border border-line bg-surface-elevated p-5 lg:grid-cols-2">
          <SpendBySystemBar />
          <SpendByVendorDonut />
        </div>

        {/* Filter bar */}
        <div className="mt-8 flex flex-wrap items-center gap-2">
          <input
            value={q} onChange={(e) => setQ(e.target.value)}
            placeholder="Search item or SKU"
            className="min-w-[200px] flex-1 rounded-md border border-line bg-surface-elevated px-3 py-1.5 text-sm placeholder:text-ink-faint focus:border-brand-primary"
            aria-label="Search items and SKUs"
          />
          <select className={selectCls} value={sys} onChange={(e) => setSys(e.target.value as SystemId | '')} aria-label="Filter by system">
            <option value="">All systems</option>
            {a.systems.map((s) => <option key={s.system_id} value={s.system_id}>{s.name}</option>)}
          </select>
          <select className={selectCls} value={ven} onChange={(e) => setVen(e.target.value)} aria-label="Filter by vendor">
            <option value="">All vendors</option>
            {a.vendors.map((v) => <option key={v.vendor_id} value={v.vendor_id}>{v.name}</option>)}
          </select>
          <select className={selectCls} value={year} onChange={(e) => setYear(e.target.value)} aria-label="Filter by year">
            <option value="">All years</option>
            {years.map((y) => <option key={y} value={y}>{y}</option>)}
          </select>
          <select className={selectCls} value={sort} onChange={(e) => setSort(e.target.value as Sort)} aria-label="Sort">
            <option value="date-desc">Newest</option>
            <option value="date-asc">Oldest</option>
            <option value="price-desc">Price high to low</option>
            <option value="price-asc">Price low to high</option>
          </select>
        </div>

        <div className="mono mt-3 flex items-center justify-between text-xs text-ink-muted">
          <span>{rows.length} of {a.totals.entries} entries</span>
          <span>filtered spend <span className="text-brand-primary">{money(filteredSpend)}</span></span>
        </div>

        {/* Table (desktop) */}
        <div className="mt-3 hidden overflow-hidden rounded-lg border border-line md:block">
          <table className="w-full text-sm">
            <thead className="bg-surface-sunken text-left text-xs uppercase tracking-wide text-ink-muted">
              <tr>
                <th className="px-3 py-2 font-medium">ID</th>
                <th className="px-3 py-2 font-medium">Item</th>
                <th className="px-3 py-2 font-medium">System</th>
                <th className="px-3 py-2 font-medium">Vendor</th>
                <th className="px-3 py-2 font-medium">Date</th>
                <th className="px-3 py-2 text-right font-medium">Ext</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((e, i) => {
                const v = a.vendorById.get(e.vendor_id)
                return (
                  <tr key={e.entry_id}
                    onClick={() => setActiveId(e.entry_id)}
                    className={cx('cursor-pointer border-t border-line/60 hover:bg-surface-elevated', i % 2 ? 'bg-surface/40' : '')}>
                    <td className="px-3 py-2"><IdMono className={e.entry_id.startsWith('S') ? 'text-brand-secondary' : ''}>{e.entry_id}</IdMono></td>
                    <td className="px-3 py-2">
                      <span className="text-ink/90">{e.item_name}</span>
                      {e.vendor_sku && <span className="ml-2"><IdMono>{e.vendor_sku}</IdMono></span>}
                      {e.attribution && <span className="ml-2 align-middle"><AttributionFlag reason={e.attribution} /></span>}
                    </td>
                    <td className="px-3 py-2 text-ink-muted">{a.systemById.get(e.system_id)?.name}</td>
                    <td className="px-3 py-2 text-ink-muted">{v?.name}</td>
                    <td className="mono px-3 py-2 text-ink-muted">{e.date ?? 'undated'}</td>
                    <td className="px-3 py-2 text-right"><Price ext={e.ext_price} /></td>
                  </tr>
                )
              })}
            </tbody>
          </table>
          {rows.length === 0 && <div className="p-6"><EmptyState>No entries match these filters.</EmptyState></div>}
        </div>

        {/* Cards (mobile) */}
        <div className="mt-3 space-y-2 md:hidden">
          {rows.map((e) => {
            const v = a.vendorById.get(e.vendor_id)
            return (
              <button key={e.entry_id} onClick={() => setActiveId(e.entry_id)} className="card block w-full p-3 text-left">
                <div className="flex items-baseline justify-between gap-2">
                  <IdMono className={e.entry_id.startsWith('S') ? 'text-brand-secondary' : ''}>{e.entry_id}</IdMono>
                  <Price ext={e.ext_price} />
                </div>
                <div className="mt-1 text-sm text-ink/90">{e.item_name}</div>
                <div className="mono mt-1 text-xs text-ink-muted">{a.systemById.get(e.system_id)?.name} &middot; {v?.name} &middot; {e.date ?? 'undated'}</div>
              </button>
            )
          })}
          {rows.length === 0 && <EmptyState>No entries match these filters.</EmptyState>}
        </div>
      </div>

      <EntryDrawer entry={active ?? null} onClose={() => setActiveId(null)} onNavigate={setActiveId} />
    </section>
  )
}

function refsIn(text: string | null | undefined, re: RegExp, self?: string) {
  if (!text) return []
  return [...new Set(text.match(re) ?? [])].filter((x) => x !== self)
}

function EntryDrawer({ entry, onClose, onNavigate }: { entry: LedgerEntry | null; onClose: () => void; onNavigate: (id: string) => void }) {
  const a = useArchive()
  const v = entry ? a.vendorById.get(entry.vendor_id) : null
  const docRefs = refsIn(entry?.notes, /DOC-\d{3}/g)
  const entryRefs = refsIn(entry?.notes, /[PS]-\d{3}/g, entry?.entry_id)

  return (
    <Modal open={!!entry} onClose={onClose} label={entry ? entry.item_name : 'Entry'} side>
      {entry && (
        <div className="p-6 pt-12">
          <div className="flex items-center gap-2">
            <IdMono className={cx('rounded bg-surface-sunken px-2 py-1', entry.entry_id.startsWith('S') ? 'text-brand-secondary' : 'text-brand-primary')}>{entry.entry_id}</IdMono>
            {entry.entry_type && <span className="text-xs uppercase tracking-wide text-ink-muted">{entry.entry_type}</span>}
            {entry.attribution && <AttributionFlag reason={entry.attribution} />}
          </div>
          <h3 className="mt-3 text-xl font-bold">{entry.item_name}</h3>

          <dl className="mt-4 grid grid-cols-2 gap-x-4 gap-y-1 text-sm">
            {[
              ['SKU', entry.vendor_sku ?? '—'],
              ['Qty', entry.qty ?? '—'],
              ['Unit price', entry.unit_price != null ? money(entry.unit_price) : '—'],
              ['System', a.systemById.get(entry.system_id)?.name],
              ['Date', fmtDate(entry.date)],
            ].map(([k, val]) => (
              <div key={k as string} className="flex justify-between gap-2 border-b border-line/60 py-1">
                <dt className="text-ink-muted">{k}</dt><dd className="mono text-ink">{val as string}</dd>
              </div>
            ))}
            <div className="col-span-2 flex justify-between gap-2 border-b border-line/60 py-1">
              <dt className="text-ink-muted">Extended (paid)</dt><dd><Price ext={entry.ext_price} /></dd>
            </div>
          </dl>

          <div className="mt-4 space-y-3 text-sm">
            <div>
              <div className="mono text-xs uppercase tracking-wide text-ink-faint">Vendor</div>
              <div className="mt-0.5 text-ink/90">{v?.name}{v?.address && <span className="text-ink-muted"> &middot; {v.address}</span>}</div>
            </div>
            <div className="flex items-center gap-2">
              <span className="mono text-xs uppercase tracking-wide text-ink-faint">Document</span>
              <DocChip id={entry.doc_id} />
            </div>
            {entry.notes && (
              <div>
                <div className="mono text-xs uppercase tracking-wide text-ink-faint">Notes</div>
                <p className="mt-0.5 leading-relaxed text-ink/90">{entry.notes}</p>
              </div>
            )}
            {(docRefs.length > 0 || entryRefs.length > 0) && (
              <div>
                <div className="mono text-xs uppercase tracking-wide text-ink-faint">Cross references</div>
                <div className="mt-1 flex flex-wrap gap-1.5">
                  {docRefs.map((d) => <DocChip key={d} id={d} />)}
                  {entryRefs.map((id) => (
                    <button key={id} onClick={() => onNavigate(id)} className="doc-chip" title="Go to this ledger entry">{id}</button>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </Modal>
  )
}
