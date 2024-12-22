import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("../data/raw_dataset.csv")

df["label"] = df[
    ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
].max(axis=1)

def clean_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = text.replace("\n", " ")
        return text
    return ""

df["cleaned_text"] = df["comment_text"].apply(clean_text)

train_texts, test_texts, train_labels, test_labels = train_test_split(
    df["cleaned_text"], df["label"], test_size=0.2, random_state=42
)
df.to_csv("cleaned_dataset.csv", index=False)
print("Dataset cleaned and saved.")
