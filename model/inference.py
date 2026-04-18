from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Load a pretrained YOLOv8n model

def detect_objects(image_path):
    results = model(image_path) # Run inference on the image
    detections = []

    for box in results[0].boxes: # Iterate through detected boxes
        cls_id = int(box.cls[0]) # Get the class ID of the detected object
        label = model.names[cls_id] # Get the label corresponding to the class ID
        xyxy = box.xyxy[0].tolist() # Get the bounding box coordinates in [x1, y1, x2, y2] format

        detections.append({
            "label": label, # Add the label to the detections list
            "box": xyxy # Add the bounding box coordinates to the detections list
        })

        return detections