import { useEffect, useRef, useState } from 'react'

interface SpinManifest { frames: string[]; alt?: string }

/**
 * Tier B: drag-to-rotate turntable. Renders only if public/spin/spin.json
 * exists and lists frames. If absent, returns null so the explorer degrades
 * cleanly with no broken UI. (No spin assets ship in v1.)
 */
export function TurntableViewer() {
  const base = import.meta.env.BASE_URL
  const [manifest, setManifest] = useState<SpinManifest | null>(null)
  const [frame, setFrame] = useState(0)
  const [loaded, setLoaded] = useState(false)
  const drag = useRef<{ x: number; frame: number } | null>(null)

  useEffect(() => {
    let alive = true
    fetch(`${base}spin/spin.json`)
      .then((r) => (r.ok ? r.json() : null))
      .then((m: SpinManifest | null) => { if (alive && m?.frames?.length) setManifest(m) })
      .catch(() => {})
    return () => { alive = false }
  }, [base])

  if (!manifest) return null
  const n = manifest.frames.length

  const onMove = (clientX: number) => {
    if (!drag.current) return
    const dx = clientX - drag.current.x
    const step = Math.round(dx / 12)
    setFrame((((drag.current.frame + step) % n) + n) % n)
  }

  return (
    <div
      className="relative aspect-[3/2] w-full cursor-ew-resize select-none overflow-hidden rounded-lg border border-line bg-surface-sunken"
      onPointerDown={(e) => { drag.current = { x: e.clientX, frame }; (e.target as HTMLElement).setPointerCapture(e.pointerId) }}
      onPointerMove={(e) => onMove(e.clientX)}
      onPointerUp={() => { drag.current = null }}
      role="img" aria-label={manifest.alt ?? 'Drag to rotate the car'}
    >
      <img
        src={`${base}${manifest.frames[frame]}`} alt="" draggable={false}
        onLoad={() => setLoaded(true)}
        className="h-full w-full object-contain"
      />
      <div className="mono pointer-events-none absolute bottom-2 right-3 text-[11px] text-ink-faint">
        {loaded ? 'drag to rotate' : 'loading'} &middot; {frame + 1}/{n}
      </div>
    </div>
  )
}
