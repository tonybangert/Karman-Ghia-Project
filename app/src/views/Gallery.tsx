import { useEffect, useState } from 'react'
import { useArchive } from '@/lib/useArchive'
import { SectionHeader, EmptyState, Pill } from '@/components/primitives'
import { DocChip } from '@/components/DocChip'
import { BeforeAfterSlider } from '@/components/BeforeAfterSlider'

interface Pair { id: string; caption: string; system?: string; before: string; after: string; docs?: string[] }

export function Gallery() {
  const a = useArchive()
  const base = import.meta.env.BASE_URL
  const [pairs, setPairs] = useState<Pair[] | null>(null)
  const [loaded, setLoaded] = useState(false)

  useEffect(() => {
    let alive = true
    fetch(`${base}gallery/gallery.json`)
      .then((r) => (r.ok ? r.json() : null))
      .then((m) => { if (alive) { setPairs(m?.pairs ?? []); setLoaded(true) } })
      .catch(() => { if (alive) { setPairs([]); setLoaded(true) } })
    return () => { alive = false }
  }, [base])

  return (
    <section id="gallery" className="scroll-mt-16 border-t border-line bg-surface-sunken/40">
      <div className="mx-auto max-w-content px-6 py-16">
        <SectionHeader kicker="Before and after" title="From green to silver-blue"
          lead="Drag each handle to cross the five-year gap, from the green project car stripped to primer on the trailer to the finished silver-blue coupe." />

        {!loaded ? null : !pairs || pairs.length === 0 ? (
          <div className="mt-8"><EmptyState>No gallery pairs yet. Add image pairs to public/gallery and list them in gallery.json.</EmptyState></div>
        ) : (
          <div className="mt-8 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
            {pairs.map((p) => (
              <figure key={p.id} className="card overflow-hidden">
                <BeforeAfterSlider before={`${base}${p.before}`} after={`${base}${p.after}`} />
                <figcaption className="p-4">
                  <p className="text-sm text-ink/90">{p.caption}</p>
                  <div className="mt-2 flex flex-wrap items-center gap-1.5">
                    {p.system && <Pill tone="blue">{a.systemById.get(p.system as any)?.name ?? p.system}</Pill>}
                    {p.docs?.map((d) => <DocChip key={d} id={d} />)}
                  </div>
                </figcaption>
              </figure>
            ))}
          </div>
        )}
      </div>
    </section>
  )
}
