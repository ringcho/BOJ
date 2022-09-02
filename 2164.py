from collections import deque

N = int(input())

arr = deque(range(1,N+1))

while True:
    if len(arr) == 1:
        print(arr[0])
        break
    arr.popleft()
    if len(arr) == 1:
        print(arr[0])
        break
    temp = arr.popleft()
    arr.append(temp)