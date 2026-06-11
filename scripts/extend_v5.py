import json

with open('/home/claude/ghia/ghia-1965-master-record-v4.json') as f:
    d = json.load(f)

d['schema_version'] = '1.4'
d['generated_from'] = 'Batches 1-5 (DOC-001 to DOC-047)'

# ============ MAJOR RESOLUTION: DOC-001 Raby receipt completed ============
for doc in d['document_archive']:
    if doc['doc_id'] == 'DOC-001':
        doc['date'] = '2013-07-29'
        doc['reference_numbers'] = {'sales_receipt': '1878', 'sales_order': '94'}
        doc['cashier'] = 'Jake'
        doc['handwritten_annotations'] = "'will be shipped as soon as possible' (arrow to Type 4 DTM STG III line); checkmarks beside each line"
        doc['title'] = 'Raby Enterprises sales receipt #1878: Type 4 DTM Stage III kit and conversion components'
        doc.pop('date_note', None)
        doc['extraction_note'] = ('Batch 5 supplied the complete, uncropped receipt, resolving GAP-02. Purchased 2013-07-29, two weeks BEFORE '
            'the NV Automotive head work (2013-08-13). Cashier listed as Jake (plausibly Jake Raby himself). 16 items, total qty 16, '
            'billed to Mahan at the Hurricane UT address. This receipt is now the earliest dated document in the archive and marks the start of the restoration.')

for v in d['vendor_registry']:
    if v['vendor_id'] == 'VEN-01':
        v['resolution_note'] = 'Receipt #1878 dated 2013-07-29 recovered in Batch 5; sales order #94 cross-reference confirmed.'

# Update Raby kit ledger entries with the date
for e in d['parts_ledger']:
    if e.get('doc_id') == 'DOC-001':
        e['date'] = '2013-07-29'

# ============ Vehicle master chronology update ============
vmr = d['vehicle_master_record']
vmr['ownership_chain'][0]['period'] = ('Documented activity 2013-07-29 (DTM kit purchase) through 2018-05-31 (Weber kits). Address chronology: '
    'Hurricane UT 2013-2014 (DTM kit Jul 2013, West Coast Metric orders Apr-May 2014, paint Jun 2014), with the Type 4 head work done at '
    'NV Automotive in Las Vegas Aug 2013 (Hurricane is ~2.5 hours from Vegas). Henderson NV from Jan 2015 onward.')

# ============ New documents ============
d['document_archive'].extend([
    {"doc_id": "DOC-046", "type": "Mail order invoice (4 pages)", "vendor_id": "VEN-13",
     "title": "West Coast Metric invoice 120072: complete body restoration seal set",
     "reference_numbers": {"invoice": "120072", "po": "JAMES", "shipment": "118151-1", "tracking": "628520412915"},
     "date": "2015-01-20", "ship_to": "James Mahan, 678 Covina Dr, Henderson NV",
     "line_item_count": 28, "freight": 11.05, "total": 364.45,
     "extraction_note": ("Four-page invoice; each page was photographed twice in Batch 5 and deduplicated on invoice number 120072. "
        "Anchored by the 141-021C Body Restoration Set for Ghias 65-69 (kit exploded into components) and the 143-018A quarter window "
        "popout seal kit for Ghia sedan 60-71. Also includes an 8-fuse fuse box with cover, Karmann side body badge emblem, wiper system "
        "refresh, dual horn boot, and glove box parts. Placed 2015-01-20, two days before the Jan 22 activator and hardware runs: "
        "the big reseal order that opens the Henderson assembly phase. Note line 1.4 and the kit headers carry 0.00 extensions (kit pricing); "
        "free glove box catalog line omitted from ledger.")},
    {"doc_id": "DOC-047", "type": "Retail invoice", "vendor_id": "VEN-12",
     "title": "McFadden-Dale Hardware invoice E46280/4: wiring supplies",
     "reference_numbers": {"invoice": "E46280/4"}, "date": "2015-02-02", "time": "1:08",
     "ship_to": "MAHAN/JAMES", "payment": "Bankcard x4772, signed James Mahan",
     "line_item_count": 9, "subtotal": 47.60, "tax": 3.86, "total": 51.46,
     "extraction_note": ("FIRST ELECTRICAL/WIRING WORK EVIDENCE (GAP-12 progress): five spools of primary wire (12ga and 16ga in yellow, "
        "white, blue, brown), 100 cable tie mounts, grommets, and stainless 1/4-20 hardware. No complete harness purchase documented anywhere, "
        "so wiring repairs/custom runs were done by hand in Feb 2015.")}
])

