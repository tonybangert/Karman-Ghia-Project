import json

with open('data/versions/ghia-1965-master-record-v6.json') as f:
    d = json.load(f)

d['schema_version'] = '1.6'
d['generated_date'] = '2026-06-11'
d['generated_from'] = 'Batches 1-7 (DOC-001 to DOC-057)'

# ============ Cross-reference: NV Automotive invoice-number collision ============
# DOC-054 (this batch) is a SECOND NV Automotive document also numbered invoice
# 125, customer 123, but dated 2013-06-29 (bottom-end parts) versus DOC-003's
# 2013-08-13 (head machine work). Bill Shapley reused the number across two
# distinct transactions. Annotate DOC-003 so the invoice-number dedupe rule is
# never applied to merge them.
for doc in d['document_archive']:
    if doc['doc_id'] == 'DOC-003':
        doc['invoice_number_collision_note'] = ("NV Automotive issued a second, distinct invoice also numbered 125 "
            "(customer 123): DOC-054, dated 2013-06-29, for the engine bottom-end parts. Same shop, same printed "
            "invoice number, different date/total/contents. Do NOT dedupe these two on invoice number.")

# ============ Vehicle master chronology update (new earliest date) ============
vmr = d['vehicle_master_record']
vmr['ownership_chain'][0]['period'] = ('Documented activity 2013-06-29 (NV Automotive engine bottom-end parts) through '
    '2018-05-31 (Weber kits). Address chronology: Las Vegas / Henderson area engine work summer 2013 (bottom-end parts '
    '2013-06-29 and head machine work 2013-08-13 at NV Automotive), DTM kit shipped to Hurricane UT Jul 2013, body and '
    'paint in Hurricane UT 2014, Henderson NV assembly from Jan 2015 onward.')

