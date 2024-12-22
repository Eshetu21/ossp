from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import joblib
import pandas as pd

df = pd.read_csv("cleaned_dataset.csv")

train_texts = df["cleaned_text"][: int(0.8 * len(df))]
train_labels = df["label"][: int(0.8 * len(df))]
test_texts = df["cleaned_text"][int(0.8 * len(df)) :]
test_labels = df["label"][int(0.8 * len(df)) :]

model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(train_texts, train_labels)

predictions = model.predict(test_texts)
print(classification_report(test_labels, predictions))

joblib.dump(model, "hatespeech_model.pkl")
print("Model saved.")

