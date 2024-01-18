from PIL import Image, ImageEnhance

def highlight(image_path, factor):
    # 画像を開く
    image = Image.open(image_path)

    # 明るい領域を抽出
    bright_pixels = image.point(lambda p: p * factor if p > 128 else p)

    # 調整後の画像を表示するか保存するかなどの処理を追加
    bright_pixels.save("adjusted_image06.jpg")

# 画像のパスとハイライトの調整係数を指定して呼び出す
highlight("IMG_2405.jpg", 1.5)

if __name__ == "__main__":
    highlight()
