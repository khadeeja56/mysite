from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):
    # Target website for headlines
    url = "https://www.bbc.com/news"
    
    # Fetch webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    # Extract headlines (top 10)
    for item in soup.select("h2"):
        text = item.get_text(strip=True)
        if text and len(headlines) < 10:
            headlines.append(text)

    # Sending headlines to template
    context = {
        "news": headlines
    }

    return render(request, "newsfetcher/home.html", context)
