import os
import sys
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
  print("❌ Error: Missing secrets!")
  sys.exit(1)

MESSAGE = """💖 *Daily Love Note*

> *“Many women have done excellently, but you surpass them all.”* — Proverbs 31:29

✨ *Today's Sweet Reminder:*
• **My Heart's Choice:** Just a gentle reminder today that you are deeply loved, cherished, and treasured. 
• **The Bright Spot:** Your smile, your warmth, and your presence make every single day infinitely better. 
• **Forever Grateful:** Thank you for being my anchor, my partner, and my greatest blessing in this life. I love you more than words can say! 💕"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(
    url, json={"chat_id": CHAT_ID, "text": MESSAGE, "parse_mode": "Markdown"}
)

if response.status_code == 200:
  print("Lovey-dovey message sent successfully!")
else:
  print(f"❌ Failed: {response.text}")
  sys.exit(1)
