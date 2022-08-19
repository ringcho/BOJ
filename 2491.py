N = int(input())

arr = list(map(int, input().split()))

stack = [arr[0]]
long = 0
for i in range(1, N):
    if arr[i] >= stack[-1]:
        stack.append(arr[i])
    else:
        if len(stack) > long:
            long = len(stack)
        stack = [arr[i]]
if len(stack) > long:
    long = len(stack)
stack = [arr[0]]
for i in range(1, N):
    if arr[i] <= stack[-1]:
        stack.append(arr[i])
    else:
        if len(stack) > long:
            long = len(stack)
        stack = [arr[i]]
if len(stack) > long:
    long = len(stack)

print(long)