'''
Created on 13/02/2015

@author: matsu
'''
from cellularautomata.modules.AutomataImage import AutomataImage
from cellularautomata.modules.CellularAutomata import TotalisticCode, ElementaryCode


if __name__ == '__main__':
    
    ec = ElementaryCode(rule=45)

    eci = AutomataImage(side = 10, ca = ec,name =  '' , filetype = '.png')



     
    tc = TotalisticCode(rule = 1074, k = 3, seed=2)
    tci = AutomataImage(side = 10, ca = tc,name = '' ,filetype = '.png')
