'''
Created on 16/10/2014

@author: matsu
@author: elloa
'''
from PIL import Image


class AutomataPicture():
    '''
    classdocs
    '''
    
    '''
    Relacao     cor  -  site - pixel
               preto     1      0
               branco    0     255
    '''
    
    '''
    Constructor
    '''
    def __init__(self, height, width, automata):

        self.height = height
        self.width = width
        self.automata = automata
        self.image = Image.new("L", (self.width, self.height), "white")
        self.image.putpixel( (int(self.height/2), 0) , 0) #Põe o pixel inicial preto

        
    def putPixel(self, value, x, y): 
        '''
        Pega o 0 ou 1 resultante da regra no hashRule, transforma em pixel branco ou preto
            e coloca na imagem
        Atencao: x e y se referem aos parametros passados ao modulo putPixel
        '''
        if (value == 0):
                self.image.putpixel( (y,x) , 255)
        elif (value == 1):
                self.image.putpixel( (y, x) , 0)
                
    
    def getSite(self, x, y):
        '''
        Pega o pixel branco ou preto na posicao (x, y) e transforma em 0 ou 1 
        '''
        try:
            pixel = self.image.getpixel((x, y))
            if (pixel == 0): #Pixel preto recebe 1
                return 1
            else: #Pixel Branco recebe 0
                return 0
        except:
            return 0 #Pixel branco recebe 0
     
         
    def setImage(self):
        '''
        
        '''
        self.image.putpixel( (int( self.width/2 ), 0) , 0)
        
        for line in range (1, self.width):
            for column in range (0, self.height):

                b1 = self.getSite(column-1, line-1)
                b2 = self.getSite(column, line-1)
                b3 = self.getSite(column+1, line-1)

                newSite = self.automata.getNext(b1,b2,b3)
                self.putPixel(newSite, line, column)
        return self.image    
                 
                 
                  
    def save(self,path,fileType):   
        self.image.save(path + str(self.automata.getName()) + fileType)