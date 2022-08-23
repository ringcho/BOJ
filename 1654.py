def find_max_length(arr, N):
    l = 1
    r = max(arr)
    while l <= r:
        len = (l + r) // 2
        cnt = 0
        for i in arr:
            cnt += i//len
        if cnt >= N:
            l = len + 1
        elif cnt < N:
            r = len - 1
    return r

K, N = map(int, input().split())
lan = [0 for _ in range(K)]
for i in range(K):
    lan[i] = int(input())

res = find_max_length(lan, N)
print(res)
