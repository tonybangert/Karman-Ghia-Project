import { useState } from 'react'
import { ArchiveProvider } from '@/lib/useArchive'
import { DocViewerProvider } from '@/components/DocViewer'
import { Nav } from '@/components/Nav'
import { ProvenanceFooter } from '@/components/Footer'
import { AboutModal } from '@/components/AboutModal'
import { Hero } from '@/views/Hero'
import { CarExplorer } from '@/views/CarExplorer'
import { Timeline } from '@/views/Timeline'
import { Ledger } from '@/views/Ledger'
import { Vendors } from '@/views/Vendors'
import { Gallery } from '@/views/Gallery'
import { Mysteries } from '@/views/Mysteries'

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
          <Ledger />
          <Vendors />
          <Gallery />
          <Mysteries />
        </main>
        <ProvenanceFooter onAbout={() => setAbout(true)} />
        <AboutModal open={about} onClose={() => setAbout(false)} />
      </DocViewerProvider>
    </ArchiveProvider>
  )
}
