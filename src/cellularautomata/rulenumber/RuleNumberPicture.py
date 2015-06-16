# -*- coding: utf-8 -*-

"""
Created on 16/10/2014

@author: Nicoli Araújo
@author: Elloá B. Guedes
"""

from __future__ import unicode_literals

from cellularautomata.AutomataPicture import AutomataPicture
from cellularautomata.rulenumber.RuleNumber import RuleNumber


class RuleNumberPicture(AutomataPicture):
   
    """Subclasse de AutomataPicture responsável por criar a imagem de um automato celular  do tipo Elementar."""
    
    def __init__(self, height, width, rule):
        """Construtor da classe. Aqui, há a instância de um autômato celular do tipo Elementar.
        
        Estende AutomataPicture.__init(height, width, rule, k, firstK).
        
        Como é um autômato celular simples, o número de estados é sempre 2, e o primeiro pixel é sempre preto.
        
        heihgt, width, rule: int
        """
        AutomataPicture.__init__(self, height, width, rule, k = 2, firstK = 1)
        self.automata = RuleNumber(rule)
        

    def save(self,path,fileType): 
        """Salva a imagem no local path, com tipo filetype. 
        
        Sobrescreve AutomataPicture.save(path, fileType).
        
        Método que salva a imagem criada no caminho path, com o formato fileType. No nome do arquivo de imagem 
        salvo consta o nome do autômato.
        
        path(string) - caminho, que deve incluir a pasta
        fileType (string) - formato desejado para a imagem
        """
        self.image.save(path + '/RN/' + str(self.automata.getName()) + fileType)