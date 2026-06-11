// Theme-aligned categorical colors. Built from the brand CSS variables so they
// follow the token palette; cycles primary and secondary across opacity steps.
export function palette(n: number): string[] {
  const bases = ['--brand-primary', '--brand-secondary']
  const ops = [1, 0.78, 0.58, 0.42, 0.3]
  const out: string[] = []
  for (let i = 0; i < n; i++) {
    const base = bases[i % bases.length]
    const op = ops[Math.floor(i / bases.length) % ops.length]
    out.push(`rgb(var(${base}) / ${op})`)
  }
  return out
}
