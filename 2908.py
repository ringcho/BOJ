N = list(map(str,input().split()))
for i,num in enumerate(N):
    N[i] = int(num[::-1])
if N[0]>N[1]:
    print(N[0])
else:
    print(N[1])
