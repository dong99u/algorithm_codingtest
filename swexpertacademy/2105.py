def check_path(sx, sy, d1, d2):
    visited_nums = set()

    x, y = sx, sy

    for _ in range(d1):
        x, y = x + 1, y + 1
        if not (0 <= x < n and 0 <= y < n):
            return 0
        if arr[x][y] in visited_nums:
            return 0
        visited_nums.add(arr[x][y])

    for _ in range(d2):
        x, y = x + 1, y - 1
        if not (0 <= x < n and 0 <= y < n):
            return 0
        if arr[x][y] in visited_nums:
            return 0
        visited_nums.add(arr[x][y])

    for _ in range(d1):
        x, y = x - 1, y - 1
        if not (0 <= x < n and 0 <= y < n):
            return 0
        if arr[x][y] in visited_nums:
            return 0
        visited_nums.add(arr[x][y])

    for _ in range(d2):
        x, y = x - 1, y + 1
        if not (0 <= x < n and 0 <= y < n):
            return 0
        if arr[x][y] in visited_nums:
            return 0
        visited_nums.add(arr[x][y])

    if x == sx and y == sy:
        return len(visited_nums)

    return 0


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 0

    # 모든 시작점 시도
    for sx in range(n):
        for sy in range(n):
            for d1 in range(1, n):
                for d2 in range(1, n):
                    cnt = check_path(sx, sy, d1, d2)
                    answer = max(answer, cnt)

    print(f'#{test_case} {answer if answer > 0 else -1}')