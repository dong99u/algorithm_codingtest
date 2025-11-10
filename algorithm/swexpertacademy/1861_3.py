def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    if memo[x][y] != -1:
        return memo[x][y]

    count = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if rooms[nx][ny] != rooms[x][y] + 1:
            continue

        count += dfs(nx, ny)

    memo[x][y] = count

    return count + 1

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]

    memo = [[-1] * n for _ in range(n)]

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]


    max_cnt = 0
    min_room_num = float('inf')

    for i in range(n):
        for j in range(n):
            cnt = dfs(i, j)

            if max_cnt < cnt:
                max_cnt = cnt
                min_room_num = rooms[i][j]
            elif max_cnt == cnt:
                min_room_num = min(min_room_num, rooms[i][j])


    print(f'#{test_case} {max_cnt} {min_room_num}')
