from PIL import Image, ImageEnhance
import os, cv2

from processororEdit.processorBase import processorBase

class colorTemperatureProcessor(processorBase):

    OUT_DIR = "./processedPicture/"

    def process(self, image_path, filepath, factor):

        outFilename = os.path.basename(filepath)
        img_colorTemperature = cv2.imread(filepath)

        # 画像を開く
        image = Image.open(image_path)

        # 色温度を調整する
        enhancer = ImageEnhance.Color(image)
        adjusted_image = enhancer.enhance(factor)
        
        corrected_image = Image.fromarray(adjusted_image.astype('uint8'))

        corrected_image.save(self.OUT_DIR + outFilename)


        return(outFilename, 6)





