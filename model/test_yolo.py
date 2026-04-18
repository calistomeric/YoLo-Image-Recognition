from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Load a pretrained YOLOv8n model
results = model('./car.jpg')  # Run inference on an image
# print(results)  # Print the results
results[0].show() # Display the results visually