# Batch 7 Extraction Summary: DOC-054 to DOC-057, the engine bottom end and the gauge heads

Extends the master record to v7. 4 new documents, 21 new ledger entries (P-189 to P-209), and three resolutions plus one new gap. Canonical data: `data/master-record.json` (frozen as `data/versions/ghia-1965-master-record-v7.json`).

---

## New earliest document: the engine bottom end, June 29, 2013

DOC-054 is **NV Automotive invoice #125 dated 2013-06-29**, total $464.76 paid cash, job header written "type 4 shit." It itemizes the 2.0L Type 4 bottom-end parts: crank, rods, gasket set, main/rod/cam bearings, front and rear seals, a Melling oil pump, a 210mm lightened flywheel (no charge), and a pilot bearing. This is now the **earliest dated document in the archive**, a month before the Raby DTM kit (2013-07-29) and six weeks before the head machine work (2013-08-13). The engine program now reads as a coherent summer-2013 arc anchored on NV Automotive in Las Vegas: bottom-end parts in June, Raby cooling kit in July, head work in August.

This **substantially resolves GAP-09**: the bottom-end vendor is NV Automotive. The invoice prices differ from the restorer's handwritten estimate ledger (DOC-043, e.g. crank $60 written vs $99 invoiced), confirming the two are independent sources. The 94mm pistons/cylinders, lifters, and rockers from DOC-043 are not on this invoice and came from elsewhere (the remaining thread of GAP-09).

### Invoice-number collision (a dedupe exception)

This is the second NV Automotive document numbered **invoice 125, customer 123**. DOC-003 (the head machine work) is also invoice 125, customer 123, but dated 2013-08-13 with a different total and different line items. Bill Shapley reused the number across two distinct transactions. The dedupe rule keys on invoice number, so both records now carry an explicit collision note, the SCHEMA dedupe rule documents the exception, and the two are never merged.

## Order 04682256 reconstructed: GAP-22 resolved, gauge heads identified

Three of this batch's images complete the Mid America order opened in Batch 6:

- **DOC-056 (order 04682256-00001, 2015-04-20, $160.92)** is the parent order. It shipped three 2-1/16in gauges (oil pressure 12V 111-150, oil temperature 111-155, voltmeter 8-16V 111-152) and four sets of chrome 12mm lug bolts (319-991). The shipped subtotal reconciles exactly: 29.99 x 3 + 49.96 = 139.93, plus 20.99 shipping = 160.92.
- **DOC-057 (order 04682256-00003, 2015-05-18, $25.98)** shipped the final two Sprintstar center caps, fulfilling the P-183 backorder from DOC-049.

Together with DOC-049 (shipment -00002) from Batch 6, the full order is now documented, **resolving GAP-22**. The gauges **substantially resolve GAP-20**: the gauge heads are Mid America 2-1/16in units. The 111157 temperature sender stayed backordered through the last shipment, so its fulfillment is still undocumented (now tracked under GAP-20).

## New gap: the lug-bolt and center-cap evidence does not reconcile (GAP-23)

The parent order surfaced a contradiction. There are now two chrome lug bolt purchases that imply different wheels: a 16pc 14mm set (319-994, DOC-028, implies 4-lug) and four sets of 5 chrome 12mm bolts (319-991, DOC-056, implies 5-lug). Order -00001 also carried "center cap, chrome, for iron" parts and chrome decals (backordered) that do not obviously belong to the Sprintstar wheels confirmed by the 319-655 caps. GAP-23 tracks confirming the wheel make, bolt pattern, lug size, and whether a second wheel set was ever involved, from photos of the car.

## DOC-055: KGPR rear-deck brightwork, March 18, 2015

KGPR invoice #445363, $105.31 on VISA: the rear hood "Volkswagen" script ($16.49) and the marquee "Karmann Ghia" rear hood script ($39.00) with their 3-piece and 4-piece clamping plate sets, plus a door striker repair kit. The fresh air inlet grille seal pair was backordered again ($0.00), another instance of the grille-seal backorder tracked in GAP-11. The customer phone 702-351-1031 matches the Shine Shop tickets from Batch 6, confirming the buyer identity.

## New documents

| Doc ID | Date | Vendor | Total | Contents |
|---|---|---|---|---|
| DOC-054 | 2013-06-29 | NV Automotive | 464.76 | Engine bottom-end parts (10 lines), paid cash |
| DOC-055 | 2015-03-18 | KGPR | 105.31 | Rear hood scripts, clamping plates, door striker kit; grille seal backordered |
| DOC-056 | 2015-04-20 | Mid America Motorworks | 160.92 | Order 04682256-00001: 3 gauges + chrome 12mm lug bolts |
| DOC-057 | 2015-05-18 | Mid America Motorworks | 25.98 | Order 04682256-00003: final 2 Sprintstar center caps |

## Running totals after v7

| Metric | Count |
|---|---|
| Documents | 57 |
| Ledger entries | 217 |
| Vendors | 17 |
| Timeline events | 56 |
| Documented date range | 2013-06-29 to 2018-05-31 |
| Documented spend (priced entries) | $5,831.52 |

## Gap movement

| Gap | Status |
|---|---|
| GAP-09 (bottom-end vendor) | SUBSTANTIALLY RESOLVED: NV Automotive, invoice 125, 2013-06-29; P&C/lifters/rockers source still open |
| GAP-20 (gauge heads) | SUBSTANTIALLY RESOLVED: Mid America 2-1/16in oil pressure, oil temp, voltmeter |
| GAP-22 (Mid America order siblings) | RESOLVED: order 04682256 fully reconstructed |
| GAP-23 (new) | Wheel/lug evidence does not reconcile: 14mm vs 12mm bolts, iron-wheel caps vs Sprintstar caps |
