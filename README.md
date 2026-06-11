# Karman-Ghia-Project
# 1965 VW Karmann Ghia Restoration Archive

A structured digital archive of the complete restoration of a 1965 Volkswagen Karmann Ghia coupe (Type 14), reconstructed from the prior restorer's folder of receipts, invoices, packing lists, and handwritten records. Every document has been photographed, extracted, and normalized into a single machine-readable master record, with human-readable references generated from it.

The long-term goal of this project is a bespoke application that understands every aspect of this car: what is on it, who supplied it, what it cost, when it happened, and what is still unknown.

## The car in one paragraph

Restored 2013-2018 by James O. Mahan, who bought the car as a $500 project. The drivetrain is the centerpiece: a 1,971cc Type 4 conversion (94mm x 71mm, 8.6:1 compression) running a Jake Raby DTM Stage III cooling system, dual Weber carburetors, an Engle cam, a lightened flywheel, and head work by NV Automotive (Bill Shapley) in Las Vegas, backed by a Freeway Flyer transaxle built by Steve Hansen. The chassis carries 2.5 inch drop spindles, an adjustable front beam, KYB shocks, and a front disc brake conversion. Body and paint were done in 2014 through Washington County Collision in Hurricane, Utah. The interior is the JBugs Deluxe Velour/Tweed kit with grey velour headliner, charcoal carpet, custom door panels, and grey 2-point Wolfsburg belts. Documented activity runs from June 29, 2013 (the NV Automotive engine bottom-end parts) to May 31, 2018 (Weber rebuild kits).

## Repository layout

```
ghia-restoration-archive/
├── README.md                  <- you are here
├── data/
│   ├── master-record.json     <- THE canonical dataset (always current)
│   └── versions/              <- frozen snapshots, v1 through v7, one per extraction batch
├── docs/
│   ├── SCHEMA.md              <- the seven-layer data model, conventions, and ID scheme
│   ├── TIMELINE.md            <- generated narrative and event log, 2013-2018
│   ├── SPEC-SHEET.md          <- generated build spec cards (engine, brakes, paint, interior...)
│   ├── VENDORS.md             <- generated registry of all 15 vendors
│   └── GAPS-AND-ACTIONS.md    <- generated open questions and the call list to close them
├── summaries/
│   └── batch-1 ... batch-7    <- human-readable narrative of what each extraction batch found
└── scripts/
    └── extend_v2 ... v7.py    <- the append scripts that produced each version (provenance)
```

`data/master-record.json` is the single source of truth. Everything in `docs/` is generated from it and should be regenerated, never hand-edited, when the data changes.

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
