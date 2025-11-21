from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q:
        cx, cy = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy

            if not in_range(nx, ny):
                continue
            if grid[nx][ny] == 1:
                continue
            if visited[nx][ny]:
                continue

            if nx == end_x and ny == end_y:
                return True

            q.append((nx, ny))
            visited[nx][ny] = True
    return False

for test_case in range(1, 10 + 1):
    t = int(input())
    n = 16
    grid = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[False] * (n + 1) for _ in range(n + 1)]

    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                start_x, start_y = i, j
            if grid[i][j] == 3:
                end_x, end_y = i, j

    valid = bfs()

    answer = 1 if valid else 0

    print(f'#{test_case} {answer}')
