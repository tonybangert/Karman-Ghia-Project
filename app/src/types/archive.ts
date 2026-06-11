// Types derived from the actual data/master-record.json (v11), not the brief's
// abbreviated field list. Optional fields are permissive: the JSON carries
// extras (bin_location, unit_measure, vendor websites[], status notes) and
// omits fields on some records. Never assume a field is present.

export type SystemId =
  | 'SYS-01' | 'SYS-02' | 'SYS-03' | 'SYS-04' | 'SYS-05' | 'SYS-06'
  | 'SYS-07' | 'SYS-08' | 'SYS-09' | 'SYS-10' | 'SYS-11' | 'SYS-12'

export interface SystemTaxon { system_id: SystemId; name: string }

export interface OwnershipEntry {
  owner: string
  role?: string
  addresses?: string[]
  location?: string
  period?: string
  registration?: string
  [k: string]: unknown
}

export interface VehicleMasterRecord {
  vehicle_id: string
  year_titled: number
  make: string
  model: string
  body_style: string
  vin: string | null
  chassis_number: string | null
  engine_serial?: string | null
  paint_code?: string | null
  m_codes?: unknown
  ownership_chain: OwnershipEntry[]
  acquisition_by_restorer?: { purchase_price?: number; source?: string; note?: string }
  odometer_observed?: string
  pre_restoration_condition?: string
  as_completed_photo_record?: string
  as_acquired_photo_record?: string
  [k: string]: unknown
}

export interface Vendor {
  vendor_id: string
  name: string
  address?: string
  phones?: Record<string, string>
  websites?: string[]
  email?: string
  contact?: string
  customer_number?: string
  specialty?: string
  current_status_note?: string
  resolution_note?: string
  note?: string
  documents?: string[]
  [k: string]: unknown
}

export interface ArchiveDocument {
  doc_id: string
  type: string
  vendor_id: string | null
  title: string
  date: string | null
  reference_numbers?: Record<string, string>
  line_item_count?: number
  subtotal?: number
  tax?: number
  freight?: number
  shipping?: number
  total?: number
  extraction_note?: string
  duplicate_note?: string
  photos?: Record<string, string>
  [k: string]: unknown
}

export interface LedgerEntry {
  entry_id: string           // P-### parts, S-### services
  doc_id: string
  vendor_id: string
  date: string | null
  item_name: string
  vendor_sku?: string | null
  qty?: number | null
  unit_price?: number | null
  ext_price?: number | null  // can be null OR 0.00; both mean "no paid amount"
  system_id: SystemId
  notes?: string | null
  entry_type?: string        // 'service', 'warranty_replacement', etc.
  attribution?: string       // 'uncertain'
  list_price?: number
  discount_pct?: number
  fitment_listed?: string
  bin_location?: string
  unit_measure?: string
  [k: string]: unknown
}

export interface SpecCard { card_id: string; sources?: string[]; [k: string]: unknown }

export interface TimelineEvent { date: string | null; event: string; doc_id?: string; [k: string]: unknown }

export interface DataGap {
  gap_id: string
  priority: 'high' | 'medium' | 'low'
  item: string
  status?: string
  resolution?: string
  note?: string
  [k: string]: unknown
}

export interface MasterRecord {
  schema_version: string
  project_name: string
  generated_date: string
  generated_from: string
  vehicle_master_record: VehicleMasterRecord
  systems_taxonomy: SystemTaxon[]
  vendor_registry: Vendor[]
  document_archive: ArchiveDocument[]
  parts_ledger: LedgerEntry[]
  build_spec_cards: Record<string, SpecCard>
  restoration_timeline: TimelineEvent[]
  data_gaps: DataGap[]
}

export const isService = (e: LedgerEntry) => e.entry_id.startsWith('S')
export const paidAmount = (e: LedgerEntry) => e.ext_price ?? 0
