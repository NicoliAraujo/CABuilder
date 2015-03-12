# -*- coding: utf-8 -*-
'''
Created on 03/03/2015

@author: matsu
'''

import shutil
from shutil import copyfile
class AutomataText():
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
    
    def imgToTxt(self, name):
        filename = './text/' +str(name)+ '.txt'
        with open(filename, 'w') as self.file:
            self.file.write('')
            self.file.truncate()
            for line in range (0, self.width):
                for column in range(0, self.height):
                    site = self.image.getpixel((column,line))
                    self.file.write(self.dictTxt[site])

                
   