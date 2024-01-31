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
import os, shutil

def blue(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)
    
    return(blueCutProcessor().process(filePath, savePath))

def red(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(redCutProcessor().process(filePath, savePath))

def green(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(greenCutProcessor().process(filePath, savePath))

def blueRed(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(blueRedHalfProcessor().process(filePath, savePath))

def blueGreen(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(blueGreenHalfProcessor().process(filePath, savePath))

def redGreen(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(redGreenHalfProcessor().process(filePath, savePath))

def colorTemperature(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(colorTemperatureProcessor().process(filePath, savePath, 1.5))

def colorCastCorrection(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(colorCastCorrectionProcessor().process(filePath, savePath, 1.2, 0.8, 1.0))

def saturation(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(saturationProcessor().process(filePath, savePath, 3))

def exposureAmount(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(exposureAmountProcessor().process(filePath, savePath, 1.5))

def contrast(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(contrastProcessor().process(filePath, savePath,1.5))

def highlight(filePath, savePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(highlightProcessor().process(filePath, savePath, 1.5))


def deleteOneImage(dir):
     shutil.rmtree(dir)
     os.mkdir(dir)