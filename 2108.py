import sys
import statistics

N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())
arr.sort()
print(round(statistics.mean(arr)))
print(statistics.median(arr))
mode = statistics.multimode(arr)
if len(mode) == 1:
    print(mode[0])
else:
    print(mode[1])
print(max(arr)-min(arr))