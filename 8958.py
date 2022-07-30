N = int(input())
test_case = []
for i in range(N):
    test_case.append(input())
for line in test_case:
    cnt = 0
    result = 0
    if line[0] == 'O':
        cnt = 1
        result = 1
    for i,ox in enumerate(line,start=1):
        if i == len(line):
            break
        if line[i-1] == line[i]:
            cnt += 1
            if line[i] == 'X':
                cnt = 0
        elif line[i] == 'O':
            cnt = 1
        else :
            cnt = 0
        result += cnt
    print(result)
        
    