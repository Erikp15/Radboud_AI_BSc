#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:51:43 2024

@author: bryancsouza
"""

import io
import numpy as np

print('This is the auxiliary script for Assignment 1B')
print('Follow the instructions to insert your answers to Problems 8, 9 and 10')

print('Problem 8:')
print('Choose the correct type of each variable. Then input its value.')

vartypes_p8 = []
varvalues_p8 = []
answer_labels = {1: 'int', 2: 'float', 3: 'str', 4: 'bool', 5: 'error', 6: 'unknown'}

var = list(np.arange(1,15))
for i in var:
    print('var' + str(i) + ' type:')
    print('  - int [1]')
    print('  - float [2]')
    print('  - str [3]')
    print('  - bool [4]')
    print('  - variable not created [5]')
    ans = input('')
    try:
        ans = int(ans)
        if ans>5 or ans<1:
            ans = 6
            print('Invalid input. Your answer should be a number from 1-5. Considering unknown type.')
    except:
        print('Invalid input. Your answer should be a number from 1-5. Considering unknown type.')
        ans = 6
        
    vartypes_p8.append(answer_labels[ans])
    if ans!=6:
        print('var' + str(i) + ' value:')
        ans = input('')
        varvalues_p8.append(ans)
    else:
        print('var' + str(i) + ' has no value')
        varvalues_p8.append('None')
    print('')   
    
fid= io.open('problem_8.txt', 'w')

for i in range(len(vartypes_p8)):
    fid.write(str(vartypes_p8[i])+'; '+ str(varvalues_p8[i]) +';\n')
fid.close()
print("File 'problem_8.txt' generated.")

#%%



print('Problem 9:')

header = 'Row # | A | B | '
expressions = ['not (A or B)', '(A or B) and not (A and B)',
               '(not A and B) or (A and not B)', '(A or B) and C']

output = []
for iexp in range(3):
    
    print('\nExpression ' + str(iexp+1) +':')
    table = [header + expressions[iexp]]
    opt = {1: 'F', 2: 'T', 3:''}
    count=0
    for i in range(1,3):
        for j in range(1,3):
            for line in table:
                print(line)
            count+=1
            row = '    '+ str(count)+ ' | '+ opt[i] +' | '+ opt[j] +' | '
            print(row+'?')
            print('Choose the missing value (?):')
            print('- F [1]')
            print('- T [2]')
            ans = input()
        
            try:
                ans = int(ans)
                if ans>2 or ans<1:
                    ans = 3
                    print('Invalid input. Your answer should be a number from 1-2. Considering unknown value.')
            except:
                print('Invalid input. Your answer should be a number from 1-2. Considering unknown value.')
                ans = 3
            row+=opt[ans]
            output.append(opt[ans])
            table.append(row)
    for line in table:
        print(line)
    print('-------------------')

header = 'Row # | A | B | C | '

for iexp in range(3,4):
    table = [header + expressions[iexp]]
    opt = {1: 'F', 2: 'T', 3:''}
    count=0
    for i in range(1,3):
        for j in range(1,3):
            for k in range(1,3):
                for line in table:
                    print(line)
                count+=1
                row = '    '+ str(count)+ ' | '+ opt[i] +' | '+ opt[j] +' | '+ opt[k] +' | '
                print(row+'?')
                print('Choose the missing value (?):')
                print('- F [1]')
                print('- T [2]')
                ans = input()
            
                try:
                    ans = int(ans)
                    if ans>2 or ans<1:
                        ans = 3
                        print('Invalid input. Your answer should be a number from 1-2. Considering unknown value.')
                except:
                    print('Invalid input. Your answer should be a number from 1-2. Considering unknown value.')
                    ans = 3
                row+=opt[ans]
                output.append(opt[ans])
                table.append(row)
    for line in table:
        print(line)
    print('-------------------')

fid= io.open('problem_9.txt', 'w')

for line in output:
    fid.write(line+'\n')
fid.close()
print("File 'problem_9.txt' generated.")


#%%

varvalues_p10 = []
opts = {1: 'True', 2: 'False', 3: 'unknown'}

var = list(np.arange(15,26))
for i in var:
    print('var' + str(i) + ' value:')
    print('  - True [1]')
    print('  - Falses [2]')
    ans = input('')
    try:
        ans = int(ans)
        if ans>2 or ans<1:
            ans = 3
            print('Invalid input. Your answer should be a number from 1-2. Considering unknown type.')
    except:
        print('Invalid input. Your answer should be a number from 1-2. Considering unknown type.')
        ans = 3
        
    varvalues_p10.append(opts[ans])
    print('')
    #% %
fid= io.open('problem_10.txt', 'w')

for line in varvalues_p10:
    fid.write(line +';\n')
fid.close()
print("File 'problem_10.txt' generated.")

for i,v in zip(var,varvalues_p10):
    print('var' + str(i) + ': ' +v)

#%%