# ============ New documents ============
d['document_archive'].extend([
    {"doc_id": "DOC-054", "type": "Parts invoice", "vendor_id": "VEN-03",
     "title": "NV Automotive invoice #125 (second of two): engine bottom-end parts",
     "reference_numbers": {"invoice": "125", "customer_id": "123"},
     "date": "2013-06-29", "bill_to": "James Mahan",
     "job_reference_as_written": "type 4 shit",
     "line_item_count": 10, "subtotal": 444.85, "taxable": 245.85, "tax_rate": "8.100%",
     "tax": 19.91, "total": 464.76, "payment": "Paid cash (handwritten 'PAID CASH')",
     "extraction_note": ("EARLIEST DATED DOCUMENT IN THE ARCHIVE, one month before the Raby DTM kit (2013-07-29) and "
        "six weeks before the head machine work (2013-08-13, DOC-003). NV Automotive supplied the 2.0L Type 4 "
        "bottom-end parts: crank, rods, gasket set, main/rod/cam bearings, front and rear seals, Melling oil pump, "
        "a 210mm lightened flywheel (no charge), and a pilot bearing. Substantially resolves GAP-09 (the bottom-end "
        "vendor is NV Automotive). INVOICE NUMBER COLLISION: this is a different document from DOC-003 despite both "
        "being NV Automotive invoice 125, customer 123; they differ in date, total, and contents. Prices here are "
        "the actual purchase prices and differ from the restorer's handwritten estimate ledger (DOC-043, e.g. crank "
        "$99 here vs $60 written), so the two are independent sources. Note: 94mm pistons/cylinders, lifters, and "
        "rockers from DOC-043 are NOT on this invoice and came from elsewhere.")},
    {"doc_id": "DOC-055", "type": "Mail order invoice", "vendor_id": "VEN-02",
     "title": "KGPR invoice #445363: rear hood scripts, door striker kit, grille seal",
     "reference_numbers": {"invoice": "445363", "customer_po": "FBM", "order_date": "2015-03-17"},
     "date": "2015-03-18", "ship_to": "James Mahan, 678 Covina Dr, Henderson NV 89002-8267",
     "customer_phone": "702-351-1031",
     "line_item_count": 6, "item_total": 91.36, "shipping": 13.95, "total": 105.31,
     "payment": "VISA x7266, James O Mahan", "ship_via": "FedEx",
     "extraction_note": ("Rear deck brightwork: the 'Volkswagen' rear hood script ($16.49) and the 'Karmann Ghia' "
        "rear hood script ($39.00) with their 3-piece and 4-piece clamping plate sets, plus a door striker repair "
        "kit. The fresh air inlet grille seal pair (853-657) was backordered (qty bko 1, $0.00), another instance of "
        "the grille-seal backorder tracked in GAP-11. Customer phone 702-351-1031 matches the Shine Shop tickets "
        "(DOC-050/051), confirming the buyer identity. Fits the March 2015 activity cluster (gear lube, rubber "
        "plugs, O'Reilly run).")},
    {"doc_id": "DOC-056", "type": "Mail order invoice", "vendor_id": "VEN-09",
     "title": "Mid America order 04682256-00001: gauges and chrome lug bolts (the parent order)",
     "reference_numbers": {"order": "04682256-00001", "customer": "23552403-000"},
     "date": "2015-04-20", "ship_to": "James Mahan, 678 Covina Dr, Henderson NV 89002-8267",
     "page_count": 2, "line_item_count": 4, "subtotal": 139.93, "shipping": 20.99, "total": 160.92,
     "extraction_note": ("THE PARENT ORDER behind DOC-049 (shipment -00002) and DOC-057 (shipment -00003), resolving "
        "GAP-22. Shipment -00001 (2 pages) charged $160.92 and shipped three 2-1/16in gauges (oil pressure 12V, oil "
        "temperature, and an 8-16V voltmeter) plus four sets of chrome 12mm lug bolts (319-991, set of 5, 20 bolts "
        "total). IDENTIFIES THE GAUGE HEADS for GAP-20: Mid America 2-1/16in units. Backordered on this invoice and "
        "shipped later or left open: the 319-655 Sprintstar center caps (shipped on -00002 and -00003), the 111157 "
        "3/8in temperature sender (still backordered through -00003), and a set of 'center cap, chrome, for iron' "
        "with chrome decals and a 20pc lug bolt set (A319993) whose fulfillment is undocumented. The chrome 'for "
        "iron' caps and the 12mm/5-per-wheel lug bolts sit oddly beside the Sprintstar caps and the separately "
        "ordered 16pc 14mm bolts (DOC-028); see GAP-23.")},
    {"doc_id": "DOC-057", "type": "Mail order invoice", "vendor_id": "VEN-09",
     "title": "Mid America order 04682256-00003: final two Sprintstar center caps",
     "reference_numbers": {"order": "04682256-00003", "customer": "23552403-000"},
     "date": "2015-05-18", "ship_to": "James Mahan, 678 Covina Dr, Henderson NV 89002-8267",
     "line_item_count": 1, "subtotal": 25.98, "shipping": 0.00, "total": 25.98,
     "extraction_note": ("Third and final shipment of order 04682256: the last two 319-655 Sprintstar center caps "
        "($25.98), fulfilling the P-183 backorder from DOC-049. Four Sprintstar caps total across -00002 and -00003 "
        "(one set of four). The 111157 3/8in temperature sender is STILL listed as backordered here, so its "
        "fulfillment remains undocumented (folds into GAP-20).")},
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
    # DOC-054: NV Automotive engine bottom-end parts (2013-06-29)
    entry("P-189", "DOC-054", "VEN-03", "2013-06-29", "Crankshaft, 2.0L Type 4", None, 1, 99.00, 99.00, "SYS-01",
          "Listed '2.0 crank'. Bottom-end parts purchase from the same shop that did the heads."),
    entry("P-190", "DOC-054", "VEN-03", "2013-06-29", "Connecting Rods, 2.0L Type 4 (set)", None, 1, 90.00, 90.00, "SYS-01",
          "Listed '2.0 rods'."),
    entry("P-191", "DOC-054", "VEN-03", "2013-06-29", "Engine Gasket Set", None, 1, 52.00, 52.00, "SYS-01", None),
    entry("P-192", "DOC-054", "VEN-03", "2013-06-29", "Main Bearings", None, 1, 49.95, 49.95, "SYS-01", None),
    entry("P-193", "DOC-054", "VEN-03", "2013-06-29", "Rod Bearings", None, 1, 24.95, 24.95, "SYS-01", None),
    entry("P-194", "DOC-054", "VEN-03", "2013-06-29", "Cam Bearings", None, 1, 13.95, 13.95, "SYS-01", None),
    entry("P-195", "DOC-054", "VEN-03", "2013-06-29", "Front and Rear Main Seals", None, 1, 25.00, 25.00, "SYS-01", None),
    entry("P-196", "DOC-054", "VEN-03", "2013-06-29", "Melling Oil Pump", None, 1, 75.00, 75.00, "SYS-01",
          "Brand Melling. Pairs with the 'oil pump milling $10' line in the handwritten ledger (DOC-043)."),
    entry("P-197", "DOC-054", "VEN-03", "2013-06-29", "Lightened Flywheel, 210mm", None, 1, 0.00, 0.00, "SYS-01",
          "Listed '210 mm lightend flywheel', no charge (n/c). Confirms the lightened flywheel spec (also in DOC-043 as 'light flywheel')."),
    entry("P-198", "DOC-054", "VEN-03", "2013-06-29", "Pilot Bearing", None, 1, 15.00, 15.00, "SYS-05",
          "Clutch pilot bearing (flywheel/input-shaft interface)."),
    # DOC-055: KGPR invoice 445363 (2015-03-18)
    entry("P-199", "DOC-055", "VEN-02", "2015-03-18", "Door Striker Repair Kit (for 1 striker)", "837-290 64 66 N KT",
          1, 27.50, 27.50, "SYS-08", None, fitment_listed="1966 GHIACP"),
    entry("P-200", "DOC-055", "VEN-02", "2015-03-18", "Seal, Fresh Air Inlet Grille, Pair (backordered)",
          "853-657 60 74 RP PR", 1, 3.75, 0.00, "SYS-08",
          "Backordered (qty bko 1) at 0.00 per convention. Another fresh air grille seal backorder, see GAP-11.",
          fitment_listed="1966 GHIACP"),
    entry("P-201", "DOC-055", "VEN-02", "2015-03-18", "Rear Hood Script, 'Volkswagen'", "853-687 66 74 RP",
          1, 16.49, 16.49, "SYS-08", None, fitment_listed="1966 GHIACP"),
    entry("P-202", "DOC-055", "VEN-02", "2015-03-18", "Rear Hood VW Script Clamping Plate, 3 pcs", "853-695 66 74 RP ST",
          1, 3.39, 3.39, "SYS-08", None, fitment_listed="1966 GHIACP"),
    entry("P-203", "DOC-055", "VEN-02", "2015-03-18", "Rear Hood Script, 'Karmann Ghia'", "853-905 63 74 RP",
          1, 39.00, 39.00, "SYS-08", "The marquee rear-deck emblem.", fitment_listed="1966 GHIACP"),
    entry("P-204", "DOC-055", "VEN-02", "2015-03-18", "Rear Hood KG Script Clamping Plate, 4 pcs", "853-907 ALL RP ST",
          1, 4.98, 4.98, "SYS-08", None, fitment_listed="1966 GHIACP"),
    # DOC-056: Mid America order 04682256-00001 (2015-04-20)
    entry("P-205", "DOC-056", "VEN-09", "2015-04-20", "Oil Pressure Gauge, 12V, 2-1/16in", "111-150",
          1, 29.99, 29.99, "SYS-10", "Gauge head (GAP-20). 2-1/16in electric oil pressure gauge."),
    entry("P-206", "DOC-056", "VEN-09", "2015-04-20", "Oil Temperature Gauge, 2-1/16in", "111-155",
          1, 29.99, 29.99, "SYS-10", "Gauge head (GAP-20). Description as written: 'OIL TEMP GAUGE, EACH VEE THREE'. Pairs with an oil temp sender (111157 backordered here; 196-107 bought Dec 2015, P-091)."),
    entry("P-207", "DOC-056", "VEN-09", "2015-04-20", "Voltmeter, 2-1/16in, 8-16V", "111-152",
          1, 29.99, 29.99, "SYS-10", "Gauge head (GAP-20)."),
    entry("P-208", "DOC-056", "VEN-09", "2015-04-20", "Lug Bolts, Chrome 12mm, Set of 5 (x4 sets)", "319-991",
          4, 12.49, 49.96, "SYS-11",
          "Alt# 00-9711-0. Four sets of 5 = 20 bolts, implying a 5-lug wheel. This conflicts with the separately ordered 16pc 14mm set (319-994, DOC-028, implying 4-lug 14mm). See GAP-23."),
    # DOC-057: Mid America order 04682256-00003 (2015-05-18)
    entry("P-209", "DOC-057", "VEN-09", "2015-05-18", "Center Cap, for Sprintstar Wheel", "319-655",
          2, 12.99, 25.98, "SYS-11",
          "Final 2 of 4 Sprintstar caps, fulfilling the P-183 backorder from DOC-049. Completes one set of four Sprintstar center caps."),
])

