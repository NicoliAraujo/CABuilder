# -*- coding: utf-8 -*-
'''
Created on 03/03/2015

@author: matsu
'''

class ImgtoText():
    '''
    classdocs
    '''


    def __init__(self, image, k, height, width):
        '''
        Constructor
        '''
        self.height = height
        self.width = width
        self.image = image
        self.k = k

        self.dictTxt = self.buildDict(self.k)
     
    def buildDict (self, k):
        dictTxt = {}
        temp = 255/(k - 1)
        aux = 0
        for i in range(0,k):
            a =  int(255 - aux)
            dictTxt[a] =  bin(i)[2:]
            aux = temp + aux

        return dictTxt
    '''truncate apaga tudo que tem no arquivo'''

    '''
    def imgToTxt(self, name):
        filename = './text/' +str(name)+ '.txt'
        with open(filename, 'w') as self.file:
            self.file.write('')
            self.file.truncate()
            for line in range (0, self.width):
                if (line>=500): 
                    for column in range(0, self.height):
                        site = self.image.getpixel((column,line))
                        self.file.write(self.dictTxt[site])
                    self.file.write('\n')
    '''
                
    def imgToTxt(self, name):
        filename = './txtfile/' +str(name)+ 'fomimg.txt'
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
        
'''
class Parser3():
    def __init__(self, oldFileName, nBits, nStrings):
        self.newfile = open('./text/tratado/' + oldFileName + 'parser3.txt', 'w')
        self.newfile.truncate()
        with open('./text/tratado/' + oldFileName + '.txt', 'r') as self.oldfile:
            while (i in range(0, nBits)):
                
                a = oldFile.place('\n', '')
                self.newfile.write(a)
        self.oldfile.close()
        self.newfile.close()
'''
        
class Parser2():
    def __init__(self, oldFileName, total, bitstreams):
        corte = 0
        self.newfile = open('./txtfile/' + oldFileName + 'parser2.txt', 'w')
        with open('./txtfile/' + oldFileName +'.txt', 'r') as self.oldfile:
            for i in range(0, total):
                self.newfile.write(self.oldfile[i])
                if (i == corte):
                    self.newfile.write('\n')
                corte+= corte+total/bitstreams
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
'''        
if __name__ == '__main__':
    from trunk.src.cellularautomata.rulenumber.RuleNumberPicture import RuleNumberPicture
     from trunk.src.cellularautomata.totalisticcode.TotalisticCodePicture import TotalisticCodePicture
     a = TotalisticCodePicture(100, 100, 600, 3, 2)
    a = RuleNumberPicture(1000,1000, 30)
    a.setImage()
      
    x= ImgtoText(a.image, a.automata.k, a.height, a.width)
  
    x.imgToTxt(a.automata.rule)
     Parser(a.automata.getName())
    print("operação terminada")
'''
