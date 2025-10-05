from utils.fetcher import fetch_rss_articles
from utils.summarizer import summarize_article
from utils.image_captioner import caption_image

def run_news_demo(rss_url, limit=3):
    articles = fetch_rss_articles(rss_url, limit)
    results = []

    for article in articles:
        data = {
            "title": article["title"],
            "summary": "",
            "image": article.get("image", None),
            "caption": ""
        }

        # Summarize
        try:
            data["summary"] = summarize_article(article["link"])
        except Exception as e:
            data["summary"] = f"Could not summarize article: {e}"

        # Caption image
        if article.get("image"):
            try:
                data["caption"] = caption_image(article["image"])
            except Exception as e:
                data["caption"] = f"Could not caption image: {e}"

        results.append(data)

    return results

