from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Annotated
import pickle
import numpy as np


app = FastAPI()

#Limit access from specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", 
                   "http://127.0.0.1:5500"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Hours(BaseModel):
    hrs: Annotated[float, Field(..., gt=0, lt=12, description="Number of hours studied", example=5.0)]

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.get("/")
def read_root():
    return {"message": "Api loaded successfully!"}

@app.post('/predict')
def predict_score(studyHours:Hours):
    prediction = model.predict(np.array([[studyHours.hrs]]))[0] #X is 2-D numpy array, obtained number should also be extracrted from numpy
    return JSONResponse(status_code=200, content={"message": f"Predicted score: {prediction:.2f}"})