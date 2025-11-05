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

    cost = [[INF] * n for _ in range(n)]
    cost[0][0] = 0

    heap = [(0, 0, 0)]

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while heap:
        curr_cost, x, y = heapq.heappop(heap)

        if curr_cost > cost[x][y]:
            continue

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(nx, ny):
                continue

            new_cost = curr_cost + maps[nx][ny]

            if new_cost < cost[nx][ny]:
                cost[nx][ny] = new_cost
                heapq.heappush(heap, (new_cost, nx, ny))

    print(f'#{test_case} {cost[-1][-1]}')