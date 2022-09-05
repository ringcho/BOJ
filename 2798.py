N, M = map(int, input().split())
arr = list(map(int, input().split()))

maxV = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = arr[i] + arr[j] + arr[k]
            if temp<=M and maxV < temp:
                maxV = temp
print(maxV)

