import json

with open('data/versions/ghia-1965-master-record-v7.json') as f:
    d = json.load(f)

d['schema_version'] = '1.7'
d['generated_date'] = '2026-06-11'
d['generated_from'] = 'Batches 1-8 (DOC-001 to DOC-059)'

# ============ New vendor ============
d['vendor_registry'].append(
    {"vendor_id": "VEN-18", "name": "ISP West (VW Restoration Parts)",
     "address": "20925 Brant Ave, Carson, CA 90810-1001",
     "phones": {"main": "310-637-2100", "fax": "310-637-1019"},
     "web": "www.vwispwest.com",
     "specialty": "VW restoration parts manufacturer; programmable speedometers and instruments",
     "documents": ["DOC-058"],
     "note": "Referenced only via the speedometer instruction manual (DOC-058); no purchase invoice for the speedometer is in the archive."})

# ============ New documents (product literature, no priced line items) ============
d['document_archive'].extend([
    {"doc_id": "DOC-058", "type": "Instruction manual (product literature)", "vendor_id": "VEN-18",
     "title": "ISP West speedometer instruction manual: 110mm VW programmable speedometer",
     "reference_numbers": {}, "date": None, "page_count": 2, "line_item_count": 0,
     "extraction_note": ("Two-sided instruction sheet for an ISP West programmable VW speedometer: 110mm standard VW "
        "diameter, M18 x 1.5 cable thread, mechanical speedometer with double odometer (pedometer) and integrated "
        "indicator lights (turn/blink alert, oil pressure, battery/charge, high beam), driven off the left front "
        "wheel hub cable. IDENTIFIES THE SPEEDOMETER HEAD (instrumentation, GAP-20). No price, invoice number, or "
        "date: this is product literature, not a transaction, so it generates no ledger entry, and the speedometer "
        "purchase itself is not documented in the archive. ATTRIBUTION NOTE: the manual states 'Exclusively for "
        "Volkswagen Beetle'; the Ghia shares the VW speedometer cable and drive, and a Beetle/aftermarket speedometer "
        "in a restored Ghia is plausible, but confirm the installed unit is this one (cf. GAP-16).")},
    {"doc_id": "DOC-059", "type": "Product literature (3 connection diagrams)", "vendor_id": "VEN-09",
     "title": "Mid America gauge connection diagrams: 111-150 oil pressure, 111-152 voltmeter, 111-155 electric temperature",
     "reference_numbers": {"forms": "111150-073003, 111152-062003, 111155-073003"},
     "date": None, "line_item_count": 0, "related_documents": ["DOC-056"],
     "extraction_note": ("Three Mid America Motorworks connection-diagram sheets (copyright 2007) that accompanied the "
        "gauges purchased on order 04682256 (DOC-056, 2015-04-20): the 111-150 oil pressure gauge (EOPG, gauge + "
        "pressure sender + battery), the 111-152 voltmeter (gauge + battery), and the 111-155 electric temperature "
        "gauge (ETG, gauge + temp sender + battery). Confirms the gauge identities recorded as P-205/P-206/P-207. "
        "Two observations: the 111-155 is titled an 'Electric Temperature Gauge' (used here for oil temperature), and "
        "the 111-150 oil pressure diagram requires a pressure sender that is not separately documented in the "
        "archive. No prices or dates: product literature, no ledger entry.")},
])

# ============ Cross-reference the gauge ledger entries to their diagrams ============
for e in d['parts_ledger']:
    if e['entry_id'] == 'P-205':
        e['notes'] = ("Gauge head (GAP-20). 2-1/16in electric oil pressure gauge. Connection diagram in DOC-059; that "
                      "diagram shows a pressure sender, which is not separately documented in the archive.")
    if e['entry_id'] == 'P-206':
        e['item_name'] = "Electric Temperature Gauge, 2-1/16in (used for oil temperature)"
        e['notes'] = ("Gauge head (GAP-20). Invoice description 'OIL TEMP GAUGE, EACH VEE THREE'; the connection "
                      "diagram (DOC-059) titles it an 'Electric Temperature Gauge'. Pairs with a temp sender (111157 "
                      "backordered; 196-107 bought Dec 2015, P-091).")
    if e['entry_id'] == 'P-207':
        e['notes'] = "Gauge head (GAP-20). Connection diagram in DOC-059."

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

# ============ Timeline cleanup: drop stale undated duplicates ============
# DOC-001 (Raby kit) and DOC-003 (head work) carry both a dated event and a
# leftover undated 'date unknown' event from before Batches 5 and 7 fixed their
# dates. Remove the stale undated duplicates; keep DOC-043 (genuinely undated).
d['restoration_timeline'] = [e for e in d['restoration_timeline']
    if not (e.get('date') is None and e['doc_id'] in ('DOC-001', 'DOC-003'))]

# ============ Timeline (undated literature entry) ============
tl = d['restoration_timeline']
idx = next((i for i, e in enumerate(tl) if e.get('date') is None), len(tl))
tl.insert(idx, {"date": None,
    "event": ("Undated: ISP West 110mm programmable VW speedometer documented via its instruction manual "
              "(speedometer head identified; no purchase invoice in archive)"),
    "doc_id": "DOC-058"})

# ============ Build spec card: instrumentation ============
inst = d['build_spec_cards']['instrumentation']
inst.pop('gauges', None)  # stale field superseded by gauge_heads/senders
inst['speedometer'] = ("ISP West 110mm programmable VW speedometer (M18 x 1.5 cable, driven off the left front wheel "
    "hub), with double odometer and integrated indicator lights for turn signals, oil pressure, battery/charge, and "
    "high beam. Documented via its instruction manual (DOC-058); the purchase itself is not in the archive. The "
    "manual is Beetle-specific, so confirm the installed unit (cf. GAP-16).")
inst['gauge_heads'] = ("Three Mid America 2-1/16in gauges from order 04682256 shipped 2015-04-20 (DOC-056), confirmed "
    "by their connection diagrams (DOC-059): oil pressure gauge 12V (111-150), electric temperature gauge used for "
    "oil temp (111-155), and an 8-16V voltmeter (111-152). The oil pressure gauge needs a pressure sender that is "
    "not separately documented.")
for s in ("DOC-058", "DOC-059"):
    if s not in inst['sources']:
        inst['sources'].append(s)

# ============ Gap movement ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-20':
        g['resolution'] = ("Batch 7: gauge heads identified as Mid America 2-1/16in units (DOC-056). Batch 8: those "
            "three gauges confirmed by their connection diagrams (DOC-059, oil pressure 111-150, voltmeter 111-152, "
            "electric temperature 111-155), and the speedometer head identified as an ISP West 110mm programmable VW "
            "unit via its instruction manual (DOC-058). Remaining: confirm the cluster against dash photos; the oil "
            "pressure sender is undocumented; the speedometer purchase invoice is not in the archive; and which temp "
            "sender (Auto Meter 2258, 196-107, or backordered 111157) feeds the temperature gauge is unresolved.")

# ============ Write v8 ============
with open('data/versions/ghia-1965-master-record-v8.json', 'w') as f:
    json.dump(d, f, indent=1)
with open('data/master-record.json', 'w') as f:
    json.dump(d, f, indent=1)

print("v8 written:",
      len(d['document_archive']), "docs,",
      len(d['parts_ledger']), "ledger,",
      len(d['vendor_registry']), "vendors,",
      len(d['restoration_timeline']), "events,",
      len(d['data_gaps']), "gaps,",
      "spend", round(sum(e['ext_price'] for e in d['parts_ledger'] if e.get('ext_price')), 2))
