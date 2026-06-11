import json

with open('/home/claude/ghia/ghia-1965-master-record-v1.json') as f:
    d = json.load(f)

d['schema_version'] = '1.1'
d['generated_date'] = '2026-06-10'
d['generated_from'] = 'Batch 1 (DOC-001 to DOC-007) + Batch 2 (DOC-008 to DOC-024)'

# ---- New vendors ----
d['vendor_registry'].extend([
    {
        "vendor_id": "VEN-07",
        "name": "Boulder Auto Parts (CarQuest / Genuine Parts Co.)",
        "address": "1500 Nevada Highway, Boulder City, NV 89005-1806",
        "phones": {"main": "702-293-1368"},
        "specialty": "Auto parts and automotive paint department (DuPont/Nason line)",
        "customer_number": "B4925",
        "documents": ["DOC-023"]
    },
    {
        "vendor_id": "VEN-08",
        "name": "Meyers Auto Parts",
        "address": "3540 Boulder Hwy, Las Vegas, NV 89121 (also West: 3345 S. Decatur Blvd, Las Vegas, NV 89102)",
        "phones": {"east": "702-431-8000 (listed for West store on form)", "fax": "702-431-8528"},
        "specialty": "Independent auto parts, VW import coverage",
        "documents": ["DOC-024"]
    }
])

# ---- Duplicate note on DOC-007 ----
for doc in d['document_archive']:
    if doc['doc_id'] == 'DOC-007':
        doc['duplicate_note'] = 'A second photo of this same receipt (invoice 2655-493365) arrived in Batch 2 and was matched by invoice number; not re-entered.'

# ---- New documents ----
oreilly = lambda inv, date, items, total, note=None, **kw: {
    "doc_id": kw.pop('doc_id'),
    "type": "Retail receipt",
    "vendor_id": "VEN-05",
    "title": f"O'Reilly Auto Parts receipt, invoice {inv}",
    "reference_numbers": {"invoice": inv},
    "date": date,
    "line_item_count": items,
    "total": total,
    **({"extraction_note": note} if note else {}),
    **kw
}