# Link the batch-6 backorder entries to their fulfillment / latest status
for e in d['parts_ledger']:
    if e['entry_id'] == 'P-183':
        e['notes'] = ("Backorder at 0.00 per convention; FULFILLED by DOC-057 shipment -00003 (2015-05-18), "
                      "ledger P-209.")
    if e['entry_id'] == 'P-184':
        e['notes'] = ("Backorder at 0.00; still backordered as of shipment -00003 (DOC-057, 2015-05-18), so "
                      "fulfillment remains undocumented. THIRD documented gauge sender, alongside the Auto Meter "
                      "2258 (P-086) and the 300-degree oil temp 196-107 (P-091). Matches the Mid America oil temp "
                      "gauge 111-155 (P-206); the Dec 2015 196-107 sender may have substituted for this backordered "
                      "unit (not asserted).")

# ============ Timeline events (inserted in date order) ============
new_events = [
    {"date": "2013-06-29", "event": "RESTORATION'S EARLIEST DOCUMENT: engine bottom-end parts from NV Automotive (crank, rods, bearings, gaskets, Melling oil pump, 210mm lightened flywheel, pilot bearing), $464.76 paid cash. One month before the Raby kit", "doc_id": "DOC-054"},
    {"date": "2015-03-18", "event": "KGPR rear-deck brightwork: 'Volkswagen' and 'Karmann Ghia' rear hood scripts with clamping plates, door striker kit; grille seal backordered", "doc_id": "DOC-055"},
    {"date": "2015-04-20", "event": "Mid America order 04682256 placed: three 2-1/16in gauges (oil pressure, oil temp, voltmeter) and chrome lug bolts ship; Sprintstar caps and temp sender backordered. GAUGE HEADS IDENTIFIED (GAP-20)", "doc_id": "DOC-056"},
    {"date": "2015-05-18", "event": "Mid America ships the final two Sprintstar center caps (order 04682256-00003); 111157 temp sender still backordered", "doc_id": "DOC-057"},
]
tl = d['restoration_timeline']
for ev in new_events:
    idx = next((i for i, e in enumerate(tl) if e.get('date') is None or e['date'] > ev['date']), len(tl))
    tl.insert(idx, ev)

