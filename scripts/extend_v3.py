import json

with open('/home/claude/ghia/ghia-1965-master-record-v2.json') as f:
    d = json.load(f)

d['schema_version'] = '1.2'
d['generated_from'] = 'Batches 1-3 (DOC-001 to DOC-035)'

# ============ MAJOR RESOLUTION: VEN-03 identified ============
for v in d['vendor_registry']:
    if v['vendor_id'] == 'VEN-03':
        v['name'] = 'NV Automotive (VW Automotive)'
        v['address'] = '4580 E. Lake Mead Blvd #104, Las Vegas, NV 89115'
        v['phones'] = {'main': '702-438-4689', 'fax': '702-531-1241'}
        v['email'] = 'nvautomotive@vw.lvcoxmail.com'
        v['contact'] = 'Bill Shapley'
        v['specialty'] = 'Quality VW racing engines and transaxles. Performed the Type 4 head machine work and supplied Weber carb kits.'
        v.pop('data_gap', None)
        v['resolution_note'] = 'Identified in Batch 3 via complete photo of invoice 125 (fax number matched the cropped fragment on the original DOC-003 photo) and a second invoice (100) from 2018.'
        v['documents'] = ['DOC-003', 'DOC-034']

# ============ DOC-003 completed ============
for doc in d['document_archive']:
    if doc['doc_id'] == 'DOC-003':
        doc['title'] = 'NV Automotive invoice #125: Type 4 cylinder head machine work'
        doc['reference_numbers'] = {'invoice': '125', 'customer_id': '123'}
        doc['date'] = '2013-08-13'
        doc['subtotal'] = 375.95
        doc['tax'] = 3.72
        doc['total'] = 379.67
        doc['payment'] = 'Cash; $200.00 deposit noted, marked PD CASH'
        doc['extraction_note'] = ('Batch 3 supplied the complete photo of this invoice, resolving the cropped Batch 1 version. '
            'Line pricing: valve job 165.00, open heads for 94mm 60.00, spark plug inserts 45.00, cc and cut .050 60.00, '
            'rocker spacer kit 45.95 (taxed). CRITICAL DATE FINDING: head work performed 2013-08-13, meaning the engine '
            'build began roughly 18 months before the 2015 receipt cluster.')
    if doc['doc_id'] == 'DOC-005':
        doc['duplicate_note'] = 'Complete flat re-photo received in Batch 3; matched on order 944952A, confirmed all line data. Not re-entered.'
    if doc['doc_id'] == 'DOC-006':
        doc['duplicate_note'] = 'Complete flat re-photo received in Batch 3; matched on order 944952C. Not re-entered.'

# Update machine-work ledger entries with date and prices
svc_prices = {'S-001': 165.00, 'S-002': 60.00, 'S-003': 45.00, 'S-004': 60.00, 'S-005': 45.95}
for e in d['parts_ledger']:
    if e['entry_id'] in svc_prices:
        e['date'] = '2013-08-13'
        e['unit_price'] = svc_prices[e['entry_id']]
        e['ext_price'] = svc_prices[e['entry_id']]
    if e['entry_id'] == 'S-006':
        e['date'] = '2013-08-13'

# ============ New vendors ============
d['vendor_registry'].extend([
    {"vendor_id": "VEN-09", "name": "Mid America Motorworks", "address": "17082 N. US Hwy 45, Effingham, IL 62401",
     "specialty": "VW and Corvette restoration catalog house", "customer_number": "23552403-000",
     "documents": ["DOC-028", "DOC-033"]},
    {"vendor_id": "VEN-10", "name": "Butch's Speed Shop", "address": "4477 Reno Ave, Las Vegas, NV 89118",
     "phones": {"main": "702-247-1277", "fax": "702-247-1167"}, "specialty": "Speed shop, offroading since 1968",
     "customer_number": "2009", "documents": ["DOC-030"]},
    {"vendor_id": "VEN-11", "name": "Drake Automotive Group (Scott Drake)", "address": "130 Cassia Way, Henderson, NV 89014",
     "phones": {"main": "800-999-0289", "fax": "702-853-2062"}, "specialty": "Restoration parts manufacturer; local will-call",
     "documents": ["DOC-031"]},
    {"vendor_id": "VEN-12", "name": "McFadden-Dale Industrial Hardware", "address": "5580 S Decatur Blvd, Suite 114, Las Vegas, NV 89118",
     "phones": {"main": "702-251-8059"}, "specialty": "Industrial fastener and hardware supply",
     "documents": ["DOC-035"]}
])

