'''
Created on Jul 2, 2015

@author: Nicoli
'''
from cellularautomata.modules.ParserImgText import ImgtoText, Parser
from cellularautomata.modules.CellularAutomata import TotalisticCode
from cellularautomata.modules.CAOutput import AutomataImage

if __name__ == '__main__':
    tc = TotalisticCode (330, 3, 2)
    tci = AutomataImage(10, tc, '', '.png')
    print(tci.dictColor)
    a = ImgtoText(3, '330.png', '')
    print (a.dictTxt)
    aParser = Parser('fromimg/Totalistic/330.txt', '')
    aParser.removeSeparator('\n')
    
    
    aParser.setBitsSeparation('\n', 7)
    print (aParser.strData)
    aParser.binary()
    print (aParser.strData)
    aParser.setNewFile()