num_of_students = int(input())
arr = []
orders = list(map(int, input().split()))
for i in range(num_of_students):
    if orders[i] == 0:
        arr.append(i+1)
    else:
        arr.insert(-orders[i], i+1)
print(*arr)