import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def match_resume_jd(resume, jd):
    resume = clean_text(resume)
    jd = clean_text(jd)

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume, jd])

    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2), vectorizer.get_feature_names_out()
