import pprint
from collections import deque

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

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x  + dx, y + dy

            if not in_range(nx, ny):
                continue

            new_cost = cost[x][y] + maps[nx][ny]

            # 핵심: 더 작은 비용으로 갱신 가능할 때만 큐에 추가
            if new_cost < cost[nx][ny]:
                cost[nx][ny] = new_cost
                q.append((nx, ny))  # 다시 큐에 넣기!

    print(f'#{test_case} {cost[-1][-1]}')

