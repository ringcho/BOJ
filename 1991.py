import sys
sys.stdin = open('1991_input.txt')


def preorder(n):
    if n:
        pro.append(chr(n+64))
        preorder(branch_l[n])
        preorder(branch_r[n])

def inorder(n):
    if n:
        inorder(branch_l[n])
        io.append(chr(n+64))
        inorder(branch_r[n])

def postorder(n):
    if n:
        postorder(branch_l[n])
        postorder(branch_r[n])
        pso.append(chr(n+64))

N = int(input())
branch_l = [0]*27
branch_r = [0]*27
pro, io, pso = [], [], []




for _ in range(N):
    adj_node = list(input().split())
    idx = ord(adj_node[0])-64
    if adj_node[1] != '.':
        branch_l[idx] = ord(adj_node[1])-64
    if adj_node[2] != '.':
        branch_r[idx] = ord(adj_node[2])-64


preorder(1)
inorder(1)
postorder(1)

for alpha in pro:
    print(alpha, end='')
print()
for alpha in io:
    print(alpha, end='')
print()
for alpha in pso:
    print(alpha, end='')

