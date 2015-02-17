'''
Created on 13/02/2015

@author: matsu
'''
from trunk.src.cellularautomata.AutomataPicture import AutomataPicture
from trunk.src.cellularautomata.CellularAutomata import CellularAutomata


if __name__ == '__main__':
    ca = CellularAutomata(rule=30, k=2)
    ap = AutomataPicture(height=3, width=3, rule=30, k=2, firstK=1)
    print(ap.dictColor)