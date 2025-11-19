import copy

def in_range(x, y):
    return 0 <= x < h and 0 <= y < w

def exists(grid, col):
    for i in range(h):
        if grid[i][col] != 0:
            return i
    return -1

def boom(grid, x, y):
    k = grid[x][y]

    if k == 0:
        return 0

    # 중심 먼저 제거!
    grid[x][y] = 0
    cnt = 1

    if k == 1:
        return cnt

    for i in range(x - k + 1, x + k):
        if i == x:
            continue
        if in_range(i, y):
            cnt += boom(grid, i, y)
    for j in range(y - k + 1, y + k):
        if j == y:
            continue
        if in_range(x, j):
            cnt += boom(grid, x, j)

    return cnt

def all_fall(grid):
    for j in range(w):
        temp = []
        for i in range(h):
            if grid[h - i - 1][j] != 0:
                temp.append(grid[h - i - 1][j])
        for i in range(h):
            if i < len(temp):
                grid[h - i - 1][j] = temp[i]
            else:
                grid[h - i - 1][j] = 0

def dfs(grid, cnt, destroyed_cnt):
    global answer

    remaining = sum(sum(1 for cell in row if cell != 0) for row in grid)
    if remaining == 0:
        answer = max(answer, destroyed_cnt)
        return

    if cnt == n:
        answer = max(answer, destroyed_cnt)
        return

    for j in range(w):
        temp_grid = copy.deepcopy(grid)

        i = exists(temp_grid, j)

        if i == -1:
            continue

        # 새 변수로 받기!
        destroyed = boom(temp_grid, i, j)
        all_fall(temp_grid)
        dfs(temp_grid, cnt + 1, destroyed_cnt + destroyed)

t = int(input())

for test_case in range(1, t + 1):
    n, w, h = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]
    answer = 0

    dfs(grid, 0, 0)

    total = sum(sum(1 for cell in row if cell != 0) for row in grid)
    result = total - answer

    print(f'#{test_case} {result}')