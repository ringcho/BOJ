given_time = list(map(int,input().split()))
if given_time[1] <45:
    temp = 45-given_time[1]
    given_time[1] = 60-temp
    if given_time[0] == 0:
        given_time[0] = 23
    else:
        given_time[0] -= 1
else:
    given_time[1] -= 45
print(given_time[0],given_time[1])