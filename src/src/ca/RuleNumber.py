'''
Created on 16/10/2014

@author: matsu
@author: elloa
'''

'''
    Classe de Automatos gerados por uma regra numerica
    Segue a definicao de Wolfram para Cellular Automata Rule Number
'''
class RuleNumber():


    '''
    Constructor
    '''
    def __init__(self, rule):
        self.rule = rule
        self.dictRule = {}
        self.buildRule()

        
    '''
    Construindo o dicionario das regras de uma instancia do automato
    '''    
    def buildRule(self):
        ruleInBinary = bin(self.rule)[2:].zfill(8)
        i = 7
        for d in ruleInBinary:
            self.dictRule[i] = d
            i -= 1

            
    '''
    Retorna o resultado da implementacao da regra para tres bits
    b3 eh o bit menos significativo
    '''
    def getNext (self, b1, b2, b3):
        tempString = int(str(b1) + str(b2) + str(b3),2)
        return int(self.dictRule.get(tempString))
    
    '''
    Retorna o dicionario de regras do automato
    '''
    def getRule(self):
        return self.dictRule
    
    '''
    Retorna o nome do automato, que eh a regra numerica que ele implementa
    '''
    def getName(self):
        return self.rule
        
