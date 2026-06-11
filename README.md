# Karman-Ghia-Project
# 1965 VW Karmann Ghia Restoration Archive

A structured digital archive of the complete restoration of a 1965 Volkswagen Karmann Ghia coupe (Type 14), reconstructed from the prior restorer's folder of receipts, invoices, packing lists, and handwritten records. Every document has been photographed, extracted, and normalized into a single machine-readable master record, with human-readable references generated from it.

The long-term goal of this project is a bespoke application that understands every aspect of this car: what is on it, who supplied it, what it cost, when it happened, and what is still unknown.

## The car in one paragraph

Restored 2013-2018 by James O. Mahan, who bought the car as a $500 project. The drivetrain is the centerpiece: a 1,971cc Type 4 conversion (94mm x 71mm, 8.6:1 compression) running a Jake Raby DTM Stage III cooling system, dual Weber carburetors, an Engle cam, a lightened flywheel, and head work by NV Automotive (Bill Shapley) in Las Vegas, backed by a Freeway Flyer transaxle built by Steve Hansen. The chassis carries 2.5 inch drop spindles, an adjustable front beam, KYB shocks, and a front disc brake conversion. Body and paint were done in 2014 through Washington County Collision in Hurricane, Utah. The interior is the JBugs Deluxe Velour/Tweed kit with grey velour headliner, charcoal carpet, custom door panels, and grey 2-point Wolfsburg belts. Documented activity runs from June 29, 2013 (the NV Automotive engine bottom-end parts) to May 31, 2018 (Weber rebuild kits).

## Repository layout

```
Karman-Ghia-Project/
├── README.md                  <- you are here
├── data/
│   ├── master-record.json     <- THE canonical dataset (always current)
│   └── versions/              <- frozen snapshots, v1 through v7, one per extraction batch
├── docs/
│   ├── SCHEMA.md              <- the seven-layer data model, conventions, and ID scheme
│   ├── TIMELINE.md            <- generated narrative and event log, 2013-2018
│   ├── SPEC-SHEET.md          <- generated build spec cards (engine, brakes, paint, interior...)
│   ├── VENDORS.md             <- generated registry of all 17 vendors
│   └── GAPS-AND-ACTIONS.md    <- generated open questions and the call list to close them
├── summaries/
│   └── batch-1 ... batch-7    <- human-readable narrative of what each extraction batch found
└── scripts/
    └── extend_v2 ... v7.py    <- the append scripts that produced each version (provenance)
```

`data/master-record.json` is the single source of truth. Everything in `docs/` is generated from it and should be regenerated, never hand-edited, when the data changes.

## Project status (start here)

**Current version: v7** (`data/master-record.json` equals `data/versions/ghia-1965-master-record-v7.json`). Working tree clean, all batches committed and pushed. The repository was reorganized from the original flat upload into the canonical layered layout, so the layout above is what is actually on disk.

### Batch history

| Batch | Version | Documents | Headline |
|---|---|---|---|
| 1 | v1 | DOC-001 to DOC-007 | Seed: Raby DTM kit, KGPR order, NV Automotive head work, JBugs interior |
| 2 | v2 | DOC-008 to DOC-024 | 17 documents: the O'Reilly receipt cluster, paint activator, Meyers |
| 3 | v3 | DOC-025 to DOC-035 | Machine shop identified as NV Automotive (GAP-03); JBugs backorders |
| 4 | v4 | DOC-036 to DOC-045 | Handwritten cost ledger ($500 car); paint trail recovered (GAP-13) |
| 5 | v5 | DOC-046, DOC-047 | Complete Raby receipt dated 2013-07-29 (GAP-02); body reseal order; wiring |
| 6 | v6 | DOC-048 to DOC-053 | Wheels identified as Sprintstars (GAP-17); bumper re-chrome story; 2 new vendors |
| 7 | v7 | DOC-054 to DOC-057 | Engine bottom-end invoice, new earliest date 2013-06-29 (GAP-09); gauge heads identified (GAP-20); Mid America order reconstructed (GAP-22) |

### Latest session (Batches 6 and 7, 2026-06-11)

Ten photographed documents extracted across two batches. Resolutions: GAP-17 and GAP-20 substantially resolved (Sprintstar wheels, Mid America 2-1/16in gauges), GAP-09 substantially resolved (NV Automotive supplied the bottom end), GAP-22 opened and fully resolved within the session (Mid America order 04682256 reconstructed across all three shipments). New gap GAP-23 opened: the lug-bolt evidence does not reconcile (14mm vs 12mm). Data housekeeping done in the same session: vendor document arrays re-synced, spec cards backfilled into the JSON, and a dedupe exception documented after NV Automotive turned out to have reused invoice number 125 on two distinct transactions.

### Where to pick up next

1. **More photographs are the highest-value input.** The top targets, in order: the VIN plate (GAP-01), the dash cluster (closes GAP-20), the wheels with a lug count (closes GAP-17 and GAP-23), and a re-shoot of O'Reilly invoice 2655-492277 laid flat (GAP-14). The full list is `docs/GAPS-AND-ACTIONS.md`.
2. **To ingest a new batch of document photos**, follow the established workflow below; the next batch is 8, producing v8 via `scripts/extend_v8.py`.

