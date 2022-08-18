
bingo_list = [[] for _ in range(5)]
ans_list = [[] for _ in range(5)]
for i in range(5):
    bingo_list[i] = list(map(int, input().split()))

for i in range(5):
    ans_list[i] = list(map(int, input().split()))

num = []
flag = 0
for i in range(5):
    for j in range(5):
        num.append(ans_list[i][j])
while flag ==0 :
    for k,ans in enumerate(num):
        cnt = 0
        crsline1 = []
        crsline2 = []
        for i in range(5):
            for j in range(5):
                if ans == bingo_list[i][j]:
                    bingo_list[i][j] = 0
                if i == j:
                    crsline1.append(bingo_list[i][j])
                if i + j == 4:
                    crsline2.append(bingo_list[i][j])
        bingoT = list(zip(*bingo_list))

        for i in range(5):
            if sum(bingo_list[i]) == 0:
                cnt += 1
            if sum(bingoT[i]) == 0:
                cnt += 1
        if sum(crsline1) == 0:
            cnt += 1
        if sum(crsline2) == 0:
            cnt += 1

        if cnt >= 3:
            print(k+1)
            flag = 1
            break








# for i in range(5):
#     for j in range(5):
#         num = ans_list[i][j]
#         for y in range(5):
#             for x in range(5):
#                 if num == bingo_list[y][x]:
#                     bingo_list[y][x] = 0
#         bingoT = list(zip(*bingo_list))
#         if sum(bingo_list[i]) == 0:
#             cnt += 1
#         elif sum(bingoT[i]) == 0:
#             cnt += 1
#


