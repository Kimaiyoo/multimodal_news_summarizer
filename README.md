# Multimodal News Summarizer
## Project Description

A Python-based tool that fetches news articles from RSS feeds, summarizes them using an LLM, and generates captions for associated images. The project demonstrates a simple multimodal news agent that combines text and images for a richer news digest experience.

## Features
- Fetches articles from RSS feeds (e.g., Al Jazeera, CNN).
- Summarizes article content in 3–4 sentences.
- Displays images associated with articles when available.
- Generates image captions using an LLM for selected images.

## Limitations
- Image display depends on RSS feed structure; not all articles include usable images.
- Captioning works reliably only for some images.
- Summarization works consistently across most articles.

## Usage
1. Install requirements:
```bash
pip install -r requirements.txt
```
2. Run the notebook/script.
3. Specify an RSS feed URL to fetch and summarize articles.You can find a list of RSS feeds [here](https://themeisle.com/blog/rss-feeds-list/#gref).
   
