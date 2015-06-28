'''
Created on 20/10/2014

@author: matsu
'''

from cellularautomata.modules.AutomataImage import RuleNumberImage


if __name__ == '__main__':
    
    
    print("Gerador de Automatos Celulares")
    for i in range(0, 256):        
        pic = RuleNumberImage(1024,1024, i)
        pic.setImage()
        
        print("Automato celular de regra %d foi gerado com sucesso" %i)
        
        pic.save('../imgoutput/','.png')