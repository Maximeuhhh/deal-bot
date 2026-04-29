import httpx
from bs4 import BeautifulSoup

async def fetch_deals():
    headers = {"User-Agent": "Mozilla/5.0"}
    async with httpx.AsyncClient() as client:
        r = await client.get("https://www.dealabs.com/visit/latest", headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    deals = []
    for item in soup.select("article.thread"):
        try:
            title = item.select_one(".thread-title").text.strip()
            temp = item.select_one(".vote-temp")
            link = item.select_one("a.thread-link")["href"]
            deals.append({
                "title": title,
                "temperature": int(temp.text.strip()) if temp else 0,
                "url": link,
                "source": "Dealabs",
                "discount_percent": 0
            })
        except:
            continue
    return deals