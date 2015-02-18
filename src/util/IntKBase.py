# -*- coding: utf-8 -*-
"""
Created on 28/11/2014

@author: Nicoli Araújo
"""

class IntKBase: 
    """Classe que abriga o método publicado por Mark Borgerding no dia 15/02/2010 no site StackOverflow.
    
    Atributos da classe:
        
        num         (int)  - número que que deve ser transformado
        b           (int)  - base na qual num deve ser escrito
        numInBase (string) - num escrito na base b
    """
    def __init__(self, num, b):
        self.num = num
        self.b = b
        self.numInBase = self.intKbase(self.num, self.b)
        
    def intKbase(self, x,b):
        """Retorna x na base b.
        
        Método que transforma x em um número na base b, e o retorna.
        
        b deve ser estar entre 2 e 32, ou seja, 2 < = b < = 32.
        b também pode ser 64, mas somente 64.
        
        >>> IntKBase(1200, 60).numInBase
        'UA'
        
        >>> IntKBase(12, 34).numInBase
        'c'
        
        >>> IntKBase(12, 2).numInBase
        '1100'
        
        >>> IntKBase(12, 8).numInBase
        '14' 
        
        retorna rets
        """
        alphabet='0123456789abcdefghijklmnopqrstuvwxyz'
        
        if b<2 or b>len(alphabet):
            if b<=64: 
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
            else:
                raise AssertionError("int2base base out of range")
        if isinstance(x,complex): 
            return ( self.intKbase(x.real,b,alphabet) , self.intKbase(x.imag,b,alphabet) )
        if x<=0:
            if x==0:
                return alphabet[0]
            else:
                return  '-' + self.intKbase(-x,b,alphabet)
        
        rets=''
        while x>0:
            x,idx = divmod(x,b)
            rets = alphabet[idx] + rets
            
        return rets
    
