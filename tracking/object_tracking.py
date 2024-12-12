import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort

class ObjectTracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)
    
    def track(self, detections, frame):
        tracks = self.tracker.update_tracks(detections.to_numpy(), frame=frame)
        return tracks
