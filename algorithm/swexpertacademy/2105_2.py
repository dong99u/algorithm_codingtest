def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(sx, sy, d1, d2):
    x, y = sx, sy
    visited = set()

    for _ in range(d1):
        x += 1
        y += 1
        if not in_range(x, y):
            return -1
        if maps[x][y] in visited:
            return -1
        visited.add(maps[x][y])

    for _ in range(d2):
        x += 1
        y -= 1
        if not in_range(x, y):
            return -1
        if maps[x][y] in visited:
            return -1
        visited.add(maps[x][y])

    for _ in range(d1):
        x -= 1
        y -= 1
        if not in_range(x, y):
            return -1
        if maps[x][y] in visited:
            return -1
        visited.add(maps[x][y])

    for _ in range(d2):
        x -= 1
        y += 1
        if not in_range(x, y):
            return -1
        if maps[x][y] in visited:
            return -1
        visited.add(maps[x][y])

    if x == sx and y == sy:
        return len(visited)

    return -1



t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    answer = -1
    for sx in range(n):
        for sy in range(n):
            for d1 in range(1, n):
                for d2 in range(1, n):
                    answer = max(answer, dfs(sx, sy, d1, d2))

    print(f'#{test_case} {answer}')