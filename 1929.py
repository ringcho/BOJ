import math
def check_prime(N):
    if N == 1:
        return False

    for i in range(2, round(math.sqrt(N))+1):
        if N % i == 0:
            return False
            break
    return True

N, M = map(int, input().split())

for j in range(N, M+1):
    if check_prime(j):
        print(j)




