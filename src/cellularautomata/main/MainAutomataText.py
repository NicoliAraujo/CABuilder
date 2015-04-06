# -*- coding: utf-8 -*-

'''
Created on 11/03/2015

@author: matsu
'''
from trunk.src.cellularautomata.automatatext.ImgtoText import Parser
from trunk.src.cellularautomata.automatatext.AutomataText import AutomataText
from trunk.src.cellularautomata.rulenumber.RuleNumberPicture import RuleNumberPicture
from trunk.src.cellularautomata.totalisticcode.TotalisticCodePicture import TotalisticCodePicture

if __name__ == '__main__':
    
    a = RuleNumberPicture(1024,1024, 30)
    a.setImage()
     
    x= AutomataText(a.image, a.automata.k, a.height, a.width)
 
    x.imgToTxt(a.automata.rule)
 
    print("Operação terminada")
     
#==============================================================================
#    b = TotalisticCodePicture(3, 3, 600, 3, 1)
#    b.setImage()
#     
#    x= AutomataText(b.image, b.automata.k, b.height, b.width)
# 
#    x.imgToTxt(b.automata.rule)
#==============================================================================
