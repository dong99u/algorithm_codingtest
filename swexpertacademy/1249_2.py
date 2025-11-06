import heapq

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

t = int(input())
INF = float('inf')
for test_case in range(1, t + 1):
    n = int(input())
    maps = [list(map(int, list(input()))) for _ in range(n)]

    dist = [[INF] * n for _ in range(n)]

    heap = [(0, 0, 0)] # w, x, y

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    answer = 0
    while heap:
        cost, curr_x, curr_y = heapq.heappop(heap)

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if not in_range(nx, ny):
                continue
            if dist[nx][ny] != INF:
                continue

            dist[nx][ny] = min(dist[nx][ny], cost + maps[nx][ny])

            if nx == n - 1 and ny == n - 1:
                answer = dist[nx][ny]
                break

            heapq.heappush(heap, (dist[nx][ny], nx, ny))

        if answer != 0:
            break

    print(f'#{test_case} {answer}')
