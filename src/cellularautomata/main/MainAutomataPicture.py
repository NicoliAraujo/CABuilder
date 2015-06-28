'''
Created on 13/02/2015

@author: matsu
'''
from cellularautomata import AutomataImage
from cellularautomata.CellularAutomata import CellularAutomata


if __name__ == '__main__':
    ca = CellularAutomata(rule=30, k=2)
    ap = AutomataImage(height=3, width=3, rule=30, k=2, firstK=1)
    print(ap.dictColor)