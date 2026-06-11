import { useEffect, useState } from 'react'
import { SECTIONS } from '@/lib/sections'
import { cx } from '@/lib/cx'

export function Nav({ onAbout }: { onAbout: () => void }) {
  const [active, setActive] = useState('overview')
  const [scrolled, setScrolled] = useState(false)

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

  return (
    <header className={cx('sticky top-0 z-40 border-b transition-colors', scrolled ? 'border-line bg-surface/85 backdrop-blur-md' : 'border-transparent bg-transparent')}>
      <nav className="mx-auto flex max-w-content items-center gap-4 px-4 py-3 sm:px-6">
        <a href="#overview" className="group flex items-center gap-2 font-display text-sm font-extrabold tracking-tight">
          <span className="grid h-6 w-6 place-items-center rounded bg-brand-primary text-[11px] font-black text-surface">$</span>
          <span className="hidden sm:inline">The $500 Ghia</span>
        </a>
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
        <button onClick={onAbout} className="ml-auto rounded-md border border-line px-3 py-1.5 text-sm text-ink-muted hover:text-ink md:ml-2">About</button>
      </nav>
    </header>
  )
}
