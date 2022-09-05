N = int(input())
arr = list(map(int, input().split()))

numbers = list(range(2, 1001))
for i in range(2, 33):
    for j, num in enumerate(numbers):
        if num == 0:
            pass
        elif num % i == 0 and num//i != 1:
            numbers[j] = 0
cnt = 0
for i in arr:
    if i in numbers:
        cnt += 1
print(cnt)