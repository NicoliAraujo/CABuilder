'''
Created on 16/10/2014

@author: matsu
'''

class CellularAutomata:
    
    Default = ("111", "110", "101", "100", "011", "010", "001", "000")

    def __init__(self, rule, ruleBin, hashRule):
        '''
        Constructor
        '''
        self.rule = rule
        self.hashRule = hashRule
        self.ruleBin = ruleBin
    
    def setRule(self, rule):
        '''
        '''
                    
            
    def implementRule (self, ruleBin):
        '''
        '''

    @staticmethod
    def input(b1, b2, b3):
        '''
        Pega as posicoes e transforma em uma chave
        '''
        key = ( str(b1) + str(b2) + str(b3) )
        return key