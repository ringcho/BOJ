def usecal(string):         # 후위 표기식을 계산
    stack = []
    operator = ['+', '-', '*', '/']
    for i in string:
        if i in operator:
            num1 = stack.pop()
            num2 = stack.pop()
            if num1 in alpha_to_num:
                num1 = float(alpha_to_num[num1])
            if num2 in alpha_to_num:
                num2 = float(alpha_to_num[num2])
        if i == '+':
            stack.append(num2 + num1)
        elif i == '*':
            stack.append(num2 * num1)
        elif i == '/':
            stack.append(num2 / num1)
        elif i == '-':
            stack.append(num2 - num1)
        else:
            stack.append(i)
    return stack[-1]

N = int(input())
large = list(map(chr, range(ord('A'), ord('Z')+1)))
alpha_to_num = {}
string1 = input()
for i in range(N):
    num = int(input())
    if large[i] not in alpha_to_num:
        alpha_to_num.update({large[i]:num})
res = usecal(string1)
print(f'{res:.2f}')