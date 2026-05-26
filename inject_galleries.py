"""
inject_galleries.py
Inserts photo gallery sections into all KONKRET site pages before <footer class="kn-footer">
"""
import os, re

BASE = r"C:\Users\wesle\Desktop\konkret-mirror"

# --------------------------------------------------------------------------
# Photo pool by folder (already copied into repo)
# --------------------------------------------------------------------------
MARS = [f"2025-mars/{f}" for f in [
    "IMG-20250319-WA0391.jpg","IMG-20250319-WA0392.jpg","IMG-20250319-WA0393.jpg",
    "IMG-20250319-WA0394.jpg","IMG-20250319-WA0400.jpg","IMG-20250319-WA0401.jpg",
    "IMG-20250319-WA0402.jpg","IMG-20250319-WA0403.jpg","IMG-20250319-WA0404.jpg",
    "IMG-20250319-WA0420.jpg","IMG-20250319-WA0421.jpg","IMG-20250319-WA0422.jpg",
    "IMG-20250322-WA0051.jpg","IMG-20250322-WA0053.jpg","IMG-20250322-WA0054.jpg",
    "IMG-20250323-WA0031.jpg","IMG-20250323-WA0032.jpg","IMG-20250323-WA0033.jpg",
    "IMG-20250323-WA0034.jpg","IMG-20250323-WA0035.jpg","IMG-20250323-WA0036.jpg",
    "IMG-20250323-WA0037.jpg","IMG-20250323-WA0038.jpg","IMG-20250323-WA0039.jpg",
    "IMG-20250323-WA0040.jpg","IMG-20250323-WA0041.jpg","IMG-20250323-WA0042.jpg",
    "IMG-20250323-WA0043.jpg","IMG-20250323-WA0047.jpg","IMG-20250323-WA0048.jpg",
    "IMG-20250323-WA0049.jpg","IMG-20250323-WA0050.jpg","IMG-20250323-WA0051.jpg",
    "IMG-20250323-WA0052.jpg","IMG-20250323-WA0053.jpg","IMG-20250323-WA0054.jpg",
    "IMG-20250323-WA0055.jpg","IMG-20250323-WA0056.jpg","IMG-20250323-WA0057.jpg",
    "IMG-20250325-WA0113.jpg","IMG-20250325-WA0116.jpg","IMG-20250325-WA0117.jpg",
    "IMG-20250325-WA0118.jpg","IMG-20250325-WA0119.jpg","IMG-20250325-WA0120.jpg",
    "IMG-20250325-WA0121.jpg","IMG-20250325-WA0122.jpg","IMG-20250325-WA0123.jpg",
    "IMG-20250325-WA0124.jpg","IMG-20250325-WA0159.jpg","IMG-20250325-WA0234.jpg",
    "IMG-20250325-WA0235.jpg","IMG-20250326-WA0099.jpg","IMG-20250326-WA0100.jpg",
    "IMG-20250326-WA0102.jpg","IMG-20250326-WA0103.jpg","IMG-20250326-WA0104.jpg",
    "IMG-20250326-WA0105.jpg","IMG-20250326-WA0106.jpg","IMG-20250326-WA0107.jpg",
    "IMG-20250326-WA0145.jpg","IMG-20250326-WA0146.jpg",
]]

