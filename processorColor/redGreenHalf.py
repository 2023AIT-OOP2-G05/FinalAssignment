import os
import cv2

from processorColor.processorBase import processorBase

class redGreenHalfProcessor(processorBase):

    OUT_DIR = "./processedPicture/"

    def process(self, filepath):
        outFilename = os.path.basename(filepath)
        img_redgreenCut = cv2.imread(filepath)
    
        # 画像処理
        rows, cols, channels = img_redgreenCut.shape
        # 画素から青色を消したい場合は次のように処理する
        for y in range(rows):
            for x in range(cols):
                # 横x縦yの画素のカラーを取得(ここでは8bitRGB)
                b, g, r = img_redgreenCut[y, x]
                # もし画素が白色だったなら何もしない
                if (b, g, r) == (255, 255, 255):
                    continue
                img_redgreenCut[y, x] = b, g//2, r//2

        cv2.imwrite(self.OUT_DIR + outFilename, img_redgreenCut)

        return(outFilename, 5)