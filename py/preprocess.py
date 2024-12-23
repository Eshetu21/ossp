import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("../data/hate_dataset.csv")

def clean_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = text.replace("\n", " ")
        return text
    return ""

df["cleaned_text"] = df["Content"].apply(clean_text)

train_texts, test_texts, train_labels, test_labels = train_test_split(
    df["cleaned_text"], df["Label"], test_size=0.2, random_state=42
)

train_data = pd.DataFrame({"text": train_texts, "label": train_labels})
test_data = pd.DataFrame({"text": test_texts, "label": test_labels})

train_data.to_csv("train_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)

print("Data preprocessed and saved.")

