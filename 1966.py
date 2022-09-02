import sys
sys.stdin = open('1966_input.txt')

T = int(input())

def printq():
    cnt = 0
    while True:
        for i in range(N-cnt):
            if Q[0][0] < Q[i][0]:
                temp = Q.pop(0)
                Q.append(temp)
                break
        else:
            if Q[0][1] == M:
                cnt += 1
                return cnt
            else:
                Q.pop(0)
                cnt += 1

for tc in range(1,T+1):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    Q = [[0] for _ in range(N)]
    check = [False]*N
    for idx,pro in enumerate(priority):
        Q[idx] = [pro,idx]
    print(printq())