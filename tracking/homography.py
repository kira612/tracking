import cv2
import numpy as np

class HomographyTransformer:
    def __init__(self, src_points, dst_points):
        self.matrix, _ = cv2.findHomography(src_points, dst_points)
    
    def transform(self, points):
        return cv2.perspectiveTransform(np.array([points], dtype='float32'), self.matrix)
