from PIL import Image, ImageEnhance

def colorTemperature(image_path, factor):
    # 画像を開く
    image = Image.open(image_path)

    # 色温度を調整する
    enhancer = ImageEnhance.Color(image)
    adjusted_image = enhancer.enhance(factor)

    # 変更後の画像を保存する
    adjusted_image.save("adjusted_image01.jpg")

# 画像のパスと色温度の調整係数を指定して呼び出す
colorTemperature("IMG_2405.jpg", 1.5)

if __name__ == "__main__":
    colorTemperature()