d['document_archive'].extend([
    oreilly("2655-493363", "2015-03-07", 1, 41.07, doc_id="DOC-008",
            note="Time 13:20:10, two minutes before DOC-007 (13:22:11). Two separate transactions in the same store visit."),
    oreilly("2655-243571", "2016-09-14", 1, None, doc_id="DOC-009",
            note="Latest-dated document in the archive so far; extends the documented restoration window to Sep 2016. Total partially cropped (subtotal 4.29 visible)."),
    oreilly("2655-187759", "2016-03-01", 2, 17.28, doc_id="DOC-010"),
    oreilly("2655-482535", "2015-01-25", 5, None, doc_id="DOC-011",
            note="Net subtotal 22.65 (list 38.40); tax/total at cropped edge."),
    oreilly("2655-486730", "2015-02-11", 3, 21.59, doc_id="DOC-012",
            note="Credit card sale; customer signature visible on this copy."),
    oreilly("2655-498473", "2015-03-18", 1, 8.63, doc_id="DOC-013"),
    oreilly("2655-496193", "2015-03-17", 1, None, doc_id="DOC-014",
            note="Subtotal 5.99 visible; tax/total at cropped edge."),
    oreilly("2655-485079", "2015-02-05", 3, None, doc_id="DOC-015",
            note="Morning visit (11:35). Same day as DOC-019 (17:23). Net subtotal 17.87."),
    oreilly("2655-492277", "2015-03-28", 0, None, doc_id="DOC-016",
            note="ILLEGIBLE LINE ITEMS: left edge of receipt cut off in photo. Visible: list total 82.15, net subtotal 48.47, debit card. Re-photograph this receipt flat and complete."),
    oreilly("2655-102376", "2015-04-09", 1, 36.73, doc_id="DOC-017",
            note="Counter lookup header reads '1967 Volkswagen Beetle [H4 1.5L] - All'. H6024 sealed beams fit the Ghia identically; the Beetle lookup is a counter-clerk convenience, but see attribution note GAP-16."),
    oreilly("2655-148201", "2015-09-30", 2, 31.87, doc_id="DOC-018"),
    oreilly("2655-485202", "2015-02-05", 2, 19.44, doc_id="DOC-019",
            note="Evening visit (17:23), second O'Reilly trip of the day after DOC-015."),
    oreilly("2655-488602", "2015-02-18", 6, None, doc_id="DOC-020",
            note="Page 1 marker; net subtotal 55.22 (list 93.58), 8 units. Handwritten annotation '-28.42' near totals. Tax/total at cropped edge."),
    oreilly("2655-489639", "2015-02-21", 2, 0.00, doc_id="DOC-021",
            note="Even exchange: Gates 7370 V-belt (from DOC-020, 2015-02-18) returned with return authorization referencing original sale, replaced with Gates 7365. Net 0.00. Receipt carries 'JON DOE' placeholder in counter name field."),
    oreilly("2655-489641", "2015-02-21", 1, 11.61, doc_id="DOC-022",
            note="Three minutes after DOC-021 in same visit."),
    {
        "doc_id": "DOC-023",
        "type": "Invoice (counter)",
        "vendor_id": "VEN-07",
        "title": "Boulder Auto Parts / CarQuest invoice L239795, paint department",
        "reference_numbers": {"invoice": "L239795", "customer": "B4925"},
        "date": "2015-01-22",
        "time": "09:26 AM",
        "terms": "PAINT DEPT-CASH",
        "line_item_count": 1,
        "subtotal": 42.69, "tax": 3.20, "total": 42.69,
        "extraction_note": "First Body/Paint system document in the archive. NAS brand prefix = Nason (DuPont refinish line); header references a DuPont price increase, corroborating. Indicates DuPont Nason clearcoat system used on the body. Taxable amount 39.49 + 3.20 tax = 42.69."
    },
    {
        "doc_id": "DOC-024",
        "type": "Invoice (counter)",
        "vendor_id": "VEN-08",
        "title": "Meyers Auto Parts invoice 854312, Type 1 carburetor kit",
        "reference_numbers": {"invoice": "854312"},
        "date": "2016-02-29",
        "time": "09:31 AM",
        "payment": "Debit 26.98",
        "line_item_count": 1,
        "total": 26.98,
        "extraction_note": "ATTRIBUTION UNCERTAIN: a Type 1 carburetor rebuild kit conflicts with this car's dual Weber 44 setup. Possibly purchased for a stock Solex before/aside from the Weber installation, for a spare carb, or for a different vehicle (see GAP-16). Leap-day purchase, 2016-02-29."
    }
])

# ---- New ledger entries ----
def entry(eid, doc, ven, date, name, sku, qty, unit, ext, sys, notes=None, **kw):
    e = {"entry_id": eid, "doc_id": doc, "vendor_id": ven, "date": date,
         "item_name": name, "vendor_sku": sku, "qty": qty,
         "unit_price": unit, "ext_price": ext, "system_id": sys, "notes": notes}
    e.update(kw)
    return e

