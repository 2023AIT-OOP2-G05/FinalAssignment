from PIL import Image, ImageEnhance
import os, cv2
from processororEdit.processorBase import processorBase

class contrastProcessor(processorBase):
    
    OUT_DIR = "./processoredPicture/contrast/"

    def process(self, image_path, filepath, factor):

        outFilename = os.path.basename(filepath)
        img_Contrast = cv2.imread(filepath)

        # 画像を開く
        image = Image.open(image_path)

        # コントラストを調整する
        enhancer = ImageEnhance.Contrast(image)
        high_contrast_image = enhancer.enhance(factor)
        
        corrected_image = Image.fromarray(high_contrast_image.astype('uint8'))
        corrected_image.save(self.OUT_DIR + outFilename)
        return(outFilename, 10)