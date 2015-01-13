'''
Created on 20/10/2014

@author: matsu
'''

from trunk.src.cellularautomata.rulenumber.RuleNumberPicture import RuleNumberPicture


if __name__ == '__main__':
    
    
    pic = RuleNumberPicture(20,20,30)
    pic.setImage()
    print("Operacao terminada")
    pic.save('../output/','.jpg')

   
    
    
    
    
    