# -*- coding: utf-8 -*-

"""
Created on 04/01/2015

@author: matsu
"""

from __future__ import unicode_literals

from PIL import Image

from trunk.src.cellularautomata.CellularAutomata import CellularAutomata


class AutomataPicture():
    
    """
    O objetivo desta classe é gerar uma imagem que represente um autômato celular. Aqui, os estados são
    representados por cores que vão de branco a preto. Cada estado é uma cor.
    
    Atributos de um AutomataPicture:
    height: int
        Altura da imagem, em pixels. Representa a quantidade de iterações desejadas para o autômato 
        celular, ou seja, é a passagem de tempo.
        
    width: int
        Largura da imagem, em pixels.
        
    firstK: int
        Estado que representa a cor que a primeira celula a ser pintada deve ter. Varia de 0 a k-1.
        
    dictColor: dict (int -> int)
        Dicionário que alia cada um dos k estados do autômato a uma cor de 0 a 255. As chaves são 
        números de 0 a k, eos valores guardados por elas são as cores.
        
    image: Image
        Imagem que representa o autômato celular. Tem dimensões (height x width), e pixels em tons de cinza. 
    """


    def __init__(self, height, width, rule, k, firstK):
        """ (int, int, int, int, int)
        Construtor da classe. Recebe a altura, largura, numero de cores, regra e cor da 
        primeira celula do automato, cria uma imagem em tons de cinza, de tamanho (height x width) 
        de pixels brancos. Constroi o dicionario de cores e põe o primeiro pixel na imagem.
        """
        
        self.height = height
        self.width = width
        self.firstK = firstK
        
        self.image = Image.new("L", (self.width, self.height), "white")
       
        self.automata = CellularAutomata(rule, k)
        
        self.dictColor = self.buildDictColor(self.automata.getK())
        self.putFirstPixel(self.firstK)
        
    def putFirstPixel(self, firstK):
        """(int) -> none
        Método que põe o primeiro pixel na imagem. 
    
        Entrada: firstK - número do estado desejado, ou seja, chave da cor desejada no dictColor. 
        """
   
        self.image.putpixel( (int(self.height/2), 0) , self.dictColor[firstK])
    
    
    def SearchSite(self, color):
        """ (dict,int) -> int
        Retorna o estado (k) referente a cor informada no dictColor
        
        >>> AutomataPicture.dictColor
        {0: 255, 1: 0}
        
        >>> AutomataPicture.SearchSite(255)
        0
        
        >>> AutomataPicture.SearchSite(0)
        1
        """
      
        for i in (self.dictColor):
            if(self.dictColor[i] == color): 
               
                return i
            
    def buildDictColor(self, k):
        
        """ (int) -> dict
        Retorna um dicionario de k cores, que relaciona cada cor a um valor que varia de 0 a k-1 
        
        >>> AutomataPicture.buildDictColor(2)
        {0: 255, 1: 0}
        
        >>> AutomataPicture.buildDictColor(3)
        {0: 255, 1: 127, 2: 0}
        
        >>> AutomataPicture.buildDictColor(4)
        {0: 255, 1: 170, 2: 85, 3: 0}
        
        >>> AutomataPicture.buildDictColor(5)
        {0: 255, 1: 191, 2: 127, 3: 63, 4: 0}
        """

        dictColor = {}
        temp = 255/(k - 1)
        aux = 0
        
        for i in range (0, k):
            dictColor[i] = int(255 - aux)
            aux = temp + aux
        return dictColor
    
    def putPixel(self, value, x, y): 
        """ (int, int, int)
        Pega um valor, transforma em na cor correspondenten no dictColor e coloca na imagem
        na posição (y,x)
        """
        
        nSite = self.dictColor[int(value)] 
       
        self.image.putpixel( (y, x) , nSite)

    def tryGetSite(self, x, y):
        """ (int, int) -> int
        O método captura a cor de um pixel na posição (x, y) e retorna seu estado (k) de acordo com 
        o dictColor.
        
        >>> AutomataPicture = AutomataPicture(3, 3, 210, 3, 1)
        
        >>> AutomataPicture.dictColor
        {0: 255, 1: 127, 2: 0}
        
        >>> AutomataPicture.tryGetSite(3, 2)
        0
        
        >>> AutomataPicture.tryGetSite(2, 2)
        2
        
        >>> AutomataPicture.tryGetSite(2, 1)
        1
        """
        try:
            pixel = self.image.getpixel((x, y))
         
            chave = self.SearchSite(pixel)
            
            return chave
        
        except:
            return 0
    
    
    def getSite(self, x, y):
        """(int, int) -> string
        Retorna o estado (k) de uma célula na posicao (x,y).
        
        >>> AutomataPicture = AutomataPicture(3, 3, 210, 3, 1)
        
        >>> AutomataPicture.dictColor
        {0: 255, 1: 127, 2: 0}
        
        >>> AutomataPicture.getSite(2, 1)
        1
        
        >>> AutomataPicture.getSite(3, 2)
        1
        
        >>> AutomataPicture.getSite(2, 2)
        2
        """ 
        b1 = self.tryGetSite(x-1, y-1)
        b2 = self.tryGetSite(x, y-1)
        b3 = self.tryGetSite(x+1, y-1)

        newSite = int (self.automata.getNext(b1,b2,b3) )
        return newSite
    
    def setImage(self):
        """() -> Image
        Edita a imagem de acordo com o autômato. Começando em t = 2 (ou na segunda linha),
        são atualizados os estados de todas as células do autômato. 
        """
        
        for line in range (1, self.width):
            
            for column in range (0, self.height):
                
                newSite = self.getSite(column, line)
                            
                self.putPixel(newSite, line, column)

        return self.image    
                 

    
    def save(self):
        pass
