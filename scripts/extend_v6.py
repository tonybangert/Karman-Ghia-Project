import json

with open('data/versions/ghia-1965-master-record-v5.json') as f:
    d = json.load(f)

d['schema_version'] = '1.5'
d['generated_date'] = '2026-06-11'
d['generated_from'] = 'Batches 1-6 (DOC-001 to DOC-053)'

# ============ New vendors ============
d['vendor_registry'].extend([
    {"vendor_id": "VEN-16", "name": "Nevada Offroad Buggy",
     "address": "3054 S. Valley View #130, Las Vegas, NV 89102",
     "phones": {"main": "702-871-4911", "fax": "702-871-5221", "toll_free": "888-755-5900"},
     "specialty": "Offroad buggy and aircooled VW parts counter",
     "documents": ["DOC-048"]},
    {"vendor_id": "VEN-17", "name": "American Polishing & Plating (DBA Shine Shop)",
     "address": "676 Middlegate Rd, Henderson, NV 89011",
     "phones": {"main": "702-566-1299", "alt": "702-307-4552"},
     "web": "www.chromeforu.biz",
     "specialty": "Chrome plating and metal polishing",
     "documents": ["DOC-050", "DOC-051"]},
])

# ============ New documents ============
d['document_archive'].extend([
    {"doc_id": "DOC-048", "type": "Retail invoice", "vendor_id": "VEN-16",
     "title": "Nevada Offroad Buggy invoice 89595: Dzus fasteners and clutch hook shaft",
     "reference_numbers": {"invoice": "89595"},
     "date": "2015-01-14", "time": "1:10 PM", "payment": "Cash sale ($100 tendered, $67.15 change)",
     "line_item_count": 3, "subtotal": 30.39, "tax": 2.46, "total": 32.85,
     "extraction_note": ("Cash counter sale at a Las Vegas buggy/aircooled VW shop. Six Dzus quarter-turn buttons (AO6550) "
        "with six spring tabs, plus one clutch hook shaft. Dated 2015-01-14, six days BEFORE the West Coast Metric reseal "
        "order (DOC-046): this is now the earliest documented purchase of the Henderson assembly phase.")},
    {"doc_id": "DOC-049", "type": "Mail order invoice", "vendor_id": "VEN-09",
     "title": "Mid America Motorworks order 04682256-00002: Sprintstar center caps (wheels identified)",
     "reference_numbers": {"order": "04682256-00002", "customer": "23552403-000"},
     "date": "2015-04-28", "ship_to": "James Mahan, 678 Covina Dr, Henderson NV 89002-8267",
     "line_item_count": 1, "backordered_line_count": 2, "subtotal": 25.98, "shipping": 0.00, "total": 25.98,
     "extraction_note": ("HEADLINE: 'CENTER CAP, FOR SPRINTSTAR' (319-655, alt# 00-9707-0) identifies the aftermarket "
        "wheels as Sprintstars (EMPI-pattern 5-spoke), substantially resolving GAP-17 and corroborating the 16pc chrome "
        "14mm lug bolt set bought 2015-04-27 on separate order 04684493 (DOC-028). This invoice is shipment -00002 of "
        "order 04682256: two caps shipped here; two more caps plus a 111157 3/8in resistance-type temperature sender "
        "remain on back order. Shipment -00001 of this order and the backorder fulfillment are not in the archive "
        "(GAP-22). Includes unused merchandise return form.")},
    {"doc_id": "DOC-050", "type": "Handwritten counter receipt", "vendor_id": "VEN-17",
     "title": "American Polishing & Plating: re-chrome two 3-piece bumpers, $350",
     "reference_numbers": {},
     "date": "2016-06-22", "customer": "James, phone 702-351-1031",
     "line_item_count": 1, "total": 350.00,
     "payment": "$300 deposit, ~$50 balance, circled 'Paid'",
     "extraction_note": ("Handwritten ticket, no invoice number. Reads: qty 2, '3 piece Bumper', $350.00, with 'deposit "
        "$300' and the balance line circled 'Paid'. '2wks' written at the top corner, read as the quoted turnaround. "
        "Ghia bumpers are three pieces each (center blade plus two ends), so this is both bumpers out for re-plating "
        "during the summer 2016 exterior brightwork phase (KGPR side moldings followed on 2016-08-17, DOC-041). "
        "Customer phone 702-351-1031 appears on both Shine Shop tickets.")},
    {"doc_id": "DOC-051", "type": "Handwritten counter receipt", "vendor_id": "VEN-17",
     "title": "American Polishing & Plating: two bumper pieces redone, no charge",
     "reference_numbers": {},
     "date": "2016-09-06", "customer": "James, phone 702-351-1031",
     "line_item_count": 1, "total": 0.00,
     "extraction_note": ("Handwritten ticket. Reads: qty 2, 'bump. pcs.' with 'Redo N/C' written large across the "
        "lines (handwriting interpretation; N/C = no charge). Two pieces of the DOC-050 bumper job were re-plated "
        "at no cost roughly ten weeks after the original ticket. The chrome mounting hardware purchase the next "
        "day (DOC-052) suggests this pickup put the bumpers back on the car.")},
    {"doc_id": "DOC-052", "type": "Retail invoice", "vendor_id": "VEN-12",
     "title": "McFadden-Dale Hardware invoice G52517/4: chrome bumper mounting hardware (mixed receipt)",
     "reference_numbers": {"invoice": "G52517/4"},
     "date": "2016-09-07", "time": "9:55", "clerk": "JOHNK", "terminal": "593",
     "ship_to": "MAHAN/JAMES O", "payment": "Bankcard x0115, signed James Mahan",
     "line_item_count": 9, "subtotal": 98.01, "tax": 7.99, "total": 106.00,
     "extraction_note": ("Purchased the DAY AFTER the bumper redo pickup (DOC-051): eight each of 5/16-18 x 3/4 chrome "
        "carriage bolts, chrome USS flat washers, chrome lock washers, and chrome hex nuts, the classic Ghia "
        "bumper-blade-to-bracket fastener set in show finish. MIXED RECEIPT: also carries clearly non-vehicle household "
        "lines omitted from the ledger per the GAP-16 convention: weed control concentrate 32oz ($13.30), 13-3/4in SS "
        "trowel ($6.40), and Seymour green rebar epoxy coating ($11.40), $31.10 of the $98.01 subtotal. Two further "
        "lines (2X gloss dark gray spray x2, FiberFix repair wrap) are plausibly project-related and are entered with "
        "attribution flags.")},
    {"doc_id": "DOC-053", "type": "Retail invoice", "vendor_id": "VEN-12",
     "title": "McFadden-Dale Hardware invoice G59126/4: small hardware run",
     "reference_numbers": {"invoice": "G59126/4"},
     "date": "2016-09-26", "time": "9:50", "clerk": "DP", "terminal": "594",
     "payment": "Cash ($20.00 tendered, $17.32 change)",
     "line_item_count": 5, "subtotal": 2.48, "tax": 0.20, "total": 2.68,
     "extraction_note": ("Tiny cash follow-up run three weeks after the bumper hardware purchase: stainless 1/4-20 "
        "socket caps, pan-head sheet metal screws, 10-24 nickel cap (acorn) nuts with matching hex nuts, and 3/16 x 1 "
        "carriage bolts. Nickel cap nuts typically finish exposed trim or license plate studs; not asserted. Same "
        "1/4-20 stainless socket-cap SKU family as DOC-047 (Feb 2015).")},
])

