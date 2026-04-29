import httpx, os
from dotenv import load_dotenv
load_dotenv()

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
YOUR_USER_ID = os.environ["DISCORD_USER_ID"]

async def notify(deal):
    payload = {
        "content": f"<@{YOUR_USER_ID}> 🔥 Bonne promo !",
        "embeds": [{
            "title": deal["title"][:256],
            "url": deal["url"],
            "color": 0xFF4500,
            "fields": [
                {"name": "Source", "value": deal["source"], "inline": True},
                {"name": "Température", "value": str(deal.get("temperature", "?")), "inline": True},
            ]
        }]
    }
    async with httpx.AsyncClient() as client:
        await client.post(WEBHOOK_URL, json=payload)