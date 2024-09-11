#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:57:59 2024

@author: bryancsouza
"""
import io
import numpy as np

print('This is the auxiliary script for Assignment 1A')
print('Follow the instructions to insert your answers to Problems 1 and 2')

print('Problem 1:')

print('Choose the correct type of each variable.')

vartypes_p1 = []
answer_labels = {1: 'int', 2: 'float', 3: 'str', 4: 'error', 5: 'unknown'}
for i in range(1,14):
    print('var' + str(i))
    print('  - int [1]')
    print('  - float [2]')
    print('  - str [3]')
    print('  - variable not created [4]')
    ans = input('')
    try:
        ans = int(ans)
        if ans > 4 or ans<1:
            ans = 5
            print('Invalid input. Your answer should be a number from 1-4. Considering unknown type.')
    except:
        print('Invalid input. Your answer should be a number from 1-4. Considering unknown type.')
        ans = 5
    vartypes_p1.append(answer_labels[ans])
    print('')
    
fid= io.open('problem_1.txt', 'w')
for v in vartypes_p1:
    fid.write(v+';\n')
fid.close()

print("File 'problem_1.txt' generated.")


print('Problem 2:')

print('Choose the correct type of each variable. Then input its value.')

vartypes_p2 = []
varvalues_p2 = []
answer_labels = {1: 'int', 2: 'float', 3: 'str', 4: 'error', 5: 'unknown'}

var = list(np.arange(13,21))+[1,21,22,5,8]
for i in var:
    print('var' + str(i) + ' type:')
    print('  - int [1]')
    print('  - float [2]')
    print('  - str [3]')
    print('  - variable not created [4]')
    ans = input('')
    try:
        ans = int(ans)
        if ans > 4 or ans<1:
            ans = 5
            print('Invalid input. Your answer should be a number from 1-4. Considering unknown type.')
    except:
        print('Invalid input. Your answer should be a number from 1-4. Considering unknown type.')
        ans = 5
        
    vartypes_p2.append(answer_labels[ans])
    if ans!=5:
        print('var' + str(i) + ' value:')
        ans = input('')
        varvalues_p2.append(ans)
    else:
        print('var' + str(i) + ' has no value')
        varvalues_p2.append('None')
    print('')
    
fid= io.open('problem_2.txt', 'w')

for i in range(len(vartypes_p2)):
    fid.write(vartypes_p2[i]+'; '+ varvalues_p2[i] +';\n')
fid.close()
print("File 'problem_2.txt' generated.")

    
