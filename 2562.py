ans_list = [0,0,0,0,0,0,0,0,0]
for i in range(9):
    ans_list[i] = int(input())
big = max(ans_list)
print(big)
print(f'{ans_list.index(big)+1}')