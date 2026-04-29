import httpx
import os
from dotenv import load_dotenv
load_dotenv()

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
YOUR_USER_ID = os.environ["DISCORD_USER_ID"]

async def notify(deal):
    embed = {
        "title": deal["title"][:256],
        "url": deal["url"],
        "color": 0xFF4500,
        "fields": [
            {"name": "💰 Prix", "value": deal.get("price", "Non précisé"), "inline": True},
            {"name": "📉 Réduction", "value": f"{deal.get('discount_percent', '?')}%", "inline": True},
            {"name": "🛒 Site", "value": deal.get("merchant", "Non précisé"), "inline": True},
        ],
        "footer": {"text": "Via Dealabs"}
    }

    if deal.get("image_url"):
        embed["image"] = {"url": deal["image_url"]}

    payload = {
        "content": f"<@{YOUR_USER_ID}> 🔥 Bonne promo détectée !",
        "embeds": [embed]
    }

    async with httpx.AsyncClient() as client:
        await client.post(WEBHOOK_URL, json=payload)
