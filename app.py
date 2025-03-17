import gradio as gr
from api import fetch_news, analyze_sentiment, generate_tts

def process_company_news(company_name):
    articles = fetch_news(company_name)
    sentiment_results = analyze_sentiment(articles)
    tts_audio_path = generate_tts(sentiment_results['Final Sentiment Analysis'])
    
    return sentiment_results, tts_audio_path

gr.Interface(
    fn=process_company_news,
    inputs=[gr.Textbox(label="Enter Company Name")],
    outputs=[gr.JSON(label="Sentiment Report"), gr.Audio(label="Hindi Audio Summary")],
    title="News Summarization and Sentiment Analysis"
).launch(share=True)
