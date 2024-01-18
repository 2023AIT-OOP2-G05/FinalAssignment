from PIL import Image, ImageEnhance

def saturation(image_path, factor):
    # 画像を開く
    image = Image.open(image_path)

    # 彩度を調整する
    enhancer = ImageEnhance.Color(image)
    saturated_image = enhancer.enhance(factor)

    # 調整後の画像を表示するか保存するかなどの処理を追加
    saturated_image.save("adjusted_image03.jpg")

# 画像のパスと彩度の調整係数を指定して呼び出す
saturation("IMG_2405.jpg", 3)

if __name__ == "__main__":
    saturation()