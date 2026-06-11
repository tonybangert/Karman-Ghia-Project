import json

with open('/home/claude/ghia/ghia-1965-master-record-v3.json') as f:
    d = json.load(f)

d['schema_version'] = '1.3'
d['generated_from'] = 'Batches 1-4 (DOC-001 to DOC-045)'

# ============ Vehicle master record updates ============
vmr = d['vehicle_master_record']
vmr['ownership_chain'][0]['owner'] = 'James O. Mahan'
vmr['ownership_chain'][0]['full_name_note'] = "Middle initial 'O' confirmed on KGPR payment line (DOC-038) and McFadden-Dale ship-to (DOC-045)."
vmr['ownership_chain'][0]['period'] = ('Documented activity Aug 2013 (Las Vegas head work) through May 2018. Address chronology now resolved: '
    'Hurricane UT during 2014 (West Coast Metric orders Apr-May 2014, paint purchase Jun 2014), Henderson NV from Jan 2015 onward. '
    'The Raby DTM kit shipped to the Hurricane UT address, placing it most likely in the 2014 Utah phase.')
vmr['acquisition_by_restorer'] = {
    "purchase_price": 500.00,
    "source": "DOC-043 handwritten cost ledger, line 1: '$500.00 price for car'",
    "note": "The car was a $500 project car at the start of the restoration."
}

# ============ New vendors ============
d['vendor_registry'].extend([
    {"vendor_id": "VEN-13", "name": "West Coast Metric Inc.", "address": "24002 Frampton Avenue, Harbor City, CA 90710",
     "phones": {"main": "310-325-0005", "toll_free": "800-247-3202"}, "customer_number": "034795",
     "specialty": "VW rubber, seals, and weatherstrip (Sure Fit line)", "documents": ["DOC-039", "DOC-040"]},
    {"vendor_id": "VEN-14", "name": "Auto Paints Plus", "address": "2291 W 500 N, Hurricane, UT 84737",
     "phones": {"main": "435-632-3648"}, "specialty": "Automotive paint supply",
     "documents": ["DOC-044"]},
    {"vendor_id": "VEN-15", "name": "Washington County Collision", "address": "Hurricane, UT area",
     "specialty": "Collision/body shop. Named purchaser on the June 2014 paint materials receipt; almost certainly performed or hosted the Ghia's body and paint work during the 2014 Utah phase.",
     "documents": ["DOC-044"]}
])

# ============ Duplicate note ============
for doc in d['document_archive']:
    if doc['doc_id'] == 'DOC-002':
        doc['duplicate_note'] = 'Complete flat re-photo received in Batch 4 (IMG_8168); matched on invoice 441346, all 16 lines confirmed. Not re-entered.'

