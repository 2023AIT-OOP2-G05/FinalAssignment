from PIL import Image, ImageEnhance
import os, cv2
import numpy as np 
from processororEdit.processorBase import processorBase

class highlightProcessor(processorBase):

    def process(self, filePath, savePath, factor):

        fileName = filePath.split("/")

        outFilename = os.path.basename(fileName[1])

        # 画像を開く
        image = Image.open(filePath)

        # 明るい領域を抽出
        bright_pixels = image.point(lambda p: p * factor if p > 128 else p)

        bright_array = np.array(bright_pixels)

        corrected_image = Image.fromarray(bright_array.astype('uint8'))
        corrected_image.save(savePath + outFilename)

        return(outFilename, 5)


       