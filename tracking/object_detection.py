import torch

class ObjectDetector:
    def __init__(self, model_path):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    
    def detect(self, frame):
        results = self.model(frame)
        return results.pandas().xyxy[0]  # Return bounding box coordinates as pandas DataFrame
    
