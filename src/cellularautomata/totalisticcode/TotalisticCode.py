# -*- coding: utf-8 -*-

"""
Created on 24/10/2014

@author: nicoli
"""

from __future__ import unicode_literals

from trunk.src.cellularautomata.CellularAutomata import CellularAutomata


class TotalisticCode(CellularAutomata):
    """
    Classe que define os autômatos do tipo totalistico, que podem ter mais de dois estados possíveis para
    cada célula. Além disso, para definir o estado de uma célula, é feita a média entre as três células vizinhas 
    da iteração imediatamente anterior.
    """
          
    def getNext (self, b1, b2, b3):
        """(int, int, int) -> int
        Método que define o estado de uma célula a partir do estado de três vizinhas. Retorna o valor
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
    