# ============ New documents ============
d['document_archive'].extend([
    {"doc_id": "DOC-036", "type": "Invoice (counter)", "vendor_id": "VEN-07",
     "title": "Boulder Auto Parts invoice L239248: Nason Ful-Thane BC/CC paint mix, GM formula 3295",
     "reference_numbers": {"invoice": "L239248", "customer": "B4925"}, "date": "2015-01-12", "time": "12:19 PM",
     "terms": "PAINT DEPT-VISA", "line_item_count": 1, "subtotal": 33.74, "tax": 2.53, "total": 33.74,
     "extraction_note": "PAINT FORMULA RECOVERED (GAP-13): line reads 'NAS 1FA-4 / FUL THANE BC/CC MIX, GM FORMULA 3295'. "
        "Nason Ful-Thane basecoat/clearcoat system mixed to GM formula 3295. Ten days before the SelectClear activator purchase (DOC-023, same store)."},
    {"doc_id": "DOC-037", "type": "Invoice (shipping copy)", "vendor_id": "VEN-02",
     "title": "KGPR invoice #448485: complete door rubber kit order",
     "reference_numbers": {"invoice": "448485"}, "date": "2015-04-21", "order_date": "2015-04-20",
     "line_item_count": 18, "handwritten_annotations": "RA 21878 (top left)",
     "extraction_note": "Full door rubber kit (142-100P60) exploded into components on invoice. Left/right door seals backordered, fulfilled on 448485-1 (DOC-038). Page 1; check folder for page 2."},
    {"doc_id": "DOC-038", "type": "Invoice (backorder fulfillment)", "vendor_id": "VEN-02",
     "title": "KGPR invoice #448485-1: door seals backorder ship",
     "reference_numbers": {"invoice": "448485-1"}, "date": "2015-04-29",
     "ship_via": "FedEx, 2 lbs", "line_item_count": 2, "total": 43.10,
     "payment": "VISA, charge line shows 'JAMES O MAHAN'",
     "extraction_note": "Fulfills the two backordered door seals from DOC-037. Confirms restorer's full name James O. Mahan."},
    {"doc_id": "DOC-039", "type": "Mail order invoice", "vendor_id": "VEN-13",
     "title": "West Coast Metric invoice 111545: striker kit and fresh air grills",
     "reference_numbers": {"invoice": "111545", "shipment": "109860-1", "tracking": "604227032710"},
     "date": "2014-04-21", "ship_to": "James Mahan, 566 W 375 S, Hurricane, UT 84737",
     "line_item_count": 4, "freight": 12.83, "total": 175.48,
     "extraction_note": "UTAH PHASE EVIDENCE: April 2014 shipment to Hurricane UT, predating all Henderson NV receipts. Door striker rebuild kit (Ghia 1964-66) plus both fresh air grills and vent seals."},
    {"doc_id": "DOC-040", "type": "Credit memo / warranty replacement", "vendor_id": "VEN-13",
     "title": "West Coast Metric invoice 112156: warranty replacement, left fresh air grill",
     "reference_numbers": {"invoice": "112156", "shipment": "110478-1"}, "date": "2014-05-07",
     "terms": "CRMEMO", "line_item_count": 1, "total": 75.78,
     "extraction_note": "'WARRANTY FOR DEFECT / CREDIT FOR FREIGHT': the left fresh air grill from DOC-039 was defective and replaced under warranty, freight credited."},
    {"doc_id": "DOC-041", "type": "Invoice", "vendor_id": "VEN-02",
     "title": "KGPR invoice 16795: exterior trim and molding order",
     "reference_numbers": {"invoice": "16795"}, "date": "2016-08-17", "order_date": "2016-08-16",
     "ship_via": "FedEx Ground", "salesperson": "Victor ext 112", "line_item_count": 5,
     "subtotal": 263.29, "freight": 5.00, "total": 268.29, "payment": "Visa 0115, PAID, auth 192361",
     "extraction_note": "Sharp-edge style complete side molding set with 52 clips, upper right door hinge, black trunk wire cover, front hood rubber stops. Exterior brightwork phase, Aug 2016. Note KGPR's newer invoice format and customer ID 157036."},
    {"doc_id": "DOC-042", "type": "Invoice", "vendor_id": "VEN-04",
     "title": "California Pacific/JBugs Order #991958A: glass seals, belts, and final trim",
     "reference_numbers": {"order": "991958A"}, "date": "2016-05-23",
     "ship_via": "FedEx Ground", "total_weight_lbs": 10.2, "line_item_count": 18,
     "invoice_total": 314.80,
     "extraction_note": "Second JBugs order (new order number series). Cal-look ('CAL') windshield and rear window seals, outside mirror, sunvisors, window cranks, and grey 2-point lap belts with chrome lift latches and Wolfsburg stickers. Glass-in and final-assembly phase, May 2016. CAL-style seals are the trimless type; verify on car whether chrome window trim is absent (styling detail)."},
    {"doc_id": "DOC-043", "type": "Handwritten cost ledger", "vendor_id": None,
     "title": "Build cost ledger: 'Karman Ghia' and '2000cc Engine' columns",
     "date": None, "author": "Presumed James O. Mahan",
     "content_verbatim": {
        "karman_ghia_column": [
            "$500.00 price for car", "$100.00 media blast", "$35.00 Bondo", "$30.00 Dolfin Glaze",
            "$125.00 Primer", "$10.00 fiberglass", "$200.00 Nose & fender & Hood Replacement parts",
            "$50.00 (struck) / $70.00 sand paper", "$170.00 L&R grill, gasket, door latch", "$100.00 final Primer"],
        "engine_2000cc_column": [
            "$169.00 94 piston & cylinder", "$1000.00 Shroud assembly", "$10.00 milling oil pump",
            "$90.00 Alternator", "$90.00 light flywheel", "$25.00 gasket set",
            "$90.00 Rod-mains-cam bearings", "$30.00 Lifters", "$90.00 Rocks (rockers)", "$60.00 Crank shaft"]},
     "extraction_note": "MAJOR PROVENANCE DOCUMENT. Records the car's acquisition price ($500) and itemizes body-prep and engine bottom-end component costs in the restorer's hand. 'Shroud assembly $1000' matches DTM Stage III kit pricing, corroborating DOC-001. 'Light flywheel' adds a spec detail (lightened flywheel) not documented elsewhere. Substantially advances GAP-09 (bottom-end components itemized; vendors still unknown)."},
    {"doc_id": "DOC-044", "type": "Sales receipt", "vendor_id": "VEN-14",
     "title": "Auto Paints Plus receipt #727: complete paint system purchase",
     "reference_numbers": {"sale": "727"}, "date": "2014-06-19",
     "sold_to": "Washington County Collision",
     "line_item_count": 7, "subtotal": 586.06, "tax": 0.00, "total": 586.06,
     "extraction_note": "PAINT TRAIL CORNERSTONE (GAP-13): full system purchased in Hurricane UT under the account of Washington County Collision (body shop), June 2014. Epoxy primer/sealer, performa-seal, mixed color line 'Dimentions Mixwa208v' ($193), slow activator, 5L urethane clear, fast reducer, masking tape. Establishes (a) the body/paint work happened in the 2014 Utah phase, (b) the shop involved, (c) a second color-formula reference ('wa208v') alongside the Jan 2015 Nason 'GM formula 3295' mix."},
    {"doc_id": "DOC-045", "type": "Retail invoice", "vendor_id": "VEN-12",
     "title": "McFadden-Dale Hardware invoice E42653/4: stainless engine/bumper hardware",
     "reference_numbers": {"invoice": "E42653/4"}, "date": "2015-01-22", "time": "12:11",
     "ship_to": "MAHAN/JAMES O", "payment": "Bankcard x7266, signed James Mahan",
     "line_item_count": 6, "subtotal": 20.49, "tax": 1.66, "total": 22.15,
     "extraction_note": "M8 stainless socket-head hardware with nyloc nuts and wave washers (classic VW tin/bumper fasteners), gloss black spray, Scotch-Brite maroon pads. Same day as the Nason activator purchase in Boulder City (DOC-023): two supply stops on 2015-01-22."}
])

