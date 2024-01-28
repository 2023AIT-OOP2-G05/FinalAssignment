from processorColor.blueCut import blueCutProcessor
from processorColor.redCut import redCutProcessor
from processorColor.greenCut import greenCutProcessor
from processorColor.blueRedHalf import blueRedHalfProcessor
from processorColor.blueGreenHalf import blueGreenHalfProcessor
from processorColor.redGreenHalf import redGreenHalfProcessor
from processororEdit.colorTemperature import  colorTemperatureProcessor
from processororEdit.colorCastCorrection import colorCastCorrectionProcessor
from processororEdit.saturation import saturationProcessor
from processororEdit.exposureAmount import exposureAmountProcessor
from processororEdit.contrast import contrastProcessor
from processororEdit.highlight import highlightProcessor
from GrayTest import grayScale
import os

# お試し
# def grayScalePro(filePath):
#     # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
#     # print(r) # True (存在する)

#     return(grayScale.grayScaleAndBinary(filePath))

def blue(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)
    
    return(blueCutProcessor().process(filePath))

def red(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(redCutProcessor().process(filePath))

def green(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(greenCutProcessor().process(filePath))

def blueRed(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(blueRedHalfProcessor().process(filePath))

def blueGreen(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(blueGreenHalfProcessor().process(filePath))

def redGreen(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(redGreenHalfProcessor().process(filePath))

def colorTemperature(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(colorTemperatureProcessor().process(filePath, 1.5))

def colorCastCorrection(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(colorCastCorrectionProcessor.process(filePath, 1.2, 0.8, 1.0))

def saturation(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(saturationProcessor().process(filePath, 3))

def exposureAmount(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(exposureAmountProcessor().process(filePath, 1.5))

def contrast(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(contrastProcessor().process(filePath,1.5))

def highlight(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(highlightProcessor().process(filePath, 1.5))

