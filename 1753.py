import heapq

def find_way(start):
    pq = []
    heapq.heappush(pq, (0, start,))
    D[start] = 0
    while pq:
        distance, fr = heapq.heappop(pq)

        if D[fr] < distance:
            continue

        for to, w in adj_list[fr]:
            n_distance = w
            if n_distance + distance < D[to]:
                D[to] = n_distance + distance
                heapq.heappush(pq, (n_distance + distance, to))


V, E = map(int, input().split())
start = int(input())
adj_list = [[] for _ in range(V+1)]
D = [10000000]*(V+1)
for i in range(E):
    fr, to, w = map(int, input().split())
    adj_list[fr].append((to, w))
find_way(start)
for i in range(1,V+1):
    if D[i] == 10000000:
        print('INF')
    else:
        print(D[i])