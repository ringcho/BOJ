N=int(input())
ans = 0
value = int(input())
for i in range(N):
    while value>0:
        ans += value%10
        value = value//10
    print(ans)

