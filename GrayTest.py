import cv2
import numpy as np
import os
# 画像の読み込み
class grayScale:
    def grayScaleAndBinary(inputImgPath):

        try:
            image = cv2.imread(inputImgPath)
        except OSError:
            print("can not open")
            return

        # グレースケール変換
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # グレースケール画像の表示
        # cv2.imshow('Gray Image', gray_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # 編集した画像を保存する
        imgName =os.path.basename(inputImgPath)
        imgName =imgName.split('.')

        filename =imgName[0] + "_grayScale.jpg"

        #print(filename)
        cv2.imwrite("processedPicture/" + filename, gray_image)
        print("gray OK")

        return(filename, "0")