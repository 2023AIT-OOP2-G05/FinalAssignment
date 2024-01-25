from PIL import Image, ImageEnhance
import os, cv2
from processorEdit.processorBase import processorBase

class exposureAmountProcessor(processorBase):
    
    OUT_DIR = "./processoredPicture/exposureAmount/"

    def process(self, image_path, filepath, factor):

        outFilename = os.path.basename(filepath)
        img_exposureAmount = cv2.imread(filepath)

        # 画像を開く
        image = Image.open(image_path)

        # 明るさを調整する
        enhancer = ImageEnhance.Brightness(image)
        brightened_image = enhancer.enhance(factor)

        corrected_image = Image.fromarray(brightened_image.astype('uint8'))
        corrected_image.save(self.OUT_DIR + outFilename)
        return(outFilename, 9)