L = d['parts_ledger']
L.extend([
    entry("P-046", "DOC-008", "VEN-05", "2015-03-07", "Ignition Wire Set", "IDW 4J276", 1, 37.99, 37.99, "SYS-10",
          "Import Direct ignition wire set, limited lifetime warranty. List 64.39.", list_price=64.39),
    entry("P-047", "DOC-009", "VEN-05", "2016-09-14", "Roll Pin", "MTM 13850", 1, 4.29, 4.29, "SYS-12",
          "Dorman/Motormite roll pin. Latest dated purchase in archive.", list_price=7.27),
    entry("P-048", "DOC-010", "VEN-05", "2016-03-01", "Threadlocker, 10ml", "PER 27200", 1, 12.99, 12.99, "SYS-12",
          "Permatex 27200 high-strength threadlocker.", list_price=22.02),
    entry("P-049", "DOC-010", "VEN-05", "2016-03-01", "Thread Repair Inserts", "HEL 5326-14", 1, 2.99, 2.99, "SYS-01",
          "Heli-Coil inserts, 14mm thread family per part number. Plausibly related to ongoing spark plug thread management (see S-003: one head carries a 2nd-oversize plug insert). Unconfirmed; flag for inspection.", list_price=5.07),
    entry("P-050", "DOC-011", "VEN-05", "2015-01-25", "Disconnect Terminal Pack", "CTI 84171", 1, 5.29, 5.29, "SYS-10", "Calterm electrical disconnect pack.", list_price=8.97),
    entry("P-051", "DOC-011", "VEN-05", "2015-01-25", "Mini Bulb 1156, Long Life", "SYL 1156LLBP", 1, 4.99, 4.99, "SYS-10", "Sylvania long-life 1156 (single-filament signal/reverse bulb).", list_price=8.46),
    entry("P-052", "DOC-011", "VEN-05", "2015-01-25", "Mini Bulb 1155, Long Life", "SYL 1155LLBP", 1, 5.99, 5.99, "SYS-10", "Sylvania long-life 1155 (license/parking bulb family).", list_price=10.15),
    entry("P-053", "DOC-011", "VEN-05", "2015-01-25", "Mini Bulb 1156, Long Life (second pack)", "SYL 1156LLBP", 1, 4.99, 4.99, "SYS-10", "Second 1156 pack on same receipt; rung separately rather than qty 2.", list_price=8.46),
    entry("P-054", "DOC-011", "VEN-05", "2015-01-25", "Dielectric/Service Grease, 4g", "VER 15320", 1, 1.39, 1.39, "SYS-12", "Versachem 4g grease packet.", list_price=2.36),
    entry("P-055", "DOC-012", "VEN-05", "2015-02-11", "Battery Cable", "SS SK943CR", 1, 7.49, 7.49, "SYS-10", None, list_price=12.69),
    entry("P-056", "DOC-012", "VEN-05", "2015-02-11", "Battery Cable", "SS SK942AC", 1, 7.49, 7.49, "SYS-10", None, list_price=12.69),
    entry("P-057", "DOC-012", "VEN-05", "2015-02-11", "Copper Lug Pack", "CTI 85635", 1, 4.99, 4.99, "SYS-10", None, list_price=8.46),
    entry("P-058", "DOC-013", "VEN-05", "2015-03-18", "Rubber Plugs", "MTM 02607", 2, 3.99, 7.98, "SYS-12", "Dorman/Motormite rubber plugs (body/firewall hole plugs).", list_price=6.76),
    entry("P-059", "DOC-014", "VEN-05", "2015-03-17", "Gear Lube", "WP 80038", 1, 5.99, 5.99, "SYS-05", "Transaxle gear oil purchase, consistent with transmission install/fill period.", list_price=10.15),
    entry("P-060", "DOC-015", "VEN-05", "2015-02-05", "Primary Wire, Roll", "CTI 85714", 1, 6.99, 6.99, "SYS-10", None, list_price=11.85),
    entry("P-061", "DOC-015", "VEN-05", "2015-02-05", "Primary Wire, Roll", "CTI 85708", 1, 6.99, 6.99, "SYS-10", None, list_price=11.85),
    entry("P-062", "DOC-015", "VEN-05", "2015-02-05", "Electrical Tape", "MMM 6138", 1, 3.89, 3.89, "SYS-10", "3M electrical tape.", list_price=6.59),
    entry("P-063", "DOC-017", "VEN-05", "2015-04-09", "Sealed Beam Headlamp H6024XV", "SYL H6024XV", 2, 16.99, 33.98, "SYS-10",
          "Sylvania XtraVision 7-inch round sealed beams. Counter lookup used a 1967 Beetle; H6024 is the correct Ghia headlamp regardless.", list_price=28.80),
    entry("P-064", "DOC-018", "VEN-05", "2015-09-30", "LED Lights", "CA 2371", 1, 21.99, 21.99, "SYS-10",
          "LED light unit, application not specified on receipt (possibly auxiliary/interior). Verify against car.", list_price=37.27),
    entry("P-065", "DOC-018", "VEN-05", "2015-09-30", "Copper Spray Sealant, 3oz", "PER 81878", 1, 7.49, 7.49, "SYS-01",
          "Permatex Copper Spray-A-Gasket. Classic aircooled use: cylinder/head sealing surfaces. Timing (Sep 2015) may correlate with engine assembly.", list_price=12.69),
    entry("P-066", "DOC-019", "VEN-05", "2015-02-05", "Disconnect Terminal Pack", "CTI 85488", 1, 8.99, 8.99, "SYS-10", None, list_price=15.24),
    entry("P-067", "DOC-019", "VEN-05", "2015-02-05", "Disconnect Pack", "CTI 85496", 1, 8.99, 8.99, "SYS-10", None, list_price=15.24),
    entry("P-068", "DOC-020", "VEN-05", "2015-02-18", "'45 STREET' (identity unconfirmed)", "EDE 224600", 2, 5.99, 11.98, "SYS-03",
          "UNCONFIRMED: purchased alongside fuel filters; plausibly carburetor jets (size 45) or similar small fuel/carb components. Verify part number 224600 against physical parts or O'Reilly records (GAP-15).", list_price=10.15),
    entry("P-069", "DOC-020", "VEN-05", "2015-02-18", "'45 STREET' (identity unconfirmed, second line)", "EDE 224600", 2, 5.99, 11.98, "SYS-03",
          "Second identical line on same receipt (4 units total across both lines).", list_price=10.15),
    entry("P-070", "DOC-020", "VEN-05", "2015-02-18", "Fuel Filter, Inline", "WIX 33001", 1, 3.99, 3.99, "SYS-03",
          "WIX small inline fuel filter. Two different inline filters purchased together, consistent with dual-carb fuel plumbing.", list_price=6.76),
    entry("P-071", "DOC-020", "VEN-05", "2015-02-18", "Fuel Filter, Inline", "WIX 33002", 1, 3.99, 3.99, "SYS-03", None, list_price=6.76),
    entry("P-072", "DOC-020", "VEN-05", "2015-02-18", "Brake Fluid, 12oz", "ORC 72126", 1, 3.29, 3.29, "SYS-07", "Brake fluid for the new disc brake system fill/bleed.", list_price=5.58),
    entry("P-073", "DOC-020", "VEN-05", "2015-02-18", "V-Belt, Gates 7370", "GAT 7370", 1, 19.99, 19.99, "SYS-02",
          "Returned 2015-02-21 and exchanged for Gates 7365 (see P-074/P-075). Belt length trial during fan/alternator setup.", list_price=33.88),
    entry("P-074", "DOC-021", "VEN-05", "2015-02-21", "V-Belt, Gates 7370 (RETURN)", "GAT 7370", -1, 19.99, -19.99, "SYS-02",
          "Return with authorization referencing original 2015-02-18 sale.", entry_type="return"),
    entry("P-075", "DOC-021", "VEN-05", "2015-02-21", "V-Belt, Gates 7365", "GAT 7365", 1, 19.99, 19.99, "SYS-02",
          "Replacement belt, one size different from 7370. Final belt fitment from this exchange: Gates 7365. Note the Raby DTM kit also includes its own DTM fan belt (P-007); reconcile which belt serves which drive on the car.", list_price=33.88),
    entry("P-076", "DOC-022", "VEN-05", "2015-02-21", "Fuel Hose, per foot", "GAT 27006", 6, 1.79, 10.74, "SYS-03", "Gates fuel hose, 6 feet.", list_price=3.03, unit_measure="FT"),
    entry("P-077", "DOC-023", "VEN-07", "2015-01-22", "Nason Select Clearcoat Activator", "NAS 483-79-4", 1, 39.49, 39.49, "SYS-08",
          "DuPont Nason SelectClear activator (483-79), paint department cash sale. First documented paint material: indicates a DuPont Nason clearcoat system on the body. Hunt for matching basecoat/color receipts in folder (GAP-13).", list_price=59.235),
    entry("P-078", "DOC-024", "VEN-08", "2016-02-29", "Type 1 Carburetor Kit", "KT 100", 1, 24.95, 24.95, "SYS-03",
          "ATTRIBUTION UNCERTAIN: Type 1 (stock Solex) carb rebuild kit conflicts with the documented dual Weber 44 setup. See DOC-024 note and GAP-16.", list_price=34.51, attribution="uncertain")
])

