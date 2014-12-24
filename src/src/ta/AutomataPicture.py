'''
Created on 16/10/2014

@author: matsu
@author: elloa
'''
from TotalisticRule import TotalisticRule
from PIL import Image



class AutomataPicture():
    '''
    classdocs
    '''

    
   
    def __init__(self, height, width, rule, k):
        '''
        Constructor
        Instancia height, width, rule e k
        Chama o constructor do totalistic rule
        Cria a imagem e poe o 1o pixel preto
        '''
        self.height = height
        self.width = width
        self.k = k
        self.rule = rule
        
        self.automata = TotalisticRule(self.rule, self.k)

        self.buildDictColor(self.k)

        self.image = Image.new("L", (self.width, self.height), "white")
        self.image.putpixel( (int(self.height/2), 0) , 0) 
    
    
    def buildDictColor(self, k):
        
        self.dictColor = {}
        temp = 255/(self.k - 1)
        aux = 0
        
        for i in range (0, self.k):
            self.dictColor[i] = 255 - aux
            aux = temp + aux
        print("DictColor>")
        print(self.dictColor)
     
    def SearchSite(self, color):
        for i in self.dictColor:
            if((color<=self.dictColor[i]+2) & (color>=self.dictColor[i]-2 ) ): # tratar
                return i
                
          
        
    def getSite(self, x, y):
        '''
        Pega os pixels nas posicoes 
            
        '''
        
        p1 = self.SearchSite( self.tryGetSite(x-1, y) ) 
        p2 = self.SearchSite( self.tryGetSite(x, y) )
        p3 = self.SearchSite( self.tryGetSite(x+1, y) )
        oldSite = (p1, p2, p3)
        print ("oldsite> ")
        print(oldSite)
        return oldSite


      
            
    def tryGetSite(self, x, y):
        try:
            pixel = self.image.getpixel((x, y))
            return pixel
        except:
            return 255 #retorna branco
        
         
    def setImage(self):
        '''
        Edita a imagem de acordo com o automato recebido
        getNext eh o metodo que devolve o dicionario de regras do automato
        Ao passar line e column pro putPixel, eles viram x e y
        '''
        
        for line in range (1, self.width):
            for column in range (0, self.height):
                (b1, b2, b3) = self.getSite(column, line-1)
                print((b1, b2, b3))
                newSite = self.automata.getNext(b1, b2, b3)
                print(newSite)
                try:
                    newPixel = self.dictColor[newSite]
                except:
                    newPixel = 255 #vai retornar um pixel branco
                print(newPixel)
                self.image.putpixel((column, line), newPixel)
                
        return self.image    
                 
                 
                  
    def save(self,path,fileType): 
        '''
        path eh o caminho, que deve incluir a pasta (no main esta output)
        fileType eh o formato desejado para a imagem
        '''  
        self.image.save(path + str(self.automata.getName()) + fileType)
        
        
    '''
    def putFirstPixel(self, height, firstColor):
        pega o valor em TA do 1o pixel e transforma na cor do dictRule
        precisa ajeitar, por enquanto e necessario dar a cor em rgb
        self.image.putpixel( (int(self.height/2), 0) , self.dictColorsOut[firstColor])
    ''' 