import numpy as np
import cv2
def redCut():
    img = cv2.imread('sample.jpg')

    rows,cols,channels = img.shape

    # 青色を消す
    for y in range(rows):
        for x in range(cols):
            b, g, r = img[y, x]
            # もし画素が白色だったな何もしない
            if (b, g, r) == (255, 255, 255):
                continue
            img[y, x] = b, g, 0

    # 編集した画像を保存する
    cv2.imwrite('red_cut.jpg', img)

if __name__ == "__main__":
    redCut()