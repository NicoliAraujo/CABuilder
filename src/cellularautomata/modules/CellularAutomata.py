# -*- coding: utf-8 -*-

"""
Created on 04/01/2015

@author: Nicoli Araújo
@author: Elloá B. Guedes
"""

from __future__ import unicode_literals

from util.IntKBase import IntKBase


class CellularAutomata():
    """SuperClasse que define autômatos celulares. 
    
    Um automato celular é um vetor multidimensional composto por células que detém um estado. O estado de 
    cada célula é determinado por uma regra numérica que considera os estados das celulas vizinhas. 
    """

    def __init__(self, rule, k):
        """Construtor do autômato celular.
        
        Aqui, são instanciados a regra (rule) e o número de estados(k). Apos isso, é criado o dictRule.
        
        rule (int) - número da regra a que o autômato obedece.
        k (int) - número de estados que cada célula do autômato pode ter. Os estados são inteiros de 0 a k - 1.
        dictRule ( dict (int -> int) ) -  dicionário que relaciona números de 0 a 7 aos bits de rule na base k.
        """
        self.rule = rule
        self.k = k
        
        self.dictRule = {}
        self.dictRule = self.buildDictRule(self.rule, self.k)
        
    def buildDictRule(self, rule, k):
        """ Cria dictRule, que relaciona rule na base k com números de 0 a 8.
        
        Retorna um dicionário de 8 chaves, cada uma um inteiro de 0 a 7 armazenando um bit da string 
        de 8 bits ruleInKBase. É nesta variável que rule escrita na base k é guardada.
        
        retorna dictRule (int -> int)
        
        >>> ca.buildDictRule(30, 2)
        {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0}
        
        >>> ca.buildDictRule(45, 3)
        {0: 0, 1: 0, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0}
        
        >>> ca.buildDictRule(200, 3)
        {0: 2, 1: 0, 2: 1, 3: 1, 4: 2, 5: 0, 6: 0, 7: 0}
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
        pass
    
    def getDictRule(self):
        """Retorna dictRule, o dicionário ."""
        return self.dictRule
    
    def getName(self):
        """Retorna rule como string."""
        return str(self.rule)
        
    def getRule(self, chave):
        """Retorna dictRule[chave].
        
        chave (int) - um inteiro de 0 a 7, que armazena um dos k estados do autômato. 
        
        >>> ca.buildDictRule(200, 3)
        {0: 2, 1: 0, 2: 1, 3: 1, 4: 2, 5: 0, 6: 0, 7: 0}
         
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
    
    
class RuleNumber(CellularAutomata):
    """Subclasse de CeCellularAutomataDefine autômatos celulares do tipo elementar. 
    
    Em um RuleNumber, as células podem apresentar apenas dois estados, levando em consideração os estados 
    das três células vizinhas presentes na iteração imediatamente anterior.
    """

    def __init__(self, rule):
        """Construtor da classe RuleNumber. 
        
        Estende CellularAuCellularAutomatale, k).
        
        Aqui, são instanciados rule e k. É implementado o conceito de apenas dois estados, dando-se
        a k fixamente o valor 2. Assim, não é necessário declarar k. 
        """
        CellularAutomata (rule, k = 2)

    def getNext (self, b1, b2, b3):
        """Retorna dictRule[b1b2b3], sendo b1b2b3 os três parâmetros concatenados.
         
        Sobrescreve CellularAutomata.CellularAutomatab3).
        
        Método que recebe o estado de tres vizinhas, concatena-os, transforma-os em inteiro para ser chave
        retornar o valor ao qual esta associado no dictRule. 
        
        >>> rn = RuleNumber(45)
        
        >>> rn.dictRule
        {0: 1, 1: 0, 2: 1, 3: 1, 4: 0, 5: 1, 6: 0, 7: 0}
        
        >>> rn.getNext(1, 0, 0)
        0
        
        >>> rn.getNext(0, 1, 1)
        1
        
        >>> rn.getNext(1, 1, 1)
        0
        """
        temp = int( str(b1) + str(b2) + str(b3),2 )
        
        return self.dictRule.get(temp)
    
    
class TotalisticCode(CellularAutomata):
    """Classe que define os autômatos do tipo totalistico.
    
    Um TotalisticCode pode ter mais de dois estados possíveis para cada célula. Além disso, para definir 
    o estado de uma célula, é feita a média entre as três células vizinhas da iteração imediatamente anterior.
    """
          
    def getNext (self, b1, b2, b3):
        """Retorna dictRule[b1+b2+b3]
        
        Sobrescreve CellularAutomCellularAutomatab2, b3).
        
        Define o estado de uma célula a partir do estado de três vizinhas, armazenados em b1, b2 e b3. Retorna o valor
        no dictRule referente à soma dos três estados fornecidos.
        
        >>> tc = TotalisticCode(200, 3)
        
        >>> tc.dictRule
        {0: 2, 1: 0, 2: 1, 3: 1, 4: 2, 5: 0, 6: 0, 7: 0}
        
        >>> tc.getNext(0, 2, 1)
        1
        >>> tc.getNext(0, 2, 2)
        2
        >>> tc.getNext(2, 2, 2)
        0
        """
        tempInt = b1 + b2 + b3
        return self.dictRule.get(tempInt)
    