# ============ Housekeeping: vendor document arrays had drifted ============
# The documents arrays on several vendors were set at vendor creation and not
# maintained by later batches. Re-sync by appending every document actually
# issued by the vendor (vendor_id match on the document record). Existing
# entries are kept even when the document was issued by another vendor:
# VEN-06 (Steve Hansen) keeps DOC-004 and VEN-15 (Washington County Collision)
# keeps DOC-044 because those are intentional named-on-document associations.
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
    # DOC-048: Nevada Offroad Buggy
    entry("P-179", "DOC-048", "VEN-16", "2015-01-14",
          "Dzus Button AO6550 (quarter-turn fastener)", "2036", 6, 1.51, 9.06, "SYS-12",
          "Six quarter-turn buttons with the six spring tabs in P-180: a removable-panel fastener set, commonly engine tin or under-dash panels on aircooled VWs. Installed location not documented."),
    entry("P-180", "DOC-048", "VEN-16", "2015-01-14",
          "Dzus Tab with Spring", "2093", 6, 1.89, 11.34, "SYS-12",
          "Spring tabs mating to the P-179 buttons."),
    entry("P-181", "DOC-048", "VEN-16", "2015-01-14",
          "Clutch Hook Shaft", "1328", 1, 9.99, 9.99, "SYS-05",
          "Buggy-shop catalog item: hook end of the clutch cable linkage (pedal-side hook shaft on Type 1 pattern). First clutch linkage part in the archive."),
    # DOC-049: Mid America Motorworks
    entry("P-182", "DOC-049", "VEN-09", "2015-04-28",
          "Center Cap, for Sprintstar Wheel", "319-655", 2, 12.99, 25.98, "SYS-11",
          "Alt# 00-9707-0 (EMPI pattern). IDENTIFIES THE WHEELS: Sprintstar 5-spokes, substantially resolving GAP-17 and matching the 16pc chrome 14mm lug bolt set (P-083). Two of four caps; the other two backordered (P-183)."),
    entry("P-183", "DOC-049", "VEN-09", "2015-04-28",
          "Center Cap, for Sprintstar Wheel (backordered)", "319-655", 2, 12.99, 0.00, "SYS-11",
          "Backorder at 0.00 per convention; fulfillment document not in the archive (GAP-22)."),
    entry("P-184", "DOC-049", "VEN-09", "2015-04-28",
          "Temperature Sender, 3/8in Resistance Type (backordered)", "111157", 1, 29.99, 0.00, "SYS-10",
          "Backorder at 0.00; fulfillment undocumented (GAP-22). THIRD documented gauge sender, alongside the Auto Meter 2258 electric temp sender (P-086, bought three weeks later) and the 300-degree oil temp sender (P-091, Dec 2015). The May purchase of the Auto Meter sender may have substituted for this backordered unit; not asserted."),
    # DOC-050 / DOC-051: American Polishing & Plating
    entry("S-007", "DOC-050", "VEN-17", "2016-06-22",
          "Chrome plating service: two 3-piece bumpers", None, 2, 175.00, 350.00, "SYS-08",
          "Front and rear bumpers re-chromed, $350 flat ($300 deposit, balance circled 'Paid'), quoted two-week turnaround. Unit price shown as the per-bumper half of the flat job price.",
          entry_type="service"),
    entry("S-008", "DOC-051", "VEN-17", "2016-09-06",
          "Re-plate two bumper pieces, no charge", None, 2, 0.00, 0.00, "SYS-08",
          "Handwritten 'Redo N/C': two pieces of the S-007 job redone at no cost, picked up ~10 weeks after drop-off. Which two pieces were redone is not recorded.",
          entry_type="no_charge_rework"),
    # DOC-052: McFadden-Dale chrome bumper hardware (consolidated per small-hardware convention)
    entry("P-185", "DOC-052", "VEN-12", "2016-09-07",
          "Chrome Bumper Mounting Hardware: 5/16-18 x 3/4 carriage bolts x8, 5/16 USS flat washers x8, 5/16 lock washers x8, 5/16-18 hex nuts x8",
          "5161834CARRCH / 516FWCH / 516LWCH / 51618NUTCH", 1, None, 41.92, "SYS-12",
          "All chrome finish, bought the day after the bumper re-plate pickup (DOC-051): the bumper-blade-to-bracket carriage bolt set for the freshly chromed bumpers. 8 positions covers both bumpers."),
    entry("P-186", "DOC-052", "VEN-12", "2016-09-07",
          "Rust-Oleum 2X Gloss Dark Gray Spray", "4039426", 2, 4.50, 9.00, "SYS-12",
          "On the mixed household/project receipt; plausibly chassis or bracket touch-up but use unconfirmed.",
          attribution="uncertain"),
    entry("P-187", "DOC-052", "VEN-12", "2016-09-07",
          "FiberFix Repair Wrap, 2in x 50in, 2-pack", "FIB00429", 1, 15.99, 15.99, "SYS-12",
          "Fiberglass repair wrap on the mixed receipt; plausibly shop supply, use unconfirmed.",
          attribution="uncertain"),
    # DOC-053: McFadden-Dale small hardware (consolidated)
    entry("P-188", "DOC-053", "VEN-12", "2016-09-26",
          "Small Hardware: 1/4-20 x 5/8 SS socket caps x4, 10 x 5/8 pan phillips SMS x2, 10-24 nickel cap nuts x4, 10-24 hex nuts x4, 3/16 x 1 carriage bolts x4",
          "142058SHCSSS / 1058PHSMS / 1024CAP / 1024NUT / B3161CARR", 1, None, 2.48, "SYS-12",
          "Cash micro-run; nickel cap (acorn) nuts suggest exposed trim or license plate studs, not asserted."),
])

