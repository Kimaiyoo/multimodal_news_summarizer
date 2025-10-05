from newspaper import Article
from langchain.prompts import ChatPromptTemplate
from utils.config import llm

def summarize_article(url):
    article = Article(url)
    article.download()
    article.parse()
    prompt = ChatPromptTemplate.from_template("""
    Summarize the following news article in 3-4 sentences, focusing on the main points:
    {text}
    """)
    chain = prompt | llm
    return chain.invoke({"text": article.text}).content