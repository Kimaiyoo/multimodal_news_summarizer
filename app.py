from utils.demo import run_news_demo
import gradio as gr
from gradio.themes import Soft 

# Predefined RSS links
RSS_LINKS = {
    "CNN": "http://rss.cnn.com/rss/edition.rss",
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "TechCrunch": "http://feeds.feedburner.com/TechCrunch/",
    "NY Times": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
}

def fetch_and_display(source):
    rss_url = RSS_LINKS.get(source)
    if not rss_url:
        return "Invalid source selected."

    results = run_news_demo(rss_url)

    html = "<div style='display:flex; flex-direction:column; gap:20px;'>"

    for r in results:
        html += f"""
        <div style='border:1px solid #ddd; border-radius:10px; padding:15px; box-shadow:2px 2px 8px rgba(0,0,0,0.05);'>
            <h3>📰 {r['title']}</h3>
            {'<img src="'+r['image']+'" alt="news image" style="width:100%; border-radius:8px;">' if r['image'] else ''}
            <p><b>📝 Summary:</b> {r['summary']}</p>
            {f"<p><b>🖼️ Caption:</b> {r['caption']}</p>" if r['caption'] else ''}
        </div>
        """
    html += "</div>"
    return html

with gr.Blocks(theme=Soft(), title="📰 Multimodal News Summarizer") as demo:
    gr.Markdown("## 🗞️ AI Multimodal News Summarizer")
    gr.Markdown("Select a news source to automatically fetch and summarize the latest stories (text + image captions).")

    with gr.Row():
        cnn_btn = gr.Button("CNN")
        bbc_btn = gr.Button("BBC")
        aj_btn = gr.Button("Al Jazeera")
        tc_btn = gr.Button("TechCrunch")
        ny_btn = gr.Button("NY Times")

    output_box = gr.HTML(value="", elem_id="output")

    cnn_btn.click(fetch_and_display, inputs=gr.Textbox(value="CNN", visible=False), outputs=output_box)
    bbc_btn.click(fetch_and_display, inputs=gr.Textbox(value="BBC", visible=False), outputs=output_box)
    aj_btn.click(fetch_and_display, inputs=gr.Textbox(value="Al Jazeera", visible=False), outputs=output_box)
    tc_btn.click(fetch_and_display, inputs=gr.Textbox(value="TechCrunch", visible=False), outputs=output_box)
    ny_btn.click(fetch_and_display, inputs=gr.Textbox(value="NY Times", visible=False), outputs=output_box)

demo.launch()
