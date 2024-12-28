# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:37:58 2024

@author: jmora
"""

#%% Original (part 1)
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def find_in_flat(m, sub):
    m_in_windows = sliding_window_view(m, len(sub))
    matches = np.where((m_in_windows == pattern).all(axis=1))[0]
    return len(matches)

with open('aoc4.txt') as fp:
    lines = fp.readlines()
    
t = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

char_to_nmbr = {'X': 1, 'M': 2, 'A': 2, 'S': 3}

# Convert the characters to their respective numbers using the mapping
matrix = np.array([[char_to_nmbr[char] for char in row.strip()] for row in t.split()])
pattern = np.array([1, 2, 3, 4])

# Horizontal search
h_cnt1 = find_in_flat(matrix.flatten(), pattern)
h_cnt2 = find_in_flat(matrix.flatten(), np.flip(pattern))

# Vertical search
v_cnt1 = find_in_flat(matrix.T.flatten(), pattern)
v_cnt2 = find_in_flat(matrix.T.flatten(), np.flip(pattern))

# Diagonal searches

# Create chunks of 4
l = len(pattern)
n_rows, n_cols = matrix.shape
n_ele = n_rows * n_cols 
max_diag = max(n_rows, n_cols)
for 
for row_i in range(matrix.shape[0]):
    new_mat = np.zeros((l, matrix.shape[1] - l))
    for col_i in range(l):
        new_mat = matrix[row_i:row_i+l, :-l]


