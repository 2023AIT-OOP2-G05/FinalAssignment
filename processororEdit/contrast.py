from PIL import Image, ImageEnhance

def contrast(image_path, factor):
    # 画像を開く
    image = Image.open(image_path)

    # コントラストを調整する
    enhancer = ImageEnhance.Contrast(image)
    high_contrast_image = enhancer.enhance(factor)

    # 調整後の画像を表示するか保存するかなどの処理を追加
    high_contrast_image.save("adjusted_image05.jpg")

# 画像のパスとコントラストの調整係数を指定して呼び出す
contrast("IMG_2405.jpg", 1.5)

if __name__ == "__main__":
    contrast()