import requests
from utils import clean_text, extract_keywords, text_to_speech

def fetch_news(company_name):
    url = f'https://newsapi.org/v2/everything?q={company_name}&apiKey=YOUR_NEWSAPI_KEY'
    response = requests.get(url)
    articles = response.json().get('articles', [])[:10]
    
    structured_articles = []
    for article in articles:
        structured_articles.append({
            "Title": article["title"],
            "Summary": clean_text(article["description"] or "No summary available."),
            "Topics": extract_keywords(article["content"] or "")
        })
    
    return structured_articles

def analyze_sentiment(articles):
    from textblob import TextBlob
    sentiment_scores = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for article in articles:
        analysis = TextBlob(article["Summary"])
        polarity = analysis.sentiment.polarity
        
        if polarity > 0:
            sentiment = "Positive"
            sentiment_scores["Positive"] += 1
        elif polarity < 0:
            sentiment = "Negative"
            sentiment_scores["Negative"] += 1
        else:
            sentiment = "Neutral"
            sentiment_scores["Neutral"] += 1
        
        article["Sentiment"] = sentiment
    
    return {"Articles": articles, "Sentiment Distribution": sentiment_scores, "Final Sentiment Analysis": f"Overall sentiment is mostly {max(sentiment_scores, key=sentiment_scores.get)}."}

def generate_tts(text):
    return text_to_speech(text)