JUIL = [f"2025-juillet/{f}" for f in [
    "IMG-20250707-WA0075.jpg","IMG-20250707-WA0076.jpg","IMG-20250707-WA0078.jpg",
    "IMG-20250707-WA0081.jpg","IMG-20250707-WA0088.jpg","IMG-20250707-WA0089.jpg",
    "IMG-20250707-WA0091.jpg","IMG-20250707-WA0092.jpg","IMG-20250707-WA0093.jpg",
    "IMG-20250707-WA0096.jpg","IMG-20250707-WA0097.jpg","IMG-20250707-WA0098.jpg",
    "IMG-20250707-WA0099.jpg","IMG-20250707-WA0100.jpg","IMG-20250707-WA0102.jpg",
    "IMG-20250710-WA0125.jpg","IMG-20250710-WA0126.jpg","IMG-20250710-WA0128.jpg",
    "IMG-20250710-WA0129.jpg","IMG-20250710-WA0320.jpg","IMG-20250710-WA0321.jpg",
    "IMG-20250710-WA0322.jpg","IMG-20250710-WA0323.jpg","IMG-20250711-WA0034.jpg",
    "IMG-20250711-WA0035.jpg","IMG-20250711-WA0193.jpg","IMG-20250711-WA0195.jpg",
    "IMG-20250711-WA0196.jpg","IMG-20250711-WA0197.jpg","IMG-20250711-WA0198.jpg",
    "IMG-20250711-WA0199.jpg","IMG-20250711-WA0200.jpg","IMG-20250711-WA0201.jpg",
    "IMG-20250711-WA0202.jpg","IMG-20250711-WA0203.jpg","IMG-20250711-WA0204.jpg",
    "IMG-20250711-WA0205.jpg","IMG-20250711-WA0209.jpg","IMG-20250711-WA0210.jpg",
    "IMG-20250711-WA0211.jpg","IMG-20250711-WA0218.jpg","IMG-20250711-WA0219.jpg",
    "IMG-20250711-WA0220.jpg","IMG-20250711-WA0221.jpg","IMG-20250711-WA0222.jpg",
    "IMG-20250711-WA0223.jpg","IMG-20250711-WA0224.jpg","IMG-20250711-WA0225.jpg",
    "IMG-20250711-WA0226.jpg","IMG-20250711-WA0227.jpg","IMG-20250711-WA0228.jpg",
    "IMG-20250711-WA0229.jpg","IMG-20250711-WA0230.jpg","IMG-20250711-WA0231.jpg",
    "IMG-20250711-WA0235.jpg","IMG-20250712-WA0146.jpg","IMG-20250712-WA0147.jpg",
    "IMG-20250712-WA0150.jpg","IMG-20250712-WA0151.jpg","IMG-20250712-WA0153.jpg",
    "IMG-20250712-WA0154.jpg","IMG-20250712-WA0155.jpg","IMG-20250712-WA0157.jpg",
    "IMG-20250712-WA0158.jpg","IMG-20250712-WA0159.jpg","IMG-20250712-WA0160.jpg",
    "IMG-20250712-WA0162.jpg","IMG-20250712-WA0168.jpg","IMG-20250712-WA0169.jpg",
    "IMG-20250712-WA0170.jpg","IMG-20250712-WA0171.jpg","IMG-20250712-WA0172.jpg",
    "IMG-20250712-WA0173.jpg","IMG-20250712-WA0174.jpg","IMG-20250712-WA0175.jpg",
    "IMG-20250712-WA0176.jpg","IMG-20250712-WA0177.jpg","IMG-20250712-WA0178.jpg",
    "IMG-20250712-WA0179.jpg","IMG-20250712-WA0181.jpg","IMG-20250712-WA0182.jpg",
    "IMG-20250712-WA0183.jpg","IMG-20250712-WA0184.jpg","IMG-20250712-WA0185.jpg",
    "IMG-20250712-WA0186.jpg",
]]

