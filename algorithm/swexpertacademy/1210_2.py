def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    while True:
        if y > 0 and maps[x][y - 1] == 1:
            while y > 0 and maps[x][y - 1] == 1:
                y -= 1
        elif y < n - 1 and maps[x][y + 1] == 1:
            while y < n - 1 and maps[x][y + 1] == 1:
                y += 1
        x += 1

        if x == n - 1:
            break

    return True if maps[x][y] == 2 else False


for test_case in range(1, 10 + 1):
    t = int(input())
    n = 100
    maps = [list(map(int, input().split())) for _ in range(n)]

    start_y_lst = []

    for j in range(n):
        if maps[0][j] == 1:
            start_y_lst.append(j)

    end_y = maps[-1].index(2)

    answer = -1
    for start_y in start_y_lst:
        if dfs(0 ,start_y):
            answer = start_y

    print(f'#{test_case} {answer}')