# ============ New ledger entries ============
def entry(eid, doc, ven, date, name, sku, qty, unit, ext, sys, notes=None, **kw):
    e = {"entry_id": eid, "doc_id": doc, "vendor_id": ven, "date": date,
         "item_name": name, "vendor_sku": sku, "qty": qty,
         "unit_price": unit, "ext_price": ext, "system_id": sys, "notes": notes}
    e.update(kw); return e

L = []
# DOC-036 paint mix
L.append(entry("P-095", "DOC-036", "VEN-07", "2015-01-12", "Nason Ful-Thane BC/CC Paint Mix, GM Formula 3295", "NAS 1FA-4",
    1, 31.21, 31.21, "SYS-08",
    "THE COLOR FORMULA: Ful-Thane basecoat/clearcoat mixed to GM formula 3295. Pair with DOC-044's 'Mixwa208v' reference to pin down the exact color name (GAP-13).", list_price=46.815))
# DOC-037 KGPR door rubber order
kgpr37 = [
    ("P-096", "Door Rubber Kit, Complete (kit header)", "142-100P60 66 N KT", 1, None, None, "Kit header line; components item-ized below."),
    ("P-097", "Seal, Door Hinge Pillar, Left", "831-711 ALL RP", 1, 14.95, 14.95, None),
    ("P-098", "Seal, Door Hinge Pillar, Right", "831-712 ALL RP", 1, 14.95, 14.95, None),
    ("P-099", "Seal, Door, Left (backordered)", "831-731 ALL RP", 1, 21.55, 0.00, "Backordered; shipped on DOC-038 (P-114)."),
    ("P-100", "Seal, Door, Right (backordered)", "831-732 ALL RP", 1, 21.55, 0.00, "Backordered; shipped on DOC-038 (P-115)."),
    ("P-101", "Gasket Set, Door Handle, 4 pcs", "837-237 56 67 RP ST", 1, 7.42, 7.42, None),
    ("P-102", "Door Check Strap", "837-253 59.5-74 RP", 2, 13.75, 27.50, None),
    ("P-103", "Door Alignment Wedge (on door)", "837-277 60 74 RP", 2, 6.45, 12.90, None),
    ("P-104", "Door Window Scraper Weatherstrip", "837-475 61.5-71 RP", 2, 7.59, 15.18, None),
    ("P-105", "Door Felts", "837-479 ALL RP", 2, 21.89, 43.78, None),
    ("P-106", "Door Window Guide Plugs (Anti-Rattle)", "837-491 60 74 RP EA", 14, 2.31, 32.34, None),
    ("P-107", "Door Window Weatherstrip, Top-to-Window", "845-211P56 66 RP", 2, 18.95, 37.90, None),
    ("P-108", "Door Window-to-Quarter Pillar Weatherstrip", "847-341P60 66 RP", 2, 9.95, 19.90, None),
    ("P-109", "Bumper Bracket Seal, Pair", "707-197 56 71 RP PR", 2, 1.99, 3.98, None),
    ("P-110", "Bumper Bracket Cover Seal, Pair", "707-251 56 71 RP PR", 2, 4.34, 8.68, None),
    ("P-111", "Bumper Mount, Rubber, Outer Front, Pair", "707-253 56 71 RP PR", 1, 4.89, 4.89, None),
    ("P-112", "Bumper Bracket, Rear Left", "707-335 56 68 U", 1, 22.15, 22.15, "U suffix likely used/original stock."),
    ("P-113", "Quarter Window Pin Gasket", "847-205P60 74 RP ST", 2, 4.25, 8.50, None),
]
for eid, name, sku, qty, unit, ext, note in kgpr37:
    sys = "SYS-08"
    L.append(entry(eid, "DOC-037", "VEN-02", "2015-04-21", name, sku, qty, unit, ext, sys, note, fitment_listed="1966 GHIACP"))
