# Food Menu Website for GitHub Pages

This is a simple, static food menu website (HTML + CSS) ready to publish on GitHub Pages.

## Files
- `index.html` — the menu page
- `styles.css` — styling
- `qr.png` — QR code pointing at `https://<your-username>.github.io/<repo-name>/`
- `generate_qr.py` — small script to create a QR code that points to your actual GitHub Pages URL

## How to publish on GitHub Pages
1. Create a **new repository** on GitHub (web UI). Name it e.g. `menu-site`.
2. Upload these files to the repository root (you can drag-and-drop in the GitHub web UI).
3. In the repository settings (Repository > Pages), select branch `main` and folder `/ (root)` and save. GitHub will publish your site at:
   `https://<your-username>.github.io/<repo-name>/`
4. Wait a minute, then open that URL in your browser.

## Customize
- Edit `index.html` to change items, prices, and text.
- Replace the placeholder URL encoded in `qr.png` by running `generate_qr.py` and supplying your actual URL.

## Regenerate the QR code locally
If you have Python on your machine, run:
```
python generate_qr.py "https://your-username.github.io/your-repo/"
```
This will create `qr.png` with the correct URL for scanning.

