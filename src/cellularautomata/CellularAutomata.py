# -*- coding: utf-8 -*-

"""
Created on 04/01/2015

@author: nicoli
"""

from __future__ import unicode_literals

from trunk.src.util.IntKBase import IntKBase


class CellularAutomata():
    """
    SuperClasse que define autômatos celulares. Um automato celular é um vetor multidimensional 
    composto por células que detém um estado. O estado de cada célula é determinado por uma regra
    numérica que considera os estados das celulas vizinhas. 
    
    Atributos de um CellularAutomata:
    
    k: int 
        número de estados que cada célula do autômato pode ter. Os estados são inteiros de 0 a k - 1
              
    rule: int
        número da regra a que o autômato obedece. 
    
    dictRule: dicionário (int -> int)
        dicionário que relaciona números de 0 a 7 aos bits de rule na base k
        
     
    """


    def __init__(self, rule, k):
        
        """ (int, int)
        Construtor do autômato celular. Aqui, são definidos a regra (rule) e o número de estados(k). 
        Apos isso, é criado o dictRule.
        """
        self.rule = rule
        self.k = k
        
        self.dictRule = {}
        self.dictRule = self.buildDictRule(self.rule, self.k)
        
    def buildDictRule(self, rule, k):
        """ (int, int) -> dict (int -> int)
        
        Retorna um dicionário de 8 chaves, cada uma um inteiro de 0 a 7 armazenando um bit da string 
        de 8 bits ruleInKBase. É nesta variável que rule escrita na base k é guardada.
        
        retorna dictRule (int->string)
        
        >>> ca.buildDictRule(30, 2)
        {0: '0', 1: '1', 2: '1', 3: '1', 4: '1', 5: '0', 6: '0', 7: '0'}
        
        >>> ca.buildDictRule(45, 3)
        {0: '0', 1: '0', 2: '2', 3: '1', 4: '0', 5: '0', 6: '0', 7: '0'}
        
        >>> ca.buildDictRule(200, 3)
        {0: '2', 1: '0', 2: '1', 3: '1', 4: '2', 5: '0', 6: '0', 7: '0'}
        
        """
        ruleInKBase = IntKBase(rule, k).numInBase
        dictRule = {}
        if (len(ruleInKBase) < 8):
            while (len(ruleInKBase) < 8):
                ruleInKBase = "0" + ruleInKBase 
        i = 7
        for d in ruleInKBase:
            dictRule[i] = int(d)
            i -=1
        return dictRule
    
    def getNext(self, b1, b2, b3):
        """(int, int, int)
        Define o estado de uma célula a partir do estado de três vizinhas. Muda de acordo com o tipo 
        de autômato.
        """
        pass
    
    def getDictRule(self):
        """Retorna dictRule (int -> string): dict."""
        return self.dictRule
    
    def getName(self):
        """() -> string
        Retorna o nome do autômato, que é o número de sua regra (rule) como string.
        """
        return str(self.rule)
        
    def getRule(self, chave):
        """ (int) -> string
        Retorna o valor guardado pela chave no dictRule. 
        
        >>> ca.buildDictRule(200, 3)
        {0: '2', 1: '0', 2: '1', 3: '1', 4: '2', 5: '0', 6: '0', 7: '0'}
         
        >>> ca.getRule(0)
        '0'
        >>> ca.getRule(2)
        '1'
        >>> ca.getRule(3)
        '1'
        """
        return self.dictRule.get(chave)
    
    def getK(self):
        """Retorna k."""
        return self.k