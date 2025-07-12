import torch
import cv2
import os
import pandas as pd

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_objects(image_dir):
    detections = []
    for img_file in os.listdir(image_dir):
        if img_file.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(image_dir, img_file)
            results = model(img_path)
            
            for *xyxy, conf, cls in results.xyxy[0]:
                detections.append({
                    "image_path": img_path,
                    "object": model.names[int(cls)],
                    "confidence": float(conf),
                    "bbox": [float(x) for x in xyxy]
                })
    
    return pd.DataFrame(detections)

if __name__ == "__main__":
    detections_df = detect_objects("data/images/")
    detections_df.to_csv("data/processed/object_detections.csv", index=False)