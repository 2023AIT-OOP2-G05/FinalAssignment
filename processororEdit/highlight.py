from PIL import Image, ImageEnhance
import os, cv2
from processororEdit.processorBase import processorBase

class highlightProcessor(processorBase):

    OUT_DIR = "./processedPicture/"


    def process(self, image_path, filepath, factor):

        outFilename = os.path.basename(filepath)
        img_highlight = cv2.imread(filepath)


        # 画像を開く
        image = Image.open(image_path)

        # 明るい領域を抽出
        bright_pixels = image.point(lambda p: p * factor if p > 128 else p)

        corrected_image = Image.fromarray(bright_pixels.astype('uint8'))
        corrected_image.save(self.OUT_DIR + outFilename)
        return(outFilename, 11)


       