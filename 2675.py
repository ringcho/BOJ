T = int(input())
lines = []
for i in range(T):
    inputs = input().split()
    lines.append(inputs)
for inputs in lines:
    rep = int(inputs[0])
    word = ' '.join(inputs[1])
    alphabets = word.split()
    for alpha in alphabets:
        print(alpha * rep, end='')
    print(' ')


    
