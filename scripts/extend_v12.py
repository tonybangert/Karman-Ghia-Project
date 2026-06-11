import json

with open('data/versions/ghia-1965-master-record-v11.json') as f:
    d = json.load(f)

d['schema_version'] = '1.11'
d['generated_date'] = '2026-06-11'
d['generated_from'] = 'Batches 1-12 (DOC-001 to DOC-064)'

# ============================================================================
# Batch 12: the first service of the new-owner era. Riverwest Automotive
# (Milwaukee WI) invoice 9697, dated 2026-06-10, is the newest document in the
# archive by eight years. It documents the car under current owner Tony Bangert
# (co-name Zara Pakroo) in Whitefish Bay WI at 1,650 miles, confirming the
# Nevada-to-Wisconsin move that the garage photo (DOC-062c, plate ZZ65KG)
# implied, and it establishes a points-type Bosch 009 distributor.
# ============================================================================

# ============ New vendor ============
d['vendor_registry'].append(
    {"vendor_id": "VEN-20", "name": "Riverwest Automotive Service",
     "address": "801 E. Keefe, Milwaukee, WI 53211", "phone": "414-534-0080",
     "specialty": "Independent automotive repair (Milwaukee WI); services the car in the current-owner Wisconsin era",
     "documents": [],
     "note": "First shop to service the car under current owner Tony Bangert (invoice 9697, 2026-06-10)."})

# ============ New document ============
d['document_archive'].append(
    {"doc_id": "DOC-064", "type": "Service invoice", "vendor_id": "VEN-20",
     "title": "Riverwest Automotive invoice #9697: no-start repair, ignition points/condenser, oil change (first service of the new-owner era)",
     "reference_numbers": {"invoice": "9697"},
     "date": "2026-06-10",
     "bill_to": "Zara Pakroo / Tony Bangert, 1459 E Bay Point Rd, Whitefish Bay, WI",
     "vehicle_as_written": "1965 vw karmann ghia", "vin_on_invoice": None, "mileage": 1650, "plate_on_invoice": None,
     "line_item_count": 5, "subtotal_taxable": 583.23, "tax_rate": "7.90%", "tax": 46.08, "total": 629.31,
     "extraction_note": ("NEWEST DOCUMENT IN THE ARCHIVE (2026-06-10), eight years after the last restoration-era "
        "document (2018-05-31), and the FIRST DOCUMENTED SERVICE OF THE NEW-OWNER ERA. Owner Tony Bangert (co-name "
        "Zara Pakroo on the invoice) in Whitefish Bay WI; the Wisconsin location and the plate context match the "
        "garage photo with plate ZZ65KG (DOC-062c), confirming the Nevada-to-Wisconsin move. Mileage 1,650. The car "
        "arrived on a no-start: a trigger wire off the switch to the starter had resistance at the connection, so a "
        "hard start relay was added; it then cranked but had no spark, so the coil/distributor were diagnosed and a "
        "new points set and condenser (for a '009' distributor) were fitted. A 20W-50 Castrol GTX Classic oil and "
        "filter change was done. Totals reconcile: 583.23 taxable + 46.08 tax (7.90%) = 629.31. The points-and-"
        "condenser service establishes the engine runs a points-type distributor, the common Bosch 009 centrifugal-"
        "advance unit (the '009' notation), not electronic ignition. The invoice's VIN field was left blank, so "
        "GAP-01 (VIN) stays open.")})

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
    entry("S-009", "DOC-064", "VEN-20", "2026-06-10",
          "Diagnostic and repair labor: no-start", None, 3.5, 120.00, 420.00, "SYS-10",
          "No start, towed in. Trigger wire off the switch to the starter had resistance at the connection; added a "
          "hard start relay. Then cranked but no spark, so diagnosed the coil/distributor. 3.5 hours at $120."),
    entry("P-212", "DOC-064", "VEN-20", "2026-06-10",
          "Hard Start Relay", None, 1, 10.00, 10.00, "SYS-10",
          "Added to bypass the resistive trigger-wire connection between the switch and the starter."),
    entry("P-213", "DOC-064", "VEN-20", "2026-06-10",
          "Ignition Condenser (for 009 distributor)", "009", 1, 14.90, 14.90, "SYS-10",
          "Listed 'ignition condensor - 009'. Points-type distributor, the common Bosch 009 centrifugal-advance unit."),
    entry("P-214", "DOC-064", "VEN-20", "2026-06-10",
          "Ignition Points Set", None, 1, 18.33, 18.33, "SYS-10",
          "Paired with the condenser above; confirms a points (contact-breaker) distributor, not electronic ignition."),
    entry("S-010", "DOC-064", "VEN-20", "2026-06-10",
          "Oil and Filter Change, 20W-50 Castrol GTX Classic", None, 1, 120.00, 120.00, "SYS-01",
          "Flat-rate service billed as one line (oil, filter, and labor). 20W-50 Castrol GTX Classic."),
])

