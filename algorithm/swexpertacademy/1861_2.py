def dfs(x, y):

    if memo[x][y] != -1:
        return memo[x][y]

    count = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if rooms[nx][ny] != rooms[x][y] + 1:
            continue

        count += dfs(nx, ny)

    memo[x][y] = count
    return count


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    memo = [[-1] * n for _ in range(n)]

    max_cnt = 0
    min_room_num = float('inf')

    for x in range(n):
        for y in range(n):
            cnt = dfs(x, y)

            if cnt > max_cnt:
                max_cnt = cnt
                min_room_num = rooms[x][y]
            elif cnt == max_cnt:
                min_room_num = min(min_room_num, rooms[x][y])