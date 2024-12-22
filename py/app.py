from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictRequest(BaseModel):
    comment_text: str

@app.post("/predict")
def predict(request: PredictRequest):
    print("Received Comment:", request.comment_text)
    if "toxic" in request.comment_text.lower():
        return {"result": "toxic"}
    return {"result": "non-toxic"}

