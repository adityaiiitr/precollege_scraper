import os
import google.generativeai as genai
from playwright.async_api import async_playwright
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import asyncio
import json

# Load environment variables
load_dotenv()

# Configure Google Generative AI API key
genai.configure(api_key=os.environ["API_KEY"])

# FastAPI app initialization
app = FastAPI()

# Function to scrape webpage and extract visible text
async def scrape_visible_text(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Launch browser in headless mode
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        page = await context.new_page()
        await page.goto(url, wait_until="networkidle")
        visible_text = await page.evaluate("document.body.innerText")
        await browser.close()
        return visible_text

# Function to structure data using Google's Gemini model
def structure_data(text, college_name):
    prompt = f"Convert the following unstructured text into a structured format with the titles and content containing the data. Properly structure tables and general text. The structured data should contain details only about the college named '{college_name}':\n{text}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# Pydantic model for request body
class URLRequest(BaseModel):
    url: str
    college_name: str

# FastAPI endpoint to scrape and structure data
@app.post("/scrape")
async def scrape_and_structure_data(request: URLRequest):
    try:
        # Scrape visible text from the webpage
        visible_text = await scrape_visible_text(request.url)
        
        # Structure the data using Google's Gemini model
        structured_data = structure_data(visible_text, request.college_name)
        
        # Return the structured data
        return {"structured_data": structured_data}
    except Exception as e:
        print(f"Error occurred while processing the request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)