# ============ Timeline events (inserted in date order) ============
new_events = [
    {"date": "2015-01-14", "event": "Dzus quarter-turn fasteners and clutch hook shaft from Nevada Offroad Buggy, Las Vegas: earliest documented purchase of the Henderson assembly phase, six days before the West Coast Metric reseal order", "doc_id": "DOC-048"},
    {"date": "2015-04-28", "event": "Sprintstar center caps ship from Mid America (2 of 4; 2 caps and a temp sender on backorder): WHEELS IDENTIFIED as Sprintstars (GAP-17)", "doc_id": "DOC-049"},
    {"date": "2016-06-22", "event": "Both bumpers (3-piece each) dropped at American Polishing & Plating, Henderson, for re-chroming: $350, two-week quote. Exterior brightwork phase underway", "doc_id": "DOC-050"},
    {"date": "2016-09-06", "event": "Two bumper pieces redone at no charge by the plating shop", "doc_id": "DOC-051"},
    {"date": "2016-09-07", "event": "Chrome bumper mounting hardware (5/16-18 carriage bolts, washers, nuts, 8 each) from McFadden-Dale, the day after the plating redo: bumpers going back on", "doc_id": "DOC-052"},
    {"date": "2016-09-26", "event": "Small hardware cash run at McFadden-Dale: nickel cap nuts, stainless socket caps, carriage bolts. New latest 2016 date; documented activity now continuous Jan 2015 to Sep 2016", "doc_id": "DOC-053"},
]
tl = d['restoration_timeline']
for ev in new_events:
    idx = next((i for i, e in enumerate(tl) if e.get('date') is None or e['date'] > ev['date']), len(tl))
    tl.insert(idx, ev)

