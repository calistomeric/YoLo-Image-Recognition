from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CV object detection API is running!"}