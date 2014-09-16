'''
Created on 16/09/2014

@author: matsu
'''

from PIL import Image

linhas =  1024
colunas = 1024

aCel = Image.new("L", (linhas, colunas), "white")

#gerando o automato

def VerificaPixel(newPixel, linha, coluna):
        if (newPixel == 0):
                aCel.putpixel( (coluna,linha) , 255)
        elif (newPixel == 1):
                aCel.putpixel( (coluna,linha) , 0)


coluna=0
linha=0
#pixel preto na metade
aCel.putpixel( (int(linhas/2), 0) , 0)

for linha in range (1, linhas):
    for coluna in range (0, colunas):
        
                         
            # pegar b1
            try:
                b1 = aCel.getpixel((coluna-1,linha-1))
                if (b1 == 0):
                    b1 = 1
                else:
                    b1 = 0
            except:
                b1 = 0
             
            try:
                b2 = aCel.getpixel((coluna,linha-1))
                if (b2 == 0):
                    b2 = 1
                else:
                    b2 = 0
            except:
                b2 = 0
                 
            try:
                b3 = aCel.getpixel((coluna+1,linha-1))
                if (b3 == 0):
                    b3 = 1
                else:
                    b3 = 0
            except:
                b3 = 0
                        

                 
            newPixel = ( (b1+ b2 + b3 + (b2*b3) ) %2) 
            VerificaPixel(newPixel,linha,coluna)    
             
             
              
                       
                 
aCel.save("./Automato.jpg")
