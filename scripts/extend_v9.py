import json

with open('data/versions/ghia-1965-master-record-v8.json') as f:
    d = json.load(f)

d['schema_version'] = '1.8'
d['generated_date'] = '2026-06-11'
d['generated_from'] = 'Batches 1-9 (DOC-001 to DOC-061)'

# ============ New vendor ============
d['vendor_registry'].append(
    {"vendor_id": "VEN-19", "name": "A-1 Performance Exhaust Systems",
     "address": "721 South Main Street, Santa Ana, CA 92701",
     "phones": {"main": "714-836-7201"},
     "email": "tigerperformance@aol.com", "web": "GenuineA1.com",
     "specialty": "Performance exhaust systems for aircooled VWs ('As seen on the fastest street and drag cars in the world'); ships ceramic coated and stainless systems",
     "documents": ["DOC-060"],
     "note": "Referenced only via the installation/maintenance literature that shipped with the exhaust (DOC-060); no purchase invoice for the exhaust is in the archive."})

# ============ New documents ============
d['document_archive'].extend([
    {"doc_id": "DOC-060", "type": "Product literature (2 sheets)", "vendor_id": "VEN-19",
     "title": "A-1 Performance Exhaust Systems installation and maintenance literature",
     "reference_numbers": {}, "date": None, "page_count": 2, "line_item_count": 0,
     "extraction_note": ("Two sheets that shipped with the exhaust: a flange-sealant instruction sheet (header flange "
        "to muffler flange is surfaced flat, no gasket, high temperature silicone only, retorque header bolts warm) "
        "and a full installation/tips/maintenance + limited lifetime warranty sheet. IDENTIFIES THE EXHAUST "
        "MANUFACTURER (GAP-07): A-1 Performance Exhaust Systems, Santa Ana CA. The maintenance sheet covers ceramic "
        "coating care ('the coated pipe', ceramic coating warranty for visual exterior corrosion) and stainless "
        "header maintenance, consistent with the car's documented ceramic coated exhaust (DOC-004): the coating "
        "reads as A-1 factory-applied rather than a third-party coater, though that is implied, not stated. "
        "HANDWRITTEN ANNOTATION on the sealant sheet, interpretation uncertain: appears to read 'Blk/wht wire power "
        "goes to RC8' (a wiring note unrelated to the exhaust, possibly radio or ignition; recorded verbatim as "
        "best readable). No price, invoice number, or date: literature only, no ledger entry; the exhaust purchase "
        "itself is not documented in the archive.")},
    {"doc_id": "DOC-061", "type": "Mail order invoice", "vendor_id": "VEN-04",
     "title": "JBugs order 1066410A: grey armrest pair and headlight switch",
     "reference_numbers": {"order": "1066410A", "customer": "467595", "sales_id": "KH/KH"},
     "date": "2016-09-28", "bill_to": "James Mahan, 678 Covina Dr, Henderson NV 89002-8267",
     "customer_phone": "702-351-1031", "ship_via": "PM (post office)",
     "line_item_count": 4, "total": 124.90,
     "payment": "VISA x0115 (same card as DOC-052, McFadden-Dale 2016-09-07)",
     "extraction_note": ("Final interior trim: grey armrests for 1958-67 (sold as a pair at $99.95, with the left and "
        "right component lines printed at 0.00, the familiar kit-header pattern) matching the grey velour/tweed "
        "interior, plus a headlight switch for Bug/Ghia 58-67 with a note to use the 10mm dash escutcheon. Shipped "
        "same day via post office (pulled by DJ, shipped by OS). NEW LATEST 2016 DATE: 2016-09-28, two days after "
        "the McFadden-Dale small hardware run (DOC-053). The VISA ending 0115 ties this account (JBugs customer "
        "467595) to the in-person McFadden-Dale purchases, and the phone 702-351-1031 matches the Shine Shop and "
        "KGPR records: one buyer across all channels.")},
])

# ============ Keep vendor document arrays in sync ============
issued = {}
for doc in d['document_archive']:
    issued.setdefault(doc['vendor_id'], []).append(doc['doc_id'])
for v in d['vendor_registry']:
    docs = v.get('documents', [])
    for doc_id in issued.get(v['vendor_id'], []):
        if doc_id not in docs:
            docs.append(doc_id)
    v['documents'] = docs

# ============ New ledger entries ============
def entry(eid, doc, ven, date, name, sku, qty, unit, ext, sys, notes=None, **kw):
    e = {"entry_id": eid, "doc_id": doc, "vendor_id": ven, "date": date,
         "item_name": name, "vendor_sku": sku, "qty": qty,
         "unit_price": unit, "ext_price": ext, "system_id": sys, "notes": notes}
    e.update(kw); return e

