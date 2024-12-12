import numpy as np
import matplotlib.pyplot as plt
import cv2

# 基準とする畳四隅の写真上の座標（単位px）
pts1 = np.array([(29, 950), (1047, 448), (1558, 553), (782, 1422)], dtype=np.float32)
# 基準とする畳四隅の実際の座標（単位cm）
pts2 = np.array([(30,30), (208,30), (208,120), (30,120)], dtype=np.float32)

# 射影行列の取得
M = cv2.getPerspectiveTransform(pts1, pts2) 
np.set_printoptions(precision=5, suppress=True)
print (M)
'''
[[    0.53757    -0.55406   831.92386]
 [    0.81283     1.95866 -1563.14951]
 [   -0.00006     0.01022     1.     ]] 
'''
