import { useRef, useState } from 'react'
import { cx } from '@/lib/cx'

function Frame({ src, badge, badgeSide }: { src: string; badge: string; badgeSide: 'left' | 'right' }) {
  const [err, setErr] = useState(false)
  return (
    <div className="absolute inset-0 h-full w-full select-none bg-surface-sunken">
      {err ? (
        <div className="grid h-full w-full place-items-center text-ink-faint"><span className="mono text-xs">image pending</span></div>
      ) : (
        <img src={src} alt="" draggable={false} onError={() => setErr(true)} className="h-full w-full object-cover" />
      )}
      <span className={cx('mono absolute top-2 rounded bg-black/55 px-1.5 py-0.5 text-[10px] uppercase tracking-wide text-white', badgeSide === 'left' ? 'left-2' : 'right-2')}>{badge}</span>
    </div>
  )
}

export function BeforeAfterSlider({ before, after }: { before: string; after: string }) {
  const [pos, setPos] = useState(50)
  const ref = useRef<HTMLDivElement>(null)
  const dragging = useRef(false)

  const setFromClientX = (clientX: number) => {
    const el = ref.current; if (!el) return
    const r = el.getBoundingClientRect()
    setPos(Math.max(0, Math.min(100, ((clientX - r.left) / r.width) * 100)))
  }

  return (
    <div
      ref={ref}
      className="relative aspect-[3/2] w-full overflow-hidden rounded-lg border border-line"
      onPointerDown={(e) => { dragging.current = true; setFromClientX(e.clientX); (e.currentTarget as HTMLElement).setPointerCapture(e.pointerId) }}
      onPointerMove={(e) => dragging.current && setFromClientX(e.clientX)}
      onPointerUp={() => { dragging.current = false }}
    >
      {/* after fills the base; before is clipped to the left of the handle */}
      <Frame src={after} badge="After" badgeSide="right" />
      <div className="absolute inset-0" style={{ clipPath: `inset(0 ${100 - pos}% 0 0)` }}>
        <Frame src={before} badge="Before" badgeSide="left" />
      </div>

      {/* handle */}
      <div className="absolute inset-y-0 z-10 -ml-px w-0.5 bg-white/80" style={{ left: `${pos}%` }} aria-hidden />
      <button
        role="slider" aria-label="Reveal before and after" aria-valuemin={0} aria-valuemax={100} aria-valuenow={Math.round(pos)}
        onKeyDown={(e) => {
          if (e.key === 'ArrowLeft') setPos((p) => Math.max(0, p - 4))
          if (e.key === 'ArrowRight') setPos((p) => Math.min(100, p + 4))
        }}
        className="absolute top-1/2 z-20 grid h-9 w-9 -translate-x-1/2 -translate-y-1/2 place-items-center rounded-full border border-line bg-surface-elevated text-ink shadow-card"
        style={{ left: `${pos}%` }}
      >
        <span aria-hidden className="text-xs">&harr;</span>
      </button>
    </div>
  )
}