# ---- Timeline additions ----
d['restoration_timeline'].extend([
    {"date": "2015-01-22", "event": "Paint phase evidence: Nason clearcoat activator purchased at Boulder Auto Parts paint dept. Body/paint work active by late Jan 2015", "doc_id": "DOC-023"},
    {"date": "2015-01-25", "event": "Lighting bulbs, electrical disconnects, grease (O'Reilly)", "doc_id": "DOC-011"},
    {"date": "2015-02-05", "event": "Two O'Reilly trips same day: primary wire and tape (morning), disconnect terminals (evening). Rewiring phase underway", "doc_id": "DOC-015, DOC-019"},
    {"date": "2015-02-11", "event": "Battery cables and copper lug", "doc_id": "DOC-012"},
    {"date": "2015-02-18", "event": "Fuel system and belt run: inline fuel filters, possible carb jets, brake fluid, Gates 7370 V-belt", "doc_id": "DOC-020"},
    {"date": "2015-02-21", "event": "V-belt exchanged 7370 to 7365 (final fitment); 6 ft fuel hose purchased minutes later", "doc_id": "DOC-021, DOC-022"},
    {"date": "2015-03-07", "event": "Ignition wire set (13:20), then K&N recharge kit (13:22), same visit", "doc_id": "DOC-008, DOC-007"},
    {"date": "2015-03-17", "event": "Transaxle gear lube purchased", "doc_id": "DOC-014"},
    {"date": "2015-03-18", "event": "Rubber plugs", "doc_id": "DOC-013"},
    {"date": "2015-03-28", "event": "O'Reilly purchase ~$48 net, line items illegible in photo (re-shoot)", "doc_id": "DOC-016"},
    {"date": "2015-04-09", "event": "Sylvania H6024XV sealed beam headlamps, pair", "doc_id": "DOC-017"},
    {"date": "2015-09-30", "event": "LED lights and Permatex copper spray sealant (possible engine assembly window)", "doc_id": "DOC-018"},
    {"date": "2016-02-29", "event": "Type 1 carburetor kit purchased at Meyers Auto Parts (attribution uncertain)", "doc_id": "DOC-024"},
    {"date": "2016-03-01", "event": "Threadlocker and 14mm thread-family Heli-Coil inserts", "doc_id": "DOC-010"},
    {"date": "2016-09-14", "event": "Roll pin purchase. New latest-dated document; restoration activity documented into Sep 2016", "doc_id": "DOC-009"}
])

