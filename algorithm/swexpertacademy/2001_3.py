t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    p = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            p[i][j] = p[i][j - 1] + p[i - 1][j] - p[i - 1][j - 1] + grid[i - 1][j - 1]

    answer = 0

    for x1 in range(1, n - m + 2):
        for y1 in range(1, n - m + 2):
            x2, y2 = x1 + m - 1, y1 + m - 1

            answer = max(answer, p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1])

    print(f'#{test_case} {answer}')
