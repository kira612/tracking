# aruco_marker_generator.py
import cv2
import cv2.aruco as aruco
import os

def generate_aruco_marker(dictionary_name, marker_id, marker_size, output_filename):
    """
    指定したIDのArUcoマーカーを生成し、ファイルに保存します。

    Parameters:
    - dictionary_name: ArUcoのディクショナリ名（例: aruco.DICT_4X4_50）
    - marker_id: マーカーのID（ディクショナリに応じた範囲で指定）
    - marker_size: 生成するマーカー画像のサイズ（ピクセル）
    - output_filename: 保存するファイルのパス

    Returns:
    - output_filename: 保存したファイル名を返します
    """
    # ArUcoマーカの辞書を取得
    aruco_dict = aruco.getPredefinedDictionary(dictionary_name)

    # ArUcoマーカの生成
    marker_image = aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

    # 出力ディレクトリが存在しない場合は作成
    output_dir = os.path.dirname(output_filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # ファイルに保存
    cv2.imwrite(output_filename, marker_image)
    print(f"ArUcoマーカを生成し、ファイル '{output_filename}' に保存しました。")

    return None
