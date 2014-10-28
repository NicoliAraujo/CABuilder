'''
Created on 16/10/2014

@author: matsu
'''
from PIL import Image

import CellularAutomata


class AutomataPicture(CellularAutomata):
    '''
    classdocs
    '''
    
    '''
    Relacao     cor  -  site - pixel
               preto     1      0
               branco    0     255
    '''
    

    def __init__(self, height, width, autoCel, rule):
        '''
        Constructor
        '''
        self.height = height
        self.width = width
        self.autoCel = autoCel
        self.autoCelImg = Image.new("L", (self.width, self.height), "white")
        self.autoCelImg.putpixel( (int(self.height/2), 0) , 0) #Põe o pixel inicial preto
        self.rule = rule
        
    def putSite(self, newSite, mLine, mColumn): 
        '''
        Pega o 0 ou 1 resultante da regra no hashRule, transforma em pixel branco ou preto
            e coloca na imagem
        Atencao: mLine e mColumn se referem aos parametros passados ao modulo putSite
        '''
        if (newSite == 0):
                self.autoCelImg.putpixel( (mColumn,mLine) , 255)
        elif (newSite == 1):
                self.autoCelImg.putpixel( (mColumn, mLine) , 0)
                
    
    def getSite(self, line, column):
        '''
        Pega o pixel branco ou preto na posicao (line, column) e transforma em 0 ou 1 
        '''
        try:
            pixel = self.autoCelImg.getpixel((line, column))
            if (pixel == 0): #Pixel preto recebe 1
                site = 1
            else: #Pixel Branco recebe 0
                site = 0
        except:
            site = 0 #Pixel branco recebe 0
        return site
     
         
    def setImage(self, width, height):
        '''
        
        '''
        self.autoCelImg.putpixel( (int( width/2 ), 0) , 0)
        
        for line in range (1, width):
            for column in range (0, height):

                try:
                    b1 = self.getSite(column-1, line-1)
                except:
                    b1 = 0
                
                try:
                    b2 = self.getSite(column, line-1)
                except:
                    b2 = 0
                   
                try:
                    b3 = self.getSite(column+1, line-1)
                except:
                    b3 = 0
                     
                newSite = self.autoCel.input(b1,b2,b3)
                self.putSite(newSite, line, column)
        return self.autoCelImg    
                 
                 
                  
    def save(self):   
        self.autoCelImg.save("./Rule"  + str(self.rule) + ".jpg")