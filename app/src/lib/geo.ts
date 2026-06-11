// Approximate placement of vendor locations on a stylized US box (x: 0 west to
// 100 east, y: 0 north to 62 south). Not a true projection; enough to show the
// supply geography: a Nevada/Utah hub, a SoCal cluster, and two far mail-order
// sources in Georgia and Illinois.
export interface Geo { x: number; y: number; place: string }

export function geoForAddress(addr: string | undefined): Geo | null {
  if (!addr) return null
  const a = addr.toLowerCase()
  if (a.includes('hurricane')) return { x: 22, y: 26, place: 'Hurricane, UT' }
  if (a.includes('boulder city')) return { x: 18.5, y: 28.5, place: 'Boulder City, NV' }
  if (a.includes('henderson')) return { x: 17.5, y: 28.2, place: 'Henderson, NV' }
  if (a.includes('las vegas')) return { x: 16.5, y: 27.6, place: 'Las Vegas, NV' }
  if (a.includes('effingham') || a.includes(' il ')) return { x: 68, y: 24, place: 'Effingham, IL' }
  if (a.includes('cleveland, ga') || a.includes(' ga ')) return { x: 78, y: 33, place: 'Cleveland, GA' }
  if (a.includes(', ca') || a.includes(' ca ')) {
    if (a.includes('ventura')) return { x: 11.5, y: 31, place: 'Ventura, CA' }
    if (a.includes('oceanside')) return { x: 13, y: 33.5, place: 'Oceanside, CA' }
    if (a.includes('santa ana')) return { x: 12.8, y: 33, place: 'Santa Ana, CA' }
    if (a.includes('carson') || a.includes('harbor city')) return { x: 12, y: 32.6, place: 'Los Angeles, CA' }
    return { x: 12.3, y: 32.6, place: 'Southern California' }
  }
  return null
}
