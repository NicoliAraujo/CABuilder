'''
Created on 04/01/2015

@author: matsu
'''
from ta.IntKBase import IntKBase

class CelularAutomata():
    '''
    Classe geral de automatos celulares
    '''


    def __init__(self, rule, k):
        '''
        Pega a regra e o numero de estados possiveis do automato
        Constroi o dicionario de regras
        '''
        self.rule = rule
        self.k = k
        self.dictRule = {}
        self.buildRule(self.rule, self.k)
        
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
    
    def getNext(self, b1, b2, b3):
        '''Metodo para definir o proximo site a ser inserido, a partir dos 3 sites em t-1'''
        pass
    
    def getDictRule(self):
        '''
        Retorna o dicionario de regras do automato
        '''
        return self.dictRule
    
    def getName(self):
        '''
        Retorna o nome do automato, que eh a regra numerica que ele implementa
        '''
        return self.rule
        
    def getRule(self, chave):
        '''
        Retorna o dicionario de regras do automato
        '''
        return self.dictRule[chave]
        