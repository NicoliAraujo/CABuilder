# -*- coding: utf-8 -*-

'''
Created on 11/03/2015

@author: Nicoli
'''

from __future__ import unicode_literals

from cellularautomata.modules.CellularAutomata import ElementaryCode, TotalisticCode
from cellularautomata.modules.ParserImgText import Parser, ImgtoText

from cellularautomata.modules.CAOutput import AutomataImage, AutomataText


if __name__ == '__main__':
     
#     elementar = [72, 136, 103, 91, 30, 73, 101, 105, 129, 137, 161, 183, 169, 214, 225, 45, 26, 57, 62, 89]
#     
#     for i in elementar: 
#     
#         rule = RuleNumber(i)
#         ruletext = AutomataText(1000, 1000, rule, 1)
#         ruletext.setFile()
#         ParserSieve(str(ruletext.autocel.rule))
 
#===============================================================================
#     ec = ElementaryCode(45)
#     ectext = AutomataText(20, 10, ec, '')
#     ecimg = AutomataImage(10, ec, '')
# 
# 
# 
#     #===========================================================================
#===============================================================================
    # ruletext.setFile()
    # ParserSieve(str(ruletext.autocel.rule))
    #  
    #===========================================================================
     

    #===========================================================================
    # print(str(e) + " :Operação terminada" )
    #===========================================================================
    tc = TotalisticCode(600, 3, 1)
    tctext = AutomataText(10, 100, tc, '')
    parsertctext = Parser('/original/Totalistic/600.txt')
    parsertctext.removeSeparator('\n')
    parsertctext.setNewFile('')
