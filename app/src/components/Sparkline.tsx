import { Area, AreaChart, ResponsiveContainer, XAxis, YAxis } from 'recharts'

export default function Sparkline({ data }: { data: { i: number; c: number; fill: number | null }[] }) {
  return (
    <ResponsiveContainer width="100%" height="100%">
      <AreaChart data={data} margin={{ top: 4, right: 2, bottom: 0, left: 2 }}>
        <defs>
          <linearGradient id="fillGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="rgb(var(--brand-primary))" stopOpacity={0.5} />
            <stop offset="100%" stopColor="rgb(var(--brand-primary))" stopOpacity={0} />
          </linearGradient>
        </defs>
        <XAxis dataKey="i" hide />
        <YAxis hide domain={[0, 'dataMax']} />
        <Area type="monotone" dataKey="c" stroke="rgb(var(--text-faint))" strokeWidth={1} fill="none" isAnimationActive={false} dot={false} />
        <Area type="monotone" dataKey="fill" stroke="rgb(var(--brand-primary))" strokeWidth={2} fill="url(#fillGrad)" isAnimationActive={false} dot={false} connectNulls={false} />
      </AreaChart>
    </ResponsiveContainer>
  )
}
