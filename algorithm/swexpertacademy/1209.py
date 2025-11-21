for test_case in range(1, 10 + 1):
    t = int(input())
    n = 100
    grid = [list(map(int, input().split())) for _ in range(n)]

    result = []
    for row in grid:
        result.append(sum(row))

    for col in zip(*grid):
        result.append(sum(col))

    sum_val = 0
    for i in range(n):
        sum_val += grid[i][i]
    result.append(sum_val)

    sum_val = 0
    for i in range(n):
        sum_val += grid[n - i - 1][i]
    result.append(sum_val)

    print(f'#{test_case} {max(result)}')