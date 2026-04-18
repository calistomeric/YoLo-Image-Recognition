from fastapi import FastAPI, UploadFile, File
import shutil
import os
from model.inference import detect_objects

app = FastAPI()

@app.get("/")
def home(): # Define a GET endpoint at the root URL
    return {"message": "CV object detection API is running!"}

@app.post("/predict") # Define a POST endpoint for object detection
async def predict(file: UploadFile = File(...)): # Accept an uploaded file as input
    temp_path = f"temp_{file.filename}" # Create a temporary file path for the uploaded file

    with open(temp_path, "wb") as buffer: # Open the temporary file in write-binary mode
        shutil.copyfileobj(file.file, buffer) # Copy the contents of the uploaded file to the temporary file

    detections = detect_objects(temp_path) # Call the detect_objects function to perform object detection on the temporary file

    os.remove(temp_path) # Remove the temporary file after processing

    return {"detections": detections} # Return the detected objects as a JSON response