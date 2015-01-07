'''
Created on 04/01/2015

@author: matsu
'''
from PIL import Image

class AutomataPicture():
    '''
    classdocs
    '''


    def __init__(self, height, width, rule, firstK):
        '''
        Construtor geral para qualquer imagem de automato celular
        '''
        self.height = height
        self.width = width
        self.rule = rule
        self.firstK = firstK
 
        
        self.image = Image.new("L", (self.width, self.height), "white")
        self.buildDictColor(self.k)
        self.putFirstPixel(self.firstK)
        
    def putFirstPixel(self, firstK):
        '''
        pega o k do 1o pixel e transforma na cor do dictRule
        '''
   
        self.image.putpixel( (int(self.height/2), 0) , self.dictColor[firstK])
    
    
    def searchSite(self, color):
        '''
        Diz o valor k (a chave) de uma cor do dicionario de cores
        '''
      
        for i in (self.dictColor):
            if(self.dictColor[i] == color): 
               
                return i
            
            
    def buildDictColor(self, k):
        '''
        Constroi o dicionario de k cores, que relaciona cada cor a um valor de 0 a k-1
        '''
        
        self.dictColor = {}
        temp = 255/(self.k - 1)
        aux = 0
        
        for i in range (0, self.k):
            self.dictColor[i] = int(255 - aux)
            aux = temp + aux
    
    def putPixel(self, value, x, y): 
        '''
        Pega o valor resultante da regra no dictRule, transforma em pixel usando o dictColor e coloca na imagem
        Atencao: x e y se referem aos parametros passados ao modulo putPixel
        '''
        
        nSite = self.dictColor[int(value)] 
       
        self.image.putpixel( (y, x) , nSite)


    
    def tryGetSite(self, x, y):
        '''
        Pega o pixel  na posicao (x, y) e transforma no equivalente do dictColor
        '''
        try:
            pixel = self.image.getpixel((x, y))
         
            chave = self.searchSite(pixel)
            
            return chave
        
        except:
            return 0 # retorna equivalente branco 
    
    
    def getSite(self, x, y):
        '''
        A partir de uma posicao (x,y), captura em t-1 os sites x-1, x e x+1
        Depois, consulta no dictRule o resultante da aplicacao da regra para os tres sites superiores
        ''' 
        b1 = self.tryGetSite(x-1, y-1)
        b2 = self.tryGetSite(x, y-1)
        b3 = self.tryGetSite(x+1, y-1)

        newSite = self.automata.getNext(b1,b2,b3)
        return newSite
    
    def setImage(self):
        '''
        Edita a imagem de acordo com o automato recebido
        getNext eh o metodo que devolve o dicionario de regras do automato
        Ao passar line e column pro putPixel, eles viram x e y
        '''
        
        for line in range (1, self.width):
            
            for column in range (0, self.height):
                
                newSite = self.getSite(column, line)
                            
                self.putPixel(newSite, line, column)

        return self.image    
                 

    
    def save(self):
        pass