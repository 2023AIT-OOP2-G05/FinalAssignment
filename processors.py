from processorColor.blueCut import buleCutProcessor
from processorColor.redCut import redCutProcessor
from processorColor.greenCut import greenCutProcessor
from processorColor.blueRedHalf import buleRedHalfProcessor
from processorColor.blueGreenHalf import buleGreenHalfProcessor
from processorColor.redGreenHalf import redGreenHalfProcessor
from processororEdit.colorTemperature import  colorTemperatureProcessor
from processororEdit.colorCastCorrection import colorCastCorrectionProcessor
from processororEdit.saturation import saturationProcessor
from processororEdit.exposureAmount import exposureAmountProcessor
from processororEdit.contrast import contrastProcessor
from processororEdit.highlight import highlightProcessor
import os

def blue(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(buleCutProcessor.process(filePath))

def red(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(redCutProcessor.process(filePath))

def green(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(greenCutProcessor.process(filePath))

def bluered(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(buleRedHalfProcessor.process(filePath))

def bluegreen(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(buleGreenHalfProcessor.process(filePath))

def redgreen(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(redGreenHalfProcessor.process(filePath))

def colorTemperature(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(colorTemperatureProcessor.colorTemperature(filePath))

def colorCastCorrection(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(colorCastCorrectionProcessor.colorCastCorrection(filePath))

def saturation(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(saturationProcessor.saturation(filePath))

def exposureAmount(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(exposureAmountProcessor.exposureAmount(filePath))

def contrast(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(contrastProcessor.contrast(filePath))

def highlight(filePath):
    # r = os.path.exists('uploadsPicture/liberoPAUI4519_TP_V.jpeg')
    # print(r) # True (存在する)

    return(highlightProcessor.highlight(filePath))