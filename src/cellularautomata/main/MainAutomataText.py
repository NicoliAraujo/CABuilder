# -*- coding: utf-8 -*-

'''
Created on 11/03/2015

@author: Nicoli
'''

from __future__ import unicode_literals
from cellularautomata.modules.AutomataText import AutomataText
from cellularautomata.modules.ParserImgText import ParserSieve
from cellularautomata.modules.CellularAutomata import RuleNumber, TotalisticCode
from cellularautomata.modules.AutomataImage import AutomataImage


if __name__ == '__main__':
     
#     elementar = [72, 136, 103, 91, 30, 73, 101, 105, 129, 137, 161, 183, 169, 214, 225, 45, 26, 57, 62, 89]
#     
#     for i in elementar: 
#     
#         rule = RuleNumber(i)
#         ruletext = AutomataText(1000, 1000, rule, 1)
#         ruletext.setFile()
#         ParserSieve(str(ruletext.autocel.rule))
 
    rn = RuleNumber(45)
    rntext = AutomataText(5, 10, rn, '')



    #===========================================================================
    # ruletext.setFile()
    # ParserSieve(str(ruletext.autocel.rule))
    #  
    #===========================================================================
     

    #===========================================================================
    # print(str(e) + " :Operação terminada" )
    #===========================================================================
    tc = TotalisticCode(1074, 3, 1)
    tctext = AutomataText(10, 10, tc, '')
