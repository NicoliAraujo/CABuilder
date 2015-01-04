'''
Created on 20/10/2014

@author: matsu
'''
from ca.RuleNumber import RuleNumber
from ca.AutomataPicture import AutomataPicture


if __name__ == '__main__':
    
    
    print("Gerador de Automatos Celulares")
    rule = int( input("De a regra do automato: ") )
    
    ca = RuleNumber(rule)
    pic = AutomataPicture(20,600,ca)
    pic.setImage()
    pic.save('../output/','.jpg')

   
    
    
    
    
    