'''
Created on 13/02/2015

@author: matsu
'''
from cellularautomata.modules.CellularAutomata import TotalisticCode, ElementaryCode

from cellularautomata.modules.CAOutput import AutomataImage


if __name__ == '__main__':
     
#===============================================================================
#     ec = ElementaryCode(30)
# 
#     eci = AutomataImage(100,ec,'')
#===============================================================================


    #===========================================================================
    # a = [1022, 1006, 1092, 1140, 1113, 1055, 600, 843, 870, 1085, 1167, 1329, 1572, 1815, 1942, 1599,993, 777, 1041, 1038, 2022,  1020, 1074, 1041, 177, 912 ,1636 ,2049,2048, 583 ,578]
    # print(len(a))
    # for i in a: 
    #     tc1 = TotalisticCode(int(i), 3, 1)
    #     tci1 = AutomataImage(1024, tc1,'fp1')
    #      
    #     tc2 = TotalisticCode(int(i), 3, 2)
    #     tci2 = AutomataImage(1024, tc2, 'fp2')
    #     print(str(i) + ' terminado')
    #===========================================================================
    
    for i in range  (1, 5):
       
        tc1 = TotalisticCode(180197744, 5, i)
        tci1 = AutomataImage(1024, tc1,'k5fp' + str(i))
             
        tc1 = TotalisticCode(180197748, 5, i)
        tci1 = AutomataImage(1024, tc1,'k5fp' + str(i))
    
