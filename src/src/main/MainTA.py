'''
Created on 20/10/2014

@author: matsu
'''

from ta.AutoPicTA import AutoPicTA 


if __name__ == '__main__':
    '''Construtor: 
            pic = AutoPicTA(altura, largura, regra, k(ou n de cores), 1o k)
    '''
    
    pic = AutoPicTA(50, 50, 777, 3, 1)
    
    pic.setImage()
    print("Operacao terminada")
    pic.save('../output/','.png')

   
    
    
    
    
    