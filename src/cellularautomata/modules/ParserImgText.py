# -*- coding: utf-8 -*-
'''
Created on 03/03/2015

@author: Nicoli Araújo

Neste módulo estão classes que manipulam os arquivos de saída das classes AutomataText e AutomataImage. Essas classes transcrevem arquivos e imagens para arquivos compostos de sequências de npumeros binários ou decimais, para que possam ser avaliados por um software que teste sua pseudo-aleatoriedade.
    - ImgtoText pega uma imagem de um autômato celular totalístico ou elementar e a transforma em um arquivo de texto. 
    - Parser edita a forma como os números estão dispostos em um arquivo de texto. 
'''
from __future__ import unicode_literals

from PIL import Image


class ImgtoText():
    '''
    Classe que pega uma imagem de um Autômato Celular e a transfere para um arquivo de texto. Utilizando o dicionário de cores do AutomataImage, transfere para um arquivo de texto o estado de cada célula, representado como uma cor na imagem.
    
    
    Atenção: imagens com formatos que sofrem perda com a compressão não poderão ser utilizadas nesta classe.
    '''


    def __init__(self, caK, caImageName, info):
        '''
        Construtor da classe ImgtoText
        
        Instancia a quantidade de estados que o autômato que originou a imagem tem (caK - int) e o nome da imagem que se deseja transcrever para arquivo: 
        
        - caK (int) : número k>=2 de estados possíveis para as células do autômato que gerou a imagem
        - caImageName (str) : string que descreve o nome da imagem, com o tipo. Ex: '45k3.png'. Não há a necessidade de dar-se a localização da imagem desejada.
        - info (str) :
                          
        Utilizando-se estes parâmetros, o construtor instancia:
        - type (str) : a partir do caK, o autômato tem seu tipo detectado e classificado em Elementar o Totalistico
        - size (int) : tamanho da imagem que deve ser manipulada
        - dictTxt (dict) : dicionário que relaciona as cores que cada pixel da imagem pode ter com os estados possíveis do autômato, que deverão ser escritos no arquivo.
        - filename (str) : nome do arquivo resultante. É utilizado como base o nome da imagem
        
        A seguir, o construtor chama o método imgtotxt(), que transcreve os estados das células do autômato representados na imagem para o arquivo de texto.
        
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
        
        Retorna dictTxt: Dict (int->int). Cada cor é utilizada como chave par guardar um dos k estados (0 a k-1) que uma célula pode apresentar.
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
        
        O método passa em cada pixel na imagem, utiliza o dictTxt para encontrar o estado numérico correspondente à cor e escreve este estado numérico no arquivo de texto. Cada linha da imagem corresponde a uma linha do arquivo.
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
    '''Classe que altera a disposição dos dados de um arquivo de texto composto apenas de números inteiros, e armazena essas alterações em um novo arquivo. '''
    def __init__(self, oldFilePath, info):
        '''Construtor da classe Parser
        
        Parâmetros de inicializão:
            - oldFilePath (str) :indica o nome e a localização do arquivo que se deseja alterar desde as subpastas de /txtoutput/
            - info (str) : informação que deve ser adicionada ao nome do novo arquivo a ser gerado 
        A partir destew parâmetros, o construtor instancia:
            - newFilePath (str) : localização e nome do novo arquivo. É instanciado utilizando o método setPath(). Arquivos criados nesta classe ficam localizados na pasta /treated/
            - strData (str) : string que armazena o conteúdo a ser modificado e escrito no novo arquivo
        
        '''
        self.newFilePath = self.setPath(oldFilePath, info)
                
        with open('../Output/txtoutput/' + oldFilePath, 'r+') as oldFile:
            self.strData = oldFile.read()
        
    
    def binary(self):
        '''Transforma todos os bits que estão no arquivo em binário.'''
        strBin = ''
        for i in self.strData:
            try:
                strBin += bin(int(i))[2:]
            except: 
                strBin+=i
        self.strData = strBin

    
    def removeSeparator(self, strDeleted):
        '''Retiram um caractere ou uma string (separator) do conteúdo do arquivo.
        
        - strDeleted (string): String que será retirada do arquivo'''
        self.strData = self.strData.replace(strDeleted, '')
    
        
    def setBitsSeparation(self, separator, qtBits):
        '''Método que adiciona uma string separator a cada qtBits do arquivo. 
        
        - separator (str) : String que será adicionada com o propósito de separar os bits do arquivo
        - qtBits (int) : Quantidade de bits entre um separator e outro 
        '''

        tempStr = self.strData 
        newStr = ''
        nBits = 0
        for oldBit in tempStr:
            if (nBits<qtBits-1):
                newStr += oldBit
                nBits+=1
            elif (nBits>=qtBits-1):
                newStr += (oldBit + separator)
                nBits = 0
        self.strData = newStr

                
    def setNewFile(self):
        '''Escreve todas as mudanças realizadas no conteúdo do arquivo antigo em um novo arquivo de texto localizado em /txtoutput/treated/, com o mesmo nome do antigo, porém com as informações adicionais requeridas'''
        
        with open (self.newFilePath, 'w') as self.newFile:
            self.newFile.truncate()
            self.newFile.write(self.strData)
        
        
    def setPath(self, oldFilePath, info):
        '''A partir do caminho do arquivo, define o tipo do autômato celular (e a pasta na qual o novo arquivo deve ser armazenado), e o nome que o novo arquivo deve ter. 
        
            - oldFilePath (str) : indica a localização e o nome do arquivo de texto
            - info (str) - O novo arquivo é salvo na pasta /treated/, subpasta do seu tipo, com o nome igual a sua regra. Caso deseje-se acrescentar outra informação, deve-se declará-la como uma string na variável info. 
        '''
        barra = 0
        oldFileName = type = oldPath = ''
        for i in oldFilePath:
            if (i !='/'):
                if (barra ==0):
                    oldPath +=i
                if (barra == 1):
                    type +=i
                elif (barra == 2):
                    oldFileName+=i   
            elif (i == '/'):
                barra +=1
        
        oldFileName = oldFileName[:-4] 
        newFileName = oldFileName + info + '.txt'    
        newFilePath = '../Output/txtoutput/treated/'  + type + '/' +  newFileName
        return newFilePath