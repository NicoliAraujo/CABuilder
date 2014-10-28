'''
Created on 20/10/2014

@author: matsu
'''
from src.CellularAutomata import RuleNumber
from src.CellularAutomata import  AutomataPicture

if __name__ == '__main__':
    
    
    print("Gerador de Automatos Celulares")
    rule = int( input("De a regra do automato") )
    width = int( input("De a largura da imagem") )
    height = int( input("De a altura da imagem") )
    ruleBin = 0
    hashRule = dict()
    
    autoCel = RuleNumber.RuleNumber(rule, ruleBin, hashRule)
    acPicture = AutomataPicture.AutomataPicture(height, width, autoCel, rule)
    acPicture.setImage(acPicture.width, acPicture.height)
    acPicture.save()
    
    
    
    
    