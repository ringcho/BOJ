import sys
sys.stdin = open('10250_input.txt')


T = int(input())
for tc in range(T):
    H, W, N = map(int,input().split())
    if N % H == 0:
        floor = H
        room = N//H
    else:
        floor = N % H
        room = N//H+1
    if room < 10:
        print(f'{floor}0{room}')
    else:
        print(f'{floor}{room}')