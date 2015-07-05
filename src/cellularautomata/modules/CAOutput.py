# -*- coding: utf-8 -*-

"""
Criado on 04/01/2015

@author: Nicoli Araújo
@author: Elloá B. Guedes

Módulo que abriga as classes que salvam os estados de um autômato celular em uma imagem de extensão .png composta de pixels com tons que vão do preto ao branco ou um arquivo de texto composto de números inteiros.
    - AutomataImage gera imagem.
    - AutomataText gera um arquivo texto.
"""

from __future__ import unicode_literals

from PIL import Image
from numpy import zeros


class AutomataImage(object):
    """Classe que tem por objetivo gerar uma imagem que represente um autômato celular.

    Aqui, os estados são representados por cores que vão do branco ao preto. Cada estado é uma cor. Cada coluna representa uma célula, que muda de estado em cada linha. Assim, as linhas representam um único vetor unidimensional, que tem seu estado mudado conforme o tempo passa.
    """

    def __init__(self, side, ca, info):
        """Construtor da classe AutomataImage 
        
        Instancia o lado da imagem a ser gerada(side) e o autômato celular a que ela pertence (ca):
        
        - side (int) : Altura da imagem, em pixels: representa a quantidade de iterações desejadas para o autômato celular, ou seja, é a passagem de tempo; Largura da imagem, em pixels.
        - ca (CellularAutomata) : Autômato celular cuja regra e semente serão utilizadas para colorir a imagem.
        - info (str) : A imagem é salva na pasta /imgoutput/, subpasta do seu tipo, com o nome igual a sua regra. Caso deseje-se acrescentar outra informação, deve-se declará-la como uma string na variável info. 
        
        A partir desses parâmetros, o construtor instancia:
        
        - image (Image) : cria uma imagem em tons de cinza, de tamanho (side x side) de pixels brancos. 
        - dictColor: dict (int -> int) : Dicionário que alia cada um dos k estados do autômato a uma cor de 0 a 255. As chaves são números de 0 a k-1, e os valores guardados por elas são as cores que representam cada estado.
        
        Então, o método setImage() edita a imagem conforme a evolução do ca, e o método save() a salva no formato .png, na pasta padrão (/Output/imgoutput/).
        """
        self.side = side

        self.__image = Image.new("L", (self.side, self.side), "white")

        self.__ca = ca
        self.__name = str(info) + str(self.ca.rule)  + '.png'        self.__dictColor = self.setDictColor(self.ca.k)
        
        self.setImage(self.ca.seed)
        self.save()

    
    def setFirstPixel(self, seed):
        '''Define a cor do primeiro pixel a ser colocado na imagem a partir do estado inical do ca.
        
        - seed (int): Um número de 0 a k-1 que representa o estado inicial do autômato celular. 
        '''
        self.firstPixel = self.dictColor[seed]
        
        
    def putFirstPixel(self, seed):
        """Método que põe o primeiro pixel na imagem. 
        
        - firstPixel(int) : Número do estado desejado, ou seja, chave da cor desejada no dictColor. 
        """
        
        self.setFirstPixel(seed)
        self.image.putpixel( (int(self.side/2), 0) , self.firstPixel)
    
    def searchSite(self, color):
        """Retorna o estado (state) que guarda a cor desejada no dictColor
        
        - color (int) : Uma cor de 0 a 255
        
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
        
        - k (int) : Número de estados do autômato. 
        
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
        
        Dado um estado de 0 a k-1, transforma-o na cor correspondenten no dictColor e coloca na imagem na posição (y,x)
        """
        nSite = self.dictColor[int(state)] 
        self.image.putpixel( (y, x) , nSite)

    def tryGetSite(self, x, y):
        """Retorna o estado correspondente à cor nas coordenadas (x, y) da imagem do autômato celular.
        
        O método captura a cor de um pixel na posição (x, y) e retorna seu estado (state) de acordo com o dictColor. Se não houver pixel em (x,y), retorna o estado 0.
        
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
        
        Dada as coordenadas (x,y) da imagem do auntômato celular, são salvos os estados das células nas posições (x-1, y-1), (x, y-1) e (x+1, y-1). Estes estados são passados ao automata, que retorna o estado resultante da célula na posição (x,y).
        
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
        
        Edita a imagem criada na iniciação de acordo com o autômato. Em t = 0 (primeira linha) põe o primeiro pixel da cor correspondente à semente dada. Começando em t = 1 (ou na segunda linha), são atualizados os estados de todas as células do autômato. 
        
        - seed (int) : estado da célula central do vetor em t = 0. Inteiro de 0 a k-1. 
        """
        self.putFirstPixel(seed)
        
        for line in range (1, self.side):
            for column in range (0, self.side):
                newState = self.getSite(column, line)     
                self.putPixel(newState, line, column)
            
         
    def save(self):
        """Salva a imagem criada no formato ".png".
        
        Método que salva a imagem criada no caminho path, com o formato ".png". No nome do arquivo de imagem salvo consta o nome do autômato.
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
    


class AutomataText(object):
    '''Classe que gera um arquivo de texto que armazena os estados de um autômato celular.

    O estado de cada célula é representado por um número inteiro de 0 a k-1, sendo k o número de estados possíveis do autômato.Cada bit representa uma célula, que muda de estado em cada linha. Assim, as linhas representam um único vetor unidimensional, que tem seu estado mudado conforme o tempo passa. Portanto, o arquivo mostrará uma matriz size x it, em que size é a largura e it é a altura.
    '''


    def __init__(self, size, it, ca, info):
        '''Construtor da classe AutomataText 
        
        Instancia o tamanho do vetor a ser gerado (size), a quantidade de iterações que ocorrerão (it) e o autômato celular que se deseja representar (ca):
        
        - size (int) : Largura do vetor
        - it (int) : Quantidade de iterações, ou seja, é a passagem de tempo
        - ca (CellularAutomata) - Autômato celular cuja regra será utilizada para alterar os estados de cada célula.
        - info (Str) : O arquivo é salvo na pasta /original/, subpasta do seu tipo, com o nome igual a sua regra. Caso deseje-se acrescentar outra informação, deve-se declará-la como uma string na variável info. 
        
        A partir desses parâmetros, o construtor instancia:
        
        - file (File) : Arquivo de texto (.txt) composto de uma matriz de dimensões size x it de bits. Cada bit tem valor de 0 a k-1.
        - firstBit (int) : Estado que a célula central do vetor deve ter no início do crescimento. Varia de 0 a k-1.
        
        Então, o método setFile altera os estados das células do vetor it vezes. Em seguida, salva os estados em file. 
        
        '''
        self.__ca = ca
        self.it = it
        self.size = size
        
        self.setFile(self.ca.seed, info)
    
    
    def __startArray(self):
        '''Cria um vetor de tamanho size x it composto de zeros.'''  
        self.__array = zeros((self.it, self.size))

        
    def __putFirstLine(self):
        '''Método que escreve a primeira linha no arquivo. É composta de zeros, com exceção do bit central, que ganha o valor de self.firstBit.'''
        mid = int (self.size/2)
        self.__array[0][mid] = int(self.firstBit)
 
        self.writeLine(self.__array, 0)
    
    
    def writeLine(self, array, line):
        '''Escreve uma linha de um array em file. Transfere os valores inteiros de cada posição, sem separador.
        
        - array (Array ou List): vetor unidimensional do mesmo tamalho de self.size
        - line (int): Linha do array que se deseja escrever no arquivo
        '''
        newLine = ''
        for j in range(0, self.size):
            newLine += str(int(array[line][j]))
        self.file.write(newLine + '\n')
    
    def tryGetBit(self, i, j):
        '''Pega o estado de uma célula na posição (i,j) do array.
        
        Retorna um inteiro de 0 a k-1 que representa o estado da célula.
        
        >>> ec = ElementaryCode(45)
        >>> ectext = AutomataText(5, 10, e, '')
        >>> ectext.array
        [[ 0.  0.  1.  0.  0.]
         [ 1.  0.  1.  0.  1.]
         [ 0.  1.  1.  1.  1.]
         [ 1.  1.  0.  0.  0.]
         [ 1.  0.  0.  1.  1.]
         [ 0.  0.  0.  1.  0.]
         [ 1.  1.  0.  1.  0.]
         [ 1.  0.  1.  1.  0.]
         [ 1.  1.  1.  0.  0.]
         [ 1.  0.  0.  0.  1.]]
        >>> ectext.tryGetBit(4, 6)
        0
        
        >>> ec = ElementaryCode(63)
        >>> ectext = AutomataText(5, 10, e, '')
        >>> ecext.array
        [[ 0.  0.  1.  0.  0.]
         [ 1.  1.  1.  1.  1.]
         [ 0.  0.  0.  0.  0.]
         [ 1.  1.  1.  1.  1.]
         [ 0.  0.  0.  0.  0.]
         [ 1.  1.  1.  1.  1.]
         [ 0.  0.  0.  0.  0.]
         [ 1.  1.  1.  1.  1.]
         [ 0.  0.  0.  0.  0.]
         [ 1.  1.  1.  1.  1.]]
        >>> ectext.tryGetBit(4, 6)
        0
        
        >>> tc = TotalisticCode(1074, 3, 1)
        >>> tctext = AutomataText(10, 10, tc, '')
        >>> tctext.array
        [[ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]
         [ 0.  0.  0.  0.  1.  1.  1.  0.  0.  0.]
         [ 0.  0.  0.  1.  2.  0.  2.  1.  0.  0.]
         [ 0.  0.  1.  0.  0.  1.  0.  0.  1.  0.]
         [ 0.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
         [ 2.  2.  0.  0.  0.  0.  0.  0.  0.  2.]
         [ 1.  1.  2.  0.  0.  0.  0.  0.  2.  2.]
         [ 1.  1.  0.  2.  0.  0.  0.  2.  1.  1.]
         [ 0.  2.  0.  2.  2.  0.  2.  0.  1.  2.]
         [ 1.  2.  1.  1.  1.  1.  2.  0.  0.  0.]]
        >>> tctext.tryGetBit(4,6)
        1
        
        '''
        try:
            return int(self.__array[i][j])
        except: 
            return 0
        
        
    
    def getBits(self, line, column):
        '''Calcula o estado de uma célula na posição (line x column). Para isso, pega o estado da vizinhança da célula na iteração anterior.
        
        Retorna o estado da célula no tempo atual. 
        
        >>> ec = ElementaryCode(45)
        >>> ectext = AutomataText(5, 10, e, '')
        >>> ectext.array
        [[ 0.  0.  1.  0.  0.]
         [ 1.  0.  1.  0.  1.]
         [ 0.  1.  1.  1.  1.]
         [ 1.  1.  0.  0.  0.]
         [ 1.  0.  0.  1.  1.]
         [ 0.  0.  0.  1.  0.]
         [ 1.  1.  0.  1.  0.]
         [ 1.  0.  1.  1.  0.]
         [ 1.  1.  1.  0.  0.]
         [ 1.  0.  0.  0.  1.]]
        >>> ectext.getBits(5, 4)
        0
        
        >>> ec = ElementaryCode(63)
        >>> ectext = AutomataText(5, 10, e, '')
        >>> ecext.array
        [[ 0.  0.  1.  0.  0.]
         [ 1.  1.  1.  1.  1.]
         [ 0.  0.  0.  0.  0.]
         [ 1.  1.  1.  1.  1.]
         [ 0.  0.  0.  0.  0.]
         [ 1.  1.  1.  1.  1.]
         [ 0.  0.  0.  0.  0.]
         [ 1.  1.  1.  1.  1.]
         [ 0.  0.  0.  0.  0.]
         [ 1.  1.  1.  1.  1.]]
        >>> ectext.getBits(5, 4)
        1
        
        >>> tc = TotalisticCode(1074, 3, 1)
        >>> tctext = AutomataText(10, 10, tc, '')
        >>> tctext.array
        [[ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]
         [ 0.  0.  0.  0.  1.  1.  1.  0.  0.  0.]
         [ 0.  0.  0.  1.  2.  0.  2.  1.  0.  0.]
         [ 0.  0.  1.  0.  0.  1.  0.  0.  1.  0.]
         [ 0.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
         [ 2.  2.  0.  0.  0.  0.  0.  0.  0.  2.]
         [ 1.  1.  2.  0.  0.  0.  0.  0.  2.  2.]
         [ 1.  1.  0.  2.  0.  0.  0.  2.  1.  1.]
         [ 0.  2.  0.  2.  2.  0.  2.  0.  1.  2.]
         [ 1.  2.  1.  1.  1.  1.  2.  0.  0.  0.]]
        >>> tctext.getBits(5, 4)
        
        '''
        b1 = int (self.tryGetBit(line-1, column-1) )
        b2 = int (self.tryGetBit(line-1, column) )
        b3 = int (self.tryGetBit(line-1, column+1) )
        
        return  self.ca.getNext(b1, b2, b3)
    
    def setFile(self, firstBit, info):
        '''Salva os estados do autômato no arquivo de texto.
        
        Edita o arquvio de texto criado na iniciação de acordo com o autômato. Em t = 0 (primeira linha) põe o primeiro bit com o valor firstBit. Começando em t = 1 (ou na segunda linha), são atualizados e salvos os estados de todas as células do autômato até que tenha sido feito o número de iterações solicitado. 
        
        - firstBit (int) : estado da célula central do vetor em t = 0. Inteiro de 0 a k-1.
        '''
        filename = str(self.ca.rule) + info + '.txt'
        self.firstBit = firstBit
        self.__startArray()
        with open ('../Output/txtoutput/original/' + self.ca.type + '/' + filename , 'w') as self.file:
        
            self.__putFirstLine()

            for i in range(1, self.it):
                for j in range(0, self.size):
                    self.__array[i][j] = self.getBits(i,j)
                    self.file.write(str(int(self.__array[i][j])))
    
                if (i!=self.it-1):
                    self.file.write('\n')

        
    @property
    def ca(self):
        return self.__ca
    
    @property
    def firstBit(self):
        return self.__firstBit
    
    @firstBit.setter
    def firstBit(self, firstBit):
        if (firstBit in range (0, self.ca.k) ):
            self.__firstBit = firstBit
        else: 
            print('FirstBit deve estar entre 0 e ' + str(self.ca.k - 1) + '!')

    @property
    def array(self):
        return self.array