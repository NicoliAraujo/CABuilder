# -*- coding: utf-8 -*-

"""
Created on 16/10/2014

@author: Nicoli Araújo
@author: Elloá B. Guedes
"""

from __future__ import unicode_literals

from src.cellularautomata.CellularAutomata import CellularAutomata


class RuleNumber(CellularAutomata):
    """Subclasse de CellularAutomata. Define autômatos celulares do tipo elementar. 
    
    Em um RuleNumber, as células podem apresentar apenas dois estados, levando em consideração os estados 
    das três células vizinhas presentes na iteração imediatamente anterior.
    """

    def __init__(self, rule):
        """Construtor da classe RuleNumber. 
        
        Estende CellularAutomata.__init(rule, k).
        
        Aqui, são instanciados rule e k. É implementado o conceito de apenas dois estados, dando-se
        a k fixamente o valor 2. Assim, não é necessário declarar k. 
        """
        CellularAutomata.__init__(self, rule, k = 2)

    def getNext (self, b1, b2, b3):
        """Retorna dictRule[b1b2b3], sendo b1b2b3 os três parâmetros concatenados.
         
        Sobrescreve CellularAutomata.getNext(b1, b2, b3).
        
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
