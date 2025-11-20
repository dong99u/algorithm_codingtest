def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def check(start_x, start_y, d1, d2):
    global answer

    path = set()

    x, y = start_x, start_y
    for _ in range(d1):
        x += 1
        y += 1
        if not in_range(x, y):
            return
        if grid[x][y] in path:
            return
        path.add(grid[x][y])
    for _ in range(d2):
        x += 1
        y -= 1
        if not in_range(x, y):
            return
        if grid[x][y] in path:
            return
        path.add(grid[x][y])
    for _ in range(d1):
        x -= 1
        y -= 1
        if not in_range(x, y):
            return
        if grid[x][y] in path:
            return
        path.add(grid[x][y])
    for _ in range(d2):
        x -= 1
        y += 1
        if not in_range(x, y):
            return
        if grid[x][y] in path:
            return
        path.add(grid[x][y])

    if x == start_x and y == start_y:
        answer = max(answer, len(path))
        return


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for x in range(n):
        for y in range(n):
            for d1 in range(1, n):
                for d2 in range(1, n):
                    check(x, y, d1, d2)

    print(f'#{test_case} {answer if answer != 0 else -1}')