# DOC-038 fulfillment
L.append(entry("P-114", "DOC-038", "VEN-02", "2015-04-29", "Seal, Door, Left (backorder ship)", "831-731 ALL RP", 1, 21.55, 21.55, "SYS-08", "Fulfills P-099."))
L.append(entry("P-115", "DOC-038", "VEN-02", "2015-04-29", "Seal, Door, Right (backorder ship)", "831-732 ALL RP", 1, 21.55, 21.55, "SYS-08", "Fulfills P-100."))
# DOC-039 WCM
L.append(entry("P-116", "DOC-039", "VEN-13", "2014-04-21", "Door Striker Rebuild Kit (one side), Ghia 1964-66", "141-898", 1, 33.50, 33.50, "SYS-08", "Note catalog fitment 1964-66 matches the title year directly."))
L.append(entry("P-117", "DOC-039", "VEN-13", "2014-04-21", "Grill, Fresh Air, Left, All Ghias 61-74", "141-651A-L", 1, 62.95, 62.95, "SYS-08", "Defective on arrival; replaced under warranty (DOC-040, P-120)."))
L.append(entry("P-118", "DOC-039", "VEN-13", "2014-04-21", "Grille, Fresh Air, Right, All Ghias 61-74", "141-652A-R", 1, 62.95, 62.95, "SYS-08", None))
L.append(entry("P-119", "DOC-039", "VEN-13", "2014-04-21", "Seals, Fresh Air Vents, Pair", "141-657A", 1, 3.25, 3.25, "SYS-08", None))
# DOC-040 warranty
L.append(entry("P-120", "DOC-040", "VEN-13", "2014-05-07", "Grill, Fresh Air, Left (WARRANTY REPLACEMENT)", "141-651A-L", 1, 62.95, 0.00, "SYS-08", "Credit memo: defect warranty, freight credited. Net cost zero.", entry_type="warranty_replacement"))
# DOC-041 KGPR molding
L.append(entry("P-121", "DOC-041", "VEN-02", "2016-08-17", "Hinge, Door, Upper, Right", "831-402 59.5-74 RP", 1, 43.95, 43.95, "SYS-08", "Pairs with the lower-left hinge bought Jan 2015 (P-026): door hinge refresh across both doors."))
L.append(entry("P-122", "DOC-041", "VEN-02", "2016-08-17", "Molding Set, Complete, Sharp-Edge Style", "853-499 60 67 RP ST", 1, 139.05, 139.05, "SYS-08", "Full exterior side molding set, sharp-edge style."))
L.append(entry("P-123", "DOC-041", "VEN-02", "2016-08-17", "Side Molding Clips, 52/Set", "853-547 ALL RP ST", 1, 15.95, 15.95, "SYS-08", None))
L.append(entry("P-124", "DOC-041", "VEN-02", "2016-08-17", "Trunk Wire Cover, Black", "063-567 56 67 RPBK", 1, 55.55, 55.55, "SYS-08", None))
L.append(entry("P-125", "DOC-041", "VEN-02", "2016-08-17", "Rubber Stop, Front Hood, Pair", "823-495 56 67 RP PR", 1, 8.79, 8.79, "SYS-08", None))
# DOC-042 JBugs glass/trim
L.append(entry("P-126", "DOC-042", "VEN-04", "2016-05-23", "Seal, Windshield, Cal-Look, Ghia 56-74", "141-121C", 1, 48.95, 48.95, "SYS-08", "CAL (trimless) style windshield seal."))
L.append(entry("P-127", "DOC-042", "VEN-04", "2016-05-23", "Rear Window Seal, Cal-Look, Ghia 56-74", "141-521C", 1, 48.95, 48.95, "SYS-08", "CAL (trimless) style rear glass seal."))
L.append(entry("P-128", "DOC-042", "VEN-04", "2016-05-23", "Mirror, Outside, Left, Ghia 66-74", "141857501", 1, 34.95, 34.95, "SYS-08", None))
L.append(entry("P-129", "DOC-042", "VEN-04", "2016-05-23", "Seal, Mirror Base, L&R, Ghia 66-74", "141-511-L/R", 1, 3.95, 3.95, "SYS-08", None))
L.append(entry("P-130", "DOC-042", "VEN-04", "2016-05-23", "Sunvisors, Ghia 65-74, Pair, Black", "21-1517", 1, 61.95, 61.95, "SYS-09", None))
L.append(entry("P-131", "DOC-042", "VEN-04", "2016-05-23", "Visor Clips, Black, Pair", "21-2018BK", 1, 4.00, 4.00, "SYS-09", None))
L.append(entry("P-132", "DOC-042", "VEN-04", "2016-05-23", "Seat Belts, 2-Point, Grey, Chrome Lift Latch, w/ Hardware", "Z VW 20 GY L", 2, 23.95, 47.90, "SYS-09", "Includes bundled 0.00 lines: 1800-60-6005-GREY lap belt entries, FHD-1046-2 hardware kits x2, Wolfsburg seat belt stickers x2. Grey belts match the grey velour interior."))
L.append(entry("P-133", "DOC-042", "VEN-04", "2016-05-23", "Window Cranks, Black x2 + Crank Handle Pins x2", "113837581E BK / 6325-3X12", 2, None, 17.90, "SYS-09", "Cranks 13.90 + pins 4.00."))
L.append(entry("P-134", "DOC-042", "VEN-04", "2016-05-23", "Door Cover Plate, Chrome, Bug 65-79", "113-239B-CM", 1, 24.95, 24.95, "SYS-09", None))
L.append(entry("P-135", "DOC-042", "VEN-04", "2016-05-23", "Small interior hardware (consolidated)", "111-086 / 111-542-BK / 111837595A / 311-247-BK", 1, None, 21.30, "SYS-09", "Visor clip screws 0.50, black knobs x2 9.90, window/door buffer 4.95, door finger cover plate 5.95."))
# DOC-044 paint system
L.append(entry("P-136", "DOC-044", "VEN-14", "2014-06-19", "Epoxy Primer/Sealer", "monps3044q", 2, 33.05, 66.10, "SYS-08", "Purchased under Washington County Collision account."))
L.append(entry("P-137", "DOC-044", "VEN-14", "2014-06-19", "Performa-Seal", "monpa3050m", 0.5, 37.88, 18.94, "SYS-08", None))
L.append(entry("P-138", "DOC-044", "VEN-14", "2014-06-19", "Mixed Color, 'Dimentions Mixwa208v'", "dimmix", 1, 193.00, 193.00, "SYS-08", "SECOND COLOR FORMULA REFERENCE: 'wa208v' in the Dimension mixing system. Cross-reference with GM formula 3295 (P-095) to recover the color name (GAP-13)."))
L.append(entry("P-139", "DOC-044", "VEN-14", "2014-06-19", "Activator, Slow", "monmp2185", 1, 98.00, 98.00, "SYS-08", None))
L.append(entry("P-140", "DOC-044", "VEN-14", "2014-06-19", "Urethane Clear, 5L", "monpe2100", 1, 100.00, 100.00, "SYS-08", None))
L.append(entry("P-141", "DOC-044", "VEN-14", "2014-06-19", "Urethane Reducer, Fast", "montho860g", 2, 37.91, 75.82, "SYS-08", None))
L.append(entry("P-142", "DOC-044", "VEN-14", "2014-06-19", "Masking Tape, 3/4 inch Yellow (3M 06652)", "3m06652", 12, 2.85, 34.20, "SYS-08", None))
# DOC-045 hardware
L.append(entry("P-143", "DOC-045", "VEN-12", "2015-01-22", "Gloss Black Spray Paint, 5-Ball", "DIVK01601", 1, 5.50, 5.50, "SYS-12", None))
L.append(entry("P-144", "DOC-045", "VEN-12", "2015-01-22", "Stainless Hardware (consolidated): M8x16 socket caps x12, M8 nyloc x12, M8 wave washers x20, M5x18 pan screws x5", "M816SHCSSS / M8125NYLOCSS / M8VWW / M518PHMS", 1, None, 13.54, "SYS-12", "M8 stainless with wave washers: classic VW engine tin and bumper fastener refresh."))
L.append(entry("P-145", "DOC-045", "VEN-12", "2015-01-22", "Scotch-Brite Maroon Hand Pads 7447", "3M04029", 1, 1.45, 1.45, "SYS-12", None))

