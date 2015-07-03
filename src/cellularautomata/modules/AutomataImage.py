# -*- coding: utf-8 -*-

"""
Created on 04/01/2015

@author: Nicoli Araújo
@author: Elloá B. Guedes
"""

from __future__ import unicode_literals

from PIL import Image



class AutomataImage(object):
    """Classe que tem por objetivo gerar uma imagem que represente um autômato celular.

    Aqui, os estados são representados por cores que vão do branco ao preto. Cada estado é uma cor.
    Cada coluna representa uma célula, que muda de estado em cada linha. Assim, as linhas representam
    um único vetor unidimensional, que tem seu estado mudado conforme o tempo passa.
    """

    def __init__(self, side, ca, name, filetype):
        """Construtor da classe AutomataImage 
        
        Instancia o lado da imagem a ser gerada(side) e o autômato celular a que ela pertence (ca):
        
        - side (int) - Altura da imagem, em pixels: representa a quantidade de iterações desejadas para o autômato 
        celular, ou seja, é a passagem de tempo; Largura da imagem, em pixels.
        - ca (CellularAutomata) - Autômato celular cuja regra e semente serão utilizadas para colorir a imagem.
        - name (Str) - A imagem é salva na pasta /imgoutput/, subpasta do seu tipo, com o nome igual a sua regra. Caso
                       deseje-se acrescentar outra informação, deve-se declará-la como uma string na variável nome. 
        
        A partir desses parâmetros, o construtor instancia:
        
        - image (Image) - cria uma imagem em tons de cinza, de tamanho (side x side) de pixels brancos. 
        - dictColor: dict (int -> int) - Dicionário que alia cada um dos k estados do autômato a uma cor de 0 a 255. 
                     As chaves são números de 0 a k-1, e os valores guardados por elas são as cores que representam 
                     cada estado.
        
        Então, o método setImage() edita a imagem conforme a evolução do ca, e o método save() a salva no formato informado, 
        na pasta padrão.
        """
        self.side = side

        self.__image = Image.new("L", (self.side, self.side), "white")

        self.__ca = ca
        self.__name = str(name) + str(self.ca.rule)  + str(filetype)        self.__dictColor = self.setDictColor(self.ca.k)
        
        self.setImage(self.ca.seed)
        self.save()

    
    def setFirstPixel(self, seed):
        '''Define a cor do primeiro pixel a ser colocado na imagem a partir do estado inical do ca.
        
        seed (int) um número de 0 a k-1 que representa o estado inicial do autômato celular. 
        '''
        self.firstPixel = self.dictColor[seed]
        
        
    def putFirstPixel(self, seed):
        """Método que põe o primeiro pixel na imagem. 
        
        firstPixel(int) - número do estado desejado, ou seja, chave da cor desejada no dictColor. 
        """
        
        self.setFirstPixel(seed)
        self.image.putpixel( (int(self.side/2), 0) , self.firstPixel)
    
    def searchSite(self, color):
        """Retorna o estado (state) que guarda a cor desejada no dictColor
        
        color (int) - uma cor de 0 a 255
        Retorna state (int) se dictColor[state] = color
        
        >>> AutomataImage.dictColor
        {0: 255, 1: 0}

        >>> AutomataImage.searchSite(255)
        0
        
        >>> AutomataImage.searchSite(0)
        1
        """
        for state in (self.dictColor):
            if(self.dictColor[state] == color): 
                return state
            
    def setDictColor(self, k):
        """Retorna um dicionario de k cores, que relaciona cada cor a um valor que varia de 0 a k-1
        
        k(int) - número de estados do autômato. 
        
        >>> AutomataImage.setDictColor(2)
        {0: 255, 1: 0}
        
        >>> AutomataImage.setDictColor(3)
        {0: 255, 1: 127, 2: 0}
        
        >>> AutomataImage.setDictColor(4)
        {0: 255, 1: 170, 2: 85, 3: 0}
        
        >>> AutomataImage.setDictColor(5)
        {0: 255, 1: 191, 2: 127, 3: 63, 4: 0}
        """
        
        dictColor = {}
        temp = 255/(k - 1)
        aux = 0
        for i in range (0, k):
            dictColor[i] = int(255 - aux)
            aux = temp + aux
        return dictColor
    
    def putPixel(self, state, x, y): 
        """ Põe nas coordenadas informadas a cor correspondente a state no dictColor.
        
        Dado um estado de 0 a k-1, transforma-o na cor correspondenten no dictColor e coloca na imagem
        na posição (y,x)
        """
        nSite = self.dictColor[int(state)] 
        self.image.putpixel( (y, x) , nSite)

    def tryGetSite(self, x, y):
        """Retorna o estado correspondente à cor nas coordenadas (x, y) da imagem do autômato celular.
        
        O método captura a cor de um pixel na posição (x, y) e retorna seu estado (state) de acordo com 
        o dictColor. Se não houver pixel em (x,y), retorna o estado 0.
        
        >>> AutomataPicture = AutomataPicture(3, 3, 210, 3, 1)
        
        >>> AutomataImage.dictColor
        {0: 255, 1: 127, 2: 0}
        
        >>> AutomataImage.tryGetSite(3, 2)
        0
        
        >>> AutomataImage.tryGetSite(2, 2)
        2
        
        >>> AutomataImage.tryGetSite(2, 1)
        1
        """
        try:
            color = self.image.getpixel((x, y))
            state = self.searchSite(color)
            return state
        except:
            return 0
    
    
    def getSite(self, x, y):
        """Retorna o novo estado (ou seja, um número de 0 a k-1) de uma célula na posicao (x,y).
        
        Dada as coordenadas (x,y) da imagem do auntômato celular, são salvos os estados das células nas posições
        (x-1, y-1), (x, y-1) e (x+1, y-1). Estes estados são passados ao automata, que retorna o estado resultante
        da célula na posição (x,y).
        
        >>> tc = TotalisticCode(210, 3, 1)    
        >>> AutomataImage = AutomataImage(3, tc, '.png')
        
        >>> AutomataImage.dictColor
        {0: 255, 1: 127, 2: 0}
        
        >>> AutomataImage.getSite(2, 1)
        1
        
        >>> AutomataImage.getSite(3, 2)
        1
        
        >>> AutomataImage.getSite(2, 2)
        2
        """ 
        b1 = self.tryGetSite(x-1, y-1)
        b2 = self.tryGetSite(x, y-1)
        b3 = self.tryGetSite(x+1, y-1)

        newState = int (self.ca.getNext(b1,b2,b3) )
        return newState
    

    
    def setImage(self, seed):
        """Gera a imagem que representa o autômato celular.
        
        Edita a imagem criada na iniciação de acordo com o autômato. Em t = 0 (primeira linha) põe o primeiro pixel da 
        cor correspondente à semente dada. Começando em t = 1 (ou na segunda linha), são atualizados os estados de todas 
        as células do autômato. 
        
        seed (int) - estado da célula central do vetor em t = 0. Inteiro de 0 a k-1. 
        """
        self.putFirstPixel(seed)
        
        for line in range (1, self.side):
            for column in range (0, self.side):
                newState = self.getSite(column, line)     
                self.putPixel(newState, line, column)
            
         
    def save(self):
        """Salva a imagem criada em, com a extensão fileType.
        
        Método que salva a imagem criada no caminho path, com o formato fileType. No nome do arquivo de imagem 
        salvo consta o nome do autômato.
        
        fileType (string) - formato desejado para a imagem: .png; .jpg; .jpeg, 
        """
        self.image.save('../Output/imgoutput/' + str(self.ca.type) + '/' + self.name) 
        self.image.close()
    
    @property
    def ca(self):
        return self.__ca
    
    
    @property
    def dictColor(self):
        return self.__dictColor

    @property
    def image(self):
        return self.__image
    
    @property
    def name(self):
        return self.__name