import sys
sys.stdin = open('1244_input.txt')

N = int(input())

switch = [0] + list(map(int, input().split()))

r_num = int(input())

for _ in range(r_num):
    gender, idx = map(int, input().split())
    if gender == 1:
        for i in range(1,(N+1)//idx+1):
            if i*idx<=N:
                if switch[i*idx]:
                    switch[i*idx] = 0
                else:
                    switch[i*idx] = 1
    else:
        x = 0
        while True:
            if 1<= idx-x and idx+x<=N:
                if switch[idx-x] == switch[idx+x]:
                    if switch[idx-x] == 1:
                        switch[idx-x], switch[idx+x] = 0, 0

                    else:
                        switch[idx-x], switch[idx+x] = 1, 1

                    x += 1
                else:
                    break
            else:
                break
switch.pop(0)
cnt = 0
for i in switch:
    print(i, end=' ')
    cnt += 1
    if cnt == 20:
        print()
        cnt = 0