# ============ New ledger entries ============
def entry(eid, doc, ven, date, name, sku, qty, unit, ext, sys, notes=None, **kw):
    e = {"entry_id": eid, "doc_id": doc, "vendor_id": ven, "date": date,
         "item_name": name, "vendor_sku": sku, "qty": qty,
         "unit_price": unit, "ext_price": ext, "system_id": sys, "notes": notes}
    e.update(kw); return e

wcm = [
    ("P-146", "Body Restoration Set, All Ghias 65-69 (kit header)", "141-021C", 1, 73.70, 0.00, "SYS-08", "Kit header; components itemized below. Fitment 65-69 matches the car's year."),
    ("P-147", "Seals, Front Turn Indicator, Ghias 1965-69", "141-165B-L/R", 1, 12.05, 12.05, "SYS-08", None),
    ("P-148", "Seals, Tail Light, L&R, Ghia 1960-69", "141-177B-L/R", 1, 15.00, 15.00, "SYS-08", None),
    ("P-149", "Seals, Headlight Ring to Body", "141-191", 1, 4.75, 4.75, "SYS-08", None),
    ("P-150", "Seals, Fresh Air Vents (kit-priced)", "141-657A", 1, 3.50, 0.00, "SYS-08", "0.00 extension within kit. Same part bought separately in 2014 (P-119)."),
    ("P-151", "Seal, Decklid", "141-705A", 1, 16.50, 16.50, "SYS-08", None),
    ("P-152", "Seal, Front Hood", "141-705H", 1, 15.60, 15.60, "SYS-08", None),
    ("P-153", "Seal, License Light", "143-191L", 1, 6.30, 6.30, "SYS-08", None),
    ("P-154", "Plug, Rear Apron / Trunk Drain", "111-110", 1, 4.95, 4.95, "SYS-08", None),
    ("P-155", "Fuse Box, 8 Fuse, Bug/Ghia 1961-66", "111-037", 1, 29.95, 29.95, "SYS-10", "Electrical refresh: correct 8-fuse box for the year range."),
    ("P-156", "Cover, Fusebox 8 Fuse", "181-555A", 1, 5.45, 5.45, "SYS-10", None),
    ("P-157", "Seal, Rear Engine, Ghia 1956-66", "111-705A", 1, 8.95, 8.95, "SYS-08", None),
    ("P-158", "Seal, Firewall", "111-741G", 1, 8.25, 8.25, "SYS-08", None),
    ("P-159", "Emblem, Karmann Side Body Badge", "141-901", 1, 29.95, 29.95, "SYS-08", "The coachbuilder badge: exterior brightwork detail."),
    ("P-160", "Seals, Quarter Window Popout Kit, Ghia Sedan 60-71 (kit header)", "143-018A", 1, 84.30, 0.00, "SYS-08", "Kit header; components itemized below."),
    ("P-161", "Hinge Set, Quarter Window, 6 Plastic Pieces", "143-319-L/R", 1, 6.95, 6.95, "SYS-08", None),
    ("P-162", "Seals, Quarter Windows Non Pop-Out", "143-321B-L/R", 1, 44.95, 44.95, "SYS-08", "Kit covers both styles; which configuration the car runs can be confirmed from photos."),
    ("P-163", "Seals, Front Upright Quarter Window", "143-327-L/R", 1, 7.15, 7.15, "SYS-08", None),
    ("P-164", "Seal, Between Roof and Molding", "143-343-L/R", 1, 10.95, 10.95, "SYS-08", None),
    ("P-165", "Seals, Top Quarter Window Post", "143-348-L/R", 1, 6.95, 6.95, "SYS-08", None),
    ("P-166", "Seals, Bottom Quarter Window Post", "143-349-L/R", 1, 7.35, 7.35, "SYS-08", None),
    ("P-167", "Cover Boot, Positive Terminal on Generator", "113-901A", 1, 3.95, 3.95, "SYS-10", None),
    ("P-168", "Wiper Blades, L&R 11 inch, Ghia 56-69", "111-482-L/R", 1, 28.95, 28.95, "SYS-08", None),
    ("P-169", "Grommets, Wiper Shaft, Ghia 1958-69", "111-265AW", 1, 2.50, 2.50, "SYS-08", None),
    ("P-170", "Seal Caps, Wiper Shafts, White Plastic", "113-275", 1, 3.10, 3.10, "SYS-08", None),
    ("P-171", "Nozzle, Window Washer, w/Seal", "111-993", 1, 6.50, 6.50, "SYS-08", None),
    ("P-172", "Boot, Dual Horn, German, All Ghias 56-74", "141-231", 1, 38.95, 38.95, "SYS-08", "German-made horn boot (nose detail)."),
    ("P-173", "Glove Box Insert, Plastic", "143-101", 1, 24.95, 24.95, "SYS-09", None),
    ("P-174", "Rubber Stops, Glove Box or Gas Door", "111-145A", 1, 2.50, 2.50, "SYS-09", None),
]
for eid, name, sku, qty, unit, ext, sys, note in wcm:
    d['parts_ledger'].append(entry(eid, "DOC-046", "VEN-13", "2015-01-20", name, sku, qty, unit, ext, sys, note))

