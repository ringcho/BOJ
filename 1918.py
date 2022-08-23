def makecal(string):            # 후위 표기식 만들기
    stack = []                  # 연산자들을 담을 stack
    isp = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    icp = {
        '(': 3,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }                      # 연산자들의 우선순위
    result = ''            # return할 후위표기식
    for i in string:       # 문자열 안에서
        if i in icp:       # 연산자를 만나면
            if stack and icp[i] <= isp[stack[-1]]:        # stack이 존재하고 입력되는 문자의 우선순위가 stack에 저장된 우선순위 보다 낮다면
                while icp[i] <= isp[stack[-1]]:           # 계속 stack맨위와 입력된 연산자의 우선순위를 비교
                    result += stack.pop()                           # 입력된 우선순위가 높으면 계속 pop
                    if not stack:                                   # 하다가 stack이 없어지면 break
                        break
                stack.append(i)                                     # 우선순위 높은거 다 없어지면 i를 append
            else:                                      # 처음부터 우선순위가 기존보다 높으면 append
                stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            result += i
    while stack:                                                     # string을 다 돌고 stack에 연산자가 남아 있으면
        result += stack.pop()
    return result

string1 = input()
print(makecal(string1))