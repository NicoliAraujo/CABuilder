'''
Created on 20/10/2014

@author: matsu
'''

from rn.AutoPicRN import AutoPicRN


if __name__ == '__main__':
    
    
    pic = AutoPicRN(20,20,30)
    pic.setImage()
    print("Operacao terminada")
    pic.save('../output/','.jpg')

   
    
    
    
    
    