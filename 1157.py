import sys
word = sys.stdin.readline()
word = word.upper()
word = ' '.join(f"{word}")
alphabets = word.split()
alpha_list = list()
for i in alphabets:
    cnt =alphabets.count(i)
    alpha_list.append(cnt)
if alpha_list.count(max(alpha_list))>1:
    print('?')
else:
    max_index = alphabets.index(max(alpha_list))
    print(alphabets[max_index])

    