AOUT = [f"2025-aout/{f}" for f in [
    "IMG-20250705-WA0057.jpg","IMG-20250705-WA0063.jpg","IMG-20250712-WA0139.jpg",
    "IMG-20250730-WA0360.jpg","IMG-20250730-WA0361.jpg","IMG-20250730-WA0362.jpg",
    "IMG-20250730-WA0363.jpg","IMG-20250730-WA0443.jpg","IMG-20250731-WA0001.jpg",
    "IMG-20250731-WA0002.jpg","IMG-20250731-WA0003.jpg","IMG-20250731-WA0008.jpg",
    "IMG-20250731-WA0009.jpg","IMG-20250731-WA0011.jpg","IMG-20250731-WA0013.jpg",
    "IMG-20250731-WA0018.jpg","IMG-20250731-WA0019.jpg","IMG-20250731-WA0020.jpg",
    "IMG-20250731-WA0091.jpg","IMG-20250731-WA0093.jpg","IMG-20250731-WA0094.jpg",
    "IMG-20250731-WA0095.jpg","IMG-20250731-WA0155.jpg","IMG-20250731-WA0156.jpg",
    "IMG-20250731-WA0159.jpg","IMG-20250731-WA0160.jpg","IMG-20250731-WA0206.jpg",
    "IMG-20250731-WA0270.jpg","IMG-20250731-WA0271.jpg","IMG-20250731-WA0272.jpg",
    "IMG-20250731-WA0284.jpg","IMG-20250801-WA0131.jpg","IMG-20250801-WA0132.jpg",
    "IMG-20250801-WA0142.jpg","IMG-20250801-WA0143.jpg","IMG-20250801-WA0144.jpg",
    "IMG-20250801-WA0152.jpg","IMG-20250801-WA0153.jpg","IMG-20250801-WA0157.jpg",
    "IMG-20250801-WA0162.jpg","IMG-20250801-WA0193.jpg","IMG-20250801-WA0194.jpg",
    "IMG-20250801-WA0210.jpg","IMG-20250801-WA0211.jpg","IMG-20250801-WA0212.jpg",
    "IMG-20250801-WA0223.jpg","IMG-20250801-WA0225.jpg","IMG-20250801-WA0231.jpg",
    "IMG-20250801-WA0232.jpg","IMG-20250801-WA0233.jpg","IMG-20250801-WA0236.jpg",
    "IMG-20250801-WA0238.jpg","IMG-20250801-WA0240.jpg","IMG-20250801-WA0268.jpg",
    "IMG-20250801-WA0270.jpg","IMG-20250801-WA0271.jpg","IMG-20250801-WA0374.jpg",
    "IMG-20250801-WA0377.jpg","IMG-20250801-WA0378.jpg","IMG-20250801-WA0382.jpg",
    "IMG-20250802-WA0122.jpg","IMG-20250802-WA0123.jpg","IMG-20250802-WA0229.jpg",
    "IMG-20250802-WA0230.jpg","IMG-20250802-WA0231.jpg","IMG-20250802-WA0233.jpg",
    "IMG-20250802-WA0234.jpg","IMG-20250802-WA0235.jpg","IMG-20250802-WA0236.jpg",
    "IMG-20250802-WA0237.jpg","IMG-20250802-WA0238.jpg","IMG-20250802-WA0239.jpg",
    "IMG-20250802-WA0240.jpg","IMG-20250802-WA0241.jpg","IMG-20250802-WA0242.jpg",
    "IMG-20250802-WA0243.jpg","IMG-20250802-WA0244.jpg","IMG-20250802-WA0245.jpg",
    "IMG-20250803-WA0137.jpg","IMG-20250822-WA0089.jpg","IMG-20250822-WA0090.jpg",
    "IMG-20250824-WA0124.jpg","IMG-20250824-WA0125.jpg","IMG-20250824-WA0126.jpg",
    "IMG-20250824-WA0128.jpg","IMG-20250824-WA0129.jpg","IMG-20250824-WA0130.jpg",
    "IMG-20250824-WA0141.jpg","IMG-20250824-WA0145.jpg","IMG-20250824-WA0194.jpg",
    "IMG-20250824-WA0195.jpg","IMG-20250824-WA0196.jpg","IMG-20250824-WA0197.jpg",
    "IMG-20250824-WA0199.jpg","IMG-20250824-WA0200.jpg","IMG-20250824-WA0282.jpg",
    "IMG-20250824-WA0283.jpg","IMG-20250824-WA0285.jpg","IMG-20250824-WA0287.jpg",
    "IMG-20250824-WA0288.jpg","IMG-20250824-WA0289.jpg","IMG-20250824-WA0291.jpg",
    "IMG-20250824-WA0292.jpg","IMG-20250824-WA0293.jpg","IMG-20250824-WA0454.jpg",
    "IMG-20250824-WA0455.jpg","IMG-20250824-WA0456.jpg","IMG-20250824-WA0457.jpg",
    "IMG-20250824-WA0458.jpg","IMG-20250824-WA0459.jpg","IMG-20250824-WA0460.jpg",
    "IMG-20250824-WA0461.jpg","IMG-20250824-WA0462.jpg","IMG-20250824-WA0464.jpg",
    "Photo from Jethro JS.jpg",
]]

