from PIL import Image, ImageEnhance
import os, cv2
import numpy as np 
from processororEdit.processorBase import processorBase

class contrastProcessor(processorBase):

    def process(self, filePath, savePath, factor):

        fileName = filePath.split("/")

        outFilename = os.path.basename(fileName[1])

        # 画像を開く
        image = Image.open(filePath)

        # コントラストを調整する
        enhancer = ImageEnhance.Contrast(image)
        high_contrast_image = enhancer.enhance(factor)
        
        high_contrast_array = np.array(high_contrast_image)
        
        corrected_image = Image.fromarray(high_contrast_array.astype('uint8'))
        corrected_image.save(savePath + outFilename)
        return(outFilename, 4)