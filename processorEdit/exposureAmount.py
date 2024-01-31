from PIL import Image, ImageEnhance
import os, cv2
import numpy as np 
from processorEdit.processorBase import processorBase

class exposureAmountProcessor(processorBase):

    def process(self, filePath, savePath, factor):

        fileName = filePath.split("/")

        outFilename = os.path.basename(fileName[1])

        # 画像を開く
        image = Image.open(filePath)

        # 明るさを調整する
        enhancer = ImageEnhance.Brightness(image)
        brightened_image = enhancer.enhance(factor)

        brightened_array = np.array(brightened_image)

        corrected_image = Image.fromarray(brightened_array.astype('uint8'))
        corrected_image.save(savePath + outFilename)
        return(outFilename, 3)