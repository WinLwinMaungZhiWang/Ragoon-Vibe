#!/usr/bin/env python3
"""
generate_qr.py
Usage:
  python generate_qr.py "https://github.com/WinLwinMaungZhiWang/Ragoon-Vibe.git" [output=qr.png]

Creates a QR code image file (PNG) pointing to the URL you provide.
"""
import sys
out_name = "qr.png"
if len(sys.argv) < 2:
    print("Usage: python generate_qr.py \"https://your-username.github.io/your-repo/\"")
    sys.exit(1)
url = sys.argv[1]
if len(sys.argv) > 2:
    out_name = sys.argv[2]

try:
    import segno
    qr = segno.make(url)
    qr.save(out_name, scale=10)
    print("Saved", out_name)
except Exception as e:
    try:
        import qrcode
        img = qrcode.make(url)
        img.save(out_name)
        print("Saved", out_name)
    except Exception as e2:
        print("Couldn't generate QR automatically. Please install 'segno' or 'qrcode' (pip install segno) and re-run.")
