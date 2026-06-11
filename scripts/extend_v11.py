import json

with open('data/versions/ghia-1965-master-record-v10.json') as f:
    d = json.load(f)

d['schema_version'] = '1.10'
d['generated_date'] = '2026-06-11'
d['generated_from'] = 'Batches 1-11 (DOC-001 to DOC-063)'

# ============ New document: pre-restoration photographs ============
d['document_archive'].append(
    {"doc_id": "DOC-063", "type": "Photographic record (3 printed photographs, rephotographed)", "vendor_id": None,
     "title": "Pre-restoration photo set: the $500 car as acquired (green, rusted, on a trailer)",
     "reference_numbers": {}, "date": None, "line_item_count": 0,
     "photos": {
        "a": "Side profile on a trailer: oxidized green paint, rust-through and primer patches along rockers and door bottoms, steel wheels with hubcaps",
        "b": "Rear three-quarter: primer/bare metal on rear lower quarters, taillight lens missing, rear bumper absent, exhaust pipe protruding, quarter vent trim present",
        "c": "Front three-quarter at a wooden building: nose and front valance damage, oxidized dark green paint, glass present"
     },
     "extraction_note": ("PRE-RESTORATION CONDITION RECORD: three printed photographs (rephotographed from the prints, "
        "which survive with the project's papers; print files retained by the owner, not stored in this repository). "
        "Undated; the condition places them at or near the $500 acquisition, before the 2014 Utah body/paint phase. "
        "What they establish: (1) PRE-RESTORATION COLOR was green, heavily oxidized, over widespread rust-through "
        "and dotted primer patches along the lower body; whether it is the factory color is unknown (GAP-01 paint "
        "code still open). (2) BODY DAMAGE corroborates the handwritten cost ledger's prep lines (DOC-043: media "
        "blast, Bondo, Dolphin Glaze, fiberglass, 'Nose & fender & Hood Replacement parts', primer stages): visible "
        "nose/front valance damage, rust along rockers and door bottoms, rear lower quarters in primer/bare metal, "
        "one taillight lens missing, rear bumper absent. (3) WHEELS: the car sat on steel wheels with hubcaps, "
        "which finally explains the backordered 'CENTER CAP, CHROME, FOR IRON' parts and decals on Mid America "
        "order 04682256-00001 (DOC-056): dress-up parts for the original steel (iron) wheels, presumably abandoned "
        "when the disc-conversion/alloy direction won out (GAP-23). (4) The car is on a trailer in two frames: "
        "transport day, consistent with the acquisition or the move to the body shop. (5) Glass present "
        "pre-restoration. Also useful for GAP-16: the project car was demonstrably this green Ghia.")})

# ============ Vehicle master record ============
vmr = d['vehicle_master_record']
vmr['pre_restoration_condition'] = ("Photographed before restoration (DOC-063): oxidized green paint (factory color "
    "unknown, GAP-01), rust-through along rockers and door bottoms, primer patches, nose/front valance damage, rear "
    "quarters in primer, one taillight lens missing, rear bumper absent, on steel wheels with hubcaps. Corroborates "
    "the DOC-043 body-prep cost lines.")
vmr['as_acquired_photo_record'] = "DOC-063"

# ============ Timeline (undated, doc-id order before DOC-043's closing entry) ============
tl = d['restoration_timeline']
idx = next((i for i, e in enumerate(tl) if e.get('date') is None and e['doc_id'] == 'DOC-043'), len(tl))
tl.insert(idx, {"date": None,
    "event": ("Undated (pre-2014): three surviving prints show the car as acquired: oxidized green, lower-body "
              "rust-through, nose damage, on steel wheels with hubcaps, riding a trailer"),
    "doc_id": "DOC-063"})

# ============ Build spec cards ============
bp = d['build_spec_cards']['body_paint']
bp['pre_restoration'] = ("Photographed before restoration (DOC-063): oxidized green over rust-through and primer "
    "patches, damaged nose/front valance, rear quarters in primer, taillight lens missing, rear bumper absent. "
    "Explains the DOC-043 prep spend (media blast, Bondo, Dolphin Glaze, fiberglass, replacement nose/fender/hood "
    "panels, multiple primer stages). Factory paint code still unknown (GAP-01).")
if "DOC-063" not in bp['sources']:
    bp['sources'].append("DOC-063")

wt = d['build_spec_cards']['wheels_tires']
wt['pre_restoration_wheels'] = ("Steel wheels with hubcaps (DOC-063). This explains the 'center cap, chrome, for "
    "iron' parts and chrome decals backordered on Mid America order 04682256-00001 (DOC-056): dress-up for the "
    "original steel wheels, evidently abandoned in favor of the alloy direction (GAP-23).")
if "DOC-063" not in wt['sources']:
    wt['sources'].append("DOC-063")

# ============ Gap movement ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-16':
        g['note'] = ("Batch 11: the pre-restoration photos (DOC-063) confirm the project car itself: a green Ghia "
                     "coupe. The attribution question for the Type 1 carb kit and 1967 Beetle lookup remains open.")
    if g['gap_id'] == 'GAP-23':
        g['resolution'] = (g['resolution'] + " Batch 11: the pre-restoration photos (DOC-063) show the car arrived "
            "on steel wheels with hubcaps, so the 'for iron' chrome caps and decals were evidently dress-up for the "
            "original steel wheels, abandoned when the disc-conversion/alloy direction won out. Remaining: physical "
            "lug confirmation on the installed alloys and the fate of the Sprintstar caps and 12mm bolts.")

# ============ Write v11 ============
with open('data/versions/ghia-1965-master-record-v11.json', 'w') as f:
    json.dump(d, f, indent=1)
with open('data/master-record.json', 'w') as f:
    json.dump(d, f, indent=1)

print("v11 written:",
      len(d['document_archive']), "docs,",
      len(d['parts_ledger']), "ledger,",
      len(d['vendor_registry']), "vendors,",
      len(d['restoration_timeline']), "events,",
      len(d['data_gaps']), "gaps,",
      "spend", round(sum(e['ext_price'] for e in d['parts_ledger'] if e.get('ext_price')), 2))
