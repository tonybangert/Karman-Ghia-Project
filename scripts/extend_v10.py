import json

with open('data/versions/ghia-1965-master-record-v9.json') as f:
    d = json.load(f)

d['schema_version'] = '1.9'
d['generated_date'] = '2026-06-11'
d['generated_from'] = 'Batches 1-10 (DOC-001 to DOC-062)'

# ============ New document: photographic record of the finished car ============
d['document_archive'].append(
    {"doc_id": "DOC-062", "type": "Photographic record (5 photos)", "vendor_id": None,
     "title": "Owner photo set: the car as completed (interior, engine bay, exterior, registration)",
     "reference_numbers": {}, "date": None, "line_item_count": 0,
     "photos": {
        "a": "Interior/dash: banjo steering wheel, instrument cluster, JBugs grey interior installed",
        "b": "Engine bay: DTM shroud, dual Webers, billet alternator stand",
        "c": "Rear in garage: Wisconsin registration ZZ65KG (current owner)",
        "d": "Front three-quarter, red-rock desert backdrop: paint, wheels, stance, trim",
        "e": "Rear, desert: exhaust, rear scripts, tail lights, LED strips"
     },
     "extraction_note": ("FIRST PHOTOGRAPHIC RECORD OF THE FINISHED CAR, supplied by the current owner to verify the "
        "paper archive against the physical machine. Image files retained by the owner; not stored in this "
        "repository (see roadmap item: photo library). Key verifications and findings: (1) WHEELS: the installed "
        "wheels are flat-five-spoke 911/Fuchs-style alloys with black spoke recesses, polished lips, and small "
        "chrome center caps; they are NOT the Sprintstar pattern that the 319-655 center cap order implied "
        "(corrects GAP-17, advances GAP-23: the 16pc 14mm chrome lug bolt set fits this 4x130-pattern style, "
        "while the 12mm sets and Sprintstar caps likely belong to an uninstalled or returned set). (2) DASH: 110mm "
        "speedometer with trip button and odometer reading 000877, consistent with the ISP West programmable unit "
        "(DOC-058), roughly 877 miles since restoration; one 2-1/16in gauge mounted right of the speedometer above "
        "a larger round instrument, and two more 2-1/16in chrome-bezel gauges center dash below the radio aperture, "
        "consistent with the three Mid America gauges (DOC-056), faces not readable at this resolution. (3) ENGINE "
        "BAY: Raby DTM Stage III black upright shroud with flexible intake duct, dual Weber carburetors with chrome "
        "oval gauze filters and hex-bar cross linkage, alternator on the Raby billet stand with integrated oil "
        "filler: DOC-001 hardware verified installed. (4) EXHAUST: polished sidewinder-style merged-collector "
        "system exiting right, consistent with A-1 Performance (DOC-060). (5) PAINT: light silver-blue metallic "
        "over black rockers (visual; formula name still open under GAP-13), chrome sharp-edge side molding, "
        "VOLKSWAGEN block and cursive Ghia rear scripts installed (DOC-055), euro tail lights, LED strips at the "
        "license plate and below the decklid (consistent with the DOC-018 LED purchase). (6) INTERIOR: JBugs grey "
        "velour kit verified installed (door panels, charcoal carpet, grey velour seats, grey 2-point belts with "
        "chrome latches, passenger door armrest per DOC-061); woven coco mats and a silver banjo-style steering "
        "wheel with decorative horn button and polished drilled column drop are present but UNDOCUMENTED in the "
        "purchase record. (7) REGISTRATION: Wisconsin plate ZZ65KG on the car in the current owner's garage.")})

# ============ Vehicle master record: current state ============
vmr = d['vehicle_master_record']
for o in vmr['ownership_chain']:
    if o.get('role') == 'Current owner':
        o['registration'] = "Wisconsin plate ZZ65KG (photographed, DOC-062c)"
vmr['odometer_observed'] = ("000877 on the 110mm speedometer (DOC-062a, undated photo): roughly 877 miles since "
                            "the instrument was installed/reset during restoration")
vmr['as_completed_photo_record'] = "DOC-062"

# ============ Timeline (undated, kept in doc-id order before DOC-043) ============
tl = d['restoration_timeline']
idx = next((i for i, e in enumerate(tl) if e.get('date') is None and e['doc_id'] == 'DOC-043'), len(tl))
tl.insert(idx, {"date": None,
    "event": ("Undated: owner photo set of the finished car verifies the archive against the machine: Fuchs-style "
              "wheels installed (not Sprintstars), DTM/Weber engine bay, A-1 style exhaust, JBugs interior, "
              "odometer 877, Wisconsin registration"),
    "doc_id": "DOC-062"})

# ============ Build spec cards ============
eng = d['build_spec_cards']['engine']
eng['as_installed_verification'] = ("Photo-verified (DOC-062b): DTM Stage III black upright shroud with flexible "
    "intake duct, dual Webers with chrome oval gauze air filters and hex-bar cross linkage, alternator on Raby "
    "billet stand with integrated oil filler, body-color engine bay with black tins.")
if "DOC-062" not in eng['sources']:
    eng['sources'].append("DOC-062")

exh = d['build_spec_cards']['exhaust']
exh['as_installed_verification'] = ("Photo-verified (DOC-062e): polished sidewinder-style merged-collector system "
    "exiting right of the rear apron, consistent with the A-1 Performance literature (DOC-060).")
if "DOC-062" not in exh['sources']:
    exh['sources'].append("DOC-062")

