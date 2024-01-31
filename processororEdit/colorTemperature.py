from PIL import Image, ImageEnhance
import os, cv2
import numpy as np 
from processororEdit.processorBase import processorBase

class colorTemperatureProcessor(processorBase):

    def process(self, filePath, savePath, factor):

        fileName = filePath.split("/")

        outFilename = os.path.basename(fileName[1])

        # 画像を開く
        image = Image.open(filePath)

        # 色温度を調整する
        enhancer = ImageEnhance.Color(image)
        adjusted_image = enhancer.enhance(factor)
        
        adjusted_array = np.array(adjusted_image)

        corrected_image = Image.fromarray(adjusted_array.astype('uint8'))

        corrected_image.save(savePath + outFilename)


        return(outFilename, 0)





