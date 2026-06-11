import { useEffect, useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { cx } from '@/lib/cx'

const SLIDES = [
  { src: 'hero-1.jpg', alt: 'The finished Karmann Ghia in silver-blue metallic, three-quarter front view on a desert road', caption: 'Finished: silver-blue metallic on Fuchs-style alloys' },
  { src: 'hero-2.jpg', alt: 'Rear view of the finished car: VW and Karmann Ghia scripts, chrome bumpers, LED strips, polished exhaust', caption: 'The tail: scripts, chrome, LED strips, and the polished exhaust' },
  { src: 'hero-3.jpg', alt: 'Interior: banjo steering wheel, round gauges, grey velour seats and door panels', caption: 'Inside: banjo wheel, Mid America gauges, grey velour' },
  { src: 'hero-4.jpg', alt: 'Engine bay: Type 4 engine on the Raby DTM cooling shroud with dual Weber carburetors', caption: 'Type 4 on the Raby DTM cooling system, dual Webers' },
]
const INTERVAL = 3000

export function HeroCarousel() {
  const base = import.meta.env.BASE_URL
  const [i, setI] = useState(0)
  const [paused, setPaused] = useState(false)

  const go = (n: number) => setI((n + SLIDES.length) % SLIDES.length)

  // Auto-advance every 3s; re-armed on each slide change, paused on hover/focus
  // and when the user prefers reduced motion.
  useEffect(() => {
    if (paused) return
    if (window.matchMedia?.('(prefers-reduced-motion: reduce)').matches) return
    const id = setTimeout(() => setI((p) => (p + 1) % SLIDES.length), INTERVAL)
    return () => clearTimeout(id)
  }, [i, paused])

  const slide = SLIDES[i]

  return (
    <figure className="lg:justify-self-end">
      <div
        className="group relative aspect-[3/2] w-full overflow-hidden rounded-xl border border-line shadow-card ring-1 ring-black/5"
        role="group"
        aria-roledescription="carousel"
        aria-label="Finished car photos"
        onMouseEnter={() => setPaused(true)}
        onMouseLeave={() => setPaused(false)}
        onFocusCapture={() => setPaused(true)}
        onBlurCapture={() => setPaused(false)}
      >
        <AnimatePresence initial={false}>
          <motion.img
            key={i}
            src={`${base}${slide.src}`}
            alt={slide.alt}
            className="absolute inset-0 h-full w-full object-cover"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.6, ease: 'easeInOut' }}
            draggable={false}
          />
        </AnimatePresence>

        {/* Prev / Next arrows */}
        <button
          type="button" onClick={() => go(i - 1)} aria-label="Previous photo"
          className="absolute left-2 top-1/2 z-10 grid h-9 w-9 -translate-y-1/2 place-items-center rounded-full border border-line bg-surface/70 text-ink opacity-0 backdrop-blur-sm transition-opacity hover:bg-surface focus-visible:opacity-100 group-hover:opacity-100"
        >
          <Chevron dir="left" />
        </button>
        <button
          type="button" onClick={() => go(i + 1)} aria-label="Next photo"
          className="absolute right-2 top-1/2 z-10 grid h-9 w-9 -translate-y-1/2 place-items-center rounded-full border border-line bg-surface/70 text-ink opacity-0 backdrop-blur-sm transition-opacity hover:bg-surface focus-visible:opacity-100 group-hover:opacity-100"
        >
          <Chevron dir="right" />
        </button>

        {/* Dot indicators */}
        <div className="absolute inset-x-0 bottom-2.5 z-10 flex items-center justify-center gap-1.5">
          {SLIDES.map((s, n) => (
            <button
              key={s.src} type="button" onClick={() => go(n)}
              aria-label={`Go to photo ${n + 1}`} aria-current={n === i ? 'true' : undefined}
              className={cx('h-1.5 rounded-full transition-all', n === i ? 'w-5 bg-white' : 'w-1.5 bg-white/50 hover:bg-white/80')}
            />
          ))}
        </div>
      </div>
      <figcaption className="mono mt-2 min-h-[1.25rem] text-right text-xs text-ink-faint" aria-live="polite">
        {slide.caption}
      </figcaption>
    </figure>
  )
}

function Chevron({ dir }: { dir: 'left' | 'right' }) {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      {dir === 'left' ? <polyline points="15 18 9 12 15 6" /> : <polyline points="9 18 15 12 9 6" />}
    </svg>
  )
}