# ============ Build spec cards ============
eng = d['build_spec_cards']['engine']
eng['bottom_end_sourcing'] = ("Bottom-end parts supplied by NV Automotive, invoice 125 dated 2013-06-29, $464.76 paid "
    "cash (DOC-054): 2.0L crank, rods, gasket set, main/rod/cam bearings, front and rear seals, Melling oil pump, "
    "210mm lightened flywheel (no charge), pilot bearing. The 94mm pistons/cylinders, lifters, and rockers (in the "
    "handwritten ledger DOC-043) are not on this invoice and came from elsewhere.")
eng['flywheel'] = "Lightened flywheel, 210mm, supplied no-charge by NV Automotive 2013-06-29 (DOC-054); also noted in DOC-043"
for s in ("DOC-054",):
    if s not in eng['sources']:
        eng['sources'].append(s)

inst = d['build_spec_cards']['instrumentation']
inst['gauge_heads'] = ("Identified (GAP-20): Mid America 2-1/16in gauges from order 04682256 shipped 2015-04-20 "
    "(DOC-056): oil pressure gauge 12V (111-150), oil temperature gauge (111-155), and an 8-16V voltmeter (111-152).")
inst['senders'] = ("Auto Meter 2258 electric temp sender (P-086, 2015-05-21); 300-degree oil temp sender 196-107, "
    "alt# V3-2305-5 (P-091, 2015-12-30); and a 111157 3/8in resistance temperature sender (P-184) ordered 2015-04-20 "
    "but still backordered as of 2015-05-18, fulfillment undocumented.")
if "DOC-056" not in inst['sources']:
    inst['sources'].append("DOC-056")