# ============ New documents ============
d['document_archive'].extend([
    {"doc_id": "DOC-025", "type": "Invoice (counter)", "vendor_id": "VEN-08",
     "title": "Meyers Auto Parts invoice 092252: EMPI master cylinder and axle boots",
     "reference_numbers": {"invoice": "092252"}, "date": "2016-04-23", "time": "2:48 PM",
     "payment": "Debit 47.45", "line_item_count": 2, "subtotal": 43.87, "tax": 3.58, "total": 47.45,
     "extraction_note": "Counter catalog line printed on receipt: '75 Volkswagen Type1: BTL, GHIA, THING 4-1600 aircooled' confirming Ghia-family fitment lookup."},
    {"doc_id": "DOC-026", "type": "Invoice (counter)", "vendor_id": "VEN-07",
     "title": "Boulder Auto Parts invoice L245733: 3M refinish tape",
     "reference_numbers": {"invoice": "L245733", "customer": "B4925"}, "date": "2015-05-04", "time": "01:25 PM",
     "line_item_count": 1, "total": 4.37},
    {"doc_id": "DOC-027", "type": "Invoice (counter)", "vendor_id": "VEN-07",
     "title": "Boulder Auto Parts invoice L245734: Permatex weatherstrip adhesive",
     "reference_numbers": {"invoice": "L245734", "customer": "B4925"}, "date": "2015-05-04", "time": "01:27 PM",
     "line_item_count": 1, "total": 2.98,
     "extraction_note": "Sequential invoice two minutes after DOC-026, same visit. Both are body-finishing materials."},
    {"doc_id": "DOC-028", "type": "Mail order invoice", "vendor_id": "VEN-09",
     "title": "Mid America Motorworks order 04684493: chrome lug bolt set",
     "reference_numbers": {"order": "04684493-00001"}, "date": "2015-04-27",
     "ship_to": "James Mahan, 678 Covina Dr, Henderson NV", "line_item_count": 1, "total": 44.99,
     "extraction_note": "First Wheels/Tires system document. Includes merchandise return form (unused)."},
    {"doc_id": "DOC-029", "type": "Retail receipt", "vendor_id": "VEN-05",
     "title": "O'Reilly Auto Parts receipt, invoice 2655-494664",
     "reference_numbers": {"invoice": "2655-494664"}, "date": "2015-03-12",
     "line_item_count": 2, "subtotal": 14.18, "tax": 1.15, "total": 15.33},
    {"doc_id": "DOC-030", "type": "Invoice (counter)", "vendor_id": "VEN-10",
     "title": "Butch's Speed Shop invoice 120445: temp sender and Bosch W8DC plugs",
     "reference_numbers": {"invoice": "120445", "sales_order": "65638"}, "date": "2015-05-21", "time": "11:21 AM",
     "payment": "Cash 40.00, change 10.43", "line_item_count": 2, "subtotal": 27.35, "tax": 2.22, "total": 29.57,
     "extraction_note": "Billed to 'martin Mahan' rather than James Mahan. Likely family member or counter-entry variant; items are squarely Type 4 relevant (W8DC is a correct aircooled VW plug). Counter person: Gavin."},
    {"doc_id": "DOC-031", "type": "Invoice (will call)", "vendor_id": "VEN-11",
     "title": "Drake Automotive invoice 832844: Silver Magic insulating sheets",
     "reference_numbers": {"invoice": "832844", "order": "445493"}, "date": "2014-12-22",
     "payment": "Handwritten: Pd Cash 12/22/14", "line_item_count": 1, "subtotal": 71.50, "tax": 5.79, "total": 77.29,
     "extraction_note": "ATTRIBUTION FLAG: billed/shipped to 'Bill Wilson, NV', not Mahan, though retained in the Ghia folder. Insulating sheets fit the interior restoration. Earliest parts-purchase date in the archive (Dec 2014). See GAP-18."},
    {"doc_id": "DOC-032", "type": "Invoice (backorder fulfillment)", "vendor_id": "VEN-04",
     "title": "California Pacific/JBugs Order #944952B: door panels and headliner ship",
     "reference_numbers": {"order": "944952B"}, "date": "2016-03-24",
     "ship_via": "FedEx Ground (shipped 03-23-16)", "total_weight_lbs": 13.1, "packages": 2,
     "line_item_count": 3, "invoice_total": 171.00,
     "extraction_note": "The missing middle shipment of the JBugs interior order. Resolves the door panel (P-034) and headliner (P-035) backorders from DOC-005. Seat upholstery still backordered here, fulfilled two days later on 944952C (DOC-006). Opening balance -198.00 consumed; -27.00 credit card refund issued then recharged on 944952C. The A/B/C money trail now fully reconciles."},
    {"doc_id": "DOC-033", "type": "Mail order invoice", "vendor_id": "VEN-09",
     "title": "Mid America Motorworks order 04740418: oil temperature sender",
     "reference_numbers": {"order": "04740418-00001"}, "date": "2015-12-30",
     "line_item_count": 1, "subtotal": 18.99, "shipping": 7.99, "total": 26.98},
    {"doc_id": "DOC-034", "type": "Invoice", "vendor_id": "VEN-03",
     "title": "NV Automotive invoice #100: Weber carburetor rebuild kits",
     "reference_numbers": {"invoice": "100"}, "date": "2018-05-31",
     "line_item_count": 1, "subtotal": 59.90, "tax": 4.88, "total": 64.78,
     "extraction_note": "NEW LATEST DATE in archive: extends documented activity to May 2018. Two Weber carb rebuild kits confirm the dual Weber setup in service and being maintained. Same shop (Bill Shapley) that did the 2013 head work, indicating an ongoing relationship across the build's life."},
    {"doc_id": "DOC-035", "type": "Retail invoice", "vendor_id": "VEN-12",
     "title": "McFadden-Dale Hardware invoice G11416/4: trim screws",
     "reference_numbers": {"invoice": "G11416/4"}, "date": "2016-05-10", "time": "10:23",
     "payment": "Cash", "line_item_count": 2, "subtotal": 2.48, "tax": 0.20, "total": 2.68,
     "extraction_note": "Oval-head #6 sheet metal screws are classic interior trim/door panel fasteners. Timing (May 2016) aligns with interior installation right after the JBugs kit fully arrived."}
])

