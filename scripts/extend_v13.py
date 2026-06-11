import json

with open('data/versions/ghia-1965-master-record-v12.json') as f:
    d = json.load(f)

d['schema_version'] = '1.12'
d['generated_date'] = '2026-06-11'
d['generated_from'] = 'Batches 1-13 (DOC-001 to DOC-064; Batch 13 re-photographs DOC-016)'

# ============================================================================
# Batch 13: a re-photograph, not a new document. The cut-off original of
# DOC-016 (O'Reilly invoice, 2015-03-28) had illegible line items and a
# misread invoice number, tracked as GAP-14. A clear flat scan recovers the
# three line items and corrects the invoice number. Per the SCHEMA dedupe rule
# ("a better photo of a known document updates the existing record"), DOC-016
# is updated in place and its previously-missing ledger entries are added.
# Date (2015-03-28), net subtotal (48.47), and list total (82.15) all match
# the original, confirming the same transaction.
# ============================================================================

# ============ Update DOC-016 in place ============
for doc in d['document_archive']:
    if doc['doc_id'] == 'DOC-016':
        doc['title'] = "O'Reilly Auto Parts receipt, invoice 2655-499277: Meguiar's paint polishing supplies"
        doc['reference_numbers'] = {"invoice": "2655-499277", "counter": "44125",
                                    "auth_code": "762937", "card_ref": "508714062283"}
        doc['invoice_number_correction'] = ("Originally recorded as 2655-492277 from the cut-off photo; the clear "
            "re-photograph (Batch 13) reads 2655-499277. The date (2015-03-28), net subtotal (48.47), and list total "
            "(82.15) all match, confirming the same transaction.")
        doc['line_item_count'] = 3
        doc['subtotal'] = 48.47
        doc['list_total'] = 82.15
        doc['tax'] = 3.93
        doc['total'] = 52.40
        doc['payment'] = "Debit VISA xxxx7266 (PIN, no signature), auth 762937, ref 508714062283"
        doc['extraction_note'] = ("RE-PHOTOGRAPHED FLAT in Batch 13, resolving GAP-14. The original photo cut off the "
            "left edge, leaving the line items illegible and the invoice number misread; the clear scan recovers "
            "both. Counter 44125, 12:19:06, debit VISA x7266 (the buyer card seen on other invoices, e.g. KGPR "
            "DOC-055). Three Meguiar's machine paint-polishing items: M0216 cleaner and M0316 machine glaze (16 oz "
            "each, $17.99) and an MPR 67-900 polish pad ($12.49). Net $48.47, list $82.15, tax $3.93, total $52.40. "
            "This is the paint buff-out: a cleaner, a machine glaze, and a pad for correcting the fresh 2014-2015 "
            "paint, fitting the March 2015 activity cluster.")

# ============ New ledger entries (previously missing from DOC-016) ============
def entry(eid, doc, ven, date, name, sku, qty, unit, ext, sys, notes=None, **kw):
    e = {"entry_id": eid, "doc_id": doc, "vendor_id": ven, "date": date,
         "item_name": name, "vendor_sku": sku, "qty": qty,
         "unit_price": unit, "ext_price": ext, "system_id": sys, "notes": notes}
    e.update(kw); return e

d['parts_ledger'].extend([
    entry("P-215", "DOC-016", "VEN-05", "2015-03-28",
          "Meguiar's Mirror Glaze Cleaner, 16 oz", "MEG M0216", 1, 17.99, 17.99, "SYS-08",
          "Description as written '16ozCleaner'. Paint cleaner for machine correction of the fresh paint.",
          list_price=30.49),
    entry("P-216", "DOC-016", "VEN-05", "2015-03-28",
          "Meguiar's Mirror Glaze Machine Glaze, 16 oz", "MEG M0316", 1, 17.99, 17.99, "SYS-08",
          "Description as written '16ozMchnGlaz'. Machine glaze, paired with the cleaner and pad for the buff-out.",
          list_price=30.49),
    entry("P-217", "DOC-016", "VEN-05", "2015-03-28",
          "Polish Pad", "MPR 67-900", 1, 12.49, 12.49, "SYS-08",
          "Description as written 'POLISH PAD'. Machine polishing pad.", list_price=21.17),
])

# ============ Keep vendor document arrays in sync (DOC-016 already on VEN-05) ============
issued = {}
for doc in d['document_archive']:
    issued.setdefault(doc['vendor_id'], []).append(doc['doc_id'])
for v in d['vendor_registry']:
    docs = v.get('documents', [])
    for doc_id in issued.get(v['vendor_id'], []):
        if doc_id not in docs:
            docs.append(doc_id)
    v['documents'] = docs

# ============ Update the DOC-016 timeline event in place ============
for e in d['restoration_timeline']:
    if e.get('doc_id') == 'DOC-016':
        e['event'] = ("O'Reilly paint buff-out supplies: Meguiar's cleaner and machine glaze (16 oz each) and a "
                      "polish pad, $52.40 on debit. Line items recovered by re-photograph in Batch 13 (GAP-14)")

# ============ Build spec card ============
bp = d['build_spec_cards']['body_paint']
bp['paint_polishing'] = ("Machine paint-correction supplies bought 2015-03-28 (DOC-016): Meguiar's M0216 cleaner and "
    "M0316 machine glaze (16 oz each) with an MPR 67-900 polish pad, the buff-out of the fresh 2014-2015 paint.")
if "DOC-016" not in bp['sources']:
    bp['sources'].append("DOC-016")

# ============ Gap movement: GAP-14 resolved ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-14':
        g['status'] = 'RESOLVED'
        g['resolution'] = ("Batch 13: re-photographed flat (DOC-016). The three line items are recovered, Meguiar's "
            "M0216 cleaner, M0316 machine glaze, and an MPR 67-900 polish pad (net $48.47, tax $3.93, total $52.40, "
            "debit VISA x7266), and the invoice number is corrected to 2655-499277 (the cut-off original misread it "
            "as 2655-492277).")

# ============ Write v13 ============
with open('data/versions/ghia-1965-master-record-v13.json', 'w') as f:
    json.dump(d, f, indent=1)
with open('data/master-record.json', 'w') as f:
    json.dump(d, f, indent=1)

print("v13 written:",
      len(d['document_archive']), "docs,",
      len(d['parts_ledger']), "ledger,",
      len(d['vendor_registry']), "vendors,",
      len(d['restoration_timeline']), "events,",
      len(d['data_gaps']), "gaps,",
      "spend", round(sum(e['ext_price'] for e in d['parts_ledger'] if e.get('ext_price')), 2))
