import { createContext, useContext, useState, useCallback, type ReactNode } from 'react'
import { useArchive } from '@/lib/useArchive'
import { Modal } from './Modal'
import { IdMono, Price, EmptyState } from './primitives'
import { fmtDate } from '@/lib/format'

const Ctx = createContext<(docId: string) => void>(() => {})
export const useDocViewer = () => useContext(Ctx)

export function DocViewerProvider({ children }: { children: ReactNode }) {
  const a = useArchive()
  const [docId, setDocId] = useState<string | null>(null)
  const open = useCallback((id: string) => setDocId(id), [])
  const doc = docId ? a.docById.get(docId) : null
  const vendor = doc?.vendor_id ? a.vendorById.get(doc.vendor_id) : null
  const lines = docId ? a.partsByDoc(docId) : []

  return (
    <Ctx.Provider value={open}>
      {children}
      <Modal open={!!doc} onClose={() => setDocId(null)} label={doc ? doc.title : 'Document'} side>
        {doc && (
          <div className="p-6 pt-12">
            <div className="flex items-center gap-2">
              <IdMono className="rounded bg-surface-sunken px-2 py-1 text-brand-primary">{doc.doc_id}</IdMono>
              <span className="text-xs uppercase tracking-wide text-ink-muted">{doc.type}</span>
            </div>
            <h3 className="mt-3 text-xl font-bold">{doc.title}</h3>
            <div className="mono mt-2 text-sm text-ink-muted">
              {fmtDate(doc.date)}{vendor && <> &middot; {vendor.name}</>}
            </div>

            {doc.reference_numbers && Object.keys(doc.reference_numbers).length > 0 && (
              <dl className="mt-4 grid grid-cols-2 gap-x-4 gap-y-1 text-sm">
                {Object.entries(doc.reference_numbers).map(([k, v]) => (
                  <div key={k} className="flex justify-between gap-2 border-b border-line/60 py-1">
                    <dt className="text-ink-muted capitalize">{k.replace(/_/g, ' ')}</dt>
                    <dd className="mono text-ink">{v}</dd>
                  </div>
                ))}
              </dl>
            )}

            {(doc.total ?? doc.subtotal) !== undefined && (
              <div className="mt-4 flex flex-wrap gap-4 rounded-md border border-line bg-surface-sunken px-4 py-3 text-sm">
                {doc.subtotal !== undefined && <span>Subtotal <Price ext={doc.subtotal} /></span>}
                {doc.tax !== undefined && <span>Tax <Price ext={doc.tax} /></span>}
                {(doc.freight ?? doc.shipping) !== undefined && <span>Freight <Price ext={(doc.freight ?? doc.shipping) as number} /></span>}
                {doc.total !== undefined && <span className="font-semibold">Total <Price ext={doc.total} className="text-ink" /></span>}
              </div>
            )}

            {doc.extraction_note && (
              <div className="mt-4">
                <div className="mono text-xs uppercase tracking-wide text-ink-muted">Extraction note</div>
                <p className="mt-1 text-sm leading-relaxed text-ink/90">{doc.extraction_note}</p>
              </div>
            )}

            {doc.photos && (
              <div className="mt-4">
                <div className="mono text-xs uppercase tracking-wide text-ink-muted">Photographic frames</div>
                <ul className="mt-1 space-y-1 text-sm text-ink/90">
                  {Object.entries(doc.photos).map(([k, v]) => (
                    <li key={k}><span className="mono text-brand-secondary">{doc.doc_id}{k}</span> {v}</li>
                  ))}
                </ul>
              </div>
            )}

            <div className="mt-5">
              <div className="mono text-xs uppercase tracking-wide text-ink-muted">
                Ledger lines on this document ({lines.length})
              </div>
              {lines.length === 0 ? (
                <div className="mt-2"><EmptyState>No priced ledger lines. This document is literature or a photographic record.</EmptyState></div>
              ) : (
                <ul className="mt-2 divide-y divide-line/60">
                  {lines.map((e) => (
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
    </Ctx.Provider>
  )
}
