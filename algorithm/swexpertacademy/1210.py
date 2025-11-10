def dfs(x, y):
    while x < n - 1:
        if y + 1 < n and ladder[x][y + 1] == 1:
            while y + 1 < n and ladder[x][y + 1] != 0:
                y += 1
        elif y - 1 > 0 and ladder[x][y - 1] == 1:
            while y - 1 >= 0 and ladder[x][y - 1] != 0:
                y -= 1
        x += 1

    if x == n - 1 and y == end_y:
        return True
    else:
        return False

for test_case in range(1, 10 + 1):
    t = int(input())
    n = 100
    ladder = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    start_points = []

    for i in range(n):
        if ladder[0][i] == 1:
            start_points.append((0, i))

    end_y = ladder[-1].index(2)

    for start_x, start_y in start_points:
        if dfs(start_x, start_y):
            print(f'#{test_case} {start_y}')
            break

