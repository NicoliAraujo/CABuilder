'''
Created on 16/10/2014

@author: matsu
@author: elloa
'''
from CelAuto.AutomataPicture import AutomataPicture
from ta.TotalisticRule import TotalisticRule

class AutoPicTA(AutomataPicture):
    '''
    classdocs
    '''
   
    def __init__(self, height, width, rule, k, firstK):
        '''
        Constructor
        Instancia height, width, rule e k
        Chama o constructor do totalistic rule
        Cria a imagem e poe o 1o pixel preto
        '''
        self.k = k
        AutomataPicture.__init__(self, height, width, rule, firstK)

        self.automata = TotalisticRule(self.rule, self.k)

    
    def save(self,path,fileType): 
        '''
        path eh o caminho, que deve incluir a pasta (no main esta output)
        O automato eh salvo com a regra, a base em que eh gerado e a cor do seu primeiro pixel
        fileType eh o formato desejado para a imagem
        '''
        self.image.save(path + '/TA/' + str(self.automata.getName()) +"k" + str(self.k) + 'fp' + str(self.firstK) + fileType)
        
        
    