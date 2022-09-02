'''
나무 높이에 대해 binary search로 해도?
백만*
'''
def length(h):
    height = 0
    for tree in trees:
        if tree > h:
            height += tree - h
    return height

N, M = map(int, input().split())
trees = list(map(int, input().split()))
r = max(trees)
l = 0
h = (r+l)//2

while l<=r:
    if length(h) == M:
        print(h)
        break
    elif length(h) < M:
        r = h-1
        h = (r + l) // 2
    elif length(h) > M:
        l = h+1
        h = (r + l) // 2
if length(h) == M:
    pass
else:
    print(h)