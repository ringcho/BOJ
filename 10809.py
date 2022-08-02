import string
s = input()
results = []
check = string.ascii_lowercase
for i in check:
    results.append(s.find(i))
for num in results:
    print(num,end=' ')

