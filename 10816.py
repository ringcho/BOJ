N = int(input())
num_list = list(map(int, input().split()))
num_dict = {}
for i in num_list:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1
M = int(input())
how_many = list(map(int, input().split()))

for num in how_many:
    try:
        print(num_dict[num], end=' ')
    except:
        print(0, end=' ')