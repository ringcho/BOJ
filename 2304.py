import sys
sys.stdin = open('2304_input.txt')

res = 0

# 기둥의 개수
N = int(input())

# 기둥을 저장할 배열 arr
arr = [0 for _ in range(1001)]

# N개의 줄에 기둥의 위치 L 높이 H
for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H

idx = 0
for i in range(1001):

    if arr[i] > arr[idx]:
        res += arr[idx]*(i-idx)
        idx = i
        if arr[idx] == max(arr):
            res += arr[idx]
            break
stack = []
for i in range(idx+1, 1001):

    if stack and stack[-1][1] > arr[i] and arr[i]:
        res += arr[i]*abs(stack[-1][0]-i)
        stack.pop()
    else:
        if arr[i]:
            stack.append([i, arr[i]])
    if i == 1000:
        res += stack[-1][1]*(stack[-1][0]-idx)

print(res)