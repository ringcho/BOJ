import sys
def find_p(x):
    while x != p[x]:
        x = p[x]
    return x

V, E = map(int, sys.stdin.readline().split())

p = [x for x in range(V+1)]
adjlist = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]
adjlist.sort(key=lambda x:x[2])
cnt, total, res = 0, 0, 0
for v, e, w in adjlist:
    if find_p(v) != find_p(e):
        cnt += 1
        total += w
        p[find_p(e)] = find_p(v)
        res = w
        if cnt == V-1:
            break
print(total-res)