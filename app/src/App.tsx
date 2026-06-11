import { ArchiveProvider, useArchive } from '@/lib/useArchive'
import { money } from '@/lib/format'

function Smoke() {
  const a = useArchive()
  const t = a.totals
  return (
    <main className="mx-auto max-w-content px-6 py-16">
      <p className="doc-chip">scaffold OK</p>
      <h1 className="mt-4 text-4xl">The $500 Ghia</h1>
      <p className="mono mt-4 text-ink-muted">
        {t.documents} docs / {t.entries} entries / {t.vendors} vendors /{' '}
        <span className="text-brand-primary">{money(t.totalSpend)}</span> / {t.firstDate} to {t.lastDate}
      </p>
    </main>
  )
}

export default function App() {
  return (
    <ArchiveProvider>
      <Smoke />
    </ArchiveProvider>
  )
}
