N = int(input())
arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(input().split())


for age in range(1,201):
    for person in arr:
        if age == int(person[0]):
            print(*person)