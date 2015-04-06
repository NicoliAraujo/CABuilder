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
    def imgToTxt(self, name):
        filename = './text/' +str(name)+ '.txt'
        with open(filename, 'w') as self.file:
            self.file.write('')
            self.file.truncate()
            for line in range (0, self.width):
                for column in range(0, self.height):
                    site = self.image.getpixel((column,line))
                    self.file.write(self.dictTxt[site])
                self.file.write('\n')
                
class Parser():
    def __init__(self, oldFileName):
        
        self.newfile = open('./text/novo.txt', 'w')
        with open('./text/' + oldFileName +'.txt', 'r') as self.oldfile:
            for line in self.oldfile:
                #===============================================================
                # a = line.replace('\t', '')
                #===============================================================
                a = a.replace('\n', '')
                self.newfile.write(a)
        self.oldfile.close()
        self.newfile.close()
        
        
if __name__ == '__main__':
    from trunk.src.cellularautomata.rulenumber.RuleNumberPicture import RuleNumberPicture
    #===========================================================================
    # from trunk.src.cellularautomata.totalisticcode.TotalisticCodePicture import TotalisticCodePicture
    # a = TotalisticCodePicture(100, 100, 600, 3, 2)
    #===========================================================================
    a = RuleNumberPicture(1000,1000, 30)
    a.setImage()
     
    x= ImgtoText(a.image, a.automata.k, a.height, a.width)
 
    x.imgToTxt(a.automata.rule)
    #===========================================================================
    # Parser(a.automata.getName())
    #===========================================================================
    print("operação terminada")