d['parts_ledger'].extend(L)

# ============ Spec cards ============
d['build_spec_cards']['body_paint'] = {
    "card_id": "SPEC-BODYPAINT",
    "body_prep": "Per restorer's cost ledger (DOC-043): media blast, Bondo and Dolphin Glaze finishing, fiberglass repair, replacement nose/fender/hood panels, multiple primer stages.",
    "body_shop": "Washington County Collision, Hurricane UT (named purchaser on the June 2014 paint receipt)",
    "paint_system_2014": "Auto Paints Plus, 2014-06-19: epoxy primer/sealer, mixed color 'Dimentions Mixwa208v' ($193), slow activator, 5L urethane clear, fast reducer",
    "paint_system_2015": "Boulder Auto Parts paint dept, Jan 2015: Nason Ful-Thane BC/CC mix to GM formula 3295 (2015-01-12) + Nason SelectClear activator (2015-01-22); likely jamb/touch-up work after relocation to Henderson",
    "color_formula_references": ["Dimentions mix 'wa208v' (DOC-044)", "GM formula 3295 in Nason Ful-Thane (DOC-036)"],
    "exterior_trim": "Sharp-edge complete side molding set w/52 clips (KGPR, Aug 2016); CAL trimless windshield and rear glass seals (JBugs, May 2016); verify trim configuration on car",
    "sources": ["DOC-023", "DOC-026", "DOC-027", "DOC-036", "DOC-043", "DOC-044", "DOC-041", "DOC-042"]
}
eng = d['build_spec_cards']['engine']
eng['flywheel'] = "Lightened flywheel ($90 per restorer's cost ledger, DOC-043)"
eng['bottom_end_cost_record'] = "DOC-043 itemizes: 94mm pistons/cylinders $169, crankshaft $60, rod/main/cam bearings $90, lifters $30, rockers $90, gasket set $25, alternator $90, oil pump milling $10, shroud assembly $1000 (matches DTM Stage III)."
eng['sources'] = sorted(set(eng['sources'] + ['DOC-043']))
d['build_spec_cards']['interior']['seat_belts'] = "Grey 2-point lap belts with chrome lift latches and Wolfsburg stickers (JBugs Z VW 20 GY L, May 2016)"
d['build_spec_cards']['interior']['sources'] = sorted(set(d['build_spec_cards']['interior']['sources'] + ['DOC-042']))

