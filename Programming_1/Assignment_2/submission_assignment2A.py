#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:26:23 2024

@author: bryancsouza
"""




import io
import numpy as np

print('This is the auxiliary script for Assignment 2A')
print('Follow the instructions to insert your answers to Problems 15')

print('Problem 15:')

varvalues_p15 = []

var = list(np.arange(1,5))
for i in var:
    print('Considering Input ' + str(i))
    print('What is the final value of num1?')
    ans1 = input('')
    print('What is the final value of num3?')
    ans2 = input('')
    try:
        ans1 = int(ans1)
        ans2 = int(ans2)
    except:
        pass
    varvalues_p15.append([str(ans1), str(ans2)])
    print('')   
    
fid= io.open('problem_15.txt', 'w')

for i in range(len(varvalues_p15)):
    fid.write(str(varvalues_p15[i][0])+'; '+ str(varvalues_p15[i][1]) +';\n')
fid.close()
print("File 'problem_15.txt' generated.")