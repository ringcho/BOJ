N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
s = sorted(arr, key=lambda x: (x[0],x[1]))

for i in s:
    print(*i)