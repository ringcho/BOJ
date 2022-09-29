import heapq

def find_money():
    pq = []
    heapq.heappush(pq, (maze[0][0], 0, 0))
    D[0][0] = maze[0][0]
    while pq:
        distance, i, j = heapq.heappop(pq)

        if D[i][j] < distance:
            continue

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                n_distance = maze[ni][nj] + distance
                if n_distance < D[ni][nj]:
                    D[ni][nj] = n_distance
                    heapq.heappush(pq, (n_distance, ni, nj))

cnt = 0
while True:
    cnt += 1
    N = int(input())
    if N == 0:
        break
    maze = [list(map(int, input().split())) for _ in range(N)]
    D = [[9*N**2]*N for _ in range(N)]
    find_money()
    print(f'Problem {cnt}: {D[N-1][N-1]}')