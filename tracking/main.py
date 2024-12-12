import cv2
import numpy as np
from object_detection import ObjectDetector
import object_tracking 
import homography
import speed_calculator
import visualization

# 各コンポーネントの初期化
model_path = 'yolov5s.pt'
max_age = 30
fps = 30
src_points = np.array([[100, 150], [200, 150], [100, 250], [200, 250]], dtype='float32')
dst_points = np.array([[0, 0], [300, 0], [0, 400], [300, 400]], dtype='float32')

detector = ObjectDetector(model_path=model_path)
tracker = object_tracking.ObjectTracker(max_age=max_age)
calculator = speed_calculator.SpeedCalculator(fps=fps)
visualizer = visualization.DataVisualizer()
transformer = homography.HomographyTransformer(src_points, dst_points)

# カメラまたはビデオファイルの読み込み
video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)

prev_positions = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # オブジェクトの検出
    detections = detector.detect(frame)
    
    # オブジェクトの追跡
    tracks = tracker.track(detections, frame)
    
     # 速度計算
    speeds = {}
    for track in tracks:
        if track.is_confirmed():
            track_id = track.track_id
            position = track.to_tlbr()[:2]  # 左上の座標
            
            # 位置の変換
            transformed_position = transformer.transform(position)
            
            if track_id in prev_positions:
                speed = calculator.calculate_speed(prev_positions[track_id], transformed_position[0][0])
                speeds[track_id] = speed
            prev_positions[track_id] = transformed_position[0][0]
    
    # データの可視化
    visualizer.update_plot(tracks, speeds)

cap.release()
cv2.destroyAllWindows()
