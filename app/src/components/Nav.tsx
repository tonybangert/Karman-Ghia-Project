import { useEffect, useState } from 'react'
import { SECTIONS } from '@/lib/sections'
import { cx } from '@/lib/cx'

export function Nav({ onAbout }: { onAbout: () => void }) {
  const [active, setActive] = useState('overview')
  const [scrolled, setScrolled] = useState(false)
  const [open, setOpen] = useState(false)

  useEffect(() => {
    const io = new IntersectionObserver(
      (entries) => {
        const vis = entries.filter((e) => e.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)
        if (vis[0]) setActive(vis[0].target.id)
      },
      { rootMargin: '-45% 0px -50% 0px', threshold: [0, 0.25, 0.5] }
    )
    SECTIONS.forEach((s) => { const el = document.getElementById(s.id); if (el) io.observe(el) })
    const onScroll = () => setScrolled(window.scrollY > 24)
    onScroll(); window.addEventListener('scroll', onScroll, { passive: true })
    return () => { io.disconnect(); window.removeEventListener('scroll', onScroll) }
  }, [])

  // Close the mobile menu on Escape, and if the viewport grows to desktop.
  useEffect(() => {
    if (!open) return
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') setOpen(false) }
    const onResize = () => { if (window.innerWidth >= 768) setOpen(false) }
    window.addEventListener('keydown', onKey)
    window.addEventListener('resize', onResize)
    return () => { window.removeEventListener('keydown', onKey); window.removeEventListener('resize', onResize) }
  }, [open])

  const solid = scrolled || open

  return (
    <header className={cx('sticky top-0 z-40 border-b transition-colors', solid ? 'border-line bg-surface/85 backdrop-blur-md' : 'border-transparent bg-transparent')}>
      <nav className="mx-auto flex max-w-content items-center gap-4 px-4 py-3 sm:px-6">
        <a href="#overview" onClick={() => setOpen(false)} className="group flex items-center gap-2 font-display text-sm font-extrabold tracking-tight">
          <span className="grid h-6 w-6 place-items-center rounded bg-brand-primary text-[11px] font-black text-surface">$</span>
          <span className="hidden sm:inline">The $500 Ghia</span>
        </a>

        {/* Desktop section links */}
        <ul className="ml-auto hidden items-center gap-1 md:flex">
          {SECTIONS.map((s) => (
            <li key={s.id}>
              <a
                href={`#${s.id}`}
                className={cx('rounded-md px-3 py-1.5 text-sm transition-colors', active === s.id ? 'bg-surface-elevated text-ink' : 'text-ink-muted hover:text-ink')}
                aria-current={active === s.id ? 'true' : undefined}
              >{s.label}</a>
            </li>
          ))}
        </ul>

        {/* Desktop About */}
        <button onClick={onAbout} className="ml-2 hidden rounded-md border border-line px-3 py-1.5 text-sm text-ink-muted hover:text-ink md:inline-flex">About</button>

        {/* Mobile hamburger */}
        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          className="ml-auto grid h-9 w-9 place-items-center rounded-md border border-line text-ink-muted hover:text-ink md:hidden"
          aria-label={open ? 'Close menu' : 'Open menu'}
          aria-expanded={open}
          aria-controls="mobile-menu"
        >
          <span className="relative block h-3.5 w-5" aria-hidden>
            <span className={cx('absolute left-0 block h-0.5 w-5 bg-current transition-all duration-200', open ? 'top-1.5 rotate-45' : 'top-0')} />
            <span className={cx('absolute left-0 top-1.5 block h-0.5 w-5 bg-current transition-all duration-200', open ? 'opacity-0' : 'opacity-100')} />
            <span className={cx('absolute left-0 block h-0.5 w-5 bg-current transition-all duration-200', open ? 'top-1.5 -rotate-45' : 'top-3')} />
          </span>
        </button>
      </nav>

      {/* Mobile menu panel */}
      {open && (
        <div id="mobile-menu" className="border-t border-line bg-surface/95 backdrop-blur-md md:hidden">
          <ul className="mx-auto flex max-w-content flex-col gap-1 px-4 py-3">
            {SECTIONS.map((s) => (
              <li key={s.id}>
                <a
                  href={`#${s.id}`}
                  onClick={() => setOpen(false)}
                  className={cx('block rounded-md px-3 py-2.5 text-base transition-colors', active === s.id ? 'bg-surface-elevated text-ink' : 'text-ink-muted hover:text-ink')}
                  aria-current={active === s.id ? 'true' : undefined}
                >{s.label}</a>
              </li>
            ))}
            <li className="mt-1 border-t border-line pt-2">
              <button
                onClick={() => { setOpen(false); onAbout() }}
                className="block w-full rounded-md px-3 py-2.5 text-left text-base text-ink-muted hover:text-ink"
              >About</button>
            </li>
          </ul>
        </div>
      )}
    </header>
  )
}
