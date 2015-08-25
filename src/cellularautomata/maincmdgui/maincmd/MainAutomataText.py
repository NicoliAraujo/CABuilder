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
#     ectext = AutomataText(20, 10, ec, '');

    #===========================================================================
    a = [1022, 1006, 1092, 1140, 1113, 1055, 600, 843, 870, 1085, 1167, 1329, 1572, 1815, 1942, 1599,993, 777, 1041, 1038, 2022,  1020, 1074, 1041, 177, 912 ,1636 ,2049,2048, 583 ,578]
    for i in a:
        tc = TotalisticCode(i, 3, 1)
        tctext = AutomataText(100, 10000, tc, '')
        parsertctext = Parser('/original/Totalistic/' + str(i) + '.txt')
        parsertctext.removeSeparator('\n')
        parsertctext.setNewFile('')
