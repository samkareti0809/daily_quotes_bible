import os
import sys
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
  print("❌ Error: Missing secrets!")
  sys.exit(1)

MESSAGE = """❤️ *Husband Daily Appreciation & Encouragement*

> *“Let your speech always be gracious, seasoned with salt...”* — Colossians 4:6

🌟 *Focus for Today:*
• **Cultivating Gratitude:** Consciously reflect on your wife's unseen sacrifices, patience, and partnership today. Let thankfulness shape your attitude before you even speak.
• **Speaking Life & Encouragement:** Intentionally offer words that build her up, ease her burdens, and express genuine appreciation. 
• **Grace in Partnership:** Lead your home with servant-hearted humility, patience, and steadfast love, mirroring Christ's love for His church."""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(
    url, json={"chat_id": CHAT_ID, "text": MESSAGE, "parse_mode": "Markdown"}
)
if response.status_code == 200:
  print("Husband Reminder sent successfully!")
else:
  print(f"❌ Failed: {response.text}")
  sys.exit(1)
