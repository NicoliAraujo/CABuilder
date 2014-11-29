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
    def __init__(self, rule, k):
        self.k = k
        self.rule = rule
        self.dictRule = {}
        self.buildRule()

        
        
    def buildRule(self):
        '''
        Constroi o dicionario das regras de uma instancia do automato
        ruleInBinary ja recebe o binario da regra sem os 2 primeiros digitos e preenchido com 0's
        no for, o dictRule eh relacionado com os digitos do ruleInBinary
        RuleInBinary eh uma variavel local
        '''
        ruleInBinary = bin(self.rule)[2:].zfill(8) 
        i = 7
        for d in ruleInBinary:
            self.dictRule[i] = d
            i -= 1 

            
    
    def getNext (self, b1, b2, b3):
        '''
        Retorna o resultado da implementacao da regra para tres bits
        b3 eh o bit menos significativo
        tempString eh uma variavel local
        '''
        tempString = int(str(b1) + str(b2) + str(b3),2)
        return int(self.dictRule.get(tempString))
    
    
    def getRule(self):
        '''
        Retorna o dicionario de regras do automato
        '''
        return self.dictRule
    
   
    def getName(self):
        '''
        Retorna o nome do automato, que eh a regra numerica que ele implementa
        '''
        return self.rule
        
