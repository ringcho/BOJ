N = int(input())
arr_N = list(map(int, input().split()))
M = int(input())
arr_M = list(map(int, input().split()))
'''
5
4 1 5 2 3
5
1 3 7 9 5
'''
def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        c = int((start+end)//2)
        if arr[c] == num:
            return arr[c]
            break
        elif arr[c] > num:
            end = c - 1
        elif arr[c] < num:
            start = c + 1

    return 0
arr_N.sort()

for i in arr_M:
    if binary_search(arr_N, i):
        print(1)
    else:
        print(0)