def stacknum():
    idx = 0
    jdx = 0
    result = ''
    while True:
        if stack and stack[-1] == ans[jdx]:
            stack.pop()
            jdx += 1
            result += '-'
        else:
            if idx == N:
                return 'NO'
            stack.append(numbers[idx])
            idx += 1
            result += '+'

        if jdx == N:
            return result

N = int(input())
numbers = list(range(1, N+1))
stack = []
ans = [0 for _ in range(N)]
for i in range(N):
    ans[i] = int(input())

res = stacknum()
if res == 'NO':
    print(res)
else:
    for i in res:
        print(i)



