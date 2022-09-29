import heapq

def find_min_price(start, end):
    pq = []
    heapq.heappush(pq, (0,start))
    D[start] = 0
    while pq:
        distance, fr = heapq.heappop(pq)

        if D[fr] < distance:
            continue

        for to, w in adjlist[fr]:
            n_distance = w + distance
            if n_distance < D[to]:
                D[to] = n_distance
                heapq.heappush(pq, (n_distance, to))
    return D[end]

V = int(input())
E = int(input())
adjlist = [[] for _ in range(V+1)]
for _ in range(E):
    fr, to, w = map(int, input().split())
    adjlist[fr].append((to, w,))
D = [1000000000]*(V+1)
start, end = map(int, input().split())
res = find_min_price(start, end)
print(res)