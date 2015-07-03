# -*- coding: utf-8 -*-
'''
Created on 03/03/2015

@author: matsu

Neste módulo estão classes que manipulam os arquivos de saída das classes AutomataText e AutomataImage. Essas classes
transcrevem arquivos e imagens para arquivos compostos de sequências de npumeros binários ou decimais, para que 
possam ser avaliados por um software que teste sua pseudo-aleatoriedade.
    - ImgtoText pega uma imagem de um autômato celular totalístico ou elementar e a transforma em um arquivo de 
                texto. 
    - ParserNist
    - ParserSieve
    - ParserCortaLinhas
'''
from __future__ import unicode_literals

from PIL import Image

class ImgtoText():
    '''
    Classe que pega uma imagem de um Autômato Celular e a transfere para um arquivo de texto. Utilizando o 
    dicionário de cores do AutomataImage, transfere para um arquivo de texto o estado de cada célula, representado
    como uma cor na imagem.  
    '''


    def __init__(self, caK, caImageName):
        '''
        Construtor da classe ImgtoText
        
        Instancia a quantidade de estados que o autômato que originou a imagem tem (caK - int) e o nome da imagem que
        se deseja transcrever para arquivo: 
        
        -caK (int) : número k>=2 de estados possíveis para as células do autômato que gerou a imagem
        -caImageName (str) : string que descreve o nome da imagem, com o tipo. Ex: '45k3.png'. Não há a necessidade de 
                            dar-se a localização da imagem desejada.
                            
        Utilizando-se estes parâmetros, o construtor instancia:
        -type (str) : a partir do caK, o autômato tem seu tipo detectado e classificado em Elementar o Totalistico
        -size (int) : tamanho da imagem que deve ser manipulada
        -dictTxt (dict) : dicionário que relaciona as cores que cada pixel da imagem pode ter com os estados possíveis
                          do autômato, que deverão ser escritos no arquivo.
        -filename (str) : nome do arquivo resultante. É utilizado como base o nome da imagem
        
        A seguir, o construtor chama o método imgtotxt(), que transcreve os estados das células do autômato representados 
        na imagem para o arquivo de texto.
        
        '''
        self.__caK = caK
        self.__type = self.__filename = ''
        
        self.type = self.caK
        self.__caImage = Image.open ('../Output/imgoutput/' + str(self.type) + '/' + str(caImageName), 'r')
        
        (self.size, self.size) = self.caImage.size
        self.__dictTxt = self.setDictTxt(self.caK)
        
        
        self.filename = caImageName
        
        self.imgToTxt()
    
    
    def setDictTxt (self, k):
        '''Constroi o dictColors de trás pra frente.
        
        Retorna dictTxt: Dict (int->int). Cada cor é utilizada como chave par guardar um dos k estados (0 a k-1) 
        que uma célula pode apresentar.
        '''
        dictTxt = {}
        temp = 255/(k - 1)
        aux = 0
        for i in range(0,k):
            a =  int(255 - aux)
            dictTxt[a] =  str(i)
            aux = temp + aux
        return dictTxt
    
                
    def imgToTxt(self):
        '''Método que transcreve os estados das células representados na imagem para um arquivo de texto.
        
        O método passa em cada pixel na imagem, utiliza o dictTxt para encontrar o estado numérico correspondente à cor
        e escreve este estado numérico no arquivo de texto. Cada linha da imagem corresponde a uma linha do arquivo.
        '''
        
        with open('../Output/txtoutput/fromimg/' + self.type + '/' + self.filename,'w') as self.file:
            self.file.truncate()
            for line in range (0, self.size): 
                for column in range (0, self.size):
                    site = self.caImage.getpixel((column, line))
                    self.file.write(self.dictTxt[site])
                if line != self.size-1:
                    self.file.write('\n')
     
        self.caImage.close()
    
    @property
    def type (self):
        return self.__type
    
    @type.setter
    def type(self, caK):
        caK = int (caK)
        if caK == 2:
            self.__type = 'Elementary'
        elif caK >= 3:
            self.__type = 'Totalistic'
        return self.__type  
    
    @property
    def filename(self):
        return self.__filename
    
    @filename.setter
    def filename(self, imgName):
        i = 0
        while (imgName[i] != '.'):
            self.__filename += imgName[i]
            i+=1    
        self.__filename+= '.txt'
    @property
    def caImage(self):
        return self.__caImage
    
    @property
    def caK(self):
        return self.__caK
    
    @property
    def dictTxt(self):
        return self.__dictTxt
    
    

class Parser():
    '''
    
    '''
    def __init__(self, oldFileName, nLinhas):
        
        self.newFile =  open ('./txtfile/tratado/' + oldFileName + 'parser.txt', 'w')
        self.newfile.truncate()
        self.oldFile =  open('./txtfile/original/' + oldFileName + '.txt', 'r')
                
                    
    def cutLines(self, nLines):
        contLine = 0
        for line in self.oldfile:
                    if (contLine >= nLines):
                        a = line.replace('\n', '')
                        self.newfile.write(a)
                    contLine+=1
        
    def carreiraDeBits(self, separador):   
        tempStr = '' 
        newStr = ''
        for oldLine in self.oldfile:
            newLine = oldLine.replace('\n', "")
            tempStr += newLine
        for oldBit in tempStr:
            newBit = (oldBit + separador)
            newStr += newBit 
        self.newfile.write(newStr)
                
    def close(self):
        '''Fecha ambos os arquivos de textos utilizados'''
        
        self.oldFile.close()
        self.newFile.close()
        

       
