'''
Created on 20/10/2014

@author: matsu
'''
from __future__ import unicode_literals

from cellularautomata.modules.AutomataImage import AutomataImage
from cellularautomata.modules.CellularAutomata import RuleNumber

if __name__ == '__main__':
    
    
    print("Gerador de Automatos Celulares")
    for i in range(0, 256):
        automata = RuleNumber(i)       
        pic = AutomataImage(1024,1024, automata)
        pic.setImage()

        print("Automato celular de regra %d foi gerado com sucesso" %i)
        
        pic.save('../imgoutput/','.png')