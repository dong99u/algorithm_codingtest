def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir_num = 0

    board = [[0] * N for _ in range(N)]
    x = y = 0
    for i in range(1, N * N + 1):
        board[x][y] = i

        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

        if not in_range(nx, ny) or board[nx][ny] != 0:
            dir_num = (dir_num + 1) % 4
            nx = x + dx[dir_num]
            ny = y + dy[dir_num]

        x = nx
        y = ny

    print(f'#{test_case}')
    for row in board:
        print(*row)

