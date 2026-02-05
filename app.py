from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# ✅ CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_data():
    with open("patients.json", "r") as f:
        return json.load(f)

@app.get("/")
async def read_root():
    return {"Patient web app": "I am Arjun"}

@app.get("/about")
async def about():
    return {"message": "Hello World"}

@app.get("/patients")
async def get_patients():
    return load_data()

@app.get("/patients/{patient_id}")
async def get_patient(patient_id: str):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"error": "Patient not found"}
