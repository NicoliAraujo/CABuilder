'''
Created on 20/10/2014

@author: matsu
'''
from RuleNumber import RuleNumber
from rn import AutoPicRN


if __name__ == '__main__':
    
    
    print("Gerador de Automatos Celulares")
    for i in range(0, 256):
        rule = i
        
        ca = RuleNumber(rule)
        pic = AutoPicRN(1024,1024,ca)
        pic.setImage()
        print("Automato celular de regra %d foi gerado com sucesso" %rule)
        pic.save('../output/','.png')