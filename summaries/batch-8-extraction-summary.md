# Batch 8 Extraction Summary: DOC-058 and DOC-059, the instrument literature

Extends the master record to v8. 2 new documents, 1 new vendor, 0 new ledger entries (both documents are product literature, not transactions). Canonical data: `data/master-record.json` (frozen as `data/versions/ghia-1965-master-record-v8.json`).

---

## The speedometer head identified: ISP West (DOC-058)

A two-sided ISP West instruction manual for a programmable VW speedometer: 110mm standard VW diameter, M18 x 1.5 cable thread, mechanical speedometer with a double odometer and integrated indicator lights for turn signals, oil pressure, battery/charge, and high beam, driven off the left front wheel hub cable. This identifies the **speedometer head**, the central instrument that the gauge work of Batches 6 and 7 surrounded. ISP West (Carson, CA, vwispwest.com) is new vendor VEN-18, referenced only through this manual.

Two cautions are recorded rather than smoothed over: the manual has no price, invoice number, or date (it is literature, so it produces no ledger entry, and the speedometer purchase itself is undocumented), and it is labelled "Exclusively for Volkswagen Beetle." The Ghia shares the VW speedometer cable and drive, and a Beetle or aftermarket speedometer in a restored Ghia is common, but the installed unit should be confirmed against the car (cf. GAP-16).

## The three gauges confirmed by their connection diagrams (DOC-059)

Three Mid America Motorworks connection-diagram sheets (copyright 2007) that accompanied the gauges bought on order 04682256 (DOC-056, 2015-04-20):

- 111-150 oil pressure gauge, 12V (EOPG: gauge + pressure sender + battery)
- 111-152 voltmeter, 12V (gauge + battery)
- 111-155 electric temperature gauge, 12V (ETG: gauge + temp sender + battery)

These confirm the gauge identities already recorded as P-205, P-206, and P-207. Two refinements came out of the diagrams: the 111-155 is titled an "Electric Temperature Gauge" (used here for oil temperature, so P-206 was renamed accordingly), and the 111-150 oil pressure diagram requires a pressure sender that is not separately documented anywhere in the archive. Grouped as one literature document tied to DOC-056, with the three form numbers recorded.

## Instrumentation now substantially complete

With the speedometer head (ISP West) and the three gauge heads (Mid America, confirmed by their diagrams) both identified, GAP-20 is well advanced. The cluster is: an ISP West programmable speedometer flanked by Mid America 2-1/16in oil pressure, oil temperature, and voltmeter gauges. Remaining open threads, all folded into GAP-20: confirm the cluster against dash photos, locate the undocumented oil pressure sender, the speedometer purchase invoice is not in the archive, and it is still unresolved which temperature sender (Auto Meter 2258, 196-107, or the backordered 111157) feeds the temperature gauge.

## Housekeeping

- The instrumentation spec card carried a stale `gauges` field still reading "gauge heads not yet documented"; removed in favor of the `speedometer`, `gauge_heads`, and `senders` fields.
- Two stale undated timeline duplicates were removed from the JSON: DOC-001 (Raby kit) and DOC-003 (head work) each had a leftover "date unknown" event from before Batches 5 and 7 fixed their dates, alongside their correct dated events. Only DOC-043 (the genuinely undated handwritten ledger) and DOC-058 (undated literature) remain undated.

## New documents

| Doc ID | Date | Vendor | Type | Contents |
|---|---|---|---|---|
| DOC-058 | undated | ISP West | Instruction manual | 110mm programmable VW speedometer with integrated indicator lights |
| DOC-059 | undated | Mid America Motorworks | Product literature (3 diagrams) | Connection diagrams for the 111-150, 111-152, 111-155 gauges |

## Running totals after v8

| Metric | Count |
|---|---|
| Documents | 59 |
| Ledger entries | 217 (unchanged: literature only) |
| Vendors | 18 |
| Timeline events | 55 |
| Documented date range | 2013-06-29 to 2018-05-31 |
| Documented spend (priced entries) | $5,831.52 (unchanged) |

## Gap movement

| Gap | Status |
|---|---|
| GAP-20 (instrumentation) | SUBSTANTIALLY RESOLVED, extended: gauges confirmed by their diagrams; speedometer head identified (ISP West). Oil pressure sender and speedometer purchase still undocumented |
