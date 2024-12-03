#!/usr/bin/env python
# -*- coding: utf-8 -*
#!/usr/bin/env python
# -*- coding: utf-8 -*
import numpy as np
import cv2
from cv2 import aruco

# 画像の読み込み
capture = cv2.VideoCapture('ArUco/ArUco-test-input/IMG_0934.JPEG')
ret, imag = capture.read()

if not ret:
    print("画像の読み込みに失敗しました。")
else:
    # グレースケール画像に変換
    gray = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)

    # 辞書の取得
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)
    
    # パラメータの設定
    parameters = aruco.DetectorParameters()

    # マーカーの検出
    corners, ids, rejectedImgPoints = aruco.ArucoDetector.detectMarkers(gray, aruco_dict, parameters=parameters)

    # 検出結果の表示
    print("Corners:", corners)
    print("IDs:", ids)

    # 検出されたマーカーを画像に描画
    aruco.drawDetectedMarkers(imag, corners, ids)
    cv2.imshow('Detected ArUco markers', imag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
