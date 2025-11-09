def is_valid(x, y):
    num = board[x][y]

    for i in range(n):
        if i == x:
            continue
        if board[i][y] == num:
            return False

    for j in range(n):
        if j == y:
            continue
        if board[x][j] == num:
            return False

    start_x = (x // 3) * 3
    start_y = (y // 3) * 3

    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):

            if i == x and j == y:
                continue

            if board[i][j] == num:
                return False

    return True

t = int(input())

for test_case in range(1, t + 1):
    n = 9
    board = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    valid = True
    for i in range(n):
        for j in range(n):
            if not is_valid(i, j):
                valid = False
                break
        if not valid:
            break

    print(f'#{test_case} {1 if valid else 0}')