# ============ Build spec cards ============
d['build_spec_cards']['wheels_tires'] = {
    "card_id": "SPEC-WHEELS-TIRES",
    "wheels": ("Aftermarket Sprintstar 5-spokes (EMPI pattern), four wheels: identified by the 4x 319-655 center caps "
               "(alt# 00-9707-0) ordered spring 2015, corroborated by the 16pc chrome 14mm lug bolt set (319-994, "
               "2015-04-27). Wheel size and finish not yet documented; confirm from photos."),
    "lug_hardware": "Chrome 14mm lug bolts, 16 pieces (4 lugs x 4 wheels)",
    "tires": "Undocumented (GAP-12); record brand/size from the car",
    "sources": ["DOC-028", "DOC-049"]
}
# The rendered SPEC-SHEET.md carried Wheels Tires, Body Paint, and Electrical
# cards that were never written into the JSON (docs drifted ahead of the data
# in earlier batches). Backfill body_paint and electrical into the JSON so the
# master record is truly canonical, and extend body_paint with the Batch 6
# bumper re-chrome story.
d['build_spec_cards']['body_paint'] = {
    "card_id": "SPEC-BODY-PAINT",
    "body_prep": ("Per restorer's cost ledger (DOC-043): media blast, Bondo and Dolphin Glaze finishing, fiberglass "
                  "repair, replacement nose/fender/hood panels, multiple primer stages."),
    "body_shop": "Washington County Collision, Hurricane UT (named purchaser on the June 2014 paint receipt)",
    "paint_system_2014": ("Auto Paints Plus, 2014-06-19: epoxy primer/sealer, mixed color 'Dimentions Mixwa208v' "
                          "($193), slow activator, 5L urethane clear, fast reducer"),
    "paint_system_2015": ("Boulder Auto Parts paint dept, Jan 2015: Nason Ful-Thane BC/CC mix to GM formula 3295 "
                          "(2015-01-12) + Nason SelectClear activator (2015-01-22); likely jamb/touch-up work after "
                          "relocation to Henderson"),
    "color_formula_references": ["Dimentions mix 'wa208v' (DOC-044)", "GM formula 3295 in Nason Ful-Thane (DOC-036)"],
    "bumpers": ("Front and rear 3-piece bumpers re-chromed Jun-Sep 2016 by American Polishing & Plating (Shine Shop), "
                "Henderson NV, $350 flat; two pieces redone at no charge Sep 2016. Remounted with chrome 5/16-18 "
                "carriage bolt hardware, 8 positions (McFadden-Dale, 2016-09-07). Bumper bracket seals, cover seals, "
                "rubber mounts, and a rear left bracket sourced from KGPR Apr 2015 (DOC-037)."),
    "exterior_trim": ("Sharp-edge complete side molding set w/52 clips (KGPR, Aug 2016); CAL trimless windshield and "
                      "rear glass seals (JBugs, May 2016); Karmann side body badge emblem (West Coast Metric, Jan "
                      "2015); verify trim configuration on car"),
    "sources": ["DOC-023", "DOC-026", "DOC-027", "DOC-036", "DOC-037", "DOC-041", "DOC-042", "DOC-043", "DOC-044",
                "DOC-046", "DOC-050", "DOC-051", "DOC-052"]
}
d['build_spec_cards']['electrical'] = {
    "card_id": "SPEC-ELECTRICAL",
    "fuse_box": "8-fuse box with cover, correct for Bug/Ghia 1961-66 (WCM 111-037 + 181-555A, Jan 2015)",
    "wiring": ("Hand-wiring work Feb 2015: 12ga and 16ga primary wire in four colors, cable tie mounts, grommets. "
               "No complete harness purchase documented."),
    "sources": ["DOC-046", "DOC-047"]
}
inst = d['build_spec_cards']['instrumentation']
inst['gauges'] = ("Aftermarket gauge senders documented, now three: Auto Meter 2258 electric temp sender short sweep "
                  "(2015-05-21); 300-degree oil temperature sender, alt# V3-2305-5 (2015-12-30); and a 111157 3/8in "
                  "resistance-type temperature sender ordered 2015-04-28 but backordered, fulfillment undocumented. "
                  "Gauge heads themselves not yet documented; identify from dash photos.")
