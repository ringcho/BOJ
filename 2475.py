N = map(int,input().split())
N = list(N)
results = 0
for i in N:
    results += i**2
results = results%10
print(results)