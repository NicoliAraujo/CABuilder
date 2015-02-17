# -*- coding: utf-8 -*-

"""
Created on 16/10/2014

@author: matsu
@author: elloa
"""

from __future__ import unicode_literals

from trunk.src.cellularautomata.AutomataPicture import AutomataPicture
from trunk.src.cellularautomata.rulenumber.RuleNumber import RuleNumber


class RuleNumberPicture(AutomataPicture):
   
    """Classe responsável por criar a imagem de um automato celular  do tipo Elementar."""
    
    def __init__(self, height, width, rule):
        
        """(int, int, int, int)
        Construtor da classe. Como é um autômato celular simples, o número de estados é sempre 2, 
        e o primeiro pixel é sempre preto.
        """

        AutomataPicture.__init__(self, height, width, rule, k = 2, firstK = 1)
        self.automata = RuleNumber(rule)
        

    def save(self,path,fileType): 
        """(string, string)
        Método que salva a imagem criada no caminho path, com o formato fileType. No nome do arquivo de imagem 
        salvo, consta o nome do autômato.
        
        path(string) - caminho, que deve incluir a pasta
        fileType (string) - formato desejado para a imagem
        """
         
        self.image.save(path + '/RN/' + str(self.automata.getName()) + fileType)