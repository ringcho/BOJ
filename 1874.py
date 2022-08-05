import random
N = int(input())
#list_n=random.sample(range(-2**31,2**31),N)
list_n = list(map(int,input().split()))
list_n.sort()
M = int(input())
#list_m=random.sample(range(-2**31,2**31),M)
list_m = list(map(int,input().split()))
center = round(len(list_n)//2)

for i in list_m:
    cnt = 0
    while True:
        cnt += 1
        v = list_n[center]
        if v == i:
            print(1)
            break
        elif v < i:
            center = round((center + len(list_n))//2)
        elif v > i:
            center = round(((center + 0))//2)
        if cnt >= 21:
            print(0)
            break

    

