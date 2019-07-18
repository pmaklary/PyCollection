# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 06:07:52 2018

@author: peterm
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
    dct = {}
    for line in txtBunch.splitlines()[1:] :     # prvy - prazdny ignorujeme
       try:
           dct[line] += 1
       except KeyError:
           dct[line] = 1        
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