d['parts_ledger'].extend([
    entry("P-210", "DOC-061", "VEN-04", "2016-09-28",
          "Armrests, Grey, 1958-67, Pair", "16-1622-16", 1, 99.95, 99.95, "SYS-09",
          "Sold as a pair; the document also prints left (16-1612-16) and right (16-1613-16) component lines at "
          "0.00 (kit-header pattern), consolidated here. Grey matches the JBugs Deluxe Velour/Tweed interior."),
    entry("P-211", "DOC-061", "VEN-04", "2016-09-28",
          "Headlight Switch, Bug/Ghia 58-67 / T2 68-70", "311941531A", 1, 24.95, 24.95, "SYS-10",
          "Invoice notes 'use 10mm dash escutcheon'. VW 311-941-531A pattern switch."),
])

# ============ Timeline ============
# Correction: DOC-053's event claimed the latest 2016 date; DOC-061 now holds it.
for e in d['restoration_timeline']:
    if e['doc_id'] == 'DOC-053':
        e['event'] = ("Small hardware cash run at McFadden-Dale: nickel cap nuts, stainless socket caps, "
                      "carriage bolts")

tl = d['restoration_timeline']
new_dated = {"date": "2016-09-28",
    "event": ("JBugs order: grey armrest pair and headlight switch, $124.90, shipped same day. Latest 2016 date; "
              "documented activity now continuous Jan 2015 to Sep 2016"),
    "doc_id": "DOC-061"}
idx = next((i for i, e in enumerate(tl) if e.get('date') is None or e['date'] > new_dated['date']), len(tl))
tl.insert(idx, new_dated)
# keep undated events in document-id order: place after DOC-058, before DOC-043
idx = next((i for i, e in enumerate(tl) if e.get('date') is None and e['doc_id'] == 'DOC-043'), len(tl))
tl.insert(idx, {"date": None,
    "event": ("Undated: A-1 Performance exhaust installation/maintenance literature (exhaust manufacturer "
              "identified; no purchase invoice in archive)"),
    "doc_id": "DOC-060"})

# ============ Build spec cards ============
d['build_spec_cards']['exhaust'] = {
    "card_id": "SPEC-EXHAUST",
    "system": ("A-1 Performance Exhaust Systems (Santa Ana CA), ceramic coated. Manufacturer identified from the "
               "installation/maintenance literature that shipped with the system (DOC-060); the ceramic coating "
               "reads as A-1 factory-applied (implied, not stated). Flat-surfaced header-to-muffler flange joint, "
               "sealed with high temperature silicone, no gasket."),
    "maintenance_notes": ("Per A-1 literature: retorque header bolts warm after first 15 minutes; coated slip "
                          "joints marked and re-fitted ~1in past the coated pipe end; anti-seize on stainless "
                          "slip joints."),
    "sources": ["DOC-004", "DOC-060"]
}

inter = d['build_spec_cards']['interior']
inter['armrests'] = "Grey armrest pair, 1958-67 style (JBugs 16-1622-16, 2016-09-28), matching the grey kit"
if "DOC-061" not in inter['sources']:
    inter['sources'].append("DOC-061")

elec = d['build_spec_cards']['electrical']
elec['headlight_switch'] = ("Headlight switch, Bug/Ghia 58-67 pattern (311941531A, JBugs 2016-09-28), fitted with "
                            "10mm dash escutcheon per invoice note")
if "DOC-061" not in elec['sources']:
    elec['sources'].append("DOC-061")

# ============ Gap movement ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-07':
        g['status'] = 'SUBSTANTIALLY RESOLVED'
        g['resolution'] = ("Batch 9: exhaust manufacturer identified as A-1 Performance Exhaust Systems (Santa Ana "
            "CA) from the installation/maintenance literature shipped with the system (DOC-060). The literature's "
            "ceramic coating care section implies the coating is A-1 factory-applied, which would close the coating "
            "vendor question too, but that is implied rather than stated. Remaining: the exhaust purchase invoice "
            "(model, date, price) is not in the archive.")

# ============ Write v9 ============
with open('data/versions/ghia-1965-master-record-v9.json', 'w') as f:
    json.dump(d, f, indent=1)
with open('data/master-record.json', 'w') as f:
    json.dump(d, f, indent=1)

print("v9 written:",
      len(d['document_archive']), "docs,",
      len(d['parts_ledger']), "ledger,",
      len(d['vendor_registry']), "vendors,",
      len(d['restoration_timeline']), "events,",
      len(d['data_gaps']), "gaps,",
      "spend", round(sum(e['ext_price'] for e in d['parts_ledger'] if e.get('ext_price')), 2))
