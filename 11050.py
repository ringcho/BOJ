import sys
sys.setrecursionlimit(10000)
N, K = map(int, input().split())
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
res = factorial(N)/(factorial(N-K)*factorial(K))
print(int(res))