import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

faq_data = {
    "What is your return policy?": "You can return any item within 30 days of purchase.",
    "How can I track my order?": "You can track your order using the tracking link sent to your email.",
    "Do you offer customer support?": "Yes, our customer support is available 24/7 via email and phone.",
    "What are the shipping charges?": "Shipping is free on orders above ₹500."
}

stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return " ".join(tokens)

faq_questions = list(faq_data.keys())
faq_answers = list(faq_data.values())

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform([preprocess(q) for q in faq_questions])

def get_best_answer(user_query):
    user_vec = vectorizer.transform([preprocess(user_query)])
    similarities = cosine_similarity(user_vec, faq_vectors)
    best_match_index = similarities.argmax()
    return faq_answers[best_match_index]

if __name__ == "__main__":
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit']:
            break
        print("Bot:", get_best_answer(query))
