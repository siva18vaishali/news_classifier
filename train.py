import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load datasets
real_df = pd.read_csv(r"C:/Users/siva0/real_vs_satire/datasets/True.csv")
satire_df = pd.read_csv(r"C:/Users/siva0/real_vs_satire/datasets/Fake.csv")

# Combine the two datasets
real_df['label'] = 'real'
satire_df['label'] = 'satire'

df = pd.concat([real_df[['title', 'label']], satire_df[['title', 'label']]])

# Display first few rows to check the data
print("Dataset preview:\n", df.head())

# Vectorize the titles using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(df['title'])  # Use 'title' instead of 'headline'

# Encode the labels (real and satire)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(df['label'])

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_vectorized, y_encoded)

# Save the model, vectorizer, and label encoder to files
with open("models/model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
    
with open("models/vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

with open("models/label_encoder.pkl", "wb") as encoder_file:
    pickle.dump(label_encoder, encoder_file)

print("Model, vectorizer, and label encoder saved successfully.")
