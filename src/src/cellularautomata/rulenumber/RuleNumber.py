'''
Created on 16/10/2014

@author: matsu
@author: elloa
'''
from src.cellularautomata.CellularAutomata import CellularAutomata

'''
    Classe de Automatos gerados por uma regra numerica
    Segue a definicao de Wolfram para Cellular Automata Rule Number
'''
class RuleNumber(CellularAutomata):

    def __init__(self, rule, k=2):
        CellularAutomata.__init__(self, rule, k)


    
    def getNext (self, b1, b2, b3):
        '''
        Retorna o resultado da implementacao da regra para tres bits
        b1, b2 e b3 sao strings, que sao concatenadas
        O resultado da concatenacao eh transformado em int, que eh usado como chave para o proximo site
        b3 eh o bit menos significativo
        '''
        tempString = int( str(b1) + str(b2) + str(b3),2 )
        return int(self.dictRule.get(tempString))
