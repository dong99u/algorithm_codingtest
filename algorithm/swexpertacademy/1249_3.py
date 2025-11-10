import heapq

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

t = int(input())
INF = float('inf')
for test_case in range(1, t + 1):
    n = int(input())

    maps = [
        list(map(int, list(input())))
        for _ in range(n)
    ]
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = 0

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    h = [(0, 0, 0)] # cost, x, y

    while h:
        cost, x, y = heapq.heappop(h)

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny):
                continue

            next_cost = maps[nx][ny]

            if dist[nx][ny] > cost + next_cost:
                dist[nx][ny] = cost + next_cost
                heapq.heappush(h, (cost + next_cost, nx, ny))

    print(f'#{test_case} {dist[-1][-1]}')