# ============ Vehicle master record: new-owner era ============
vmr = d['vehicle_master_record']
vmr['odometer_observed'] = ("000877 on the 110mm speedometer (DOC-062a, undated photo); 1,650 miles recorded on the "
    "Riverwest Automotive service invoice 2026-06-10 (DOC-064). The gap reflects driving between the dash photo and "
    "the 2026 service.")
vmr['service_history'] = [
    ("2026-06-10, Riverwest Automotive (Milwaukee WI), 1,650 mi: no-start repair (hard start relay; new points and "
     "condenser for the 009 distributor) and a 20W-50 Castrol GTX Classic oil and filter change, $629.31 (DOC-064).")
]
for o in vmr.get('ownership_chain', []):
    if o.get('owner') == 'Tony Bangert':
        o['location'] = "Whitefish Bay, WI"
        o['addresses'] = ["1459 E Bay Point Rd, Whitefish Bay, WI"]
        o['household'] = "Zara Pakroo (co-name on the Riverwest service invoice, DOC-064)"
        o['period'] = ("Current owner. The car moved from Nevada to Wisconsin. First documented service 2026-06-10 at "
                       "1,650 miles (Riverwest Automotive, Milwaukee WI, DOC-064).")
        o['location_note'] = ("Invoice address is Whitefish Bay WI (DOC-064); an earlier record read 'Bayside, WI', an "
                              "adjacent North Shore Milwaukee village.")

# ============ Timeline ============
new_events = [
    {"date": "2026-06-10", "event": ("NEW-OWNER ERA, FIRST DOCUMENTED SERVICE: Riverwest Automotive (Milwaukee WI) "
        "services the car for owner Tony Bangert at 1,650 miles. No-start repair (hard start relay; new points and "
        "condenser for the 009 distributor) and a 20W-50 Castrol GTX Classic oil and filter change, $629.31. Newest "
        "document in the archive, eight years after the restoration era"), "doc_id": "DOC-064"},
]
tl = d['restoration_timeline']
for ev in new_events:
    idx = next((i for i, e in enumerate(tl) if e.get('date') is None or e['date'] > ev['date']), len(tl))
    tl.insert(idx, ev)

# ============ Build spec cards ============
eng = d['build_spec_cards']['engine']
eng['ignition'] = ("Points-type distributor, the common Bosch 009 centrifugal-advance unit (the '009' on the 2026 "
    "service invoice). New points and condenser fitted 2026-06-10 to cure a no-spark (DOC-064).")
eng['engine_oil'] = "20W-50 Castrol GTX Classic, with filter, per the 2026-06-10 service (DOC-064)."
if "DOC-064" not in eng['sources']:
    eng['sources'].append("DOC-064")

el = d['build_spec_cards']['electrical']
el['starting'] = ("A hard start relay was added 2026-06-10 after the trigger wire from the switch to the starter "
    "showed resistance at the connection (DOC-064).")
el.setdefault('sources', [])
if "DOC-064" not in el['sources']:
    el['sources'].append("DOC-064")

# ============ Gap movement ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-01':
        g['note'] = ("Batch 12: the 2026-06-10 Riverwest service invoice (DOC-064) also left the VIN field blank, so "
                     "the VIN remains undocumented. Photograph the chassis VIN plate.")

# ============ Write v12 ============
with open('data/versions/ghia-1965-master-record-v12.json', 'w') as f:
    json.dump(d, f, indent=1)
with open('data/master-record.json', 'w') as f:
    json.dump(d, f, indent=1)

print("v12 written:",
      len(d['document_archive']), "docs,",
      len(d['parts_ledger']), "ledger,",
      len(d['vendor_registry']), "vendors,",
      len(d['restoration_timeline']), "events,",
      len(d['data_gaps']), "gaps,",
      "spend", round(sum(e['ext_price'] for e in d['parts_ledger'] if e.get('ext_price')), 2))
