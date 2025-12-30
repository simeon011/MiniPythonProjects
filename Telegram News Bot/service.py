

import requests
import yfinance as yf
import feedparser


def get_news_api(api_key):
    url = f"https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])[:7]

    if not articles: return "No articles found"

    report = "🌍 **Global Investment News:**\n\n"
    for art in articles:
        report += f"🔹 {art.get('title')}\n🔗 {art.get('url')}\n\n"
    return report


def current_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.fast_info['last_price']
    currency = stock.fast_info['currency']
    return f"Price of {ticker} is {price:.3f} {currency}"




