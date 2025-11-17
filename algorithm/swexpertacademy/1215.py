def check(strs):
    n = len(strs)
    if n == 1:
        return True

    for i in range(n // 2):
        if strs[i] != strs[n - 1 - i]:
            return False

    return True

t = 10
for test_case in range(1, t + 1):
    n = 8
    k = int(input())
    arr = [input() for _ in range(n)]

    answer = 0

    for i in range(n):
        for j in range(n - k + 1):
            if check(arr[i][j:j + k]):
                answer += 1

    for j in range(n):
        for i in range(n - k + 1):
            col = [arr[i + di][j] for di in range(k)]
            if check(col):
                answer += 1

    print(f'#{test_case} {answer}')

