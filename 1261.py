import sys
sys.stdin = open('1261_input.txt','r')
import heapq

def find_exit():
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    D[0][0] = 0
    while pq:
        distance, y, x = heapq.heappop(pq)

        if D[y][x] < distance:
            continue

        for dy, dx in [[0,1],[1,0],[0,-1],[-1,0]]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if maze[ny][nx] == '1':
                    n_distance = distance + 1
                else:
                    n_distance = distance
                if n_distance < D[ny][nx]:
                    D[ny][nx] = n_distance
                    heapq.heappush(pq, (n_distance, ny, nx))

M, N = map(int, input().split())
maze = [list(input()) for _ in range(N)]
D = [[N*M+1]*M for _ in range(N)]
find_exit()
print(D[N-1][M-1])