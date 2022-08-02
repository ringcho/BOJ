n = []
temp = []
for i in range(10):
    n.append(int(input()))
for num in n:
    temp.append(num%42)
a = set(temp)
print(len(a))