'''
Created on 24/10/2014

@author: matsu
'''

'''
    Explicar aqui a geracao dos totalistic rules
'''
from IntKBase import IntKBase
class TotalisticRule():
    

    '''
    Constructor
    '''
    def __init__(self, rule, k):
        self.rule = rule
        self.k = k
        self.dictRule = {}
        self.buildRule()

        
        
    def buildRule(self):
        '''
        '''
        x = IntKBase()
        ruleInKBase = x.intKbase(self.rule, self.k)
        if (len(ruleInKBase) < 8):
            while (len(ruleInKBase) < 8):
                ruleInKBase = "0" + ruleInKBase 
        i = 7
        for d in ruleInKBase:
            self.dictRule[i] = d
            i -=1
            
    
    def getNext (self, nColor):
        '''
        Retorna o resultado da implementacao da regra para tres bits
        b3 eh o bit menos significativo
        tempString eh uma variavel local
        '''
        return int(self.dictRule[nColor])
    
    
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
    
    