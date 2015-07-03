# -*- coding: utf-8 -*-

"""
Created on 04/01/2015

@author: Nicoli Araújo
@author: Elloá B. Guedes


Este módulo contém as classes que definem um Autômato Celular.
    Superclasse CellularAutomata - Define métodos e atributos gerais de um CA
    Classe ElementaryCode - Instancia métodos e atributos específicos para autômatos celulares com k = 2
    Classe TotalisticCode - Instancia métodos e atributos para autômatos celulares com k > 2 
"""

from __future__ import unicode_literals

from util.IntKBase import IntKBase


class CellularAutomata(object):
    """SuperClasse que define autômatos celulares. 
    
    Um automato celular é um vetor multidimensional composto por células que detém um estado. O estado de 
    cada célula é determinado por uma regra numérica que considera os estados das celulas vizinhas. 
    """

    def __init__(self, rule, k, seed):
        """Construtor do autômato celular.
        
        Aqui, são instanciados a regra (rule), o número de estados(k), e o primeiro estado da célula que se encontra 
        exatamente no centro do vetor (seed).
        Apos isso, é criado um dicionário que associa o estado da vizinhança de uma célula com o seu próprio
        (dictRule).
        
        rule (int) - número da regra a que o autômato obedece.
        k (int) - número de estados que cada célula do autômato pode ter. Os estados são inteiros de 0 a k - 1.
        seed (int) - estado inicial da célula central do autômato celular
        dictRule ( dict (int -> int) ) -  dicionário que relaciona os estados de uma vizinhança (inteiros de 0 a 7) 
                                          ao estado de uma célula (bits de rule na base k).
                                          
        type (str) - tipo do autômato celular. Inicialmente, é vazio, ou genérico.
        """
        self.__rule = rule
        self.__k = k
        self.__seed = seed
        self.__type = ''

        self.__dictRule = self.setDictRule(self.rule, self.k)
    

        
    def setDictRule(self, rule, k):
        """ Cria o dicionário de 8 chaves dictRule, que relaciona a vizinhança com o estado de uma célula.
        
        Cada chave é um inteiro de 0 a 7 que representa uma soma dos estados de uma vizinhança. 
        As chaves guardam inteiros que vão de 0 a k-1, que representam os possíveis estados da célula
        a partir da vizinhança designada na chave. Cada estado é um bit da string de tamalho 8
        ruleInKBase. É nesta variável que rule escrita na base k é guardada.
        
        retorna dictRule (int -> int)
        
        >>> ca.setDictRule(30, 2)
        {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0}
        
        >>> ca.setDictRule(45, 3)
        {0: 0, 1: 0, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0}
        
        >>> ca.setDictRule(200, 3)
        {0: 2, 1: 0, 2: 1, 3: 1, 4: 2, 5: 0, 6: 0, 7: 0}
        """
        ruleInKBase = IntKBase(rule, k).numInBase
        self.__dictRule = {}
        if (len(ruleInKBase) < 8):
            while (len(ruleInKBase) < 8):
                ruleInKBase = "0" + ruleInKBase 
        i = 7
        for d in ruleInKBase:
            self.__dictRule[i] = int(d)
            i -=1
        return self.__dictRule
    
    
    def getNext(self, b1, b2, b3):     
        pass
    

    def __str__(self):
        """Retorna o nome do autômato celular."""
        return str(self.type) + str(self.rule)
    
    
    def getState(self, chave):
        """Retorna dictRule[chave].
        
        chave (int) - um inteiro de 0 a 7, que armazena uma das oito possíveis combinações de estados
        da vizinhança de uma célula. 
        
        >>> ca.setDictRule(200, 3)
        {0: 2, 1: 0, 2: 1, 3: 1, 4: 2, 5: 0, 6: 0, 7: 0}
         
        ca.getState(0)
        2
        ca.getState(6)
        0
        ca.getState(4)
        2
        """
        
        return self.dictRule[chave]
    
    @property
    def rule(self):
        return self.__rule
    
    @property
    def k(self):
        """Retorna k."""
        return self.__k
    
    @property
    def dictRule(self):
        return self.__dictRule
    
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, type):
        self.__type = type
        
    @property
    def seed(self):
        return self.__seed
    
    
class ElementaryCode(CellularAutomata):
    """Subclasse de CellularAutomata: Define autômatos celulares do tipo elementar. 
    
    Em um ElementaryCode, as células podem apresentar apenas dois estados ao levar em consideração os estados 
    das três células vizinhas da iteração imediatamente anterior.
    """

    def __init__(self, rule):
        """Construtor da classe ElementaryCode. 
        
        Estende o construtor de CellularAutomata.
        
        Aqui, são instanciados rule, k, type e seed. É implementado o conceito de apenas dois estados, dando-se
        a k o valor 2 e a seed o valor 1 . Também é alterado o tipo do autômato celular, assumindo-se sua 
        característica elementar.
        """

        super().__init__(rule, k = 2, seed = 1)
        self.type = 'Elementary'
        
            
    def getNext (self, b1, b2, b3):
        """Retorna dictRule[b1b2b3], sendo b1b2b3 os três parâmetros concatenados.
         
        Sobrescreve CellularAutomata.getNext(b1, b2, b3).
        
        Método que recebe o estado de tres vizinhas, concatena-os para transformá-los em um binário, e 
        os transforma no número inteiro correspondente, que é utilizado como chave do dictRule.
        
        Retornar o valor ao qual a chave esta associada no dictRule. 
        
        >>> ec = ElementaryCode(45)
        
        >>> ec.dictRule
        {0: 1, 1: 0, 2: 1, 3: 1, 4: 0, 5: 1, 6: 0, 7: 0}
        
        >>> ec.getNext(1, 0, 0)
        0
        
        >>> ec.getNext(0, 1, 1)
        1
        
        >>> ec.getNext(1, 1, 1)
        0
        """
        temp = int( str(b1) + str(b2) + str(b3),2 )
        
        return self.dictRule[temp]
    

    
    
class TotalisticCode(CellularAutomata):
    """Subclasse que define os autômatos do tipo totalistico.
    
    Um TotalisticCode pode ter mais de dois estados possíveis para cada célula. Além disso, para definir 
    o estado de uma célula, é feita a média entre as três células vizinhas da iteração imediatamente anterior.
    
    """

    def __init__(self, rule, k, seed):
        '''
        Construtor da subclasse TotalisticCode
        
        Estende o método construtor de CellularAutomata.
        
        Também é instanciado o tipo do autômato: Totalístico
        '''
        super().__init__(rule, k, seed)
        self.type = 'Totalistic'
          
    def getNext (self, b1, b2, b3):
        """Retorna dictRule[b1+b2+b3]
        
        Sobrescreve CellularAutomata.getNext(b1, b2, b3).
        
        Define o estado de uma célula a partir do de três vizinhas, armazenados em b1, b2 e b3. Retorna o valor
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
        return self.dictRule[b1 + b2 + b3]
