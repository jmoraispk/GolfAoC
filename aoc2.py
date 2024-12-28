# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 06:50:53 2024

@author: jmora
"""

#%% Original (part 1)
import numpy as np

with open('aoc2.txt') as fp:
    lines = fp.readlines()
    
n_safe = 0
for line in lines:
    
    a = np.fromstring(line, sep=' ', dtype=int)
    d = np.diff(a) # a[1:] - a[:-1]
    
    # all between 1 and 3 or all between -1 and -3
    cond1 = np.logical_and(d >= 1, d <= 3).all()
    cond2 = np.logical_and(-d >= 1, -d <= 3).all()
    if cond1 or cond2:
        n_safe += 1

print(n_safe)

#%% Golfed (part 1)

n_safe = 0
with open('aoc2.txt') as fp:
    for line in fp.readlines():
        d = np.diff(np.fromstring(line, sep=' '))
        if np.logical_and(d >= 1, d <= 3).all() or \
            np.logical_and(-d >= 1, -d <= 3).all():
            n_safe += 1
print(n_safe)

#%% Original (part 2)

n_safe = 0
for line in lines:
    
    a = np.fromstring(line, sep=' ', dtype=int)
    d = np.diff(a) # a[1:] - a[:-1]
    
    # all between 1 and 3 or all between -1 and -3
    cond1 = np.logical_and(d >= 1, d <= 3).all()
    cond2 = np.logical_and(-d >= 1, -d <= 3).all()
    if cond1 or cond2:
        n_safe += 1
    else:
        # check 1 element less substrings
        for el_idx in range(len(a)):
            sub_a = np.delete(a, el_idx)
            d = np.diff(sub_a)
            
            cond1 = np.logical_and(d >= 1, d <= 3).all()
            cond2 = np.logical_and(-d >= 1, -d <= 3).all()
            if cond1 or cond2:
                n_safe += 1
                break

print(n_safe)

#%% Golfed (part 2)

n_safe = 0
with open('aoc2.txt') as fp:
    for line in fp.readlines():
        a = np.fromstring(line, sep=' ')
        for el_idx in range(len(a)):
            d = np.diff(np.delete(a, el_idx))
            if np.logical_and(d >= 1, d <= 3).all() or \
                np.logical_and(-d >= 1, -d <= 3).all():
                n_safe += 1
                break
            
print(n_safe)