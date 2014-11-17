# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 19:38:11 2014

@author: Kuo Liu
@email: liukuo99@gmail.com
"""
import numpy as np

with open('p042_words.txt') as f:
    words = f.readlines()[0]
words = words.replace('"','').split(',')

count = 0
for x in words:
    val = sum([ord(y)-64 for y in x])
    n = int(np.sqrt(2*val))
    if n*(n+1) == 2*val:
        count += 1

print count
        
    

