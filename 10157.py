from pprint import pprint
C, R = map(int, input().split())
goal = int(input())
cnt = 0
arr = [[0]*C for _ in range(R)]
cycle = 0
while True:
    for i in range(cycle, R-cycle):
        if C * R <= cnt:
            break
        cnt += 1
        arr[i][cycle] = cnt
    for i in range(cycle, C-cycle):
        if C * R <= cnt:
            break
        cnt += 1
        arr[-cycle][i-cycle] = cnt
    for i in range(cycle, R-cycle):
        if C * R <= cnt:
            break
        cnt += 1
        arr[-i][-cycle] = cnt
    for i in range(cycle, C-cycle):
        if C * R <= cnt:
            break
        cnt += 1
        arr[cycle-1][-i] = cnt
    if C * R <= cnt:
        break
    print(cnt)
    cycle += 1
pprint(arr)