from datetime import datetime
import os
import sys
import requests

# --- CONFIGURATION ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# Check if secrets are loaded properly
if not BOT_TOKEN or not CHAT_ID:
  print(
      "❌ Error: BOT_TOKEN or CHAT_ID are missing! Make sure you added them"
      " to GitHub Repository Secrets."
  )
  sys.exit(1)

# Set the anchor start date for Day 1 of your cycle (Year, Month, Day)
START_DATE = datetime(2026, 9, 27).date()

# --- THE 7-DAY REFLECTION PLAN (Joshua 1:9) ---
VERSE_PLAN = {
    1: """📖 *Day 1: Memorization & Repetition*

> *“Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.”* — Joshua 1:9

*Action:* Read the verse out loud five times this morning and five times tonight. Get the words fixed firmly in your mind.""",
    2: """📖 *Day 2: Deconstruct the Key Words*

> *“Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.”* — Joshua 1:9

*Action:* Focus on the words *strong*, *courageous*, *afraid*, and *discouraged*. Acknowledge that fear is normal, but courage is a choice fueled by God.""",
    3: """📖 *Day 3: Personalize the Promise*

> *“Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.”* — Joshua 1:9

*Action:* Re-read the verse today inserting your own name or current situation into it. Remind yourself He is actively with *you*.""",
    4: """📖 *Day 4: Connect to Past Faithfulness*

> *“Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.”* — Joshua 1:9

*Action:* Spend a few minutes thinking about a past moment when you felt overwhelmed, but God carried you through safely.""",
    5: """📖 *Day 5: Turn the Verse into a Prayer*

> *“Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.”* — Joshua 1:9

*Action:* Pray the verse back to God: *"Lord, because You are with me wherever I go, I choose not to be afraid today..."*""",
    6: """📖 *Day 6: Practical Application*

> *“Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.”* — Joshua 1:9

*Action:* Identify one specific situation today where you feel anxious. Step into it consciously repeating this verse as your anchor.""",
    7: """📖 *Day 7: Review & Harvest*

> *“Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.”* — Joshua 1:9

*Action:* Recite the verse from memory. Reflect on how spending a full week with this single truth has shifted your mindset.""",
}


def send_telegram_message(message):
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
  response = requests.post(url, json=payload)

  if response.status_code == 200:
    print("Daily reflection sent successfully!")
  else:
    print(f"❌ Failed to send message to Telegram: {response.text}")
    sys.exit(1)


if __name__ == "__main__":
  today = datetime.now().date()
  days_elapsed = (today - START_DATE).days
  current_day = (days_elapsed % 7) + 1

  message = f"🌅 *Your Daily Morning Reflection*\n\n{VERSE_PLAN[current_day]}"
  send_telegram_message(message)
