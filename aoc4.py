# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:37:58 2024

@author: jmora
"""
# 
#%% Original (part 1)
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def find_in_flat(m, sub):
    m_in_windows = sliding_window_view(m, len(sub))
    matches = np.where((m_in_windows == pattern).all(axis=1))[0]
    return len(matches)

# def find_in_flat(array, pattern):
#     array = np.array(array)
#     pattern = np.array(pattern)
#     pattern_length = len(pattern)
#     count = 0
#     idx = 0  # Pointer for the main array
#     pattern_idx = 0  # Pointer for the pattern

#     while idx < len(array):
#         if array[idx] == pattern[pattern_idx]:  # Match current pattern element
#             pattern_idx += 1
#             if pattern_idx == pattern_length:  # Completed a full match
#                 count += 1
#                 pattern_idx = 0  # Reset pattern pointer for next match
#         idx += 1  # Move to the next element in the main array

#     return count

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

char_to_nmbr = {'X': 1, 'M': 2, 'A': 3, 'S': 4}

# Convert the characters to their respective numbers using the mapping
matrix = np.array([[char_to_nmbr[char] for char in row.strip()] for row in t.split()])
pattern = np.array([1, 2, 3, 4])

# Horizontal search
h_cnt1 = find_in_flat(matrix.flatten(), pattern)
h_cnt2 = find_in_flat(matrix.flatten(), np.flip(pattern))

# Vertical search
v_cnt1 = find_in_flat(matrix.T.flatten(), pattern)
v_cnt2 = find_in_flat(matrix.T.flatten(), np.flip(pattern))

# Diagonal search
l = len(pattern)
n_rows, n_cols = matrix.shape
max_diag = max(n_rows, n_cols)

d_cnt1, d_cnt2, d_cnt3, d_cnt4 = 0, 0, 0, 0
for diag_i in range(-max_diag+l, max_diag-l+1):
    # print(diag_i)
    diag = np.diag(matrix, diag_i)
    d_cnt1 += find_in_flat(diag, pattern)
    d_cnt2 += find_in_flat(diag, np.flip(pattern))
    # print(diag)
    
    diag2 = np.diag(np.fliplr(matrix), diag_i) 
    d_cnt3 += find_in_flat(diag2, pattern)
    d_cnt4 += find_in_flat(diag2, np.flip(pattern))
    # print(diag2)

tot_cnt = (h_cnt1 + h_cnt2) + (v_cnt1 + v_cnt2) + (d_cnt1 + d_cnt2 + d_cnt3 + d_cnt4)
print(tot_cnt)
    


