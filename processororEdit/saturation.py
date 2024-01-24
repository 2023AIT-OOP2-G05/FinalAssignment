from PIL import Image, ImageEnhance
import os, cv2
from processororEdit.processorBase import processorBase

class saturationProcessor(processorBase):

    OUT_DIR = "./processoredPicture/saturation/"

    def process(self, image_path, filepath, factor):

        outFilename = os.path.basename(filepath)
        img_saturation = cv2.imread(filepath)

        # 画像を開く
        image = Image.open(image_path)

        # 彩度を調整する
        enhancer = ImageEnhance.Color(image)
        saturated_image = enhancer.enhance(factor)

        
        corrected_image = Image.fromarray(saturated_image.astype('uint8'))
        corrected_image.save(self.OUT_DIR + outFilename)
        return(outFilename, 8)

   