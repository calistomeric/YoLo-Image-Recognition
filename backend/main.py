from fastapi import FastAPI, UploadFile, File
import shutil
import os
from model.inference import detect_objects
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5500",   # Common for VS Code Live Server
    "http://127.0.0.1:5500",
    "http://localhost:3000",   # Common for React/Next.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

upload_dir = "uploads"
os.makedirs(upload_dir, exist_ok=True)

@app.get("/")
def home(): # Define a GET endpoint at the root URL
    return {"message": "CV object detection API is running!"}

@app.post("/predict") # Define a POST endpoint for object detection
async def predict(file: UploadFile = File(...)): # Accept an uploaded file as input
    file_path = os.path.join(upload_dir, file.filename) # Create a temporary file path for the uploaded file

    with open(file_path, "wb") as buffer: # Open the temporary file in write-binary mode
        shutil.copyfileobj(file.file, buffer) # Copy the contents of the uploaded file to the temporary file

    detections = detect_objects(file_path) # Call the detect_objects function to perform object detection on the temporary file

    os.remove(file_path) # Remove the temporary file after processing

    return {"detections": detections} # Return the detected objects as a JSON response