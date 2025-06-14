#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np


square_size = 2.2      # 正方形の1辺のサイズ[cm]
pattern_size = (7, 7)  # 交差ポイントの数

reference_img = 11 # 参照画像の枚数

pattern_points = np.zeros( (np.prod(pattern_size), 3), np.float32 ) #チェスボード（X,Y,Z）座標の指定 (Z=0)
pattern_points[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)
pattern_points *= square_size
objpoints = []
imgpoints = []

pictuers = [
"ArUco\ArUco-test-input\cari\IMG_0937.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0938.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0939.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0940.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0941.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0942.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0943.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0944.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0945.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0946.JPEG",
"ArUco\ArUco-test-input\cari\IMG_0947.JPEG"
]

n = 0
while len(objpoints) < reference_img:
	capture = cv2.VideoCapture(pictuers[n])
	n += 1
# 画像の取得
	ret, img = capture.read()
	height = img.shape[0]
	width = img.shape[1]

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# チェスボードのコーナーを検出
	ret, corner = cv2.findChessboardCorners(gray, pattern_size)
	# コーナーがあれば
	if ret == True:
		print("detected coner!")
		print(str(len(objpoints)+1) + "/" + str(reference_img))
		term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
		cv2.cornerSubPix(gray, corner, (5,5), (-1,-1), term)
		imgpoints.append(corner.reshape(-1, 2))   #appendメソッド：リストの最後に因数のオブジェクトを追加
		objpoints.append(pattern_points)

	cv2.imshow('image', img)
	# 毎回判定するから 200 ms 待つ．遅延するのはココ
	if cv2.waitKey(200) & 0xFF == ord('q'):
		break

print("calculating camera parameter...")
# 内部パラメータを計算
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# 計算結果を保存
np.save("ArUco\CameraPalams\mtx", mtx) # カメラ行列
np.save("ArUco\CameraPalams\dist", dist.ravel()) # 歪みパラメータ
# 計算結果を表示
print("RMS = ", ret)
print("mtx = \n", mtx)
print("dist = ", dist.ravel())
