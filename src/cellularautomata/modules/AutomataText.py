# -*- coding: utf-8 -*-

'''
Created on 23/03/2015

@author: matsu
'''
from __future__ import unicode_literals
from numpy import zeros

class AutomataText(object):
    '''Classe que gera um arquivo de texto que armazena os estados de um autômato celular.

    O estado de cada célula é representado por um número inteiro de 0 a k-1, sendo k o número de estados possíveis 
    do autômato.Cada bit representa uma célula, que muda de estado em cada linha. Assim, as linhas representam
    um único vetor unidimensional, que tem seu estado mudado conforme o tempo passa. Portanto, o arquivo mostrará uma
    matriz size x it, em que size é a largura e it é a altura.
    '''


    def __init__(self, size, it, ca, name):
        '''Construtor da classe AutomataText 
        
        Instancia o tamanho do vetor a ser gerado (size), a quantidade de iterações que ocorrerão (it) e o autômato
        celular que se deseja representar (ca):
        
        - size (int) - Largura do vetor
        - it (int) - quantidade de iterações, ou seja, é a passagem de tempo
        - ca (CellularAutomata) - Autômato celular cuja regra será utilizada para alterar os estados de cada célula.
        - name (Str) - O arquivo é salvo na pasta /original/, subpasta do seu tipo, com o nome igual a sua regra. Caso
                       deseje-se acrescentar outra informação, deve-se declará-la como uma string na variável nome. 
        
        A partir desses parâmetros, o construtor instancia:
        
        - file (File) - arquivo de texto (.txt) composto de uma matriz de dimensões size x it de bits. Cada bit tem
                        valor de 0 a k-1.
        - firstBit (int) - Estado que a célula central do vetor deve ter no início do crescimento. Varia de 0 a k-1.
        
        Então, o método setFile altera os estados das células do vetor it vezes. Em seguida, salva os estados em file. 
        
        '''
        self.__ca = ca
        self.it = it
        self.size = size
        
        self.setFile(self.ca.seed, name)
    
    
    def __startArray(self):
        '''Cria um vetor de tamanho size x it composto de zeros'''  
        self.__array = zeros((self.it, self.size))

        
    def __putFirstLine(self):
        '''Método que escreve a primeira linha no arquivo. É composta de zeros, com exceção do bit central, que ganha
        o valor de self.firstBit.
        '''
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
        '''Calcula o estado de uma célula na posição (line x column). Para isso, pega o estado da vizinhança da célula na
        iteração anterior.
        
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
    
    def setFile(self, firstBit, name):
        '''Salva os estados do autômato no arquivo de texto.
        
        Edita o arquvio de texto criado na iniciação de acordo com o autômato. Em t = 0 (primeira linha) põe o primeiro 
        bit com o valor firstBit. Começando em t = 1 (ou na segunda linha), são atualizados e salvos os estados de todas 
        as células do autômato até que tenha sido feito o número de iterações solicitado. 
        
        firstBit (int) - estado da célula central do vetor em t = 0. Inteiro de 0 a k-1.
        '''
        filename = str(self.ca.rule) + name + '.txt'
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
    def file(self):
        return self.__file
    
    @property
    def array(self):
        return self.array