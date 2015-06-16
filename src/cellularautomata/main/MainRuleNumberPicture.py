# -*- coding: utf-8 -*-
'''
Created on 20/10/2014

@author: matsu
'''

from src.cellularautomata.rulenumber.RuleNumberPicture import RuleNumberPicture


if __name__ == '__main__':
    
    
    pic = RuleNumberPicture(400,400,30)
    pic.setImage()
    pic.save('../output/','.png')
    print("Operacao terminada")

   
    
    
    
    
    