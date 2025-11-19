import qrcode
from PIL import Image
import os

# URL zu deinem GitHub-Profil
github_url = "https://github.com/altawfik"  # ← USERNAME ersetzen

# QR-Code erstellen
qr = qrcode.QRCode(
    version=4,  # Größere Version für Logo
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # hohe Fehlerkorrektur
    box_size=10,
    border=4
)
qr.add_data(github_url)
qr.make(fit=True)

# QR-Code Bild mit Farben generieren
qr_img = qr.make_image(fill_color="darkblue", back_color="lightyellow").convert("RGB")

# Name der Logo-Datei
logo_path = "github-logo.png"

# Prüfen, ob das Logo existiert
if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")

    # Logo auf 20% der QR-Code-Größe skalieren
    logo_size = int(qr_img.size[0] * 0.20)
    logo = logo.resize((logo_size, logo_size))

    # Transparenz-Kanal für mask extrahieren
    mask = logo.split()[3]

    # Position in der Mitte
    pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)

    # Logo einfügen
    qr_img.paste(logo, pos, mask=mask)
    print(" Logo wurde in den QR-Code eingefügt.")
else:
    print(" Logo nicht gefunden, QR-Code wird ohne Logo erstellt.")

# Bild speichern
qr_img.save("my_github_qr_final.png")
print(" QR-Code erfolgreich erstellt: my_github_qr_final.png")
