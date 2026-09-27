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

🌟 *Your Daily Conscious Effort:*
• **The Word:** **APPRECIATE**
• **The Action:** Today, I will consciously notice one unseen sacrifice, effort, or act of patience from my wife and explicitly say thank you. 
• **Speaking Life:** I will intentionally choose words that build her up and ease her burdens, reflecting Christ's steadfast, servant-hearted love in our home."""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(
    url, json={"chat_id": CHAT_ID, "text": MESSAGE, "parse_mode": "Markdown"}
)

if response.status_code == 200:
  print("Husband Daily Anchor sent successfully!")
else:
  print(f"❌ Failed: {response.text}")
  sys.exit(1)
