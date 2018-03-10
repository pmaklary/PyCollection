# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:34:09 2018

Porovnavanie viacriadkovych textov priamo v skripte pomocou dictionaries

@author: lynx_pmaklary
"""

txtBunchA = """
alfa
beta
gama
"""

txtBunchB = """
alfa
beta
beta
game
"""


def txtBuncToDict(txtBunch):
    pos = 0
    dct = {}
    oneLine = ""
    for c in txtBunch:
        if pos == 0 : 
            pos = 1
            continue
        if c == '\n' :
           try:
               dct[oneLine] += 1
           except KeyError:
               dct[oneLine] = 1
            
           oneLine = ""
        else:
            oneLine += c
        pos += 1
    return dct        

dctA = txtBuncToDict(txtBunchA)
dctB = txtBuncToDict(txtBunchB)

def dct1_to_2(dct1, dct2):
    for item in dct2:
        try:
            if dct1[item] != dct2[item]: print(item + ' different times')
        except KeyError:
            print(item + ' not found')

print('')
print('B vs A:')
dct1_to_2(dctA, dctB)
print('A vs B:')
dct1_to_2(dctB, dctA)
print('')
