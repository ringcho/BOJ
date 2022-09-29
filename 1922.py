def find_p(x):
    while x != p[x]:
        x = p[x]
    return x
def union(x,y):
    p[find_p(y)] = find_p(x)

V = int(input())
E = int(input())
adjlist = [list(map(int, input().split())) for _ in range(E)]
adjlist.sort(key=lambda x:x[2])
p = [0]*(V+1)
for i in range(1,V+1):
    p[i] = i
cnt, total = 0, 0
for v, e, w in adjlist:
    if find_p(v) != find_p(e):
        cnt += 1
        total += w
        union(v, e)
        if cnt == V - 1:
            break
print(total)