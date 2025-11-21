def check(strs):
    n = len(strs)
    if n == 1:
        return True
    for i in range(n // 2):
        if strs[i] != strs[n - i - 1]:
            return False
    return True

t = 10
for test_case in range(1, t + 1):
    n = int(input())
    grid = [list(input()) for _ in range(8)]

    answer = 0
    for i in range(8):
        for j in range(8 - n + 1):
            if check(''.join(grid[i][j:j + n])):
                answer += 1

    for j in range(8):
        for i in range(8 - n + 1):
            if check(''.join([grid[k][j] for k in range(i, i + n)])):
                answer += 1

    print(f'#{test_case} {answer}')