import feedparser
import re

async def fetch_deals():
    deals = []
    
    # Flux RSS Dealabs — les plus chauds du moment
    feeds = [
        "https://www.dealabs.com/rss/hot",
        "https://www.dealabs.com/rss/latest",
    ]
    
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.title

            # Cherche un pourcentage dans le titre
            discount = 0
            match = re.search(r'(\d+)\s*%', title)
            if match:
                discount = int(match.group(1))

            # Cherche un prix dans le titre
            price = "Non précisé"
            price_match = re.search(r'(\d+[.,]\d+|\d+)\s*€', title)
            if price_match:
                price = price_match.group(0)

            deals.append({
                "title": title,
                "url": entry.link,
                "price": price,
                "prix_moyen": "N/A",
                "discount_percent": discount,
                "temperature": 0,
                "image_url": None,
                "merchant": "Dealabs",
                "source": "Dealabs RSS"
            })

    return deals
