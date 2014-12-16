'''
Created on 20/10/2014

@author: matsu
'''
from TotalisticRule import TotalisticRule
from AutomataPicture import AutomataPicture


if __name__ == '__main__':
    
    
    print("Gerador de Automatos Celulares")
    
    k = int(input("De o numero de cores do automato: "))
    rule = int( input("De a regra do automato: ") )
    firstColor = int( input("De a cor (numero de 0 a k-1) do primeiro site do automato: ") )
    
    ca = TotalisticRule(k, rule)

    pic = AutomataPicture(1024,1024,ca, firstColor)
    pic.setImage()
    print("Operacao terminada")
    pic.save('../output/','.jpg')

   
    
    
    
    
    