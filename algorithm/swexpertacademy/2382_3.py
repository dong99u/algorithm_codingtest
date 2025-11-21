from collections import defaultdict

t = int(input())

dxs = [0, -1, 1, 0, 0]
dys = [0, 0, 0, -1, 1]

opposite = [0, 2, 1, 4, 3]

for test_case in range(1, t + 1):
    n, m, k = map(int, input().split())
    infos = []
    for _ in range(k):
        x, y, cnt, d = map(int, input().split())
        infos.append([x, y, cnt, d])

    for _ in range(m):
        for info in infos:
            x, y, cnt, d = info
            nx, ny = x + dxs[d], y + dys[d]

            if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                cnt //= 2
                d = opposite[d]

            info[0], info[1], info[2], info[3] = nx, ny, cnt, d

        infos = [c for c in infos if c[2] > 0]

        cnt_dict = defaultdict(list)
        for info in infos:
            x, y, cnt, d = info
            cnt_dict[(x, y)].append((cnt, d))

        new_infos = []
        for (x, y), values in cnt_dict.items():
            if len(values) == 1:
                new_infos.append([x, y, values[0][0], values[0][1]])
            else:
                total_sum = sum(value[0] for value in values)
                d = max(values, key=lambda x: x[0])[1]
                new_infos.append([x, y, total_sum, d])

        infos = new_infos

    answer = sum(cnt for x, y, cnt, d in infos)

    print(f'#{test_case} {answer}')

