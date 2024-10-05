#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:26:23 2024

@author: bryancsouza
"""


import io
import numpy as np

print('This is the auxiliary script for Assignment 2B')
print('Follow the instructions to insert your answers to Problems 21')

print('Problem 21:')


header = ' | Loop number | Code line | i | my_sum'

table = [header]

rows = [(4,3),(4,4),(5,3),(5,4),(7,3),(7,4)]

# opt = {1: 'i', 2: 'mysum', 3:''}
output=[]
count=0
for i in range(len(rows)):
    for line in table:
        print(line)
    count+=1
    row = str(count)+ '| '+ str(rows[i][0]) +'\t       | '+ str(rows[i][1]) +'\t   | '+ '?' +' | '
    print(row)

    print('Choose the missing value (?):')
    ans = input()
    
    # for line in table:
    #     print(line)
    
    try:
        ans1 = int(ans)
    except:
        print('Invalid input. Your answer should be a number. Considering unknown value.')
        ans1 = ''
    
    row = str(count)+ '| '+ str(rows[i][0]) +'\t       | '+ str(rows[i][1]) +'\t   | '+ str(ans1) +' | ?'
    print(row)

    print('Choose the missing value (?):')
    ans = input()
    
    try:
        ans2 = int(ans)
    except:
        print('Invalid input. Your answer should be a number. Considering unknown value.')
        ans2 = ''
    row = str(count)+ '| '+ str(rows[i][0]) +'\t       | '+ str(rows[i][1]) +'\t   | '+ str(ans1) +' | ' + str(ans2)
    
    output.append([ans1,ans2])
    table.append(row)
    
for line in table:
    print(line)
    
fid= io.open('problem_21.txt', 'w')

for i in range(len(output)):
    fid.write(str(output[i][0])+'; '+ str(output[i][1]) +';\n')
fid.close()
print("File 'problem_21.txt' generated.")

print('-------------------')
