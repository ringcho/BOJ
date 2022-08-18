N = int(input())


max_arr =[N]
for i in range(1,N+1):
    arr = [N]
    arr.append(i)
    while True:
        x = arr[-2] - arr[-1]
        if x >= 0:
            arr.append(x)
        else:
            break
    if len(arr) > len(max_arr):
        max_arr = arr

print(len(max_arr))
print(*max_arr)