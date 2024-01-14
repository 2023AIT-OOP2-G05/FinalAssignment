import numpy as np
import cv2
def blueGreenHalf():
    img = cv2.imread('sample.jpg')

    rows,cols,channels = img.shape

    # 青色を消す
    for y in range(rows):
        for x in range(cols):
            b, g, r = img[y, x]
            # もし画素が白色だったな何もしない
            if (b, g, r) == (255, 255, 255):
                continue
            img[y, x] = b//2, g//2, r

    # 編集した画像を保存する
    cv2.imwrite('blue_green_half.jpg', img)

if __name__ == "__main__":
    blueGreenHalf()