SAK = [f"sakala/{f}" for f in [
    "IMG-20250822-WA0001.jpg","IMG-20250822-WA0002.jpg","IMG-20250822-WA0003.jpg",
    "IMG-20250822-WA0004.jpg","IMG-20250822-WA0005.jpg","IMG-20250822-WA0006.jpg",
    "IMG-20250822-WA0007.jpg","IMG-20250822-WA0008.jpg","IMG-20250822-WA0009.jpg",
    "IMG-20250822-WA0010.jpg",
]]

def gallery_html(photos, label="Photos du terrain -- KONKRET 2025"):
    items = "\n".join(
        f'      <div class="kn-gallery-item kn-img-frame">'
        f'<img src="photos/{p}" alt="KONKRET -- programme agricole, Haiti 2025" loading="lazy"></div>'
        for p in photos
    )
    return f"""
<section class="kn-gallery-section">
  <div class="kn-container">
    <p class="kn-gallery-label">{label}</p>
    <div class="kn-gallery-grid">
{items}
    </div>
  </div>
</section>
"""

# --------------------------------------------------------------------------
# Page -> photo batch assignments (9-12 photos each, varied per page)
# --------------------------------------------------------------------------
PAGE_PHOTOS = {
    "index.html":                              AOUT[31:40],
    "nos-actions.html":                        MARS[15:24],
    "summer-2026.html":                        SAK + JUIL[0:2],
    "notre-histoire.html":                     MARS[24:33],
    "a-propos.html":                           MARS[33:42],
    "temoignages.html":                        JUIL[9:18],
    "leadership.html":                         AOUT[80:89],
    "contact.html":                            AOUT[40:49],
    "blog.html":                               JUIL[18:27],
    "conseil-dadministration.html":            AOUT[90:99],
    "employer.html":                           MARS[42:51] + JUIL[27:30],
    "je-veux-un-emploi.html":                  JUIL[36:45],
    "je-veux-investir.html":                   AOUT[50:59],
    "devenir-partenaire.html":                 AOUT[60:69],
    "formulaire-devenir-partenaire.html":      AOUT[70:79],
    "formulaire-je-veux-employer-des-jeunes.html": MARS[51:60],
    "formulaire-je-veux-travailler.html":      JUIL[45:54],
    "nous-rejoindre.html":                     AOUT[0:9],
    "travailler-avec-nous.html":               JUIL[54:63],
    "konkret.html":                            JUIL[63:72],
    "shop.html":                               AOUT[99:108],
    "achat-davance.html":                      AOUT[9:18],
    "documents-publics.html":                  JUIL[72:81],
    "faq.html":                                AOUT[18:27],
    "travailler-avec-nous.html":               JUIL[54:63],
    "customer-cabinet.html":                   AOUT[108:117],
}

FOOTER_TAGS = [
    '<footer class="kn-footer">',
    '<footer class="site-footer"',
    '<footer class="brz-footer',
]

def inject_page(filename, photos):
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"SKIP (not found): {filename}")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    if "kn-gallery-section" in html:
        print(f"SKIP (gallery exists): {filename}")
        return
    gallery = gallery_html(photos)
    for tag in FOOTER_TAGS:
        if tag in html:
            html = html.replace(tag, gallery + tag, 1)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"OK: {filename} ({len(photos)} photos)")
            return
    # fallback: insert before </body>
    if "</body>" in html:
        html = html.replace("</body>", gallery + "</body>", 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"OK (body fallback): {filename} ({len(photos)} photos)")
        return
    print(f"SKIP (no insertion point): {filename}")

for page, photos in PAGE_PHOTOS.items():
    inject_page(page, photos)

print("\nDone.")