# DOC-001 Raby kit date estimate update
for doc in d['document_archive']:
    if doc['doc_id'] == 'DOC-001':
        doc['date_note'] = ("Date cropped from scan; re-photograph top. BEST ESTIMATE NOW ~2014: the kit shipped to the Hurricane UT address, "
            "which Batch 4 places in the 2014 phase (West Coast Metric Apr-May 2014, paint Jun 2014). Consistent with head work Aug 2013 preceding the cooling kit purchase.")

# ============ Timeline ============
d['restoration_timeline'].extend([
    {"date": "2014-04-21", "event": "UTAH PHASE: West Coast Metric order to Hurricane UT: door striker kit, fresh air grills, vent seals", "doc_id": "DOC-039"},
    {"date": "2014-05-07", "event": "Defective left fresh air grill replaced under warranty by West Coast Metric", "doc_id": "DOC-040"},
    {"date": "2014-06-19", "event": "PAINT DAY MATERIALS: full system ($586) from Auto Paints Plus, Hurricane UT, purchased under Washington County Collision. Epoxy primer, 'Dimentions Mixwa208v' color, 5L urethane clear. Body/paint executed in Utah, mid-2014", "doc_id": "DOC-044"},
    {"date": "2015-01-12", "event": "Nason Ful-Thane BC/CC mix to GM formula 3295, Boulder Auto Parts paint dept (color formula recovered)", "doc_id": "DOC-036"},
    {"date": "2015-01-22", "event": "Two supply stops same day: Nason SelectClear activator (Boulder City) and stainless M8 hardware + gloss black spray (McFadden-Dale, Las Vegas)", "doc_id": "DOC-023, DOC-045"},
    {"date": "2015-04-21", "event": "KGPR complete door rubber kit order (18 lines): door resealing phase", "doc_id": "DOC-037"},
    {"date": "2015-04-29", "event": "Backordered left/right door seals ship from KGPR", "doc_id": "DOC-038"},
    {"date": "2016-05-23", "event": "JBugs glass and final-trim order: CAL windshield/rear seals, mirror, sunvisors, grey 2-point belts. Glass-in phase", "doc_id": "DOC-042"},
    {"date": "2016-08-17", "event": "KGPR exterior brightwork order: sharp-edge side molding set, hinge, trunk wire cover, hood stops", "doc_id": "DOC-041"},
    {"date": None, "event": "Undated: handwritten build cost ledger records $500 car acquisition and itemized body/engine component costs", "doc_id": "DOC-043"}
])
d['restoration_timeline'].sort(key=lambda e: (e['date'] is None, e['date'] or ''))