### Batch workflow (how every version is produced)

1. Read each photographed document; verify line-item arithmetic against printed subtotals/tax/totals before entering anything.
2. Check for dedupe (invoice/order number) against the document archive, and for vendor matches against the registry. Mind the documented exception: identical invoice numbers with different dates/totals/contents are distinct documents (see `docs/SCHEMA.md`).
3. Write `scripts/extend_vN.py` reading the frozen `data/versions/...v(N-1).json` and writing both v(N) and `data/master-record.json`. Continue IDs from the current high-water marks, never reuse. Backorders at 0.00 with cross-references; uncertainty flagged, not asserted; no em dashes.
4. Run it, then validate: unique IDs, valid doc/vendor references, timeline sorted with undated entries last, vendor document arrays in sync, canonical file equals the new snapshot, script is deterministic.
5. Regenerate the affected files in `docs/`, update the statistics in this README, and write `summaries/batch-N-extraction-summary.md`.
6. Commit and push.

## Archive statistics (v7)

| Metric | Value |
|---|---|
| Documents extracted | 57 |
| Parts and services ledger entries | 217 |
| Vendors | 17 |
| Timeline events | 56 |
| Documented date range | 2013-06-29 to 2018-05-31 |
| Documented spend (priced ledger entries) | $5,831.52 |
| Restorer's own handwritten cost ledger | ~$2,994 including the $500 car |
| Data gaps | 23 tracked: 15 open, 5 partially resolved, 3 fully resolved |

## The data model in brief

Seven layers, fully described in `docs/SCHEMA.md`:

1. **Vehicle Master Record**: identity, ownership chain, acquisition.
2. **Systems Taxonomy**: SYS-01 through SYS-12 (Engine, Cooling, Fuel/Carburetion, Exhaust, Transmission, Front Suspension/Steering, Brakes, Body/Paint, Interior, Electrical, Wheels/Tires, Consumables).
3. **Parts Ledger**: every line item, P-### for parts and S-### for services, with SKU, quantity, pricing, system assignment, and notes.
4. **Vendor Registry**: VEN-## entries with addresses, contacts, and document cross-references.
5. **Document Archive**: DOC-### entries, deduplicated on invoice number.
6. **Build Spec Cards**: rolled-up specifications per system, each fact traceable to documents.
7. **Restoration Timeline and Data Gaps**: dated events and tracked unknowns (GAP-##).

## Conventions

- IDs increment continuously across batches and are never reused.
- Duplicate photographs are matched on invoice number, noted on the original document record, and never re-entered.
- Anything uncertain is flagged (for example, two invoices billed to other names carry attribution flags) rather than asserted.
- Facts on spec cards cite their source documents.
- Em dashes are not used anywhere in this project.

## Provenance highlights

- The engine program is the documented start of the restoration: NV Automotive supplied the bottom-end parts on June 29, 2013 (now the earliest dated document), the Raby DTM kit followed on July 29, and NV Automotive finished the head machine work on August 13.
- The handwritten cost ledger records the $500 purchase of the car and itemizes the engine bottom end; its estimates differ from the NV Automotive invoice prices, so the two are independent sources.
- NV Automotive reused invoice number 125 on two distinct 2013 transactions (bottom-end parts and head work); both are kept, with the collision flagged so they are never merged.
- The paint trail is recoverable: Washington County Collision (Hurricane UT), a 2014 Auto Paints Plus system purchase referencing mix "wa208v," and a 2015 Nason Ful-Thane mix to GM formula 3295. Translating those references into a color name is action item 2 in `docs/GAPS-AND-ACTIONS.md`.
- The three-part JBugs interior order (944952A/B/C) reconciles to the penny, including a refund cycle.
- A warranty replacement, a returned-then-recharged backorder, and two same-day cross-town supply runs are all preserved in the record.
- The wheels are Sprintstar 5-spokes, identified by a center cap order; the gauge heads are Mid America 2-1/16in oil pressure, oil temperature, and voltmeter units from the same multi-shipment order, reconstructed in full across Batches 6 and 7.
- The bumper chrome story is complete: both 3-piece bumpers re-plated in summer 2016, two pieces redone at no charge, and the chrome mounting hardware bought the day after the redo pickup.

## Roadmap

1. **Ingest remaining documents** (if any surface) using the same batch process: extract, append, snapshot a new version, regenerate docs.
2. **Close the gaps**: work the call list in `docs/GAPS-AND-ACTIONS.md`, starting with the VIN plate, the paint color name, and the re-photographs.
3. **Photo library**: tag build and bodywork photos to systems and timeline events.
4. **Application layer**: load `master-record.json` into a retrieval-backed assistant (Claude Project, or a local stack such as Ollama + Qdrant + Obsidian) so the car can be queried conversationally: "what brake fluid does it take," "who built the transaxle," "show me everything bought in May 2016."

## A note on the source material

The original paper folder was assembled by the restorer over five years and survived a cross-state move. It includes counter receipts on thermal paper, multi-page mail-order invoices, a packing list with a handwritten promise to ship as soon as possible, and one page of lined notebook paper that turned out to be the most valuable document in the box. Handle the originals kindly; scan anything new at the top of the page first, since cropped headers cost us two mysteries that took three batches to solve.
