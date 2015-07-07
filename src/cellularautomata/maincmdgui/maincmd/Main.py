'''
Created on Jun 28, 2015

@author: Nicoli


from __future__ import unicode_literals

from cellularautomata.modules.CellularAutomata import ElementaryCode, TotalisticCode

from cellularautomata.modules.CAOutput import AutomataImage


if __name__ == '__main__':
    print('Cellular Automata Builder')
    print('Which type is the cellular automata you want to generate?')
    type = input('Options: Elementary or Totalistic\n')
    if (type == 'Elementary'):
        rule = int(input('Rule: '))
        ca = ElementaryCode(rule)
    elif (type == 'Totalistic'):
        rule = int(input('Rule: '))
        k = int(input('Quantity of States: '))
        seed = int(input('Seed: '))
        ca = TotalisticCode(rule, k, seed)

        
    print('In which format do you want to save the automata? ')
    media = input('Options: Image or Text\n')
    if media == 'Image':
        side = int(input('It will be generated an lxl (square) image. Give a value for its side: '))
        caImage = AutomataImage(side, side, ca)
        caImage.setImage()
        caImage.save('.png')
        txtFromImg = input('Do you wish to create a txt file from the generated image?\n Type ''Yes'' or ''No'': ')
        if txtFromImg == 'Yes':
            print('Enter:')
            print('\n\t1 - To turn the image into a linear sequence of bits')
            print('\n\t0 - To seperate the bits in any way')
            formatting = int(input('\n'))
            if formatting == 1:
                separador = input('')
                
    elif media == 'Text':
        lenght = int(input())
        height = int(input())'''
        
        
        


