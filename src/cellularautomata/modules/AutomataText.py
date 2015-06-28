# -*- coding: utf-8 -*-

'''
Created on 23/03/2015

@author: matsu
'''

class AutomataText(object):
    """
    classdocs
    """


    def __init__(self, width, cycles, autocel, firstk):
        '''
        Constructor
        '''
        self.autocel = autocel
        self.cycles = cycles
        self.width = width
        self.firstk = firstk
        self.file = open('../Output/txtoutput/original/' + str(self.autocel.rule) + '.txt', 'w')
        self.startlist()
        self.putFirstK(self.firstk)
        self.dictTxt = self.autocel.dictRule
    
    def putFirstK(self, firstk):
        string = ''
        for i in range (0, self.width):
            if (i == int(self.width/2)):
                string+=(str(firstk))
            else:
                string +=('0')
        self.list[0] = (string+('\n'))
        self.file.write(self.list[0])
    
    def trygetbit(self, line, i):
        try:
            b = line[i]
        except: 
            b = '0'
        return b
     
     
    def startlist(self):
        self.list = []
        for i in range(0, self.cycles):
            self.list.append('')
     
    def getbits(self, line, i):
        b1 = self.trygetbit(line, i-1)
        b2 = self.trygetbit(line, i)
        b3 = self.trygetbit(line, i+1)

        return  self.autocel.getNext(b1, b2, b3)
    
    def setFile(self):

        for i in range(1, self.cycles):
            for j in range(0, self.width):
                self.list[i] += ( str(self.getbits(self.list[i-1], j ) ) )
            if (i==self.cycles-1):
                self.file.write(self.list[i])
            else:
                self.file.write(self.list[i] + '\n')

        self.file.close()
                 
