import raw from '@data/master-record.json'
import type {
  MasterRecord, SystemId, SpecCard, TimelineEvent,
} from '@/types/archive'
import { paidAmount } from '@/types/archive'

const data = raw as MasterRecord

/* ---- Spec card area key -> system id (1 -> many; SYS-10 has two cards) ---- */
const CARD_TO_SYSTEM: Record<string, SystemId> = {
  engine: 'SYS-01', cooling: 'SYS-02', exhaust: 'SYS-04', transmission: 'SYS-05',
  front_suspension_steering: 'SYS-06', brakes: 'SYS-07', body_paint: 'SYS-08',
  interior: 'SYS-09', instrumentation: 'SYS-10', electrical: 'SYS-10', wheels_tires: 'SYS-11',
}

/* ---- Restoration phases (the four documented groupings, by year) ---- */
export interface Phase { id: string; label: string; place: string; startYear: number; endYear: number }
export const PHASES: Phase[] = [
  { id: 'engine', label: 'Engine Program Launch', place: 'Hurricane UT / Las Vegas NV', startYear: 2013, endYear: 2013 },
  { id: 'paint', label: 'Body & Paint', place: 'Hurricane, Utah', startYear: 2014, endYear: 2014 },
  { id: 'assembly', label: 'Assembly', place: 'Henderson, Nevada', startYear: 2015, endYear: 2016 },
  { id: 'running', label: 'Running & Maintenance', place: 'Henderson, Nevada', startYear: 2017, endYear: 2018 },
]
export const phaseForDate = (iso: string | null): Phase | null => {
  if (!iso) return null
  const y = Number(iso.slice(0, 4))
  return PHASES.find((p) => y >= p.startYear && y <= p.endYear) ?? null
}

function groupSum<T>(items: T[], key: (t: T) => string, val: (t: T) => number) {
  const m = new Map<string, { total: number; count: number }>()
  for (const it of items) {
    const k = key(it)
    const cur = m.get(k) ?? { total: 0, count: 0 }
    cur.total += val(it); cur.count += 1
    m.set(k, cur)
  }
  return m
}

function build() {
  const ledger = data.parts_ledger
  const vendorById = new Map(data.vendor_registry.map((v) => [v.vendor_id, v]))
  const docById = new Map(data.document_archive.map((d) => [d.doc_id, d]))
  const systemById = new Map(data.systems_taxonomy.map((s) => [s.system_id, s]))
  const entryById = new Map(ledger.map((e) => [e.entry_id, e]))

  const spendBySystem = groupSum(ledger, (e) => e.system_id, paidAmount)
  const spendByVendor = groupSum(ledger, (e) => e.vendor_id, paidAmount)

  const docsByVendor = new Map<string, number>()
  for (const d of data.document_archive) {
    if (d.vendor_id) docsByVendor.set(d.vendor_id, (docsByVendor.get(d.vendor_id) ?? 0) + 1)
  }

  // Spec cards grouped by system (preserve area key for labelling).
  const cardsBySystem = new Map<SystemId, { key: string; card: SpecCard }[]>()
  for (const [key, card] of Object.entries(data.build_spec_cards)) {
    const sys = CARD_TO_SYSTEM[key]
    if (!sys) continue
    const arr = cardsBySystem.get(sys) ?? []
    arr.push({ key, card }); cardsBySystem.set(sys, arr)
  }

  // Cumulative documented spend over time (dated, priced entries only).
  const datedPriced = ledger
    .filter((e) => e.date && paidAmount(e) > 0)
    .sort((a, b) => (a.date! < b.date! ? -1 : 1))
  let run = 0
  const cumulativeSpend = datedPriced.map((e) => {
    run += paidAmount(e)
    return { date: e.date as string, amount: paidAmount(e), cumulative: run }
  })

  const totalSpend = ledger.reduce((s, e) => s + paidAmount(e), 0)
  const datedAll = ledger.map((e) => e.date).filter(Boolean).sort() as string[]

  return {
    raw: data,
    vehicle: data.vehicle_master_record,
    systems: data.systems_taxonomy,
    vendors: data.vendor_registry,
    documents: data.document_archive,
    ledger,
    timeline: data.restoration_timeline as TimelineEvent[],
    gaps: data.data_gaps,
    specCards: data.build_spec_cards,
    // lookups
    vendorById, docById, systemById, entryById, cardsBySystem,
    // aggregates
    spendBySystem, spendByVendor, docsByVendor, cumulativeSpend,
    totals: {
      documents: data.document_archive.length,
      entries: ledger.length,
      parts: ledger.filter((e) => e.entry_id.startsWith('P')).length,
      services: ledger.filter((e) => e.entry_id.startsWith('S')).length,
      vendors: data.vendor_registry.length,
      timelineEvents: data.restoration_timeline.length,
      gaps: data.data_gaps.length,
      totalSpend,
      firstDate: datedAll[0] ?? null,
      lastDate: datedAll[datedAll.length - 1] ?? null,
    },
    // selectors
    partsBySystem: (id: SystemId) => ledger.filter((e) => e.system_id === id),
    partsByVendor: (id: string) => ledger.filter((e) => e.vendor_id === id),
    partsByDoc: (id: string) => ledger.filter((e) => e.doc_id === id),
    docsForVendor: (id: string) => data.document_archive.filter((d) => d.vendor_id === id),
    cardsForSystem: (id: SystemId) => cardsBySystem.get(id) ?? [],
  }
}

export type Archive = ReturnType<typeof build>
export const archive: Archive = build()
