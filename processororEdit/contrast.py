from PIL import Image, ImageEnhance
import os, cv2
import numpy as np 
from processororEdit.processorBase import processorBase

class contrastProcessor(processorBase):
    
    OUT_DIR = "./processedPicture/"

    def process(self, filepath, factor):

        outFilename = os.path.basename(filepath)

        # 画像を開く
        image = Image.open(filepath)

        # コントラストを調整する
        enhancer = ImageEnhance.Contrast(image)
        high_contrast_image = enhancer.enhance(factor)
        
        high_contrast_array = np.array(high_contrast_image)
        
        corrected_image = Image.fromarray(high_contrast_array.astype('uint8'))
        corrected_image.save(self.OUT_DIR + outFilename)
        return(outFilename, 10)