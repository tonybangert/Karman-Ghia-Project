import { motion } from 'framer-motion'
import { useArchive } from '@/lib/useArchive'
import { useCountUp } from '@/lib/useCountUp'
import { moneyCompact } from '@/lib/format'
import { GhiaSilhouette } from '@/components/GhiaSilhouette'

function Stat({ value, label, prefix = '', display }: { value: number; label: string; prefix?: string; display?: (n: number) => string }) {
  const { n, ref } = useCountUp(value)
  return (
    <div className="rounded-lg border border-line bg-surface-elevated/70 px-5 py-4 paper-grain">
      <div className="mono text-3xl font-medium tabular-nums text-ink sm:text-4xl">
        <span ref={ref}>{prefix}{display ? display(n) : Math.round(n).toLocaleString('en-US')}</span>
      </div>
      <div className="mt-1 text-xs uppercase tracking-wide text-ink-muted">{label}</div>
    </div>
  )
}

export function Hero() {
  const a = useArchive()
  const t = a.totals
  const y0 = t.firstDate?.slice(0, 4) ?? '2013'
  const y1 = t.lastDate?.slice(0, 4) ?? '2018'

  return (
    <section id="overview" className="relative overflow-hidden scroll-mt-16">
      <div className="absolute inset-0 blueprint-grid opacity-60" aria-hidden />
      <div className="pointer-events-none absolute inset-0 flex items-center justify-end" aria-hidden>
        <GhiaSilhouette decorative className="mr-[-4%] w-[78%] text-brand-secondary/10" />
      </div>
      <div className="absolute inset-x-0 bottom-0 h-24 bg-gradient-to-t from-surface to-transparent" aria-hidden />

      <div className="relative mx-auto max-w-content px-6 pb-20 pt-16 sm:pt-24">
        <motion.div initial={{ opacity: 0, y: 14 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}>
          <div className="mono inline-flex items-center gap-2 rounded-full border border-line bg-surface-elevated/70 px-3 py-1 text-xs text-ink-muted">
            1965 Volkswagen Karmann Ghia &middot; Type 14
          </div>
          <h1 className="mt-5 max-w-3xl font-display text-5xl font-extrabold leading-[0.95] text-balance sm:text-7xl">
            The <span className="text-brand-primary">$500</span> Ghia
          </h1>
          <p className="mt-5 max-w-xl text-lg leading-relaxed text-ink/90">
            A coupe bought as a 500 dollar project, restored from {y0} to {y1}, and documented down to the
            receipt. A Type 4 engine on a Raby cooling system, dual Webers, a body taken to bare metal and back.
            This is its entire paper trail, made explorable.
          </p>
        </motion.div>

        <motion.div
          className="mt-10 grid max-w-3xl grid-cols-2 gap-3 sm:grid-cols-4"
          initial="hidden" animate="show"
          variants={{ hidden: {}, show: { transition: { staggerChildren: 0.08, delayChildren: 0.2 } } }}
        >
          {[
            <Stat key="d" value={t.documents} label="Documents" />,
            <Stat key="e" value={t.entries} label="Ledger lines" />,
            <Stat key="s" value={t.totalSpend} label="Documented spend" prefix="" display={(x) => moneyCompact(x)} />,
            <Stat key="y" value={Number(y1) - Number(y0)} label={`Years, ${y0} to ${y1}`} />,
          ].map((el, i) => (
            <motion.div key={i} variants={{ hidden: { opacity: 0, y: 12 }, show: { opacity: 1, y: 0 } }}>{el}</motion.div>
          ))}
        </motion.div>

        <a href="#explorer" className="group mt-12 inline-flex items-center gap-2 text-sm text-ink-muted transition-colors hover:text-ink">
          <span>Explore the car</span>
          <motion.span aria-hidden animate={{ y: [0, 4, 0] }} transition={{ repeat: Infinity, duration: 1.6 }}>&darr;</motion.span>
        </a>
      </div>
    </section>
  )
}
