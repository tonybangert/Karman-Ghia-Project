import { useMemo } from 'react'
import { Bar, BarChart, Cell, Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'
import { useArchive } from '@/lib/useArchive'
import { palette } from '@/lib/palette'
import { money, moneyCompact } from '@/lib/format'

function ChartTip({ active, payload }: any) {
  if (!active || !payload?.length) return null
  const p = payload[0].payload
  return (
    <div className="mono rounded-md border border-line bg-surface-elevated px-2.5 py-1.5 text-xs shadow-card">
      <div className="text-ink">{p.name}</div>
      <div className="text-brand-primary">{money(p.value)}</div>
      <div className="text-ink-faint">{p.count} entries</div>
    </div>
  )
}

export function SpendBySystemBar() {
  const a = useArchive()
  const data = useMemo(() =>
    a.systems.map((s) => {
      const g = a.spendBySystem.get(s.system_id)
      return { name: s.name, value: g?.total ?? 0, count: g?.count ?? 0 }
    }).filter((d) => d.value > 0).sort((x, y) => y.value - x.value)
  , [a])
  const colors = palette(data.length)
  return (
    <div className="min-w-0">
      <div className="mono mb-2 text-xs uppercase tracking-wide text-ink-faint">Spend by system</div>
      <div className="h-[260px] w-full min-w-0">
        <ResponsiveContainer>
          <BarChart data={data} layout="vertical" margin={{ left: 4, right: 12, top: 0, bottom: 0 }}>
            <XAxis type="number" hide />
            <YAxis type="category" dataKey="name" width={120} tick={{ fill: 'rgb(var(--text-muted))', fontSize: 11 }} axisLine={false} tickLine={false} />
            <Tooltip content={<ChartTip />} cursor={{ fill: 'rgb(var(--surface-elevated))' }} />
            <Bar dataKey="value" radius={[0, 3, 3, 0]} isAnimationActive={false}>
              {data.map((_, i) => <Cell key={i} fill={colors[i]} />)}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}

export function SpendByVendorDonut() {
  const a = useArchive()
  const data = useMemo(() => {
    const rows = a.vendors.map((v) => {
      const g = a.spendByVendor.get(v.vendor_id)
      return { name: v.name, value: g?.total ?? 0, count: g?.count ?? 0 }
    }).filter((d) => d.value > 0).sort((x, y) => y.value - x.value)
    const top = rows.slice(0, 8)
    const restTotal = rows.slice(8).reduce((s, r) => s + r.value, 0)
    const restCount = rows.slice(8).reduce((s, r) => s + r.count, 0)
    if (restTotal > 0) top.push({ name: 'Other vendors', value: restTotal, count: restCount })
    return top
  }, [a])
  const colors = palette(data.length)
  const total = data.reduce((s, d) => s + d.value, 0)
  return (
    <div className="min-w-0">
      <div className="mono mb-2 text-xs uppercase tracking-wide text-ink-faint">Spend by vendor</div>
      <div className="flex min-w-0 items-center gap-4">
        <div className="relative h-[180px] w-[180px] shrink-0">
          <ResponsiveContainer>
            <PieChart>
              <Pie data={data} dataKey="value" nameKey="name" innerRadius={52} outerRadius={84} paddingAngle={1.5} stroke="rgb(var(--surface))" strokeWidth={2} isAnimationActive={false}>
                {data.map((_, i) => <Cell key={i} fill={colors[i]} />)}
              </Pie>
              <Tooltip content={<ChartTip />} />
            </PieChart>
          </ResponsiveContainer>
          <div className="pointer-events-none absolute inset-0 grid place-items-center text-center">
            <div>
              <div className="mono text-sm text-ink">{moneyCompact(total)}</div>
              <div className="text-[10px] uppercase text-ink-faint">total</div>
            </div>
          </div>
        </div>
        <ul className="min-w-0 flex-1 space-y-1 text-xs">
          {data.map((d, i) => (
            <li key={d.name} className="flex items-center gap-2">
              <span className="h-2.5 w-2.5 shrink-0 rounded-sm" style={{ background: colors[i] }} />
              <span className="min-w-0 flex-1 truncate text-ink-muted">{d.name}</span>
              <span className="mono text-ink">{moneyCompact(d.value)}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default function SpendSummary() {
  return (
    <div className="grid gap-6 rounded-xl border border-line bg-surface-elevated p-5 lg:grid-cols-2">
      <SpendBySystemBar />
      <SpendByVendorDonut />
    </div>
  )
}
