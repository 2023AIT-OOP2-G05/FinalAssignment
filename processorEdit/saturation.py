from PIL import Image, ImageEnhance
import os, cv2
import numpy as np 
from processorEdit.processorBase import processorBase

class saturationProcessor(processorBase):

    def process(self, filePath, savePath, factor):

        fileName = filePath.split("/")

        outFilename = os.path.basename(fileName[1])
        # img_saturated = cv2.imread(filepath)

        # 画像を開く
        image = Image.open(filePath)

        # 彩度を調整する
        enhancer = ImageEnhance.Color(image)
        saturated_image = enhancer.enhance(factor)

        saturated_array = np.array(saturated_image)

        corrected_image = Image.fromarray(saturated_array.astype('uint8'))
        corrected_image.save(savePath + outFilename)
        return(outFilename, 2)

   