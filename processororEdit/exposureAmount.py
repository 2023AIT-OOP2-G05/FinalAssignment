from PIL import Image, ImageEnhance
import os, cv2
import numpy as np 
from processororEdit.processorBase import processorBase

class exposureAmountProcessor(processorBase):
    
    OUT_DIR = "./processedPicture/"

    def process(self, filepath, factor):

        outFilename = os.path.basename(filepath)

        # 画像を開く
        image = Image.open(filepath)

        # 明るさを調整する
        enhancer = ImageEnhance.Brightness(image)
        brightened_image = enhancer.enhance(factor)

        brightened_array = np.array(brightened_image)

        corrected_image = Image.fromarray(brightened_array.astype('uint8'))
        corrected_image.save(self.OUT_DIR + outFilename)
        return(outFilename, 3)