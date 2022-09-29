from collections import deque

def find_brother(start, end):
    q = deque()
    q.append((start, 0))
    visited[start] = True
    while q:
        v, time = q.popleft()
        if v == end:
            return time
        for w in [v+1, v-1, v*2]:
            if 0 <= w <= 100000:
                if not visited[w]:
                    visited[w] = True
                    if w == v*2:
                        q.appendleft((w, time))
                    else:
                        q.append((w, time+1))
visited = [0 for _ in range(10000001)]
N, K = map(int, input().split())
res = find_brother(N, K)
print(res)
