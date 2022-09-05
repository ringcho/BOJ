N = int(input())
arr = [0] * (N//5+1)
for i in range(N//5+1):
    cnt1 = i
    temp = N - i * 5
    cnt2 = temp//3
    temp = temp - 3 * (temp//3)
    if temp == 0:
        arr[i] = cnt1 + cnt2

if N == 3:
    print(1)
elif arr.count(0) == N//5+1:
    print(-1)
else:
    minV = N//3
    for V in arr:
        if V != 0 and V < minV:
            minV = V
    print(minV)
