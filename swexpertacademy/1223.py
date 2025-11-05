d = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}

for test_case in range(1, 10 + 1):
    n = int(input())

    expression = input()
    stack = []

    answers = []
    for elem in expression:
        if elem.isdigit():
            answers.append(elem)
        else:
            if not stack or d[stack[-1]] < d[elem]:
                stack.append(elem)

            else:
                while len(stack) != 0 and d[stack[-1]] >= d[elem]:
                    answers.append(stack.pop())
                stack.append(elem)

    while stack:
        answers.append(stack.pop())

    for i in range(len(answers)):
        if answers[i].isdigit():
            stack.append(int(answers[i]))
        else:
            b = stack.pop()
            a = stack.pop()
            result = 0
            if answers[i] == '+':
                result = a + b
            elif answers[i] == '-':
                result = a - b
            elif answers[i] == '*':
                result = a * b
            else:
                result = a / b

            stack.append(result)

    print(f'#{test_case} {stack.pop()}')


