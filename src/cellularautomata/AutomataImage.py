# -*- coding: utf-8 -*-

"""
Created on 04/01/2015

@author: Nicoli Araújo
@author: Elloá B. Guedes
"""

from __future__ import unicode_literals

from PIL import Image
from cellularautomata.CellularAutomata import CellularAutomata, RuleNumber, TotalisticCode

class AutomataImage():
    """SuperClasse que tem por objetivo gerar uma imagem que represente um autômato celular.

    Aqui, os estados são representados por cores que vão de branco a preto. Cada estado é uma cor.
    As linhas da imagem constituem unidades de tempo.
    """

    def __init__(self, height, width, rule, k, firstK):
        """ Instancia height, width, rule, k, firstk: int; dictRule, image e automata.
        
        Construtor da classe. Recebe a altura, largura, numero de cores, regra e cor da 
        primeira celula do automato, cria uma imagem em tons de cinza, de tamanho (height x width) 
        de pixels brancos. Constroi o dicionario de cores e põe o primeiro pixel na imagem.
        
        height (int) - Altura da imagem, em pixels. Representa a quantidade de iterações desejadas para o autômato 
        celular, ou seja, é a passagem de tempo.
        
        width (int) - Largura da imagem, em pixels.
        
        firstK (int) - Estado que representa a cor que a primeira celula a ser pintada deve ter. Varia de 0 a k-1.
        
        dictColor: dict (int -> int) - Dicionário que alia cada um dos k estados do autômato a uma cor de 0 a 255. As chaves são 
        números de 0 a k, eos valores guardados por elas são as cores.
        
        image (Image) - Imagem que representa o autômato celular. Tem dimensões (height x width), e pixels em tons de cinza. 
        """
        self.height = height
        self.width = width
        self.firstK = firstK
        
        self.image = Image.new("L", (self.width, self.height), "white")
       
        self.automata = CellularAutomata(CellularAutomata)
        self.dictColor = self.buildDictColor(self.automata.getK())
        self.putFirstPixel(self.firstK)
        
    def putFirstPixel(self, firstK):
        """Método que põe o primeiro pixel na imagem. 
        firstK(int) - número do estado desejado, ou seja, chave da cor desejada no dictColor. 
        """
        self.image.putpixel( (int(self.height/2), 0) , self.dictColor[firstK])
    
    def SearchSite(self, color):
        """Retorna o estado (k) referente a cor informada no dictColor
        
        color (int) - uma cor de 0 a 255
        Retorna i (int) se dictColor[i] = color
        
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
        """Retorna um dicionario de k cores, que relaciona cada cor a um valor que varia de 0 a k-1
        
        k(int) - número de estados do autômato. 
        
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
    
    def putPixel(self, k, x, y): 
        """ Põe nas coordenadas informadas a cor dictColor[k].
        
        Dado um estado de 0 a k-1, transforma-o na cor correspondenten no dictColor e coloca na imagem
        na posição (y,x)
        """
        nSite = self.dictColor[int(k)] 
        self.image.putpixel( (y, x) , nSite)

    def tryGetSite(self, x, y):
        """Retorna o estado correspondente à cor nas coordenadas (x, y) da imagem do autômato celular.
        
        O método captura a cor de um pixel na posição (x, y) e retorna seu estado (k) de acordo com 
        o dictColor. Se não houver pixel em (x,y), retorna o estado 0.
        
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
        """Retorna o estado (ou seja, um número de 0 a k-1) de uma célula na posicao (x,y).
        
        Dada as coordenadas (x,y) da imagem do auntômato celular, são salvos os estados das células nas posições
        (x-1, y-1), (x, y-1) e (x+1, y-1). Estes estados são passados ao automata, que retorna o estado resultante
        da célula na posição (x,y).
                
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
        """Gera a imagem que representa o autômato celular.
        
        Edita a imagem criada na iniciação de acordo com o autômato. Começando em t = 2 (ou na segunda linha),
        são atualizados os estados de todas as células do autômato. 
        """
        for line in range (1, self.width):
            for column in range (0, self.height):
                newSite = self.getSite(column, line)     
                self.putPixel(newSite, line, column)
        return self.image    
                 
    def save(self,path,fileType):
        """Salva a imagem criada em path, com a extensão fileType.
        
        Método que salva a imagem criada no caminho path, com o formato fileType. No nome do arquivo de imagem 
        salvo consta o nome do autômato.
        
        path(string) - caminho, que deve incluir a pasta
        fileType (string) - formato desejado para a imagem
        """
        self.image.save(path + str(self.automata.getName()) + fileType) 
        
    
class RuleNumberPicture(AutomataImage):
    
   
    """Subclasse de AuAutomataPictureesponsável por criar a imagem de um automato celular  do tipo Elementar."""
    
    def __init__(self, height, width, rule):
        """Construtor da classe. Aqui, há a instância de um autômato celular do tipo Elementar.
        
        Estende AutomaAutomataPicturet(height, width, rule, k, firstK).
        
        Como é um autômato celular simples, o número de estados é sempre 2, e o primeiro pixel é sempre preto.
        
        heihgt, width, rule: int
        """
        AutomataImage(height, width, rule, k = 2, firstK = 1)
        self.automata = RuleNumber(rule)
        

    def save(self,path,fileType): 
        """Salva a imagem no local path, com tipo filetype. 
        
        Sobrescreve AutomataPicAutomataPicture fileType).
        
        Método que salva a imagem criada no caminho path, com o formato fileType. No nome do arquivo de imagem 
        salvo consta o nome do autômato.
        
        path(string) - caminho, que deve incluir a pasta
        fileType (string) - formato desejado para a imagem
        """
        self.image.save(path + '/RN/' + str(self.automata.getName()) + fileType)
    
class TotalisticCodePicture(AutomataImage):
    """Subclasse de AuAutomataPictureesponsável por criar uma imagem que represente autômatos celulares Totalísticos."""
   
    def __init__(self, height, width, rule, k, firstK):
        """Construtor da classe. Aqui, há a instância de um autômato celular do tipo Totalístico.
        
        Estende AutomataPAutomataPictureeight, width, rule, k, firstK)
        
        height, width, rule, k, firstk: int
        """
        AutomataImage(height, width, rule, k, firstK)
        self.automata = TotalisticCode(rule, k)

    
    def save(self,path,fileType): 
        """Salva a imagem no local path, com tipo filetype. 
        
        Sobrescreve AutomataPAutomataPictureh, fileType).
        
        O automato é salvo com o nome, a base em que é gerado e a cor do seu primeiro pixel.
        
        path(string) - caminho, que deve incluir a pasta
        fileType (string) - formato desejado para a imagem
        """
        self.image.save(path + '/TA/' + str(self.automata.getName()) +"k" + str(self.automata.getK()) + 'fp' + str(self.firstK) + fileType)
        

