from PIL import Image, ImageEnhance
import os, cv2
import numpy as np 
from processororEdit.processorBase import processorBase

class saturationProcessor(processorBase):

    OUT_DIR = "./processedPicture/"

    def process(self, filepath, factor):

        outFilename = os.path.basename(filepath)
        # img_saturated = cv2.imread(filepath)

        # 画像を開く
        image = Image.open(filepath)

        # 彩度を調整する
        enhancer = ImageEnhance.Color(image)
        saturated_image = enhancer.enhance(factor)

        saturated_array = np.array(saturated_image)

        corrected_image = Image.fromarray(saturated_array.astype('uint8'))
        corrected_image.save(self.OUT_DIR + outFilename)
        return(outFilename, 2)

   