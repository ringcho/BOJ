import sys
sys.stdin = open('2116_input.txt')

pair = [5,3,4,1,2,0]
N = int(input())
ans = N
dices = [list(map(int, input().split()))for _ in range(N)]
for idx in range(6):
    cnt = 0
    bottom = idx
    top = pair[idx]
    copydice = dices[0].copy()
    copydice[bottom], copydice[top] = 0, 0
    cnt += max(copydice)
    for i in range(1,N):
        dice = dices[i].copy()
        for jdx in range(6):
            if dices[i-1][top] == dices[i][jdx]:
                bottom = jdx
        top = pair[bottom]
        dice[bottom], dice[top] = 0, 0
        cnt += max(dice)
    if cnt > ans:
        ans = cnt
print(ans)