# ============ New ledger entries ============
def entry(eid, doc, ven, date, name, sku, qty, unit, ext, sys, notes=None, **kw):
    e = {"entry_id": eid, "doc_id": doc, "vendor_id": ven, "date": date,
         "item_name": name, "vendor_sku": sku, "qty": qty,
         "unit_price": unit, "ext_price": ext, "system_id": sys, "notes": notes}
    e.update(kw); return e

d['parts_ledger'].extend([
    entry("P-079", "DOC-025", "VEN-08", "2016-04-23", "Buggy Master Cylinder w/ Reservoir (EMPI)", "EM 00-6112-0",
          1, 29.89, 29.89, "SYS-07",
          "SECOND master cylinder in the archive (TRW unit purchased Jan 2015, P-019). Reconcile which is installed: replacement, upgrade, or the TRW didn't fit as hoped despite 'customer says it will fit.'", list_price=53.00),
    entry("P-080", "DOC-025", "VEN-08", "2016-04-23", "Axle Boot & Kit (EMPI), Type 1/Ghia/Thing", "EM 00-9916-0",
          2, 6.99, 13.98, "SYS-05", "Swing/IRS axle boots, pair.", list_price=12.50),
    entry("P-081", "DOC-026", "VEN-07", "2015-05-04", "Refinish Masking Tape, 1/4 inch (3M)", "MMM 26344",
          1, 4.04, 4.04, "SYS-08", "Fine-line masking tape, body refinish supply.", list_price=4.88),
    entry("P-082", "DOC-027", "VEN-07", "2015-05-04", "Super Weatherstrip Adhesive (Permatex)", "PER 80638",
          1, 2.76, 2.76, "SYS-08", "For body seal installation. May 2015 = seals going on after paint.", list_price=5.59),
    entry("P-083", "DOC-028", "VEN-09", "2015-04-27", "Lug Bolt Set, 16 pc Chrome, 14mm", "319-994",
          1, 44.99, 44.99, "SYS-11",
          "First Wheels/Tires entry. 16 bolts = 4 wheels x 4 lugs; chrome 14mm lug bolts strongly imply aftermarket wheels. Identify wheels from photos (GAP-17)."),
    entry("P-084", "DOC-029", "VEN-05", "2015-03-12", "J-B Weld, 2oz", "JBW 8272",
          1, 7.49, 7.49, "SYS-12", None, list_price=12.69),
    entry("P-085", "DOC-029", "VEN-05", "2015-03-12", "Brake Fluid, 32oz", "ORC 72120",
          1, 6.69, 6.69, "SYS-07", "Large-format fluid two weeks after the 12oz can (P-072): full system bleed of the new disc setup.", list_price=11.34),
    entry("P-086", "DOC-030", "VEN-10", "2015-05-21", "Electrical Temp Sender, Short Sweep (Auto Meter)", "AM 2258",
          1, 16.99, 16.99, "SYS-10",
          "Auto Meter 2258 sender. Combined with the oil temp sender (P-091), confirms aftermarket gauge instrumentation.", list_price=17.99),
    entry("P-087", "DOC-030", "VEN-10", "2015-05-21", "Spark Plugs, Bosch W8DC", "BOSC W8DC",
          4, 2.59, 10.36, "SYS-01",
          "DOCUMENTS THE PLUG SPEC: Bosch W8DC x4, a correct heat range for the aircooled Type 4. Recorded on engine spec card.", list_price=3.99),
    entry("P-088", "DOC-031", "VEN-11", "2014-12-22", "Silver Magic Insulating Sheets, Kit", "UL-SM",
          1, 71.50, 71.50, "SYS-09",
          "Under-carpet heat/sound insulation kit. ATTRIBUTION UNCERTAIN: invoice billed to Bill Wilson, NV (see DOC-031, GAP-18). Earliest dated parts purchase in archive.", attribution="uncertain"),
    entry("P-089", "DOC-032", "VEN-04", "2016-03-24", "Door Panel, Ghia, 12 inch Insert, 56-61 style (backorder ship)", "14-1522-CUST",
          1, 110.00, 99.00, "SYS-09", "Fulfills P-034 backorder from DOC-005.", discount_pct=10),
    entry("P-090", "DOC-032", "VEN-04", "2016-03-24", "Headliner, Grey Velour #56 (backorder ship)", "20-1510-V 56",
          1, 80.00, 72.00, "SYS-09", "Fulfills P-035 backorder from DOC-005.", discount_pct=10),
    entry("P-091", "DOC-033", "VEN-09", "2015-12-30", "Oil Temperature Sender, 300 degree", "196-107",
          1, 18.99, 18.99, "SYS-10", "Alt# V3-2305-5 (VDO-pattern). Aftermarket oil temp gauge sender, essential instrumentation on a performance aircooled engine."),
    entry("P-092", "DOC-034", "VEN-03", "2018-05-31", "Weber Carburetor Rebuild Kits", "(none, shop line item)",
          2, 29.95, 59.90, "SYS-03",
          "Confirms dual Webers in service and maintained as of May 2018. Latest dated purchase in archive."),
    entry("P-093", "DOC-035", "VEN-12", "2016-05-10", "Sheet Metal Screws, #4 x 5/8 Pan Phillips Zinc", "458PHSMS",
          12, 0.04, 0.48, "SYS-09", None),
    entry("P-094", "DOC-035", "VEN-12", "2016-05-10", "Sheet Metal Screws, #6 x 1/2 Oval Phillips Zinc", "612OHSMS",
          40, 0.05, 2.00, "SYS-09", "Oval-head trim screws, classic door panel/interior trim fastener; interior install evidence May 2016.")
])

