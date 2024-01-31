import os
import cv2

from processorColor.processorBase import processorBase

class blueCutProcessor(processorBase):

    def process(self, filePath, savePath):

        fileName = filePath.split("/")

        outFilename = os.path.basename(fileName[1])

        img_blueCut = cv2.imread(filePath)
    
        # 画像処理
        rows, cols, channels = img_blueCut.shape
        # 画素から青色を消したい場合は次のように処理する
        for y in range(rows):
            for x in range(cols):
                # 横x縦yの画素のカラーを取得(ここでは8bitRGB)
                b, g, r = img_blueCut[y, x]
                # もし画素が白色だったなら何もしない
                if (b, g, r) == (255, 255, 255):
                    continue
                img_blueCut[y, x] = 0, g, r

        cv2.imwrite(savePath + outFilename, img_blueCut)

        return(outFilename, 0)