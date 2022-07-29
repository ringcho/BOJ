import sys
word = sys.stdin.readline()
word = word.upper()
word = ' '.join(f"{word}")
alphabets = word.split()
alpha_list = []
for i in alphabets:
    if [alphabets.count(i),i] not in alpha_list:
        alpha_list.append([alphabets.count(i),i])
alpha_list.sort(reverse=True)
if alpha_list[0][0] == alpha_list[1][0]:
    print('?')
else:
    print(alpha_list[0][1])

    
