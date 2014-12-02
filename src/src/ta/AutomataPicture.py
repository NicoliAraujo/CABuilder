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

    
   
    def __init__(self, height, width, automata, firstColor):
        '''
        Constructor
        Instancia height, width, o automato
        Cria a imagem e poe o 1o pixel preto
        '''
        self.height = height
        self.width = width
        self.automata = automata
        self.nTons = self.calcTons(self.automata.k)
        self.firstColor = firstColor 
        self.image = Image.new("L", (self.width, self.height), "white")
        self.putFirstPixel(self, self.height, self.firstColor)
    
       
    def putFirstPixel(self, height, firstColor):
        self.image.putpixel( (int(self.height/2), 0) , firstColor)
        
    def calcTons(self, k):
        nTons = 3*self.automata.k + 2 
        return nTons
    
    def setColor(self, k):
        self.dictColors = {0:0}
        aux = round(255/(self.nTons-1))
        for i in range ((self.nTons), 1):
            self.dictColors[i] = 255 - aux
            aux=aux+self.dictColors[i-1]

            
    def getSite(self, x, y):
        '''
        Pega os pixels nas posicoes (x, y-1), (x, y) e (x, y+1), tira a média
        dos seus tons e passa seu valor correspondente do dictColor
            
        '''
        p1 = self.tryGetSite(x, y-1)
        p2 = self.tryGetSite(x, y)
        p3 = self.tryGetSite(x, y+1)
        p = p1+p2+p3/3
        return self.dictColor[p]

    
    def tryGetSite(self, x, y):
        try:
            pixel = self.image.getpixel((x, y))
            return pixel
        except:
            return 0
        
         
    def setImage(self):
        '''
        Edita a imagem de acordo com o automato recebido
        getNext eh o metodo que devolve o dicionario de regras do automato
        Ao passar line e column pro putPixel, eles viram x e y
        '''
        
        for line in range (1, self.width):
            for column in range (0, self.height):

                nColor = self.getSite(column-1, line)
                newSite = self.automata.getNext(self.dictColors[nColor])
                self.putpixel(newSite, line, column)
        return self.image    
                 
                 
                  
    def save(self,path,fileType): 
        '''
        path eh o caminho, que deve incluir a pasta (no main esta output)
        fileType eh o formato desejado para a imagem
        '''  
        self.image.save(path + str(self.automata.getName()) + fileType)