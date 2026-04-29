import feedparser
import re

async def fetch_deals():
    feed = feedparser.parse("https://www.dealabs.com/rss/hot")
    deals = []
    for entry in feed.entries:
        title = entry.title
        
        # Cherche un pourcentage de réduction dans le titre
        discount = 0
        match = re.search(r'(\d+)\s*%', title)
        if match:
            discount = int(match.group(1))
        
        deals.append({
            "title": title,
            "url": entry.link,
            "temperature": 0,
            "discount_percent": discount,
            "source": "Dealabs"
        })
    return deals
