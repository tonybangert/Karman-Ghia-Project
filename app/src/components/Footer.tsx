import { useArchive } from '@/lib/useArchive'
import { money } from '@/lib/format'

export function ProvenanceFooter({ onAbout }: { onAbout: () => void }) {
  const a = useArchive()
  const t = a.totals
  return (
    <footer className="mt-24 border-t border-line bg-surface-sunken">
      <div className="mx-auto max-w-content px-6 py-12">
        <div className="flex flex-col gap-8 md:flex-row md:items-start md:justify-between">
          <div className="max-w-md">
            <div className="font-display text-lg font-extrabold">The $500 Ghia</div>
            <p className="mt-2 text-sm leading-relaxed text-ink-muted">
              A digital museum exhibit for one car. Every figure here is computed at load time from a single
              machine readable record, and every fact is one click from its source document.
            </p>
            <button onClick={onAbout} className="mt-4 rounded-md border border-line px-3 py-1.5 text-sm text-ink-muted hover:text-ink">
              About this archive
            </button>
          </div>
          <dl className="grid grid-cols-2 gap-x-10 gap-y-2 text-sm sm:grid-cols-4">
            {[
              ['Documents', t.documents], ['Ledger lines', t.entries],
              ['Vendors', t.vendors], ['Gaps tracked', t.gaps],
            ].map(([k, v]) => (
              <div key={k as string}>
                <dt className="text-ink-muted">{k}</dt>
                <dd className="mono text-lg text-ink">{v as number}</dd>
              </div>
            ))}
            <div className="col-span-2 sm:col-span-4">
              <dt className="text-ink-muted">Documented spend</dt>
              <dd className="mono text-lg text-brand-primary">{money(t.totalSpend)}</dd>
            </div>
          </dl>
        </div>
        <div className="mono mt-10 text-xs text-ink-faint">
          {a.raw.project_name} &middot; record {a.raw.schema_version} &middot; {a.raw.generated_from}
        </div>
      </div>
    </footer>
  )
}
