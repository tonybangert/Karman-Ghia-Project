# Karman-Ghia-Project
# 1965 VW Karmann Ghia Restoration Archive

A structured digital archive of the complete restoration of a 1965 Volkswagen Karmann Ghia coupe (Type 14), reconstructed from the prior restorer's folder of receipts, invoices, packing lists, and handwritten records. Every document has been photographed, extracted, and normalized into a single machine-readable master record, with human-readable references generated from it.

The long-term goal of this project is a bespoke application that understands every aspect of this car: what is on it, who supplied it, what it cost, when it happened, and what is still unknown.

## The car in one paragraph

Restored 2013-2018 by James O. Mahan, who bought the car as a $500 project. The drivetrain is the centerpiece: a 1,971cc Type 4 conversion (94mm x 71mm, 8.6:1 compression) running a Jake Raby DTM Stage III cooling system, dual Weber carburetors, an Engle cam, a lightened flywheel, and head work by NV Automotive (Bill Shapley) in Las Vegas, backed by a Freeway Flyer transaxle built by Steve Hansen. The chassis carries 2.5 inch drop spindles, an adjustable front beam, KYB shocks, and a front disc brake conversion. Body and paint were done in 2014 through Washington County Collision in Hurricane, Utah. The interior is the JBugs Deluxe Velour/Tweed kit with grey velour headliner, charcoal carpet, custom door panels, and grey 2-point Wolfsburg belts. Documented activity runs from June 29, 2013 (the NV Automotive engine bottom-end parts) to May 31, 2018 (Weber rebuild kits), and the record now continues into the new-owner era: the car moved to Wisconsin and was first serviced there on June 10, 2026. The car now lives with its current owner in Wisconsin (plate ZZ65KG), photographed with 877 miles on the speedometer installed during restoration.

## Repository layout

```
Karman-Ghia-Project/
├── README.md                  <- you are here
├── data/
│   ├── master-record.json     <- THE canonical dataset (always current)
│   └── versions/              <- frozen snapshots, v1 through v11, one per extraction batch
├── docs/
│   ├── SCHEMA.md              <- the seven-layer data model, conventions, and ID scheme
│   ├── TIMELINE.md            <- generated narrative and event log, 2013-2018
│   ├── SPEC-SHEET.md          <- generated build spec cards (engine, brakes, paint, interior...)
│   ├── VENDORS.md             <- generated registry of all 20 vendors
│   └── GAPS-AND-ACTIONS.md    <- generated open questions and the call list to close them
├── summaries/
│   └── batch-1 ... batch-11   <- human-readable narrative of what each extraction batch found
├── scripts/
│   └── extend_v2 ... v11.py   <- the append scripts that produced each version (provenance)
└── app/                       <- "The $500 Ghia", the interactive archive web app
```

`data/master-record.json` is the single source of truth. Everything in `docs/` is generated from it and should be regenerated, never hand-edited, when the data changes.

## The interactive app

`app/` is a single-page React app, a digital museum exhibit for the car. It imports `data/master-record.json` directly as its database and computes every figure at load time, so it always matches the archive. Seven views: an overview, an interactive car explorer with twelve system hotspots, a phased timeline with a cumulative-spend sparkline, a filterable parts ledger with spend charts, a vendor grid with a supply-geography map, a before/after gallery, and the open mysteries from the data gaps. Every fact is one click from its source document.

```
cd app
npm install
npm run dev      # local dev server
npm run build    # static bundle in app/dist, base path /Karman-Ghia-Project/
```

Stack: React, Vite, TypeScript, Tailwind, Framer Motion, Recharts; fonts self-hosted via Fontsource. The base path auto-detects the deploy target: Vercel builds (VERCEL env) serve from the domain root, everything else uses `/Karman-Ghia-Project/` (override with `BASE_PATH`). To deploy on Vercel, import the repo and set the project Root Directory to `app`; the Vite preset handles the rest. GitHub Pages deploy is also wired: `.github/workflows/deploy.yml` builds `app/` and publishes on push to `main` (set Pages source to GitHub Actions). Optional assets: drop before/after photos in `app/public/gallery/` with a `gallery.json` manifest, and turntable frames in `app/public/spin/` with a `spin.json`; both degrade gracefully when absent.

## Project status (start here)

