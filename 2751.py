import sys
sys.stdin = open('2751_input.txt')

N = int(input())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())

arr.sort()

for i in arr:
    print(i)