from PIL import Image, ImageEnhance
import os, cv2
import numpy as np 
from processororEdit.processorBase import processorBase

class colorTemperatureProcessor(processorBase):

    OUT_DIR = "./processedPicture/"

    def process(self, filepath, factor):

        outFilename = os.path.basename(filepath)

        # 画像を開く
        image = Image.open(filepath)

        # 色温度を調整する
        enhancer = ImageEnhance.Color(image)
        adjusted_image = enhancer.enhance(factor)
        
        adjusted_array = np.array(adjusted_image)

        corrected_image = Image.fromarray(adjusted_array.astype('uint8'))

        corrected_image.save(self.OUT_DIR + outFilename)


        return(outFilename, 0)





