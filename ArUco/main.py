import Generate_marker
import cv2.aruco as aruco

# パラメータを設定
dictionary_name = aruco.DICT_4X4_250
output_folder = "ArUco\ArUco-output"
marker_id = 0
marker_size = 600
marker_quantity = 5

# マーカーを生成して保存

# for i in range(marker_quantity):  
      
#     output_filename = output_folder + str(i) + ".png"
#     Generate_marker.generate_aruco_marker(dictionary_name, marker_id, marker_size, output_filename)
#     marker_id += 1

#　マーカの座標取得