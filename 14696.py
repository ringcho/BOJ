N = int(input())
for rd in range(N):
    result_a = [0]*4
    result_b = [0]*4
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = a[1:]
    b = b[1:]
    for i in range(4):
        result_a[i] = a.count(i+1)
        result_b[i] = b.count(i+1)
    i = 3
    while i >= 0:
        if result_a[i] > result_b[i]:
            print('A')
            i = -1
        elif result_b[i] > result_a[i]:
            print('B')
            i = -1
        elif i == 0:
            print('D')
            break
        i = i-1