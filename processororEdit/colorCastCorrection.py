from PIL import Image
import numpy as np
import os, cv2


class colorCastCorrectionProcessor:

    # 引数の数が多いためよくない
    def process(self, filePath, savePath, red_factor, green_factor, blue_factor):

        fileName = filePath.split("/")

        outFilename = os.path.basename(fileName[1])

        # 画像を開く
        image = Image.open(filePath)

        # 画像をNumPy配列に変換
        img_array = np.array(image)

        # 各色チャンネルに補正係数を乗算
        img_array[:, :, 0] = np.clip(img_array[:, :, 0] * red_factor, 0, 255)
        img_array[:, :, 1] = np.clip(img_array[:, :, 1] * green_factor, 0, 255)
        img_array[:, :, 2] = np.clip(img_array[:, :, 2] * blue_factor, 0, 255)

     # NumPy配列をImageオブジェクトに変換
        corrected_image = Image.fromarray(img_array.astype('uint8'))

    # 補正後の画像を表示するか保存するかなどの処理を追加
        corrected_image.save(savePath + outFilename)


        return(outFilename, 1)


    