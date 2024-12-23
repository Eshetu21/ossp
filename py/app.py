from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = joblib.load("hatespeech_model.pkl")


class PredictRequest(BaseModel):
    comment_text: str

def clean_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = text.replace("\n", " ")
        return text
    return ""

@app.post("/predict")
def predict(request: PredictRequest):
    print("Received Comment:", request.comment_text)
    
    cleaned_text = clean_text(request.comment_text)
    
    prediction = model.predict([cleaned_text])
    
    result = "toxic" if prediction[0] == 1 else "non-toxic"
    return {"result": result}
