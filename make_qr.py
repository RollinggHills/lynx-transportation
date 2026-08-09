"""Generate the Lynx Transportation Services booking QR code (PNG + SVG).

Usage:  python3 make_qr.py [url]
Defaults to the planned production domain. Re-run with the real URL
once the site is deployed (e.g. the GitHub Pages URL or custom domain).
"""
import sys

import qrcode
import qrcode.image.svg

URL = sys.argv[1] if len(sys.argv) > 1 else "https://lynxdriver.com"

# High error correction so the code still scans on flyers/cards with wear
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=2)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="#060810", back_color="white")
img.save("booking-qr.png")

svg = qr.make_image(image_factory=qrcode.image.svg.SvgPathImage)
svg.save("booking-qr.svg")

print(f"QR encodes: {URL}")
print("Wrote booking-qr.png and booking-qr.svg")
