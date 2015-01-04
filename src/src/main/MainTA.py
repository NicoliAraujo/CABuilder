'''
Created on 20/10/2014

@author: matsu
'''

from ta.AutomataPicture import AutomataPicture


if __name__ == '__main__':
    '''Construtor: 
            pic = AutomataPicture(altura, largura, regra, k(ou n de cores), 1o k)
    '''
    
    pic = AutomataPicture(512, 512, 2040, 3, 1)
    
    pic.setImage()
    print("Operacao terminada")
    pic.save('../output/','.png')

   
    
    
    
    
    