# Batch 13 Extraction Summary: DOC-016 re-photographed, GAP-14 resolved

Extends the master record to v13. No new document; instead an existing one is updated. 3 new ledger entries (P-215 to P-217), one gap resolved, one invoice number corrected. Canonical data: `data/master-record.json` (frozen as `data/versions/ghia-1965-master-record-v13.json`).

This is the first batch to **update an existing document rather than append a new one**, using the schema's dedupe rule: a better photo of a known document updates the existing record.

---

## What was wrong, and what the re-shoot fixed

DOC-016 was an O'Reilly receipt photographed with its left edge cut off. Two things were lost: the line items (illegible) and one digit of the invoice number. It carried zero ledger entries, a null total, and the note "ILLEGIBLE LINE ITEMS," and it was tracked as **GAP-14** (high priority).

A clear flat re-photograph recovers everything. The date (2015-03-28), the net subtotal ($48.47), and the list total ($82.15) all match the original exactly, confirming the same transaction, so DOC-016 is updated in place.

## Recovered line items (Meguiar's paint buff-out)

| Ledger | Item | SKU | List | Net |
|---|---|---|---|---|
| P-215 | Meguiar's Mirror Glaze Cleaner, 16 oz | MEG M0216 | 30.49 | 17.99 |
| P-216 | Meguiar's Mirror Glaze Machine Glaze, 16 oz | MEG M0316 | 30.49 | 17.99 |
| P-217 | Polish Pad | MPR 67-900 | 21.17 | 12.49 |

Net $48.47, list $82.15, tax $3.93, total **$52.40**, paid by debit VISA x7266 (the buyer card seen on other invoices). All three are SYS-08 (Body and Paint), consistent with how the 3M refinish tape and weatherstrip adhesive were classified. A cleaner, a machine glaze, and a pad together are a machine paint-correction kit: this is the buff-out of the fresh 2014-2015 paint, fitting the March 2015 activity cluster.

## Invoice number correction

The cut-off original recorded **2655-492277**; the clear scan reads **2655-499277**. The obscured digit was misread. Because the date, net, and list totals all match, this is the same document, and the number is corrected on the record with a note explaining the change.

## Records updated

- **DOC-016**: title, reference numbers (corrected invoice, counter 44125, auth/ref codes), line item count (0 to 3), subtotal/list/tax/total, payment, and a new extraction note replacing the "illegible" note.
- **Parts ledger**: P-215 to P-217 added.
- **Timeline**: the 2015-03-28 DOC-016 event rewritten from "line items illegible" to the recovered contents.
- **Body and Paint spec card**: a Paint Polishing line added; DOC-016 added to its sources.
- **GAP-14**: marked RESOLVED.

## Running totals after v13

| Metric | Count |
|---|---|
| Documents | 64 (unchanged; DOC-016 updated, not added) |
| Ledger entries | 227 |
| Vendors | 20 |
| Timeline events | 60 |
| Documented date range | 2013-06-29 to 2026-06-10 |
| Documented spend (priced entries) | $6,588.12 |
| Data gaps | 24 tracked: 13 open, 7 partially or substantially resolved, 4 fully resolved |

## Gap movement

| Gap | Status |
|---|---|
| GAP-14 (DOC-016 line items cut off) | RESOLVED: line items recovered (Meguiar's cleaner, machine glaze, polish pad, $52.40) and invoice number corrected to 2655-499277. |
