from collections import deque
import copy

def in_range(x, y):
    return 0 <= x < h and 0 <= y < w

def dfs(grid, cnt, destroyed_cnt):
    global answer

    remaining = sum(sum(1 for cell in row if cell != 0) for row in grid)
    if remaining == 0:
        answer = max(answer, destroyed_cnt)
        return

    if cnt == n:
        answer = max(answer, destroyed_cnt)
        return

    for col in range(w):
        temp = copy.deepcopy(grid)
        row = exists(temp, col)

        if row is False:
            continue

        boom_cnt = boom(temp, row, col)
        all_fall(temp)
        dfs(temp, cnt + 1, destroyed_cnt + boom_cnt)


def exists(grid, col):
    for i in range(h):
        if grid[i][col] != 0:
            return i
    return False

def all_fall(grid):
    for j in range(w):
        temp = []
        for i in range(h - 1, -1, -1):
            if grid[i][j] != 0:
                temp.append(grid[i][j])

        for i in range(h):
            if i < len(temp):
                grid[h - i - 1][j] = temp[i]
            else:
                grid[h - i - 1][j] = 0

def boom(grid, x, y):
    k = grid[x][y]

    if k == 0:
        return 0

    grid[x][y] = 0

    if k == 1:
        return 1

    q = deque([(x, y, k)])
    cnt = 1

    while q:
        cx, cy, ck = q.popleft()

        for dx, dy in zip(dxs, dys):
            for dist in range(1, ck):
                nx = cx + dx * dist
                ny = cy + dy * dist

                if in_range(nx, ny) and grid[nx][ny] != 0:
                    nk = grid[nx][ny]
                    grid[nx][ny] = 0
                    q.append((nx, ny, nk))
                    cnt += 1

    return cnt

t = int(input())

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

for test_case in range(1, t + 1):
    n, w, h = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]

    answer = 0
    dfs(grid, 0, 0)

    total = sum(sum(1 for cell in row if cell != 0) for row in grid)
    result = total - answer

    print(f'#{test_case} {result}')