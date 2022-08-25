import sys
sys.stdin = open('2304_input.txt')

'''
max 찾고 좌우 나눠서
max2 찾고 사이에 다 0으로 만들고 res + 
다음 max 찾고 max 가 0이 될때 까지
'''

N = int(input()) # 기둥의 개수
res = 0
# 기둥을 저장할 배열 arr
arr = [0 for _ in range(N)]
calculated = [0 for _ in range(1001)]
stack = []
# N개의 줄에 기둥의 위치 L 높이 H
for i in range(N):

    L, H = map(int, input().split())
    arr[i] = [L, H]

for i in range(N):
    maxh = []

print(stack)

