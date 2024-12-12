import numpy as np

class SpeedCalculator:
    def __init__(self, fps):
        self.fps = fps
    
    def calculate_speed(self, prev_position, current_position):
        distance = np.linalg.norm(np.array(current_position) - np.array(prev_position))
        speed = distance * self.fps  # ピクセル毎秒
        return speed
