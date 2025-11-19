def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):

    if memo[x][y] != 0:
        return memo[x][y]

    cnt = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if grid[nx][ny] != grid[x][y] + 1:
            continue

        cnt += dfs(nx, ny)

    memo[x][y] = cnt
    return cnt


t = int(input())

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

for test_case in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    memo = [[0] * n for _ in range(n)]

    answer = 0
    min_room = float('inf')
    for x in range(n):
        for y in range(n):
            cnt = dfs(x, y)
            if cnt > answer:
                answer = cnt
                min_room = grid[x][y]
            elif cnt == answer:
                min_room = min(min_room, grid[x][y])

    print(f'#{test_case} {min_room} {answer}')