if "DOC-049" not in inst['sources']:
    inst['sources'].append("DOC-049")

# ============ Gap movement ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-17':
        g['status'] = 'SUBSTANTIALLY RESOLVED'
        g['resolution'] = ("Batch 6: wheels identified as Sprintstar 5-spokes (EMPI pattern) by the 319-655 center cap "
                           "order, DOC-049, consistent with the chrome 14mm lug bolts (DOC-028). Remaining: wheel size "
                           "and finish, and the tire spec, from photos of the car.")
    if g['gap_id'] == 'GAP-20':
        g['item'] = ("Identify gauge heads (Auto Meter? VDO?) matching the documented senders, now three: Auto Meter "
                     "2258 electric temp (P-086), 300-degree oil temp 196-107 (P-091), and the backordered 3/8in "
                     "resistance sender 111157 (P-184, fulfillment undocumented). Photograph dash cluster.")
d['data_gaps'].append({
    "gap_id": "GAP-22", "priority": "low",
    "item": ("Mid America order 04682256: shipment -00001 contents and the backorder fulfillment (2x Sprintstar "
             "center caps and the 111157 temperature sender, $55.97 if charged) are undocumented. Check the folder "
             "for sibling Mid America invoices; the May 2015 Auto Meter sender purchase may indicate the backordered "
             "sender was cancelled.")
})

# ============ Write v6 ============
with open('data/versions/ghia-1965-master-record-v6.json', 'w') as f:
    json.dump(d, f, indent=1)
with open('data/master-record.json', 'w') as f:
    json.dump(d, f, indent=1)

print("v6 written:",
      len(d['document_archive']), "docs,",
      len(d['parts_ledger']), "ledger,",
      len(d['vendor_registry']), "vendors,",
      len(d['restoration_timeline']), "events,",
      len(d['data_gaps']), "gaps,",
      "spend", round(sum(e['ext_price'] for e in d['parts_ledger'] if e.get('ext_price')), 2))
