arr = [[0]*100 for _ in range(100)]
N = int(input())
for _ in range(N):
    x1, y1 = map(int, input().split())
    for i in range(y1,y1+10):
        for j in range(x1,x1+10):
            arr[j][i] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[j][i]:
            cnt += 1
print(cnt)