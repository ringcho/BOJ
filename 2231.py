N = int(input())
arr = []
for i in range(1, N):
    cnt = i
    temp = i
    while temp > 0:
        cnt += temp % 10
        temp //= 10
    if cnt == N:
        arr.append(i)
if len(arr):
    print(min(arr))
else:
    print(0)