d['parts_ledger'].extend([
    entry("P-175", "DOC-047", "VEN-12", "2015-02-02", "Primary Wire Assortment (5 spools: 12ga yellow 12ft, 12ga white 12ft, 16ga white/blue/brown 28ft)",
          "DEK00486 / DEK00488 / DEK00472 / DEK00473 / DEK00476", 5, 5.80, 29.00, "SYS-10",
          "Hand-wiring evidence: multiple colors and gauges for circuit repairs or custom runs. No complete harness documented in archive."),
    entry("P-176", "DOC-047", "VEN-12", "2015-02-02", "Cable Tie Mounts, 3/4 inch Black (bag of 100)", "NELNAM750C", 1, 11.70, 11.70, "SYS-10", None),
    entry("P-177", "DOC-047", "VEN-12", "2015-02-02", "Grommets, 7/16 inch VL, 9 pc", "NOB1124D", 1, 3.00, 3.00, "SYS-10", "Wire pass-through grommets."),
    entry("P-178", "DOC-047", "VEN-12", "2015-02-02", "Stainless Hardware: 1/4-20 x 1/2 socket caps x15, 1/4 flat washers x15", "142012SHCSSS / 14FWSS", 1, None, 3.90, "SYS-12", None)
])

# ============ Spec/system updates ============
eng = d['build_spec_cards']['engine']
eng['dtm_kit_purchase'] = '2013-07-29, Raby Enterprises receipt #1878 (sales order #94), shipped to Hurricane UT'
d['build_spec_cards']['electrical'] = {
    "card_id": "SPEC-ELECTRICAL",
    "fuse_box": "8-fuse box with cover, correct for Bug/Ghia 1961-66 (WCM 111-037 + 181-555A, Jan 2015)",
    "wiring": "Hand-wiring work Feb 2015: 12ga and 16ga primary wire in four colors, cable tie mounts, grommets. No complete harness purchase documented.",
    "sources": ["DOC-046", "DOC-047"]
}

# ============ Timeline ============
d['restoration_timeline'].extend([
    {"date": "2013-07-29", "event": "RESTORATION BEGINS (earliest documented date): Type 4 DTM Stage III kit and conversion components purchased from Raby Enterprises, receipt #1878, shipped to Hurricane UT. Two weeks later the heads go to NV Automotive in Las Vegas", "doc_id": "DOC-001"},
    {"date": "2015-01-20", "event": "Body restoration seal set ordered from West Coast Metric ($364.45, 28 lines): full reseal including quarter window kit, fuse box, Karmann badge, wiper refresh. Opens the Henderson assembly phase", "doc_id": "DOC-046"},
    {"date": "2015-02-02", "event": "Wiring supplies from McFadden-Dale: primary wire in four colors, tie mounts, grommets. Hand-wiring work underway", "doc_id": "DOC-047"}
])
d['restoration_timeline'].sort(key=lambda e: (e['date'] is None, e['date'] or ''))

# ============ Gaps ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-02':
        g['status'] = 'RESOLVED (Batch 5)'
        g['resolution'] = 'Complete Raby receipt recovered: #1878, dated 2013-07-29, sales order #94, cashier Jake.'
    if g['gap_id'] == 'GAP-12':
        g['status'] = 'PARTIALLY RESOLVED (Batch 5)'
        g['resolution'] = 'Wiring work documented (DOC-047, Feb 2015): primary wire and supplies, but no complete harness. Tires remain undocumented.'

with open('/home/claude/ghia/ghia-1965-master-record-v5.json', 'w') as f:
    json.dump(d, f, indent=2)

print('v5 written')
print('documents:', len(d['document_archive']))
print('ledger entries:', len(d['parts_ledger']))
print('vendors:', len(d['vendor_registry']))
print('timeline events:', len(d['restoration_timeline']))
resolved = [g for g in d['data_gaps'] if 'RESOLVED' in g.get('status','') and 'PARTIALLY' not in g.get('status','') and 'SUBSTANTIALLY' not in g.get('status','')]
print('gaps: %d total, %d fully resolved' % (len(d['data_gaps']), len(resolved)))
spend = sum(e.get('ext_price') or 0 for e in d['parts_ledger'])
print('documented spend (priced entries): $%.2f' % spend)
dates = [e['date'] for e in d['parts_ledger'] if e.get('date')]
print('date range:', min(dates), 'to', max(dates))
