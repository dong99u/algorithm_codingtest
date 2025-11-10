def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    count = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if board[nx][ny] - board[x][y] != 1:
            continue

        count += dfs(nx, ny)

    return count


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    board = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    max_cnt = 0
    min_room_num = float('inf')

    for x in range(n):
        for y in range(n):
            cnt = dfs(x, y)
            room_num = board[x][y]

            if cnt > max_cnt:
                max_cnt = cnt
                min_room_num = room_num  # 새로운 최대값이면 무조건 갱신!
            elif cnt == max_cnt:  # 같을 때만 최소값 비교
                min_room_num = min(min_room_num, room_num)


    print(f'#{test_case} {min_room_num} {max_cnt}')


