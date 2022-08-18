import random

small_height = [0 for _ in range(9)]
check_7 = []
for i in range(9):
    small_height[i] = int(input())
result = [[0]*9 for _ in range(1<<9)]
for i in range(1<<9):
    for j in range(9):
        if i & (1<<j):
           result[i][j] = small_height[j]
    if sum(result[i]) == 100 and result[i].count(0) == 2:
        check_7 = sorted(result[i])

for i in range(2, 9):
    print(check_7[i])

