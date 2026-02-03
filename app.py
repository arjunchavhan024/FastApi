from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "I am Arjun"}

@app.get("/about")
async def read_root():
    return {"message": "Hello World"}