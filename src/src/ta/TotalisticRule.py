'''
Created on 24/10/2014

@author: matsu
'''

'''
    Explicar aqui a geracao dos totalistic rules
'''
from IntKBase import IntKBase
class TotalisticRule():
    

    
    def __init__(self, rule, k):
        '''
        Constructor
        Inicia o totalistic Rule: pega a regra e a quantidadede cores, e gera o dicionario
        '''
        self.rule = rule
        self.k = k
        self.nTons = ( 3 * self.k ) - 2
        self.dictRule = {}
        self.buildRule(rule, k)

        
      
    def buildRule(self, rule, k):
        '''
        Pega a regra e o k
        Escreve a regra na base k
        Coloca a regra na base k
        Atribui a cada uma das 8 casas do dictRule um digito da regraInKBase, ao contrario 
        '''  
        x = IntKBase()
        ruleInKBase = x.intKbase(rule, k)
        if (len(ruleInKBase) < 8):
            while (len(ruleInKBase) < 8):
                ruleInKBase = "0" + ruleInKBase 
        i = 7
        for d in ruleInKBase:
            self.dictRule[i] = d
            i -=1
        print ("dictRule: " )
        print((self.dictRule))
            
    
    
    def getNext (self, b1, b2, b3):
        '''
        Retorna o resultado da implementacao da regra para tres bits
        b1, b2 e b3 sao strings 
        '''
        print ("rule4" + str(b1) + " " + str(b2) + " " + str(b3) + " : ")
        print(self.dictRule [b1 + b2 + b3])
        return self.dictRule [b1 + b2 + b3]
    
    
    
    def getRule(self):
        '''
        Retorna o dicionario de regras do automato
        '''
        return self.dictRule
        
    
    def getSite(self, b):
        return self.dictRule[b]
    
    def getTons(self):
        '''
        Retorna a quantidade de tons que existe para um numero k de cores
        '''
        return self.nTons
    
    
   
    def getName(self):
        '''
        Retorna o nome do automato, que eh a regra numerica que ele implementa
        '''
        return self.rule
    
    