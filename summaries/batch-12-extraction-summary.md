# Batch 12 Extraction Summary: DOC-064, the new-owner era begins

Extends the master record to v12. 1 new document, 5 new ledger entries (S-009, P-212 to P-214, S-010), 1 new vendor (VEN-20), no new gaps. Canonical data: `data/master-record.json` (frozen as `data/versions/ghia-1965-master-record-v12.json`).

This is the first document from outside the restoration. Every prior document came from James Mahan's 2013 to 2018 build in Nevada and Utah. DOC-064 is a 2026 service invoice from Wisconsin, under a new owner, and it opens an ongoing maintenance record.

---

## DOC-064: Riverwest Automotive invoice #9697, June 10, 2026

Riverwest Automotive Service (801 E. Keefe, Milwaukee WI) serviced the car for owner **Tony Bangert** (co-name **Zara Pakroo** on the invoice), 1459 E Bay Point Rd, Whitefish Bay WI, at **1,650 miles**. Total **$629.31** ($583.23 in line items plus $46.08 sales tax at 7.90%; arithmetic verified against the printed total).

The visit was a no-start repair plus routine maintenance:

- **Labor, 3.5 hr at $120 = $420.00 (S-009).** Towed in, no start. A trigger wire off the switch to the starter had resistance at the connection, so a hard start relay was added. It then cranked but had no spark, so the coil/distributor were diagnosed.
- **Hard start relay, $10.00 (P-212).**
- **Ignition condenser for a '009' distributor, $14.90 (P-213).**
- **Ignition points set, $18.33 (P-214).**
- **20W-50 Castrol GTX Classic oil and filter change, flat $120.00 (S-010).**

The ignition condenser, points, and relay are classified SYS-10 (Electrical), matching how the Ignition Wire Set (P-046) was filed; the oil-and-filter change stays a single SYS-01 service line, as the invoice bills it.

## What it establishes

- **Ownership and location.** The car moved from Nevada to Wisconsin. The Wisconsin location and the existing garage photo (DOC-062c, plate ZZ65KG) now reconcile: Tony Bangert is the current owner, in Whitefish Bay WI. The ownership chain, the odometer record, and a new `service_history` field on the vehicle master record are updated. (An earlier record read 'Bayside, WI'; the invoice gives the precise Whitefish Bay address, noted on the record.)
- **Ignition type.** The points-and-condenser service confirms the engine runs a **points-type distributor, the common Bosch 009 centrifugal-advance unit** (the '009' notation), not electronic ignition. Added to the engine spec card.
- **Engine oil.** **20W-50 Castrol GTX Classic.** Added to the engine spec card, so 'what oil does it take' is now answerable.
- **Mileage.** 1,650 miles, up from the 877 seen on the dash photo (DOC-062a). Recorded in `odometer_observed`.
- **VIN still open.** The invoice's VIN field was left blank, so GAP-01 (VIN) stays open; noted on the gap.

## New vendor

| Vendor | Location | Specialty | Source |
|---|---|---|---|
| VEN-20 Riverwest Automotive Service | Milwaukee, WI | Independent auto repair; current-owner service era | DOC-064 |

## Running totals after v12

| Metric | Count |
|---|---|
| Documents | 64 |
| Ledger entries | 224 |
| Vendors | 20 |
| Timeline events | 60 |
| Documented date range | 2013-06-29 to 2026-06-10 |
| Documented spend (priced entries, pre-tax) | $6,539.65 |

## Gap movement

| Gap | Status |
|---|---|
| GAP-01 (VIN / chassis / paint code) | Still OPEN: the 2026 service invoice also left the VIN field blank. Photograph the chassis VIN plate. |
