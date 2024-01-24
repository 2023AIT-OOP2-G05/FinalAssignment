from PIL import Image
import numpy as np
import os, cv2

from processororEdit.processorBase import processorBase

class colorCastCorrectionProcessor(processorBase):

    OUT_DIR = "./processoredPicture/colorCastCorrection/"

    def process(self, filepath, red_factor, green_factor, blue_factor):

        outFilename = os.path.basename(filepath)
        img_redgreenCut = cv2.imread(filepath)

        # 画像を開く
        image = Image.open(self, filepath)

        # 画像をNumPy配列に変換
        img_array = np.array(image)

        # 各色チャンネルに補正係数を乗算
        img_array[:, :, 0] = np.clip(img_array[:, :, 0] * red_factor, 0, 255)
        img_array[:, :, 1] = np.clip(img_array[:, :, 1] * green_factor, 0, 255)
        img_array[:, :, 2] = np.clip(img_array[:, :, 2] * blue_factor, 0, 255)

     # NumPy配列をImageオブジェクトに変換
        corrected_image = Image.fromarray(img_array.astype('uint8'))

    # 補正後の画像を表示するか保存するかなどの処理を追加
        corrected_image.save(self.OUT_DIR + outFilename)


        return(outFilename, 7)


    