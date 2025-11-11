for test_case in range(1, 10 + 1):
    n = int(input())
    arr = input()

    stack = []

    d = {
        '}': '{',
        ']': '[',
        ')': '(',
        '>': '<'
    }

    valid = True
    for s in arr:
        if s in '{[(<':
            stack.append(s)
        else:
            if stack:
                if stack[-1] == d[s]:
                    stack.pop()
                else:
                    valid = False
                    break

    if stack:
        valid = False

    print(f'#{test_case} {1 if valid else 0}')
