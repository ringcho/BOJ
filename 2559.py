N, K = map(int, input().split())
arr_temp = list(map(int, input().split()))

temp_sum = sum(arr_temp[0:K]) #01234
max_sum = -100*N
if temp_sum > max_sum:
    max_sum = temp_sum

for i in range(1, N-K+1):
    temp_sum = temp_sum - arr_temp[i-1] + arr_temp[i+K-1] #12345
    if temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)