N, K = map(int,input().split())

visited = [0]*(N+1)
number = list(range(N+1))
res = []
idx = 0
while True:
    idx = idx + K
    idx = idx % N
    while True: