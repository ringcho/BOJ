K,N = map(int,input().split())
length_K = []
middle = 1
for i in range(K):
    length_K.append(int(input()))
'''
for length in range(1,(max(length_K)+1)):
    cnt = 0
    for j in length_K:
        cnt += j//(length)
    if cnt < N:
        print(length-1)
        break
시간초과로 실패
'''           
while True:
    cnt = 0
    for j in length_K:
        cnt += j//middle
    if cnt == N:
        print(middle)
        break
    elif cnt > N :
        middle = round((middle+max(length_K))/2)
        print(middle)
    elif cnt < N:
        middle = round((1+middle)/2)
        print(middle)

    
