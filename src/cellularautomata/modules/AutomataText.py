# -*- coding: utf-8 -*-

'''
Created on 23/03/2015

@author: matsu
'''
from __future__ import unicode_literals


class AutomataText(object):
    '''
    Classe que gera um arquivo de texto a partir de um autômato celular pré-existente
    '''


    def __init__(self, height, cycles, ca):
        '''
        
        '''
        self.__ca = ca
        self.cycles = cycles
        self.height = height
        self.firstBit = self.ca.seed
        self.file = open('../Output/txtoutput/original/' + str(self.ca.rule) + '.txt', 'w')
        self.setFile()
        
    def putFirstBit(self, firstBit):
        string = ''
        for i in range (0, self.height):
            if (i == int(self.height/2)):
                string+=(str(firstBit))
            else:
                string +=('0')
        self.list[0] = (string+('\n'))
        self.file.write(self.list[0])
    
    def trygetbit(self, line, i):
        try:
            return int(line[i])
        except: 
            return 0

    def startlist(self):
        self.list = []
        for i in range(0, self.cycles):
            self.list.append('')
     
    def getbits(self, line, i):
        b1 = self.trygetbit(line, i-1)
        b2 = self.trygetbit(line, i)
        b3 = self.trygetbit(line, i+1)
        
        return  bin(self.ca.getNext(b1, b2, b3))[2:]
    
    def setFile(self):
        
        self.startlist()
        self.putFirstBit(self.firstBit)
        
        for i in range(1, self.cycles):
            for j in range(0, self.height):
                self.list[i] += ( str(self.getbits(self.list[i-1], j ) ) )
            if (i==self.cycles-1):
                self.file.write(self.list[i])
            else:
                self.file.write(self.list[i] + '\n')

        self.file.close()
                 
    @property
    def ca(self):
        return self.__ca
    
    
    @property
    def file(self):
        return self.__file