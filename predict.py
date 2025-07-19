import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# Load the vectorizer, model, and label encoder
with open(r"C:/Users/siva0/real_vs_satire/models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open(r"C:/Users/siva0/real_vs_satire/models/model.pkl", "rb") as f:
    model = pickle.load(f)

with open(r"C:/Users/siva0/real_vs_satire/models/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

def predict_headline(headline):
    transformed = vectorizer.transform([headline])
    prediction = model.predict(transformed)
    return label_encoder.inverse_transform(prediction)[0]
