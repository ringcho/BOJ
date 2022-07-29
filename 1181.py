N = int(input())
word_list =[]
for i in range(N):
    word = input()
    if [len(word),word] not in word_list:
        word_list.append([len(word),word])
word_list.sort()
word_list = [y for [x,y] in word_list]

print(*word_list, sep='\n')