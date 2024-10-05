#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:26:23 2024

@author: bryancsouza
"""

import io
import numpy as np

print('This is the auxiliary script for Assignment 2C')
print('Follow the instructions to insert your answers to Problem 30')

print('Problem 30:')

answers=[]
opt = ["Global", 'Local (check-balance)', 'Local (transfer_x)']
for namespace in opt:
    print('What are the variables associated with the ' + namespace + ' namespace?')
    print('(Enter the variable names separated by comma)')
    ans1 = input('')

    answers.append(namespace + ';' + ans1 + ';')
    print('')
    

print('-------------------')
opt = ["print #1", 'print #2', 'print #3']
for output in opt:
    print('What are the variables that can be printed when the program reaches ' + output + '?')
    print('(Enter the variable names separated by comma)')
    ans1 = input('')

    answers.append(output + ';' + ans1 + ';')
    print('')
    

fid= io.open('problem_30.txt', 'w')

for i in range(len(answers)):
    fid.write(answers[i] +'\n')
fid.close()
print("File 'problem_30.txt' generated.")

print('-------------------')

#%%