from PIL import Image, ImageEnhance

def exposureAmount(image_path, factor):
    # 画像を開く
    image = Image.open(image_path)

    # 明るさを調整する
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(factor)

    # 調整後の画像を表示するか保存するかなどの処理を追加
    brightened_image.save("adjusted_image04.jpg")

# 画像のパスと露光量の調整係数を指定して呼び出す
exposureAmount("IMG_2405.jpg", 1.5)

if __name__ == "__main__":
    exposureAmount()