**Current version: v12** (`data/master-record.json` equals `data/versions/ghia-1965-master-record-v12.json`). Working tree clean, all batches committed and pushed. **The restorer's paper folder is fully ingested** (Batch 9 was the last folder document), and **Batch 12 opens the new-owner service era**: the first maintenance invoice since the car moved to Wisconsin. New service and ownership records are now an ongoing source. The repository was reorganized from the original flat upload into the canonical layered layout, so the layout above is what is actually on disk.

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
| 8 | v8 | DOC-058, DOC-059 | Product literature: ISP West speedometer manual (speedometer head identified) and Mid America gauge connection diagrams (confirm the three gauges); 1 new vendor |
| 9 | v9 | DOC-060, DOC-061 | Folder complete: A-1 Performance identified as the exhaust manufacturer (GAP-07); JBugs grey armrests and headlight switch, the latest 2016 document; 1 new vendor |
| 10 | v10 | DOC-062 | Owner photo set of the finished car: installed wheels CORRECTED to 911/Fuchs-style (not Sprintstars), engine bay / exhaust / interior / instruments photo-verified, odometer 877, Wisconsin registration |
| 11 | v11 | DOC-063 | Pre-restoration prints: the $500 car was oxidized green with lower-body rust and nose damage, on steel wheels with hubcaps, explaining the 'for iron' caps order (GAP-23) and corroborating the handwritten prep ledger |
| 12 | v12 | DOC-064 | New-owner era begins: Riverwest Automotive (Milwaukee WI) service invoice, 2026-06-10, 1,650 mi. No-start repair (hard start relay, points and condenser for the 009 distributor) and a 20W-50 oil change; the newest document by eight years; 1 new vendor |

### Latest session (Batch 12, 2026-06-11)

One new document, the first of the new-owner era. Riverwest Automotive Service (Milwaukee WI) invoice #9697, dated 2026-06-10, is the newest document in the archive by eight years. It documents the car under current owner Tony Bangert (co-name Zara Pakroo) in Whitefish Bay WI at 1,650 miles, confirming the Nevada-to-Wisconsin move that the garage photo (DOC-062c, plate ZZ65KG) implied. The visit was a no-start repair: a trigger wire to the starter had resistance at the connection (a hard start relay was added), then a no-spark was cured with new points and a condenser, which establishes a points-type Bosch 009 distributor (not electronic ignition); a 20W-50 Castrol GTX Classic oil and filter change was also done. $629.31 total ($583.23 in line items plus $46.08 tax). Five ledger entries (S-009, P-212 to P-214, S-010), one new vendor (VEN-20), and the engine, electrical, and ownership records updated. The VIN field was blank again, so GAP-01 stays open.

### Prior session (Batches 6 through 11, 2026-06-11)

Sixteen documents (DOC-048 to DOC-063: fourteen from the paper folder plus two photographic records) extracted across six batches. Resolutions: GAP-07, GAP-17, and GAP-20 substantially resolved (Sprintstar wheels; Mid America 2-1/16in gauges, with the gauge identities later confirmed by their connection diagrams and the speedometer head identified as an ISP West unit), GAP-09 substantially resolved (NV Automotive supplied the bottom end), GAP-22 opened and fully resolved within the session (Mid America order 04682256 reconstructed across all three shipments). New gap GAP-23 opened: the lug-bolt evidence does not reconcile (14mm vs 12mm). Data housekeeping done in the same session: vendor document arrays re-synced, spec cards backfilled into the JSON, a dedupe exception documented after NV Automotive turned out to have reused invoice number 125 on two distinct transactions, and two stale undated timeline duplicates (DOC-001, DOC-003) removed now that both carry firm dates. Batch 8 added only product literature (no spend). Batch 9, the final batch, identified the exhaust manufacturer as A-1 Performance Exhaust Systems (GAP-07 substantially resolved) and added the JBugs armrest/headlight-switch order of 2016-09-28, the latest 2016 document; with it, every document in the restorer's folder has been ingested. Batch 10 added the first photographs of the finished car (DOC-062), which verified the engine bay, exhaust, interior, and instruments against the paper record and CORRECTED the wheel identification: the installed wheels are 911/Fuchs-style alloys, not the Sprintstars the 2015 center cap order implied; the Sprintstar caps evidently belong to a set that never went on the car (GAP-23). The photos also surfaced two undocumented items, the banjo steering wheel and coco mats (new GAP-24). Batch 11 closed the session with three pre-restoration prints (DOC-063): the $500 car was oxidized green with lower-body rust-through and nose damage, on steel wheels with hubcaps, which corroborates the handwritten prep ledger line by line and explains the 'for iron' chrome caps order as abandoned dress-up for the original steel wheels.

