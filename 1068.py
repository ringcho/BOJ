import sys
sys.stdin = open('1068_input.txt')

def dfs(n):
    global cnt
    if not adjlist[n]:
        cnt += 1
        return
    for j in range(len(adjlist[n])):
        if adjlist[n][j] == deletion_node:
            if len(adjlist[n]) == 1:
                cnt += 1
            else:
                continue
        else:
            dfs(adjlist[n][j])
N = int(input()) # number of nodes
par_of_node = list(map(int, input().split()))
adjlist = [[] for _ in range(N)]
for i, par in enumerate(par_of_node):
    if par == -1:
        root = i
    else:
        adjlist[par].append(i)
deletion_node = int(input())
'''
tree니까 밑에 있는 것들을 0으로 만든다음
'''
# adjlist[deletion_node] = []
cnt = 0
if root == deletion_node:
    print(0)
else:
    dfs(root)
    print(cnt)