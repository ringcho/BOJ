N,X = map(int,input().split())
nums = list(map(int,input().split()))
a = []
for num in nums:
    if num < X:
        a.append(num)
for i in a:
    print(i, end=' ')

