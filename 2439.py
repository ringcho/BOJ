from audioop import reverse


N = int(input())
for i in reversed(range(N)):
    for j in range(i):
        print(' ',end='')
    print('*' * (N-i))


    