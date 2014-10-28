'''
Created on 16/10/2014

@author: matsu
'''
from src.CellularAutomata.CellularAutomata import CellularAutomata

class RuleNumber(CellularAutomata):
    '''
    Classe de Automatos gerados por uma regra simples
    '''

    def __init__(self, rule, ruleBin, hashRule):
        '''
        Constructor
        '''
        CellularAutomata.__init__(self, rule, ruleBin, hashRule)
        self.ruleBin = self.setRule(self.rule)
        self.setRule(self.rule)
        self.implementRule(self.ruleBin)
    
    def setRule(self, rule):
        '''
        Funcao que transforma a regra em uma string de tamanho 8
        para que seja possivel fazer a comparacao com a tupla default
        '''
        self.ruleBin = CellularAutomata.setRule(self, rule)
        self.ruleBin = str (bin(rule) ) 
        self.ruleBin = self.ruleBin[2:]
               
        if len(self.ruleBin) < 8: 
                for i in range(len(self.ruleBin),8):
                    self.ruleBin = "0" + self.ruleBin
        return str(self.ruleBin)

    def input(self, b1, b2, b3):
        '''
        Pega as posicoes, transforma em uma chave, passa pro hashRule e retorna 
        o valor correspondente
        '''

        key = CellularAutomata.input(b1, b2, b3)
        return self.hashRule[key]
            
    def implementRule (self, ruleBin):
        '''
        
        '''
        CellularAutomata.implementRule(self, self.ruleBin)
        for i in range(0,8):
            self.hashRule[ CellularAutomata.Default[i] ] = self.ruleBin[i]
        
