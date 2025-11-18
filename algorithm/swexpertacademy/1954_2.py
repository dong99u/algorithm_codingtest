def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir_num = 0

    grid = [[0] * n for _ in range(n)]

    x, y = 0, 0
    for num in range(1, n * n + 1):
        grid[x][y] = num

        nx, ny = x + dx[dir_num], y + dy[dir_num]

        if not in_range(nx, ny) or grid[nx][ny] != 0:
            dir_num = (dir_num + 1) % 4
            nx, ny = x + dx[dir_num], y + dy[dir_num]

        x, y = nx, ny

    print(f'#{test_case}')
    for row in grid:
        for num in row:
            print(num, end=' ')
        print()