N, K = map(int, input().split())
arr = [0]*N
w = []
m = []
result = 0
for i in range(N):
    arr[i] = list(map(int, input().split()))
arr.sort()
for i in range(N):
    if arr[i][0] == 0:
        w.append(arr[i][1])
    else:
        m.append(arr[i][1])
for i in range(1,7):
    result += w.count(i)//K + m.count(i)//K
    if w.count(i)%K != 0:
        result += 1
    if m.count(i)%K != 0:
        result += 1
print(result)