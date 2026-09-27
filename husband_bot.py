import os
import sys
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
  print("❌ Error: Missing secrets!")
  sys.exit(1)

MESSAGE = """❤️ *Husband Daily Anchor Word: "APPRECIATE"*

> *“Let your speech always be gracious, seasoned with salt...”* — Colossians 4:6

🎯 *Daily Conscious Anchor:*
• **The Word:** **APPRECIATE**
• **Cultivating Gratitude:** Consciously reflect on your wife's unseen sacrifices, patience, and partnership today. Let thankfulness shape your attitude before you speak.

📚 *Theological Wisdom & Partnership:*
• **Christ-like Headship & Servant Love (MacArthur / Piper):** True spiritual leadership means laying down your life for your bride, cherishing and nurturing her with sacrificial humility, mirroring Christ's love for His church.
• **Speech Seasoned with Grace (Spurgeon / Sproul):** As Spurgeon noted, gentle and gracious words carry profound power. Eliminate harshness; let every word build her up and honor God *Coram Deo* (before the face of God).
• **Intentional Devotion (Washer / Baucham):** Biblical love is active and steadfast—a daily commitment to lead your home with steadfast patience, Gospel-centered strength, and genuine appreciation."""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(
    url, json={"chat_id": CHAT_ID, "text": MESSAGE, "parse_mode": "Markdown"}
)

if response.status_code == 200:
  print("Husband Daily Anchor sent successfully!")
else:
  print(f"❌ Failed: {response.text}")
  sys.exit(1)
