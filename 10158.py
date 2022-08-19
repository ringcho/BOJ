w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

if ((p+t)//w) % 2:          # 벽을 찍을 때 마다 방향이 바뀌는 것을 표현
    x = w - ((p+t) % w)     # 벽을 한번, 세번 째 찍을 때 dx = -1
else:
    x = (p+t) % w

if ((q+t)//h) % 2:         # 벽을 한번, 세번 찍을 때 dy = -1
    y = h - ((q+t) % h)
else:
    y = (q+t) % h

print(x, y)
