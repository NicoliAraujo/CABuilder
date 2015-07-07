'''
Created on Jul 7, 2015

@author: Nicoli
'''
from cellularautomata.modules.CAOutput import AutomataImage, AutomataText
from cellularautomata.modules.CellularAutomata import TotalisticCode, ElementaryCode
from cellularautomata.modules.ParserImgText import ImgtoText, Parser


#MainGenImg
def GenImg(catype, rule, k, seed, side, info):
    #get params dos labels
    ca = setCellularAutomata(rule, k, seed, catype)
    caimg = AutomataImage(side, ca, info)

    #enviar signal pro dialog do SUCCESS

def GenNumSeq(catype, rule, k, seed, size, it,  info):
    if catype == 'Elementary':
        ca = ElementaryCode(rule)
    elif catype == 'Totalistic':
        ca = TotalisticCode(rule, k, seed)
    return ca 
    catxt = AutomataText(size, it, ca, info)

    
def GenNumSeqFromImg(caK, caImageName, info):
    imgtext = ImgtoText(caK, caImageName, info)

def ManNumSeq(oldFilePath):
    txtparser = Parser(oldFilePath)