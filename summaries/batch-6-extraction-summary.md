# Batch 6 Extraction Summary: DOC-048 to DOC-053, the wheels identified and the bumper chrome story

Extends the master record to v6. 6 new documents, 12 new ledger entries (P-179 to P-188, S-007 and S-008), 2 new vendors, and one headline resolution. Canonical data: `data/master-record.json` (frozen as `data/versions/ghia-1965-master-record-v6.json`).

---

## GAP-17 substantially resolved: the wheels are Sprintstars

Mid America Motorworks shipment 04682256-00002 (April 28, 2015) reads **"CENTER CAP, FOR SPRINTSTAR"** (319-655, alt# 00-9707-0): the aftermarket wheels are Sprintstar 5-spokes (EMPI pattern). This locks together with the 16pc chrome 14mm lug bolt set bought one day earlier on separate order 04684493 (DOC-028): caps and bolts for four wheels, ordered the same week of spring 2015. Two caps shipped on this invoice; two more caps plus a 111157 3/8in resistance-type temperature sender remain on back order, and neither the order's first shipment (-00001) nor the backorder fulfillment is in the archive. That is new GAP-22, and the 111157 sender is now the third documented sender on the GAP-20 watch list. Remaining for GAP-17: wheel size and finish, and the tires, from photos of the car.

## The bumper chrome story, June to September 2016

Three documents reconstruct a complete arc during the exterior brightwork phase:

1. **DOC-050 (2016-06-22)**: both bumpers, three pieces each, dropped at American Polishing & Plating (DBA Shine Shop), Henderson, for re-chroming. $350 flat, $300 deposit, balance circled "Paid", "2wks" quoted.
2. **DOC-051 (2016-09-06)**: two bumper pieces redone at no charge ("Redo N/C"), picked up about ten weeks after drop-off.
3. **DOC-052 (2016-09-07)**: the very next day, McFadden-Dale sells Mahan eight each of 5/16-18 x 3/4 chrome carriage bolts, chrome flat washers, chrome lock washers, and chrome hex nuts: the bumper-blade-to-bracket fastener set in show finish. The bumpers were going back on the car.

The Shine Shop is new vendor VEN-17, and the KGPR sharp-edge side molding order (DOC-041, 2016-08-17) now sits inside this same brightwork window.

## The Henderson phase starts six days earlier

DOC-048, a cash counter sale at **Nevada Offroad Buggy** (new vendor VEN-16, Las Vegas) dated **January 14, 2015**: six Dzus quarter-turn buttons with spring tabs and a clutch hook shaft, the first clutch linkage part in the archive. This now predates the West Coast Metric reseal order (DOC-046, Jan 20) as the earliest documented purchase of the Henderson assembly phase.

## A mixed receipt, handled per the GAP-16 convention

DOC-052 also carries clearly non-vehicle household lines (weed control concentrate, a stainless trowel, rebar epoxy coating, $31.10 of the $98.01 subtotal). These are noted on the document record and omitted from the parts ledger. Two borderline lines (2X gloss dark gray spray, FiberFix repair wrap) are entered with attribution flags. Direct evidence that the folder mixes personal and project purchases at the hardware counter, exactly what GAP-16 anticipated.

## Housekeeping: data drift corrected

- The `documents` arrays on the vendor registry had not been maintained since each vendor's creation (e.g. VEN-05 listed one O'Reilly document instead of seventeen). Re-synced from the document archive; the intentional named-on-document associations (VEN-06 on DOC-004, VEN-15 on DOC-044) are preserved.
- The rendered SPEC-SHEET.md carried Wheels Tires, Body Paint, and Electrical cards that had never been written into the JSON. Backfilled as `wheels_tires`, `body_paint`, and `electrical` build spec cards so the master record is canonical again.

## New documents

| Doc ID | Date | Vendor | Total | Contents |
|---|---|---|---|---|
| DOC-048 | 2015-01-14 | Nevada Offroad Buggy | 32.85 | Dzus fasteners x6+6, clutch hook shaft |
| DOC-049 | 2015-04-28 | Mid America Motorworks | 25.98 | 2x Sprintstar center caps; 2 caps + temp sender backordered |
| DOC-050 | 2016-06-22 | American Polishing & Plating | 350.00 | Re-chrome two 3-piece bumpers |
| DOC-051 | 2016-09-06 | American Polishing & Plating | 0.00 | Two bumper pieces redone, no charge |
| DOC-052 | 2016-09-07 | McFadden-Dale | 106.00 | Chrome bumper mounting hardware (mixed receipt) |
| DOC-053 | 2016-09-26 | McFadden-Dale | 2.68 | Small hardware cash run |

## Running totals after v6

| Metric | Count |
|---|---|
| Documents | 53 |
| Ledger entries | 196 |
| Vendors | 17 |
| Timeline events | 52 |
| Documented date range | 2013-07-29 to 2018-05-31 |
| Documented spend (priced entries) | $5,129.40 |

## Gap movement

| Gap | Status |
|---|---|
| GAP-17 (wheel identification) | SUBSTANTIALLY RESOLVED: Sprintstar 5-spokes; size/finish and tires remain |
| GAP-20 (gauge heads) | Updated: three documented senders, including the backordered 111157 |
| GAP-22 (new) | Mid America order 04682256: shipment -00001 and backorder fulfillment undocumented |
