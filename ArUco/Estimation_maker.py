#!/usr/bin/env python3
# coding: utf-8
import cv2
import cv2.aruco as aruco
# ArUcoのライブラリを導入
aruco = cv2.aruco



cnt = 9


# def estimation_aruco_mark (inputimage, dictionary, outputfile)
# 	results = aruco.detectMarkers(image=inputimage, dictionary=dictionary)
# 	for i in results.ids:	


def recognizeArMarker(dictionary_name, input_img):
	parameters = aruco.DetectorParameters()
	dictionary = aruco.getPredefinedDictionary(dictionary_name)
	for i in range(cnt + 1):
		# 入力ファイル名
		input_file_nm = "ar" + str(i) + ".png"
		# 出力ファイル名
		output_file_nm = "ar_detection" + str(i) + ".png"
		# 入力ファイルの読み込み
		input_img = cv2.imread(input_file_nm)
		# ArUcoマーカの検出
		corners, ids, rejectedCandidates = aruco.detectMarkers(input_img, dictionary, parameters=parameters)
		# ArUcoマーカの検出結果の描画
		ar_image = aruco.drawDetectedMarkers(input_img, corners, ids)

		# ArUcoマーカの検出結果をファイル出力
		cv2.imwrite(output_file_nm, ar_image)

if __name__ == "__main__":
    recognizeArMarker()
