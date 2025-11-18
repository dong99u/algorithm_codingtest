from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

t = int(input())

# 상 좌 하 우
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

pipe_dirs = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 3],
    5: [2, 3],
    6: [1, 2],
    7: [0, 1]
}

connectable = {
    0: [1, 2, 5, 6],
    1: [1, 3, 4, 5],
    2: [1, 2, 4, 7],
    3: [1, 3, 6, 7]
}

for test_case in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    q = deque([(r, c, 1)])
    visited[r][c] = True
    cnt = 1

    while q:
        x, y, time = q.popleft()

        if time >= l:
            break

        for dir_num in pipe_dirs[grid[x][y]]:
            nx, ny = x + dxs[dir_num], y + dys[dir_num]

            if not in_range(nx, ny):
                continue
            if grid[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue
            if grid[nx][ny] not in connectable[dir_num]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny, time + 1))
            cnt += 1

    print(f'#{test_case} {cnt}')