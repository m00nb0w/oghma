#!/bin/python3

import sys


grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)
    
dy = [1, 1, 1, 0]
dx = [-1, 0, 1, 1]

m = len(grid)
n = len(grid[0])
res = 0
for i in range(0, m):
    for j in range(0, n):
        for k in range(0, 4):
            t = 1
            flag = True
            for l in range(0, 4):
                if (i + dx[k] * l >= 0) and (i + dx[k] * l < m) and (j + dy[k] * l >= 0) and (j + dy[k] * l < n):
                    t *= grid[i + dx[k] * l][j + dy[k] * l]
                else:
                    flag = False
                    break
            res = max(res, t)

print(res)
