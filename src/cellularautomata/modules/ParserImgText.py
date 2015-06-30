# -*- coding: utf-8 -*-
'''
Created on 03/03/2015

@author: matsu
'''
from __future__ import unicode_literals
class ImgtoText():
    '''
    classdocs
    '''


    def __init__(self, caImage):
        '''
        Constructor
        '''
        self.caImage = caImage

        self.dictTxt = self.buildDict(self.k)
     
    def buildDict (self, k):
        '''Constroi o dictColors de trás pra frente'''
        dictTxt = {}
        temp = 255/(k - 1)
        aux = 0
        for i in range(0,k):
            a =  int(255 - aux)
            dictTxt[a] =  bin(i)[2:]
            aux = temp + aux

        return dictTxt

                
    def imgToTxt(self, name):
        filename = '..Output/txtoutput/' + str(name)+ 'fromImg.txt'
        with open(filename, 'w') as self.file:
            self.file.write('')
            self.file.truncate()
            for line in range (0, self.width): 
                for column in range(0, self.height):
                    site = self.image.getpixel((column,line))
                    self.file.write(self.dictTxt[site])
                self.file.write('\n')
      
class ParserCortaLinhas():
    def __init__(self, oldFileName):
        contLine = 0
        self.newfile = open('./txtfile/tratado/' + oldFileName + 'parser.txt', 'w')
        self.newfile.truncate()
        with open('./txtfile/original/' + oldFileName + '.txt', 'r') as self.oldfile:
            for line in self.oldfile:
                
                if (contLine >= 500):
                    a = line.replace('\n', '')
                    self.newfile.write(a)
                contLine+=1
        self.oldfile.close()
        self.newfile.close()
        
       
 
class ParserNist():
    def __init__(self, oldFileName):
        self.newfile = open('./txtfile/tratado/versaoponto/' + str(oldFileName) + 'parser.txt', 'w')
        self.newfile.truncate()
        with open('./txtfile/original/' + oldFileName + '.txt', 'r') as self.oldfile:
            tempStr = '' 
            newStr = ''
            for oldLine in self.oldfile:
                newLine = oldLine.replace('\n', "")
                tempStr += newLine
            for oldBit in tempStr:
                    newBit = (oldBit + '.')
                    newStr += newBit 
            self.newfile.write(newStr)
                
            
        self.oldfile.close()
        self.newfile.close()
        
class ParserSieve():
    def __init__(self, oldFileName):
        self.newfile = open('./txtfile/tratado/continuo/' + str(oldFileName) + 'parser.txt', 'w')
        self.newfile.truncate()
        with open('./txtfile/original/' + oldFileName + '.txt', 'r') as self.oldfile: 
            newStr = ''
            for oldLine in self.oldfile:
                newLine = oldLine.replace('\n', "")
                newStr += newLine
            self.newfile.write(newStr)
            print(newStr)
        self.oldfile.close()
        self.newfile.close()        
