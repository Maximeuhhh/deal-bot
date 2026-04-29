import feedparser
import re

async def fetch_deals():
    feed = feedparser.parse("https://www.dealabs.com/rss/hot")
    deals = []
    for entry in feed.entries:
        title = entry.title

        # Extrait la température (ex: "156° - Titre du deal")
        temperature = 0
        match = re.search(r'(\d+)°', title)
        if match:
            temperature = int(match.group(1))

        deals.append({
            "title": title,
            "url": entry.link,
            "price": "Voir le deal",
            "prix_moyen": "N/A",
            "discount_percent": 0,
            "temperature": temperature,
            "image_url": None,
            "merchant": "Dealabs",
            "source": "Dealabs Hot"
        })
    return deals
