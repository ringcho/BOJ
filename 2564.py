import sys
sys.stdin = open('2564_input.txt')


x, y = map(int, input().split())
N = int(input())
arr = [[0]*(x+1) for _ in range(y+1)]
result = 0

def find_len(i,j):
    global result
    visited = [[0]*(x+1) for _ in range(y+1)]
    visited[i][j] = 1
    q = [[i, j]]
    while q:
        i, j = q.pop(0)
        if arr[i][j]:
            result += (visited[i][j]-1)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<(y+1) and 0<=nj<(x+1) and visited[ni][nj] == 0 and arr[ni][nj] != -1:
                q.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1

for i in range(1,y):
    for j in range(1,x):
        arr[i][j] = -1

for i in range(1, N+1):
    direc, lota = map(int, input().split())
    if direc == 1:
        arr[0][lota] = i
    elif direc == 2:
        arr[y][lota] = i
    elif direc == 3:
        arr[lota][0] = i
    elif direc == 4:
        arr[lota][x] = i


direc1, lota1 = map(int, input().split())
if direc1 == 1:
    sti, stj = 0, lota1
elif direc1 == 2:
    sti, stj = y, lota1
elif direc1 == 3:
    sti, stj = lota1, 0
elif direc1 == 4:
    sti, stj = lota1, x

find_len(sti, stj)

print(result)