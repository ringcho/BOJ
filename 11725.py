import sys
sys.stdin = open('11725_input.txt')
from collections import deque

def bfs(n):
    visited[n] = 1
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        for w in adjlist[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                res[w] = v
                bfs(w)
T = int(input())
for tc in range(T):
    N = int(input())
    adjlist = [[] for _ in range(N+1)]
    for i in range(N-1):
        a, b = map(int, input().split())
        adjlist[a].append(b)
        adjlist[b].append(a)
    visited = [0]*(N+1)
    res = [0]*(N+1)
    bfs(1)
    for i in range(2,N+1):
        print(res[i])