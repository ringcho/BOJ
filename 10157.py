from pprint import pprint
C, R = map(int, input().split())
goal = int(input())
cnt = 0
arr = [[0]*C for _ in range(R)]
cycle = 1
result = 0
while True:
    for i in range(cycle-1, R-cycle):
        if C * R <= cnt:
            break
        cnt += 1
        arr[i][cycle-1] = cnt

    for i in range(cycle-1, C-cycle):
        if C * R <= cnt:
            break
        cnt += 1
        arr[-cycle][i] = cnt

    for i in range(cycle-1, R-cycle):
        if C * R <= cnt:
            break
        cnt += 1
        arr[-i-1][-cycle] = cnt

    for i in range(cycle-1, C-cycle):
        if C * R <= cnt:
            break
        cnt += 1
        arr[cycle-1][-i-1] = cnt
    if C * R <= cnt:
        break
    cycle += 1

for i in range(R):
    for j in range(C):
        if arr[i][j] == goal:
            print(j+1, i+1)
            result =1
if not result:
    print(0)