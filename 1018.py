import sys
sys.stdin = open('1018_input.txt')

T = int(input())

for tc in range(1,T+1):
    M, N = map(int, input().split())
    chess = [list(map(str, input())) for _ in range(M)]
    p1 = [
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ]
    p2 = [
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ]
    minchess = 64
    for i in range(M-8+1):
        for j in range(N-8+1):
            cnt1, cnt2 = 0, 0
            for y in range(8):
                for x in range(8):
                    if chess[i+y][j+x] != p1[y][x]:
                        cnt1 += 1
                    if chess[i+y][j+x] != p2[y][x]:
                        cnt2 += 1
            if min(cnt1,cnt2) < minchess:
                minchess = min(cnt1,cnt2)
    print(minchess)