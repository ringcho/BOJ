import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        if q:
            res = q.popleft()
            print(res)
        else:
            print('-1')
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if not q:
            print('1')
        else:
            print('0')
    elif order[0] == 'front':
        if q:
            print(q[0])
        else:
            print('-1')
    elif order[0] == 'back':
        if q:
            print(q[-1])
        else:
            print('-1')
