def in_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def dfs(x, y, visited):
    if len(visited) == 7:
        answer.add(''.join(map(str, visited)))
        return

    cx, cy = x, y
    for dx, dy in zip(dxs, dys):
        nx, ny = cx + dx, cy + dy

        if not in_range(nx, ny):
            continue

        visited.append(grid[nx][ny])
        dfs(nx, ny, visited)
        visited.pop()


t = int(input())

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
for test_case in range(1, t + 1):
    grid = [list(map(int, input().split())) for _ in range(4)]

    answer = set()
    for x in range(4):
        for y in range(4):
            dfs(x, y, [grid[x][y]])


    print(f'#{test_case} {len(answer)}')