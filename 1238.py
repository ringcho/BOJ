import heapq
def dijk(s, D):
    pq = []
    heapq.heappush(pq, (0,s))
    while pq:
        distance, fr = heapq.heappop(pq)

        if D[fr] < distance:
            continue

        for to, w in adjlist[fr]:
            n_distance = w + distance
            if n_distance < D[to]:
                D[to] = n_distance
                heapq.heappush(pq, (n_distance, to))


V, E, goal = map(int, input().split())
adjlist = [[] for _ in range(V+1)]
for _ in range(E):
    fr, to, w = map(int, input().split())
    adjlist[fr].append((to, w))
D = [10000000]*(V+1)
dijk(goal, D)
max_v = 0
for i in range(1, V+1):
    if i == goal:
        pass
    else:
        new_D = [10000000]*(V+1)
        dijk(i, new_D)
        if max_v < D[i] + new_D[goal]:
            max_v = D[i] + new_D[goal]
print(max_v)