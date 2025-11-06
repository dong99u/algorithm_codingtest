def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y, count, used_cut):
    global max_dist

    max_dist = max(max_dist, count)

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if visited[nx][ny]:
            continue

        # 경우 1: 그냥 갈 수 있음
        if maps[nx][ny] < maps[x][y]:
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, used_cut)
            visited[nx][ny] = False

        # 경우 2: 깎아야 함
        elif not used_cut:
            # ✨ 핵심: 1부터 k까지 모든 깎기 시도!
            for cut in range(1, k + 1):
                # 깎은 후 높이가 현재보다 낮아야 함
                if maps[nx][ny] - cut < maps[x][y]:
                    maps[nx][ny] -= cut
                    visited[nx][ny] = True

                    dfs(nx, ny, count + 1, True)

                    visited[nx][ny] = False
                    maps[nx][ny] += cut

t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    maps = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    max_height = max(max(maps))
    max_height_coords = []

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == max_height:
                max_height_coords.append((i, j))

    max_dist = 0
    for x, y in max_height_coords:
        visited = [[False] * n for _ in range(n)]
        visited[x][y] = True
        dfs(x, y, 1, False)

    print(f'#{test_case} {max_dist}')