### Where to pick up next

1. **Close-up photographs are the highest-value input.** Overview photos arrived in Batch 10; the remaining targets are close-ups: the VIN plate (GAP-01), the gauge faces and speedometer branding (GAP-20), a wheel with its brand stamp and lug count plus tire sidewalls (GAP-17/GAP-23/GAP-12), and a re-shoot of O'Reilly invoice 2655-492277 laid flat (GAP-14). The full list is `docs/GAPS-AND-ACTIONS.md`.
2. **The paper folder is fully ingested, and the service era has begun.** New maintenance and ownership records now arrive from the current owner; ingest each with the workflow below. The next batch would be 13, producing v13 via `scripts/extend_v13.py`. Known absences from the restoration folder remain the exhaust and speedometer purchase invoices.

### Batch workflow (how every version is produced)

1. Read each photographed document; verify line-item arithmetic against printed subtotals/tax/totals before entering anything.
2. Check for dedupe (invoice/order number) against the document archive, and for vendor matches against the registry. Mind the documented exception: identical invoice numbers with different dates/totals/contents are distinct documents (see `docs/SCHEMA.md`).
3. Write `scripts/extend_vN.py` reading the frozen `data/versions/...v(N-1).json` and writing both v(N) and `data/master-record.json`. Continue IDs from the current high-water marks, never reuse. Backorders at 0.00 with cross-references; uncertainty flagged, not asserted; no em dashes.
4. Run it, then validate: unique IDs, valid doc/vendor references, timeline sorted with undated entries last, vendor document arrays in sync, canonical file equals the new snapshot, script is deterministic.
5. Regenerate the affected files in `docs/`, update the statistics in this README, and write `summaries/batch-N-extraction-summary.md`.
6. Commit and push.

## Archive statistics (v12)

| Metric | Value |
|---|---|
| Documents extracted | 64 (61 paper, 2 photographic records, 1 service invoice) |
| Parts and services ledger entries | 224 |
| Vendors | 20 |
| Timeline events | 60 |
| Documented date range | 2013-06-29 to 2026-06-10 |
| Documented spend (priced ledger entries) | $6,539.65 |
| Restorer's own handwritten cost ledger | ~$2,994 including the $500 car |
| Data gaps | 24 tracked: 14 open, 7 partially resolved, 3 fully resolved |

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
- The car's whole arc is now photographed: oxidized green and rusted on a trailer at acquisition, then silver-blue metallic and finished in the desert, with the engine bay matching its receipts.
- The wheel story is a lesson in evidence: a 2015 Sprintstar center cap order pointed one way, but photos of the finished car show 911/Fuchs-style alloys installed; the caps evidently belong to a set that never went on. The gauge heads are Mid America 2-1/16in units (confirmed by their own connection diagrams), the speedometer is an ISP West 110mm programmable VW unit, and the exhaust is an A-1 Performance system, photo-verified on the car.
- The bumper chrome story is complete: both 3-piece bumpers re-plated in summer 2016, two pieces redone at no charge, and the chrome mounting hardware bought the day after the redo pickup.

## Roadmap

1. **Ingest remaining documents** (if any surface) using the same batch process: extract, append, snapshot a new version, regenerate docs.
2. **Close the gaps**: work the call list in `docs/GAPS-AND-ACTIONS.md`, starting with the VIN plate, the paint color name, and the re-photographs.
3. **Photo library** (begun): the finished-car and pre-restoration photo sets are in the record as DOC-062 and DOC-063, with lettered frames cited from spec cards and gaps; the image files themselves are retained by the owner. Next: store the images in the repository and tag build/bodywork photos to systems and timeline events.
4. **Application layer**: load `master-record.json` into a retrieval-backed assistant (Claude Project, or a local stack such as Ollama + Qdrant + Obsidian) so the car can be queried conversationally: "what brake fluid does it take," "who built the transaxle," "show me everything bought in May 2016."

## A note on the source material

The original paper folder was assembled by the restorer over five years and survived a cross-state move. It includes counter receipts on thermal paper, multi-page mail-order invoices, a packing list with a handwritten promise to ship as soon as possible, and one page of lined notebook paper that turned out to be the most valuable document in the box. Handle the originals kindly; scan anything new at the top of the page first, since cropped headers cost us two mysteries that took three batches to solve.
