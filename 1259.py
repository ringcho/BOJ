while True :
    n = int(input())
    if n == 0:
        False
        break
    prd_check=[]
    output = 'yes'
    while n >=1:
        prd_check.append(n%10)
        n = n//10
    for i,num in enumerate(prd_check, start=1):
        if num == prd_check[-i]:
            output = 'yes'
        else :
            output = 'no'
            break
    print(output)