# ============ Spec card updates ============
eng = d['build_spec_cards']['engine']
eng['spark_plugs'] = 'Bosch W8DC (4 purchased 2015-05-21, Butch\'s Speed Shop)'
eng['head_work_date'] = '2013-08-13, NV Automotive (Bill Shapley), Las Vegas, invoice 125, $379.67'
eng['sources'] = sorted(set(eng['sources'] + ['DOC-030']))
d['build_spec_cards']['instrumentation'] = {
    "card_id": "SPEC-INSTRUMENTATION",
    "gauges": "Aftermarket gauge senders documented: Auto Meter 2258 electric temp sender short sweep (2015-05-21) and 300-degree oil temperature sender, alt# V3-2305-5 (2015-12-30). Gauge heads themselves not yet documented; identify from dash photos.",
    "sources": ["DOC-030", "DOC-033"]
}
d['build_spec_cards']['wheels_tires'] = {
    "card_id": "SPEC-WHEELS",
    "lug_hardware": "16 pc chrome 14mm lug bolt set (Mid America Motorworks 319-994, 2015-04-27), implying aftermarket 4-lug wheels",
    "wheels": "Unknown, identify from photos (GAP-17)",
    "sources": ["DOC-028"]
}
fuel_note = d['build_spec_cards']['engine'].get('carburetion', '')
d['build_spec_cards']['engine']['carburetion'] = fuel_note + '. Dual Weber setup confirmed in continued service via 2x rebuild kits purchased 2018-05-31 (NV Automotive).'

