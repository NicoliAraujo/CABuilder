'''
Created on 24/10/2014

@author: matsu
'''

from src.cellularautomata.CellularAutomata import CellularAutomata
'''
    Explicar aqui a geracao dos totalistic rules
'''

class TotalisticCode(CellularAutomata):
    

    
    def __init__(self, rule, k):
        '''
        Inicia o totalistic Rule: pega a regra e a quantidadede cores, e gera o dicionario
        '''
        CellularAutomata.__init__(self, rule, k)

        

    def getNext (self, b1, b2, b3):
        '''
       Teste
        '''
        tempInt = int(b1) + int(b2) + int(b3)
        return self.dictRule[tempInt]
    