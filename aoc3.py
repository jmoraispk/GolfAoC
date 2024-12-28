# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:56:01 2024

@author: jmora
"""

#%% Original (part 1)

with open('aoc3.txt') as fp:
    lines = fp.readlines()

res = 0
for line in lines:
    
    l_split = line.split('mul(')
    for i, splt in enumerate(l_split):
        too_numb = splt.split(')')[0].split(',')
        if len(too_numb) != 2:
            continue
        print(f'i = {i}')
        print(f'too_numb = {too_numb}')
        try:
            res += int(too_numb[0]) * int(too_numb[1])
        except:
            print('ignoring')
            continue

print(res)

#%% Golfed (part1)

res = 0
with open('aoc3.txt') as fp:
    for line in fp.readlines():
        for i, splt in enumerate(line.split('mul(')):
            too_numb = splt.split(')')[0].split(',')
            try:
                assert len(too_numb) == 2
                res += int(too_numb[0]) * int(too_numb[1])
            except:
                continue
print(res)

#%% Original (part 2)
import re

with open('aoc3.txt') as fp:
    lines = fp.readlines()

def calc_chunk(chunk):
    aux = 0
    l_split = chunk.split('mul(')
    for i, splt in enumerate(l_split):
        too_numb = splt.split(')')[0].split(',')
        if len(too_numb) != 2:
            continue
        # print(f'i = {i}')
        # print(f'too_numb = {too_numb}')
        try:
            aux += int(too_numb[0]) * int(too_numb[1])
        except:
            # print('ignoring')
            continue
    return aux
    
pattern = r"do\(\)(.*?)don't\(\)"
res = 0
for line in lines:
    
    # Split line between do and don't (ON from do->dont, OFF don't->do)
    matches = re.findall(pattern, line)
    
    for mtch in matches:
        res += calc_chunk(mtch)
    
    # Add beginning of the line (up to do() or up to don't(), whtv comes first)
    s1, s2 = line.split("do()")[0], line.split("don't()")[0]
    res += calc_chunk(s1) if s1 < s2 else calc_chunk(s2)

print(res)

# 69556683 too high
