from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

def index(request):
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    for item in soup.select("h2"):
        text = item.get_text(strip=True)
        if text and len(headlines) < 10:
            headlines.append(text)

    context = {"news": headlines}
    return render(request, "newsfetcher/home.html", context)


# ⭐ NEW CODE (Redirect Function)
def go_to_bbc(request):
    return redirect("https://www.bbc.com/news")
