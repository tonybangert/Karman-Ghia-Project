// Money always renders in mono with a thin space grouping. A null/0 ext_price
// is an honest "no priced amount", not "$0.00 spent".
export const money = (n: number) =>
  n.toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 2 })

export const moneyCompact = (n: number) =>
  n.toLocaleString('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })

/** Distinguishes "no priced amount" (null or 0) from a real charge. */
export function priceLabel(ext: number | null | undefined): string {
  if (ext === null || ext === undefined) return 'no price'
  if (ext === 0) return '$0.00'
  return money(ext)
}

export const fmtDate = (iso: string | null) =>
  iso
    ? new Date(iso + 'T00:00:00').toLocaleDateString('en-US', {
        year: 'numeric', month: 'short', day: 'numeric',
      })
    : 'undated'

export const fmtMonthYear = (iso: string) =>
  new Date(iso + 'T00:00:00').toLocaleDateString('en-US', { year: 'numeric', month: 'short' })

export const yearOf = (iso: string | null) => (iso ? iso.slice(0, 4) : null)
