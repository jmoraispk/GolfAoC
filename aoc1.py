# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:51:39 2024

@author: jmora
"""
#%% Original (part1)
import numpy as np

data = np.loadtxt('aoc1.txt')

data_sorted = np.sort(data, axis=0)

diff = np.abs(data_sorted[:,0] - data_sorted[:,1])

sum_diff = np.sum(diff)

print(sum_diff)

#%% Golfed (part1)

sorted_data = np.loadtxt('aoc1.txt').sort(axis=0)
print(np.abs(data_sorted[:,0] - data_sorted[:,1]).sum())
# 2 lines

#%% Original (part2)

data = np.loadtxt('aoc1.txt')
sim_score = 0
for i in range(data.shape[0]):
    sim_score += data[i,0] * len(data[data[:,1] == data[i,0]])

print(sim_score)

#%% Golfed (part2)

data = np.loadtxt('aoc1.txt')
print(np.sum([data[i,0] * len(data[data[:,1] == data[i,0]])
              for i in range(data.shape[0])]))
# 2 lines