wt = d['build_spec_cards']['wheels_tires']
wt['lug_hardware'] = ("Two distinct chrome lug bolt purchases that do not reconcile: a 16pc 14mm set (319-994, DOC-028, "
    "2015-04-27) implying 4 lugs x 4 wheels, and four sets of 5 chrome 12mm bolts (319-991, DOC-056, 2015-04-20) "
    "implying 5 lugs x 4 wheels. Confirm the wheel bolt pattern and lug size from the car (GAP-23).")
wt['center_caps'] = ("Four Sprintstar center caps (319-655) across shipments -00002 and -00003. Order -00001 also "
    "carried 'center cap, chrome, for iron' parts and chrome decals (backordered, fulfillment undocumented), which do "
    "not obviously belong to Sprintstar wheels; see GAP-23.")
for s in ("DOC-056", "DOC-057"):
    if s not in wt['sources']:
        wt['sources'].append(s)

bp = d['build_spec_cards']['body_paint']
bp['rear_deck_emblems'] = ("Rear hood 'Volkswagen' script (853-687) and 'Karmann Ghia' script (853-905) with VW "
    "3-piece and KG 4-piece clamping plates; door striker repair kit (KGPR invoice 445363, 2015-03-18).")
for s in ("DOC-055",):
    if s not in bp['sources']:
        bp['sources'].append(s)

# ============ Gap movement ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-09':
        g['status'] = 'SUBSTANTIALLY RESOLVED'
        g['resolution'] = ("Batch 7: NV Automotive invoice 125 dated 2013-06-29 (DOC-054) documents the bottom-end "
            "vendor and itemizes crank, rods, bearings, gaskets, seals, Melling oil pump, 210mm lightened flywheel, "
            "and pilot bearing, $464.76 paid cash. Remaining: source of the 94mm pistons/cylinders, lifters, and "
            "rockers, which are in the handwritten ledger (DOC-043) but not on this invoice.")
    if g['gap_id'] == 'GAP-20':
        g['status'] = 'SUBSTANTIALLY RESOLVED'
        g['resolution'] = ("Batch 7: gauge heads identified as Mid America 2-1/16in units (DOC-056, 2015-04-20): oil "
            "pressure 12V (111-150), oil temperature (111-155), and 8-16V voltmeter (111-152). Remaining: confirm "
            "against the dash cluster and resolve which temperature sender (Auto Meter 2258, 196-107, or the "
            "backordered 111157) feeds the oil temp gauge.")
    if g['gap_id'] == 'GAP-22':
        g['status'] = 'RESOLVED'
        g['resolution'] = ("Batch 7: shipment -00001 (DOC-056, gauges and lug bolts, $160.92) and shipment -00003 "
            "(DOC-057, final 2 Sprintstar caps, $25.98) recovered, completing order 04682256 alongside -00002 "
            "(DOC-049). Only open thread: the 111157 temperature sender stayed backordered through -00003 (tracked "
            "under GAP-20).")
d['data_gaps'].append({
    "gap_id": "GAP-23", "priority": "medium",
    "item": ("Reconcile the wheel/lug evidence. Two lug bolt purchases conflict: 16pc chrome 14mm (319-994, DOC-028, "
             "implies 4-lug) versus four sets of 5 chrome 12mm (319-991, DOC-056, implies 5-lug). Order 04682256-00001 "
             "also carried 'center cap, chrome, for iron' parts and chrome decals (backordered) that do not obviously "
             "match the Sprintstar caps (319-655). Confirm from the car: wheel make (Sprintstar confirmed by caps), "
             "bolt pattern, lug size, and whether a second wheel set or iron-wheel caps were involved.")
})

# ============ Write v7 ============
with open('data/versions/ghia-1965-master-record-v7.json', 'w') as f:
    json.dump(d, f, indent=1)
with open('data/master-record.json', 'w') as f:
    json.dump(d, f, indent=1)

print("v7 written:",
      len(d['document_archive']), "docs,",
      len(d['parts_ledger']), "ledger,",
      len(d['vendor_registry']), "vendors,",
      len(d['restoration_timeline']), "events,",
      len(d['data_gaps']), "gaps,",
      "spend", round(sum(e['ext_price'] for e in d['parts_ledger'] if e.get('ext_price')), 2))
