'''
Created on 24/10/2014

@author: matsu
'''

from CelAuto.CelularAutomata import CelularAutomata
'''
    Explicar aqui a geracao dos totalistic rules
'''

class TotalisticRule(CelularAutomata):
    

    
    def __init__(self, rule, k):
        '''
        Inicia o totalistic Rule: pega a regra e a quantidadede cores, e gera o dicionario
        '''
        CelularAutomata.__init__(self, rule, k)

        

    def getNext (self, b1, b2, b3):
        '''
        Retorna o resultado da implementacao da regra para tres bits
        b1, b2 e b3 sao strings 
        São transformadas em inteiros, e o valor dessa soma eh usado como chave para o site que sera inserido
        '''
        tempInt = int(b1) + int(b2) + int(b3)
        return self.dictRule[tempInt]
    