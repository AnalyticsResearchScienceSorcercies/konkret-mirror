"""
swap_banner_photos.py
Replace poor banner/split images with the best field photos from the collection.
"""
import os

BASE = r"C:\Users\wesle\Desktop\konkret-mirror"

SWAPS = [
    # (filename, old_string, new_string, description)

    # index.html hero: distant field -> smiling woman, blue sky
    ("index.html",
     'src="photos/2025-aout/IMG-20250730-WA0360.jpg"',
     'src="photos/2025-aout/IMG-20250824-WA0460.jpg"',
     "hero: WA0360 -> WA0460 (smiling woman, blue sky)"),

    # index.html WHAT IS KONKRET split: dispensary meeting -> workers in labeled plots
    ("index.html",
     'src="photos/2025-juillet/IMG-20250711-WA0196.jpg"',
     'src="photos/2025-juillet/IMG-20250712-WA0162.jpg"',
     "split: WA0196 (meeting) -> WA0162 (field plots)"),

    # index.html section break before VALUES: dispensary meeting -> wide field
    ("index.html",
     'src="photos/2025-juillet/IMG-20250711-WA0199.jpg"',
     'src="photos/2025-aout/IMG-20250730-WA0360.jpg"',
     "break: WA0199 (meeting) -> WA0360 (wide field)"),

    # summer-2026 hero bg: dispensary meeting -> KONKRET banner + blue sky
    ("summer-2026.html",
     'src="photos/2025-juillet/IMG-20250711-WA0196.jpg"',
     'src="photos/2025-mars/IMG-20250325-WA0113.jpg"',
     "hero: WA0196 (meeting) -> WA0113 (banner + blue sky)"),

    # notre-histoire founding story split: seated meeting -> full group lineup
    ("notre-histoire.html",
     'src="photos/2025-mars/IMG-20250319-WA0393.jpg"',
     'src="photos/2025-juillet/IMG-20250711-WA0218.jpg"',
     "split: WA0393 (meeting) -> WA0218 (full group)"),

    # notre-histoire TIMELINE break: seeds close-up -> group working with banner
    ("notre-histoire.html",
     'src="photos/2025-mars/IMG-20250323-WA0036.jpg"',
     'src="photos/2025-mars/IMG-20250323-WA0034.jpg"',
     "break: WA0036 (seeds bag) -> WA0034 (crew working, banner)"),

    # a-propos visual break: WordPress PNG -> watering in field with mountains
    ("a-propos.html",
     'src="wp-content/uploads/brizy/imgs/12-860x664x0x88x860x488x1749174738.png"',
     'src="photos/2025-aout/IMG-20250824-WA0458.jpg"',
     "visual break: WP image -> WA0458 (watering, mountains)"),

    # a-propos visual break: also increase height and fix alt
    ("a-propos.html",
     'style="overflow:hidden; max-height:260px;"',
     'style="overflow:hidden; max-height:400px;"',
     "visual break: height 260 -> 400px"),

    # a-propos alt text
    ("a-propos.html",
     'alt="KONKRET -- présence de marque"',
     'alt="Jeune participant KONKRET arrosant les cultures, Grand Bassin, Milot"',
     "visual break: update alt text"),

    # a-propos: remove brightness filter (field photo doesn't need it)
    ("a-propos.html",
     'style="object-position: center; filter: brightness(0.7);"',
     'style="object-position: center 30%;"',
     "visual break: remove dim filter"),

    # employer.html field photo: banana tree / no people -> watering + mountains
    ("employer.html",
     'src="photos/2025-aout/IMG-20250801-WA0131.jpg"',
     'src="photos/2025-aout/IMG-20250824-WA0458.jpg"',
     "field photo: WA0131 (banana tree) -> WA0458 (watering, mountains)"),

    # employer.html: update alt text
    ("employer.html",
     'alt="Encadrement des jeunes KONKRET sur le terrain -- suivi employeur"',
     'alt="Jeune participant KONKRET au travail dans les champs, Grand Bassin"',
     "employer: update alt text"),
]


def run():
    changed = {}
    for filename, old, new, desc in SWAPS:
        path = os.path.join(BASE, filename)
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        if old in html:
            html = html.replace(old, new, 1)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            changed.setdefault(filename, []).append(f"  OK: {desc}")
        else:
            changed.setdefault(filename, []).append(f"  SKIP (not found): {desc}")

    for fname, results in changed.items():
        print(f"\n{fname}")
        for r in results:
            print(r)

    print("\nDone.")


run()
