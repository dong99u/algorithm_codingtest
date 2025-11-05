from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_move(x, y):
    return maps[x][y] != 1

for test_case in range(1, 10 + 1):
    t = int(input())
    n = 16

    maps = [
        list(map(int, list(input())))
        for _ in range(n)
    ]

    start_x, start_y = 0, 0
    dest_x, dest_y = 0, 0

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 2:
                start_x, start_y = i, j
            if maps[i][j] == 3:
                dest_x, dest_y = i, j

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    q = deque([(start_x, start_y)])

    visited = [[False] * n for _ in range(n)]

    is_arrived = False

    while q:
        curr_x, curr_y = q.popleft()

        if curr_x == dest_x and curr_y == dest_y:
            is_arrived = True
            break

        visited[curr_x][curr_y] = True

        for dx, dy in zip(dxs, dys):
            nx = curr_x + dx
            ny = curr_y + dy

            if not in_range(nx, ny):
                continue
            if not can_move(nx, ny):
                continue
            if visited[nx][ny]:
               continue

            q.append((nx, ny))

    answer = 1 if is_arrived else 0

    print(f'#{test_case} {answer}')
