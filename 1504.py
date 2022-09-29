import sys
sys.stdin = open('1504_input.txt','r')
import heapq
def dijk(s, D):
    pq = []
    heapq.heappush(pq, (0, s))
    D[s] = 0
    while pq:
        distance, fr = heapq.heappop(pq)

        if D[fr] < distance:
            pass
        for to, w in adjlist[fr]:
            n_distance = w + distance
            if n_distance < D[to]:
                D[to] = n_distance
                heapq.heappush(pq, (n_distance, to))

V, E = map(int, input().split())
adjlist = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    adjlist[a].append((b,w))
    adjlist[b].append((a,w))
must1, must2 = map(int, input().split())
'''
1- must1, must1- must2, must2 - N
1 - must2, must2 - must1, must1 - N
'''
# case 1
D_1 = [10000000]*(V+1)
D_must2_N = [10000000]*(V+1)
D_must1_N = [10000000]*(V+1)

dijk(1, D_1)
dijk(must1, D_must1_N)
dijk(must2, D_must2_N)
# case 1 1->m1->m2->V
case_1 = D_1[must1] + D_must1_N[must2] + D_must2_N[V]
# case 2 1->m2->m1->V
case_2 = D_1[must2] + D_must2_N[must1] + D_must1_N[V]
res = min(case_1, case_2)

if res >= 10000000:
    print(-1)
else:
    print(res)