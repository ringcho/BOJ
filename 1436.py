N = int(input())
cnt = 0
for i in range(N*1000):
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        break
