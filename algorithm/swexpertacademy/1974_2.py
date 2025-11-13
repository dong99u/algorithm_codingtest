def is_valid(x, y):
    curr_num = arr[x][y]

    # 가로 방향 확인
    for j in range(n):
        if j != y and arr[x][j] == curr_num:
            return False

    # 세로 방향 확인
    for i in range(n):
        if i != x and arr[i][y] == curr_num:
            return False

    start_x = (x // 3) * 3
    start_y = (y // 3) * 3

    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if i != x and j != y and arr[i][j] == curr_num:
                return False

    return True


t = int(input())
n = 9

for test_case in range(1, t + 1):
    arr = [list(map(int, input().split())) for _ in range(n)]

    valid = True
    for i in range(n):
        for j in range(n):
            if not is_valid(i, j):
                valid = False
                break

        if not valid:
            break

    print(f'#{test_case} {1 if valid else 0}')