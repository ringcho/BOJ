N = int(input())
arr = [[0] * 1001 for _ in range(1001)]

for k in range(1, N+1):
    x, y, dx, dy = map(int, input().split())
    for j in range(y, y+dy):
        for i in range(x, x+dx):
            arr[j][i] = k
for i in range(1, N+1):
    cnt = 0
    for y in range(1001):
        for x in range(1001):
            if arr[y][x] == i:

                cnt += 1
    print(cnt)