# ============ Gaps ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-13':
        g['status'] = 'SUBSTANTIALLY RESOLVED (Batch 4)'
        g['resolution'] = ("Paint trail recovered: body shop = Washington County Collision (Hurricane UT); June 2014 full system from Auto Paints Plus "
            "with mixed color 'Dimentions Mixwa208v'; Jan 2015 Nason Ful-Thane BC/CC mixed to GM formula 3295 + SelectClear activator (Boulder Auto Parts). "
            "Remaining: translate formula references (wa208v / GM 3295) into the color name, and confirm which system is the final topcoat.")
    if g['gap_id'] == 'GAP-09':
        g['status'] = 'PARTIALLY RESOLVED (Batch 4)'
        g['resolution'] = "DOC-043 cost ledger itemizes the bottom end: 94mm P&C, crank, bearings, lifters, rockers, lightened flywheel, gasket set, alternator, oil pump milling. Vendors for these components still undocumented."
    if g['gap_id'] == 'GAP-02':
        g['item'] += " UPDATE: best estimate now ~2014 (kit shipped to the Hurricane UT address used during the 2014 phase)."
d['data_gaps'].append(
    {"gap_id": "GAP-21", "priority": "medium", "item": "Contact/lookup Washington County Collision (Hurricane UT): possible body work records or photos; also translate paint formulas 'wa208v' and 'GM 3295' to a color name via a paint supplier."}
)

with open('/home/claude/ghia/ghia-1965-master-record-v4.json', 'w') as f:
    json.dump(d, f, indent=2)

print('v4 written')
print('documents:', len(d['document_archive']))
print('ledger entries:', len(d['parts_ledger']))
print('vendors:', len(d['vendor_registry']))
print('timeline events:', len(d['restoration_timeline']))
print('gaps:', len(d['data_gaps']))
spend = sum(e.get('ext_price') or 0 for e in d['parts_ledger'])
print('documented spend (priced entries): $%.2f' % spend)
ledger_cash = 500 + 100 + 35 + 30 + 125 + 10 + 200 + 70 + 170 + 100 + 169 + 1000 + 10 + 90 + 90 + 25 + 90 + 30 + 90 + 60
print('handwritten cost ledger total (incl. $500 car): $%d' % ledger_cash)
dates = [e['date'] for e in d['parts_ledger'] if e.get('date')]
print('date range:', min(dates), 'to', max(dates))