# ---- New data gaps ----
d['data_gaps'].extend([
    {"gap_id": "GAP-13", "priority": "high", "item": "Paint system: Nason clearcoat activator confirmed (DOC-023). Locate basecoat/color and primer receipts to recover the exact paint color formula and product line. Boulder Auto Parts paint dept may retain the mix formula under customer B4925."},
    {"gap_id": "GAP-14", "priority": "high", "item": "DOC-016 (O'Reilly 2655-492277, 2015-03-28, ~$48.47 net): line items cut off in photo. Re-photograph flat and complete."},
    {"gap_id": "GAP-15", "priority": "medium", "item": "Identify 'EDE 224600 45 STREET' (4 units, DOC-020). Possibly carburetor jets. Verify against physical parts or O'Reilly part lookup."},
    {"gap_id": "GAP-16", "priority": "medium", "item": "Attribution check: Type 1 carb kit (DOC-024) and 1967 Beetle counter lookup (DOC-017) raise the question of whether every receipt in the folder belongs to the Ghia, or whether Mahan had another aircooled VW. Sort folder accordingly; tag any non-Ghia documents as excluded."}
])

# ---- Sort ledger and timeline ----
d['restoration_timeline'].sort(key=lambda e: (e['date'] is None, e['date'] or ''))

with open('/home/claude/ghia/ghia-1965-master-record-v2.json', 'w') as f:
    json.dump(d, f, indent=2)

print('v2 written')
print('documents:', len(d['document_archive']))
print('ledger entries:', len(d['parts_ledger']))
print('vendors:', len(d['vendor_registry']))
print('timeline events:', len(d['restoration_timeline']))
print('gaps:', len(d['data_gaps']))
# spend check
spend = sum(e.get('ext_price') or 0 for e in d['parts_ledger'])
print('documented spend (where priced): $%.2f' % spend)
