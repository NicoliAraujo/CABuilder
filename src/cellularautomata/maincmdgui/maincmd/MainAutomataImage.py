'''
Created on 13/02/2015

@author: matsu
'''
from cellularautomata.modules.CellularAutomata import TotalisticCode, ElementaryCode

from cellularautomata.modules.CAOutput import AutomataImage


if __name__ == '__main__':
#===============================================================================
#     
#     ec = ElementaryCode(rule=45)
# 
#     eci = AutomataImage(side = 10, ca = ec,name =  '' , filetype = '.png')
#===============================================================================


     
    tc = TotalisticCode(rule = 600, k = 3, seed=1)
    tci = AutomataImage(side = 16, ca = tc,info = '')
