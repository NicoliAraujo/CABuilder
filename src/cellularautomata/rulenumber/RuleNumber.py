# -*- coding: utf-8 -*-

"""
Created on 16/10/2014

@author: nicoli
@author: elloa
"""

from __future__ import unicode_literals

from trunk.src.cellularautomata.CellularAutomata import CellularAutomata


class RuleNumber(CellularAutomata):
    """
    Classe de Autômatos celulares do tipo elementar, cujas células podem 
    apresentar apenas dois estados, levando em consideração os estados 
    das tres celulas vizinhas presentes na iteração imediatamente anterior.

    """

    def __init__(self, rule, k=2):
        """(int)
        Construtor da classe RuleNumber. Aqui, é implementado o conceito de apenas dois estados, 
        dando-se a k o valor 2.  
        """
        CellularAutomata.__init__(self, rule, k)

    def getNext (self, b1, b2, b3):
        """(int, int, int) -> int
        Método que recebe o estado de tres vizinhas, transforma-os em uma chave e retorna o valor
        ao qual esta associada. 
        
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
