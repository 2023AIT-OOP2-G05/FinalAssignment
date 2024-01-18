from GrayTest import grayScale
import os

def gray(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(grayScale.grayScaleAndBinary(filePath))