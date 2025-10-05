import feedparser

def fetch_rss_articles(rss_url, limit=3):
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries[:limit]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "image": entry.get("media_content", [{}])[0].get("url")   # type: ignore
        })
    return articles