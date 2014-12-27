'''
Created on 20/10/2014

@author: matsu
'''
from RuleNumber import RuleNumber
from AutomataPicture import AutomataPicture


if __name__ == '__main__':
    
    
    print("Gerador de Automatos Celulares")
    rule = int( input("De a regra do automato: ") )
    
    ca = RuleNumber(rule)
    pic = AutomataPicture(1024,1024,ca)
    pic.setImage()
    pic.save('../output/','.jpg')

   
    
    
    
    
    