'''
Created on 20/10/2014

@author: matsu
'''

from cellularautomata.modules.AutomataImage import TotalisticCodeImage


if __name__ == '__main__':
    '''Construtor: 
            pic = AutoPicTA(altura, largura, regra, k(ou n de cores), 1o k)
    '''
    
    pic = TotalisticCodeImage(100, 100, 600, 3, 1)
    
    pic.setImage()
    print("Operacao terminada")
    pic.save('../output/','.png')

   
    
    
    
    
    