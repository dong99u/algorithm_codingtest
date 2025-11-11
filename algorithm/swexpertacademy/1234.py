for test_case in range(1, 10 + 1):
    arr = list(input().split())
    n = int(arr[0])
    arr = arr[1]
    arr = list(map(int, list(arr)))

    stack = []

    for i in range(n):
        if not stack:
            stack.append(arr[i])
        else:
            if stack[-1] == arr[i]:
                stack.pop()
            else:
                stack.append(arr[i])

    print(f'#{test_case} {"".join(map(str, stack))}')