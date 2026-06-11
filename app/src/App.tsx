import { useState } from 'react'
import { ArchiveProvider } from '@/lib/useArchive'
import { DocViewerProvider } from '@/components/DocViewer'
import { Nav } from '@/components/Nav'
import { ProvenanceFooter } from '@/components/Footer'
import { AboutModal } from '@/components/AboutModal'
import { Hero } from '@/views/Hero'
import { CarExplorer } from '@/views/CarExplorer'
import { Timeline } from '@/views/Timeline'

function Placeholder({ id, title }: { id: string; title: string }) {
  return (
    <section id={id} className="mx-auto max-w-content scroll-mt-24 px-6 py-20">
      <h2 className="text-2xl font-bold text-ink-muted">{title}</h2>
      <p className="mono mt-2 text-sm text-ink-faint">In progress.</p>
    </section>
  )
}

export default function App() {
  const [about, setAbout] = useState(false)
  return (
    <ArchiveProvider>
      <DocViewerProvider>
        <Nav onAbout={() => setAbout(true)} />
        <main>
          <Hero />
          <CarExplorer />
          <Timeline />
          <Placeholder id="ledger" title="Parts Ledger" />
          <Placeholder id="vendors" title="Vendors" />
          <Placeholder id="gallery" title="Gallery" />
          <Placeholder id="mysteries" title="Open Mysteries" />
        </main>
        <ProvenanceFooter onAbout={() => setAbout(true)} />
        <AboutModal open={about} onClose={() => setAbout(false)} />
      </DocViewerProvider>
    </ArchiveProvider>
  )
}
