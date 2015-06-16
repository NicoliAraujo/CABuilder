# -*- coding: utf-8 -*-
'''
Created on 06/05/2015

@author: Nicoli
'''
from src.cellularautomata.automatatext.AutomataText import AutomataText


if __name__ == '__main__':
    from trunk.src.cellularautomata.rulenumber.RuleNumber import RuleNumber
    from trunk.src.cellularautomata.automatatext.ParserImgToText import ParserNist
    rule30 = RuleNumber(30)
    rule30text = AutomataText(8, 25, rule30, 1)
    rule30text.setFile()
    ParserNist(str(rule30text.autocel.rule))
    print("operação terminada")