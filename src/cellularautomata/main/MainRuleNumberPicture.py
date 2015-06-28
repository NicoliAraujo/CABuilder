# -*- coding: utf-8 -*-
'''
Created on 20/10/2014

@author: matsu
'''

from cellularautomata.modules.AutomataImage import RuleNumberImage


if __name__ == '__main__':
    
    
    pic = RuleNumberImage(400,400,30)
    pic.setImage()
    pic.save('../output/','.png')
    print("Operacao terminada")

   
    
    
    
    
    