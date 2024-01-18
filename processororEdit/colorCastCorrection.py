from PIL import Image
import numpy as np

def colorCastCorrection(image_path, red_factor, green_factor, blue_factor):
    # 画像を開く
    image = Image.open(image_path)

    # 画像をNumPy配列に変換
    img_array = np.array(image)

    # 各色チャンネルに補正係数を乗算
    img_array[:, :, 0] = np.clip(img_array[:, :, 0] * red_factor, 0, 255)
    img_array[:, :, 1] = np.clip(img_array[:, :, 1] * green_factor, 0, 255)
    img_array[:, :, 2] = np.clip(img_array[:, :, 2] * blue_factor, 0, 255)

    # NumPy配列をImageオブジェクトに変換
    corrected_image = Image.fromarray(img_array.astype('uint8'))

    # 補正後の画像を表示するか保存するかなどの処理を追加
    corrected_image.save("adjusted_image02.jpg")

# 画像のパスと各色チャンネルの補正係数を指定して呼び出す
colorCastCorrection("IMG_2405.jpg", 1.2, 0.8, 1.0)

if __name__ == "__main__":
    colorCastCorrection()