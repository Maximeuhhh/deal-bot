import feedparser

async def fetch_rss_deals():
    feed = feedparser.parse("https://www.dealabs.com/rss/latest")
    return [{"title": e.title, "url": e.link, "temperature": 0, "discount_percent": 0, "source": "RSS"} for e in feed.entries]