import os
import sys
import requests

# --- CONFIGURATION ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
  print("❌ Error: BOT_TOKEN or CHAT_ID are missing!")
  sys.exit(1)

# --- UNIFIED DAILY DEVOTION MESSAGE ---
DAILY_DEVOTION = """📖 *Daily Devotion & Parent Anchor*

> *“Folly is bound up in the heart of a child, but the rod of discipline drives it far from him.”* — Proverbs 22:15

🛡️ *Theological Focus & Mindset:*
• **The Reality of Folly (Baucham/MacArthur):** His stubbornness and pride are expressions of inherited sin and defensive armor, not personal attacks. I will not meet his rebellion with frustration.
• **Shepherding the Heart (Washer/Sproul):** Lead with holy consistency and objective truth. True parenting reaches the heart rather than demanding mere surface compliance.
• **Sovereign Rest (Spurgeon/Piper):** Rest completely in God's sovereignty. Model living *Coram Deo* (before the face of God) with quiet strength and unwavering patience."""


def send_telegram_message(message):
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
  response = requests.post(url, json=payload)

  if response.status_code == 200:
    print("Daily devotion sent successfully!")
  else:
    print(f"❌ Failed to send message to Telegram: {response.text}")
    sys.exit(1)


if __name__ == "__main__":
  send_telegram_message(DAILY_DEVOTION)
