# -*- coding: utf-8 -*-

"""
Created on 16/10/2014

@author: matsu
@author: elloa
"""

from __future__ import unicode_literals

from trunk.src.cellularautomata.AutomataPicture import AutomataPicture
from trunk.src.cellularautomata.totalisticcode.TotalisticCode import TotalisticCode


class TotalisticCodePicture(AutomataPicture):
    """Classe responsável por criar uma imagem que represente autômatos celulares do tipo Totalístico."""
   
    def __init__(self, height, width, rule, k, firstK):
        """(int, int, int, int, int)
        Construtor da classe. Aqui, há a instância de um autômato celular do tipo Totalístico.
        """
        AutomataPicture.__init__(self, height, width, rule, k, firstK)
        self.automata = TotalisticCode(rule, k)

    
    def save(self,path,fileType): 
        """(string, string)
        Salva a imagem no local path, com tipo filetype. O automato é salvo com o nome, a base em que
        é gerado e a cor do seu primeiro pixel.
        
        path(string) - caminho, que deve incluir a pasta
        fileType (string) - formato desejado para a imagem
        """
        
        self.image.save(path + '/TA/' + str(self.automata.getName()) +"k" + str(self.automata.getK()) + 'fp' + str(self.firstK) + fileType)
        
