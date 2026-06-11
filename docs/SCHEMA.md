# Data Model Reference

The archive is a single JSON document (`data/master-record.json`) with seven top-level layers. This file defines each layer, its fields, and the conventions that keep the dataset consistent as it grows.

## Versioning

Each extraction batch produces a new frozen snapshot in `data/versions/` (v1, v2, ...) via an append-only script preserved in `scripts/`. The canonical file `data/master-record.json` always equals the latest version. Records are never deleted; corrections and resolutions are written onto the existing record (see Gap lifecycle below).

## Layer 1: vehicle_master_record

Identity and provenance of the car itself.

| Field | Notes |
|---|---|
| year, make, model, body_style | 1965 Volkswagen Karmann Ghia coupe (Type 14) |
| vin, chassis_number, m_codes | Open (GAP-01) until the plates are photographed |
| ownership_chain | Array; entry 0 is the restorer James O. Mahan with documented period and address chronology |
| acquisition_by_restorer | Purchase price ($500) and source document |

## Layer 2: systems_taxonomy

Twelve fixed system buckets used to classify every ledger entry.

| ID | System |
|---|---|
| SYS-01 | Engine |
| SYS-02 | Cooling |
| SYS-03 | Fuel and Carburetion |
| SYS-04 | Exhaust |
| SYS-05 | Transmission and Drivetrain |
| SYS-06 | Front Suspension and Steering |
| SYS-07 | Brakes |
| SYS-08 | Body and Paint |
| SYS-09 | Interior |
| SYS-10 | Electrical, Lighting, and Instrumentation |
| SYS-11 | Wheels and Tires |
| SYS-12 | Consumables, Hardware, and Shop Supplies |

## Layer 3: parts_ledger

One entry per line item across all documents. Parts are `P-###`, services are `S-###`.

| Field | Notes |
|---|---|
| entry_id | P-001... / S-001..., continuous across batches, never reused |
| doc_id / vendor_id | Cross-references to layers 5 and 4 |
| date | ISO date of the document |
| item_name / vendor_sku | Name normalized for readability; SKU verbatim from the document |
| qty / unit_price / ext_price | Extended price is what was actually paid; kit headers and backordered lines may carry 0.00 |
| system_id | One of SYS-01..12 |
| notes | Free text: fitment quirks, backorder linkage, reconciliation pointers |
| Optional flags | `attribution` (uncertain), `entry_type` (warranty_replacement, etc.), `list_price`, `discount_pct`, `fitment_listed` |

Conventions: small-hardware lines may be consolidated into one entry with all SKUs listed; backorders are entered at 0.00 on the original order and at the charged price on the fulfillment document, with cross-references both ways.

## Layer 4: vendor_registry

`VEN-##` entries: name, address, phones, contact person, customer number where known, specialty, and the documents they appear on.

## Layer 5: document_archive

`DOC-###` entries, one per source document (multi-page invoices are one document).

| Field | Notes |
|---|---|
| doc_id, type, vendor_id, title, date | Type examples: invoice (counter), mail order invoice, packing list, credit memo, handwritten cost ledger |
| reference_numbers | Invoice, order, tracking, customer numbers verbatim |
| totals | subtotal / tax / freight / total as printed |
| extraction_note | Anything noteworthy: cropped areas, handwriting, attribution flags, story context |
| duplicate_note | Added when a later batch re-photographs the same document; matched on invoice number, never re-entered |

Dedupe rule: the invoice or order number is the dedupe key. A better photo of a known document updates the existing record. Exception: a small shop can reuse the same printed invoice number on genuinely different transactions. NV Automotive issued two distinct invoices both numbered 125 (DOC-003, head machine work, 2013-08-13; DOC-054, bottom-end parts, 2013-06-29). When the date, total, and line items differ, treat the documents as distinct and annotate each with an invoice-number collision note rather than merging.

## Layer 6: build_spec_cards

Rolled-up specifications per area (engine, instrumentation, wheels, body_paint, interior, electrical...). Every fact cites source documents in its `sources` array. `docs/SPEC-SHEET.md` is the rendered form.

## Layer 7: restoration_timeline and data_gaps

- `restoration_timeline`: dated events with doc references, sorted ascending, undated items last.
- `data_gaps`: `GAP-##` tracked unknowns with priority. Lifecycle: open, then `status` is set to PARTIALLY RESOLVED / SUBSTANTIALLY RESOLVED / RESOLVED with a `resolution` field describing what was learned and what remains. Gaps are never deleted; resolved gaps preserve the answer.

## House rules

- No em dashes anywhere in data or docs.
- Uncertainty is recorded, not smoothed over.
- Generated docs (`TIMELINE.md`, `SPEC-SHEET.md`, `VENDORS.md`, `GAPS-AND-ACTIONS.md`) are regenerated from the JSON, never hand-edited.