# ============ Timeline ============
d['restoration_timeline'].extend([
    {"date": "2013-08-13", "event": "ENGINE BUILD BEGINS: Type 4 head machine work at NV Automotive (Bill Shapley), Las Vegas. Valve job, 94mm openings, .050 cut, 8.6:1 target. $379.67, $200 deposit. Earliest documented work, ~18 months before the 2015 receipt cluster", "doc_id": "DOC-003"},
    {"date": "2014-12-22", "event": "Silver Magic insulating sheets, Drake Automotive will-call (billed to Bill Wilson, attribution open)", "doc_id": "DOC-031"},
    {"date": "2015-03-12", "event": "J-B Weld and 32oz brake fluid (full brake system bleed)", "doc_id": "DOC-029"},
    {"date": "2015-04-27", "event": "Chrome 14mm lug bolt set from Mid America Motorworks: aftermarket wheels going on", "doc_id": "DOC-028"},
    {"date": "2015-05-04", "event": "Body finishing materials: 3M refinish tape and Permatex weatherstrip adhesive, Boulder Auto Parts, same visit", "doc_id": "DOC-026, DOC-027"},
    {"date": "2015-05-21", "event": "Auto Meter temp sender and Bosch W8DC plugs x4, Butch's Speed Shop", "doc_id": "DOC-030"},
    {"date": "2015-12-30", "event": "300-degree oil temperature sender ordered from Mid America Motorworks", "doc_id": "DOC-033"},
    {"date": "2016-03-24", "event": "JBugs backorder B ships: custom door panels and grey velour headliner (resolves DOC-005 backorders)", "doc_id": "DOC-032"},
    {"date": "2016-04-23", "event": "EMPI master cylinder w/reservoir and axle boot kits, Meyers Auto Parts", "doc_id": "DOC-025"},
    {"date": "2016-05-10", "event": "Interior trim screws from McFadden-Dale: interior installation underway", "doc_id": "DOC-035"},
    {"date": "2018-05-31", "event": "Two Weber carb rebuild kits from NV Automotive. NEW LATEST DATE: documented activity now spans Aug 2013 to May 2018", "doc_id": "DOC-034"}
])
d['restoration_timeline'].sort(key=lambda e: (e['date'] is None, e['date'] or ''))

# ============ Gaps ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-03':
        g['status'] = 'RESOLVED (Batch 3)'
        g['resolution'] = 'Machine shop identified as NV Automotive, 4580 E. Lake Mead Blvd #104, Las Vegas (Bill Shapley). Complete invoice 125 dated 2013-08-13, total $379.67.'
d['data_gaps'].extend([
    {"gap_id": "GAP-17", "priority": "medium", "item": "Identify aftermarket wheels (implied by 16pc chrome 14mm lug bolt purchase). Use car photos; record wheel make/model/size and tire spec."},
    {"gap_id": "GAP-18", "priority": "medium", "item": "Attribution: Drake insulating sheets invoice (DOC-031) billed to 'Bill Wilson, NV'. Determine whether Wilson was a helper/friend purchasing for the Ghia or this document belongs to another project."},
    {"gap_id": "GAP-19", "priority": "medium", "item": "Two master cylinders documented (TRW Jan 2015, EMPI buggy m/c Apr 2016). Determine which is installed and why the second was purchased."},
    {"gap_id": "GAP-20", "priority": "low", "item": "Identify gauge heads (Auto Meter? VDO?) matching the two documented senders; photograph dash cluster."}
])

with open('/home/claude/ghia/ghia-1965-master-record-v3.json', 'w') as f:
    json.dump(d, f, indent=2)

print('v3 written')
print('documents:', len(d['document_archive']))
print('ledger entries:', len(d['parts_ledger']))
print('vendors:', len(d['vendor_registry']))
print('timeline events:', len(d['restoration_timeline']))
gaps_open = [g for g in d['data_gaps'] if 'RESOLVED' not in g.get('status','')]
print('gaps: %d total, %d open' % (len(d['data_gaps']), len(gaps_open)))
spend = sum(e.get('ext_price') or 0 for e in d['parts_ledger'])
print('documented spend (priced entries): $%.2f' % spend)
dates = [e['date'] for e in d['parts_ledger'] if e.get('date')]
print('date range:', min(dates), 'to', max(dates))
