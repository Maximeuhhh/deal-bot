import feedparser
import re
from bs4 import BeautifulSoup

async def fetch_deals():
    feed = feedparser.parse("https://www.dealabs.com/rss/hot")
    deals = []
    for entry in feed.entries:
        title = entry.title

        # Pourcentage de réduction
        discount = 0
        match = re.search(r'(\d+)\s*%', title)
        if match:
            discount = int(match.group(1))

        # Prix
        price = "Non précisé"
        price_match = re.search(r'(\d+[.,]\d+|\d+)\s*€', title)
        if price_match:
            price = price_match.group(0)

        # Image et site marchand depuis la description RSS
        image_url = None
        merchant = "Non précisé"
        if hasattr(entry, 'summary'):
            soup = BeautifulSoup(entry.summary, "html.parser")
            img = soup.find("img")
            if img:
                image_url = img.get("src")
            merchant_match = re.search(r'Marchand\s*:\s*(.+?)(<|$)', entry.summary)
            if merchant_match:
                merchant = merchant_match.group(1).strip()

        deals.append({
            "title": title,
            "url": entry.link,
            "temperature": 0,
            "discount_percent": discount,
            "price": price,
            "image_url": image_url,
            "merchant": merchant,
            "source": "Dealabs"
        })
    return deals
