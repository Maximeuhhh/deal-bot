import feedparser

async def fetch_deals():
    feed = feedparser.parse("https://www.dealabs.com/rss/hot")
    deals = []
    for entry in feed.entries:
        deals.append({
            "title": entry.title,
            "url": entry.link,
            "temperature": 999,
            "discount_percent": 50,
            "source": "Dealabs"
        })
    return deals
