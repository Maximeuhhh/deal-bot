import asyncio, json
from pathlib import Path
from scrapers.dealabs import fetch_deals
from scrapers.rss import fetch_rss_deals
from filter import is_good_deal
from discord_notify import notify

SEEN_FILE = Path("seen_deals.json")

def load_seen():
    if SEEN_FILE.exists():
        return set(json.loads(SEEN_FILE.read_text()))
    return set()

def save_seen(seen):
    SEEN_FILE.write_text(json.dumps(list(seen)))

async def run():
    print("🤖 Bot démarré !")
    seen = load_seen()
    while True:
        try:
            deals = await fetch_deals() + await fetch_rss_deals()
            for deal in deals:
                if deal["url"] in seen:
                    continue
                seen.add(deal["url"])
                if is_good_deal(deal):
                    print(f"✅ Promo : {deal['title']}")
                    await notify(deal)
            save_seen(seen)
        except Exception as e:
            print(f"❌ Erreur : {e}")
        await asyncio.sleep(45)

asyncio.run(run())