nums=[]
num = 1
ans_list =[]
dict_ans={}
for i in range(3):
    nums.append(int(input()))
for n in nums:
    num = n*num
while num > 0:
    ans_list.append(num%10)
    num = num//10
for number in ans_list:
    dict_ans[number] = dict_ans.get(number,0) + 1
for j in range(10):
    if j in dict_ans:
        print(dict_ans[j])
    else:
        print(0)