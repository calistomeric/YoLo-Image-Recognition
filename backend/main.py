from fastapi import FastAPI, UploadFile, File
import shutil
import os
from model.inference import detect_objects

app = FastAPI()

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