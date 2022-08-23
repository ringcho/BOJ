K = int(input())
len_list = []
direction = []
large = []

for i in range(6):
    len_list.append(list(map(int, input().split())))
    direction.append(len_list[i][0])

len_list = len_list*2
direction = direction*2

for i in range(12-4+1):
    if direction[i] == direction[i+2] and direction[i+1] == direction[i+3]:
        small = [len_list[i+1][1], len_list[i+2][1]]
        break
for i in range(1, 5):
    if direction.count(i) == 2:
        for num in len_list:
            if num[0] == i:
                large.append(num[1])
                break

print((large[0]*large[1]-small[0]*small[1])*K)