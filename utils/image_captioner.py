import requests
from PIL import Image
from io import BytesIO
from langchain.prompts import ChatPromptTemplate
from utils.config import llm

# caption image function
def caption_image(image_url):
    if not image_url:
        return "No image available."
    try:
        
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.verify()
        
        # Generate caption (text-based LLM prompt)
        prompt = ChatPromptTemplate.from_template("""
        Generate a short descriptive caption for this news image.
        Focus on key objects and context in 1-2 sentences.
        {text}
        """)
        chain = prompt | llm
        caption = chain.invoke({"text": f"Image URL: {image_url}"}).content
        return caption
    except:
        return "Image could not be loaded."