wt = d['build_spec_cards']['wheels_tires']
wt['wheels'] = ("INSTALLED (photo-verified, DOC-062d): flat-five-spoke 911/Fuchs-style alloys, black spoke recesses, "
    "polished lips, small chrome center caps; brand and size not yet read from the wheel. This CORRECTS the earlier "
    "Sprintstar inference: the 319-655 Sprintstar center caps bought in 2015 do not match the installed wheels and "
    "likely belong to an uninstalled or returned set (GAP-23).")
wt['lug_hardware'] = ("The 16pc chrome 14mm set (319-994, DOC-028) matches the installed 4-lug Fuchs-style wheels. "
    "The four 5-bolt sets of chrome 12mm (319-991, DOC-056) imply a 5-lug set that is not on the car.")
wt['center_caps'] = ("Installed wheels wear small chrome caps (DOC-062d), not obviously the 319-655 Sprintstar "
    "caps; the Sprintstar caps and 'for iron' caps from order 04682256 are unaccounted for on the car (GAP-23).")
if "DOC-062" not in wt['sources']:
    wt['sources'].append("DOC-062")

bp = d['build_spec_cards']['body_paint']
bp['color_visual'] = ("Light silver-blue metallic over black rocker panels (owner photos, DOC-062d/e). Formula "
    "name still open under GAP-13 (wa208v / GM 3295 references).")
bp['as_installed_verification'] = ("Photo-verified (DOC-062): chrome sharp-edge side molding, VOLKSWAGEN block and "
    "cursive Ghia rear scripts (DOC-055 parts), euro tail lights, chrome bumpers, LED strips at license plate and "
    "below decklid (consistent with DOC-018), lowered stance consistent with the 2.5in drop spindles.")
if "DOC-062" not in bp['sources']:
    bp['sources'].append("DOC-062")

inter = d['build_spec_cards']['interior']
inter['as_installed_verification'] = ("Photo-verified (DOC-062a): grey velour door panels, charcoal carpet, grey "
    "velour seats, grey 2-point belts with chrome latches, passenger door armrest. Present but UNDOCUMENTED in the "
    "purchase record: woven coco floor mats, and a silver banjo-style steering wheel with decorative horn button "
    "on a polished drilled column drop.")
if "DOC-062" not in inter['sources']:
    inter['sources'].append("DOC-062")

inst = d['build_spec_cards']['instrumentation']
inst['as_installed_verification'] = ("Photo-verified (DOC-062a): 110mm speedometer with trip button, odometer "
    "000877, consistent with the ISP West unit (DOC-058); one 2-1/16in gauge right of the speedometer above a "
    "larger round instrument, plus two 2-1/16in chrome-bezel gauges center dash below the radio aperture, "
    "consistent with the three Mid America gauges (DOC-056). Gauge faces not readable; close-ups would finish "
    "GAP-20.")
if "DOC-062" not in inst['sources']:
    inst['sources'].append("DOC-062")

# ============ Gap movement ============
for g in d['data_gaps']:
    if g['gap_id'] == 'GAP-07':
        g['resolution'] = g['resolution'] + (" Batch 10: owner photos (DOC-062e) show a polished sidewinder-style "
            "merged-collector system on the car, visually consistent with A-1 Performance.")
    if g['gap_id'] == 'GAP-13':
        g['resolution'] = g['resolution'] + (" Batch 10: owner photos (DOC-062d/e) show the color as a light "
            "silver-blue metallic over black rockers; the formula-to-name translation remains open.")
    if g['gap_id'] == 'GAP-17':
        g['resolution'] = ("Batch 6 inferred Sprintstar wheels from the 319-655 center cap order (DOC-049). "
            "Batch 10 CORRECTED this from owner photos (DOC-062d): the installed wheels are flat-five-spoke "
            "911/Fuchs-style alloys with small chrome caps, matched by the 16pc 14mm chrome lug bolts (DOC-028). "
            "Remaining: wheel brand/size from a stamp or close-up, and the tire spec (GAP-12).")
    if g['gap_id'] == 'GAP-20':
        g['resolution'] = g['resolution'] + (" Batch 10: dash photographed (DOC-062a): 110mm speedometer "
            "consistent with the ISP West unit, odometer 000877, three small gauges placed one high right of the "
            "speedometer and two center dash. Faces not readable; close-ups would close this gap.")
    if g['gap_id'] == 'GAP-23':
        g['status'] = 'PARTIALLY RESOLVED'
        g['resolution'] = ("Batch 10: owner photos (DOC-062d) show the installed wheels are 911/Fuchs-style "
            "(consistent with 4-lug 14mm, the DOC-028 bolt set), so the 12mm 5-bolt sets and the Sprintstar caps "
            "from order 04682256 evidently belong to a set that is not on the car (returned, planned, or spare). "
            "Remaining: physically confirm lug size/pattern, read the wheel brand stamp, and account for the "
            "Sprintstar caps and 12mm bolts.")
d['data_gaps'].append({
    "gap_id": "GAP-24", "priority": "low",
    "item": ("Banjo-style steering wheel (silver, decorative horn button, polished drilled column drop) and woven "
             "coco floor mats are installed (DOC-062a) but appear nowhere in the purchase record. Identify maker "
             "(wheel likely Flat4/EMPI pattern) and source if paperwork ever surfaces.")
})

# ============ Write v10 ============
with open('data/versions/ghia-1965-master-record-v10.json', 'w') as f:
    json.dump(d, f, indent=1)
with open('data/master-record.json', 'w') as f:
    json.dump(d, f, indent=1)

print("v10 written:",
      len(d['document_archive']), "docs,",
      len(d['parts_ledger']), "ledger,",
      len(d['vendor_registry']), "vendors,",
      len(d['restoration_timeline']), "events,",
      len(d['data_gaps']), "gaps,",
      "spend", round(sum(e['ext_price'] for e in d['parts_ledger'] if e.get('ext_price')), 2))
