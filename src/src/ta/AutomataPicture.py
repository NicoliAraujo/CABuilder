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
        '''
        Constroi o dicionario de k cores, que relaciona cada cor a um valor de 0 a k-1
        '''
        
        self.dictColor = {}
        temp = 255/(self.k - 1)
        aux = 0
        
        for i in range (0, self.k):
            self.dictColor[i] = int(255 - aux)
            aux = temp + aux

    def SearchSite(self, color):
        '''
        Diz o valor k (a chave) de uma cor do dicionario de cores
        '''
        print("Cor que foi pro dictColor: ")
        print(color)
        
        for i in (self.dictColor):
            if(self.dictColor[i] == color): 

                return i

  
    def putPixel(self, value, x, y): 
        '''
        Pega o valor resultante da regra no dictRule, transforma em pixel usando o dictColor e coloca na imagem
        Atencao: x e y se referem aos parametros passados ao modulo putPixel
        '''

        nSite = self.dictColor[int(value)] 

        self.image.putpixel( (y, x) , nSite)
        
          
        
    def getSite(self, x, y):
        '''
        Pega o pixel na posicao (x, y) e transforma no correspondente do dictRule
        '''
        



      
            
    def tryGetSite(self, x, y):
        '''
        Pega o pixel  na posicao (x, y) e transforma no equivalente do dictColors
        '''
        try:
            pixel = self.image.getpixel((x, y))
            chave = self.SearchSite(pixel)
            site = self.automata.getRule(chave)

            return site
        except:
            return 0 # retorna equivalente branco 
        
         
    def setImage(self):
        '''
        Edita a imagem de acordo com o automato recebido
        getNext eh o metodo que devolve o dicionario de regras do automato
        Ao passar line e column pro putPixel, eles viram x e y
        '''
        
        for line in range (1, self.width):
            
            for column in range (0, self.height):
                b1 = self.tryGetSite(column-1, line-1)
                print ("b1: " + str(b1))
                b2 = self.tryGetSite(column, line-1)
                print ("b2: " + str(b2))
                b3 = self.tryGetSite(column+1, line-1)
                print ("b3: " + str(b3))
                
                newSite = self.automata.getNext(b1, b2, b3)
                self.putPixel(newSite, line, column)

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