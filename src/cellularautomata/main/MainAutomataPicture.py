'''
Created on 13/02/2015

@author: matsu
'''
from cellularautomata.modules.AutomataImage import AutomataImage
from cellularautomata.modules.CellularAutomata import TotalisticCode, RuleNumber


if __name__ == '__main__':
    rn = RuleNumber(rule=45)

    rni = AutomataImage(side = 1000, ca = rn, filetype = '.png')



     
    tc = TotalisticCode(rule = 1074, k = 3, seed=2)
    tci = AutomataImage(side = 10, ca = tc, filetype = '.png')
