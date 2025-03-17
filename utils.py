import nltk
from gtts import gTTS

def clean_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_keywords(text):
    words = nltk.word_tokenize(text)
    keywords = [word for word in words if word.isalpha() and word.lower() not in nltk.corpus.stopwords.words('english')]
    return list(set(keywords))[:5]

def text_to_speech(text, lang='hi'):
    tts = gTTS(text, lang=lang)
    output_path = "output.mp3"
    tts.save(output_path)
    return output_path
