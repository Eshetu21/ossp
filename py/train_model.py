import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import joblib

train_data = pd.read_csv("train_data.csv", skipinitialspace=True)
test_data = pd.read_csv("test_data.csv", skipinitialspace=True)

train_data = train_data[train_data["label"] != "Label"]
test_data = test_data[test_data["label"] != "Label"]


train_data = train_data.dropna(subset=["text", "label"]) 
test_data = test_data.dropna(subset=["text", "label"])

train_labels = train_data["label"].astype(int)
test_labels = test_data["label"].astype(int)

train_texts = train_data["text"]
test_texts = test_data["text"]

model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(train_texts, train_labels)

predictions = model.predict(test_texts)

print(classification_report(test_labels, predictions))

joblib.dump(model, "hatespeech_model.pkl")
print("Model saved.")
