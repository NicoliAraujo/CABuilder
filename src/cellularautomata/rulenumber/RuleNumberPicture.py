'''
Created on 16/10/2014

@author: matsu
@author: elloa
'''

from trunk.src.cellularautomata.AutomataPicture import AutomataPicture
from trunk.src.cellularautomata.rulenumber.RuleNumber import RuleNumber

class RuleNumberPicture(AutomataPicture):
    '''
    classdocs
    '''
    
    '''
    Relacao     cor  -  site - pixel
               preto     1      0
               branco    0     255
    '''
    
   
    def __init__(self, height, width, rule):
        '''
        Constructor
        Como eh um automato celular simples, o numero de estados eh sempre 2, e o primeiro pixel eh sempre preto
        '''
        AutomataPicture.__init__(self, height, width, rule, k = 2, firstK = 1)
        self.automata = RuleNumber(self.rule)
        

    def save(self,path,fileType): 
        '''
        path e o caminho, que deve incluir a pasta (no main esta output)
        fileType eh o formato desejado para a imagem
        '''  
        self.image.save(path + '/RN/' + str(self.automata.getName()) + fileType)