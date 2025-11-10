from collections import defaultdict

t = int(input())

for test_case in range(1, t + 1):
    n, m, k = map(int, input().split())

    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    # 반대 방향
    opposite = [0, 2, 1, 4, 3]

    clusters = []
    for _ in range(k):
        x, y, cnt, d = map(int, input().split())
        clusters.append([x, y, cnt, d])

    for _ in range(m):
        for cluster in clusters:
            x, y, cnt, d = cluster
            nx, ny = x + dx[d], y + dy[d]

            if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                cnt //= 2
                d = opposite[d]

            cluster[0], cluster[1], cluster[2], cluster[3] = nx, ny, cnt, d

        clusters = [c for c in clusters if c[2] > 0]

        position_map = defaultdict(list)
        for cluster in clusters:
            x, y, cnt, d = cluster
            key = (x, y)
            position_map[key].append([cnt, d])

        new_clusters = []
        for (x, y), group in position_map.items():
            if len(group) == 1:
                # 혼자면 그대로
                new_clusters.append([x, y, group[0][0], group[0][1]])
            else:
                # 여러 개면 합치기
                total_cnt = sum(g[0] for g in group)
                max_cluster = max(group, key=lambda g: g[0])
                new_clusters.append([x, y, total_cnt, max_cluster[1]])

        clusters = new_clusters

    answer = sum(c[2] for c in clusters)
    print(f'#{test_case} {answer}')