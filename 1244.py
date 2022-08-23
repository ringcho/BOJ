N = int(input())

switch = [0] + list(map(int, input().split()))

r_num = int(input())

for _ in range(r_num):
    gender, idx = map(int, input().split())
    if gender == 1:
        for i in range(1,N+1):
            if switch[i]:
                switch[i] = 0
            else:
                switch[i] = 1
    else:
        while True:
            x = 1
            if
