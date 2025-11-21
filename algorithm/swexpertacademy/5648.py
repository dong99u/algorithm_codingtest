from collections import defaultdict

t = int(input())

# 상 하 좌 우
dx = [0, 0, -0.5, 0.5]
dy = [0.5, -0.5, 0, 0]

for test_case in range(1, t + 1):
    n = int(input())
    infos = []
    for _ in range(n):
        x, y, d, k = map(int, input().split())
        infos.append([x, y, d, k])

    answer = 0
    for _ in range(4000):
        for info in infos:
            x, y, d, k = info
            nx, ny = x + dx[d], y + dy[d]

            info[0], info[1] = nx, ny

        cnt_dict = defaultdict(list)
        for info in infos:
            x, y, d, k = info
            cnt_dict[(x, y)].append([d, k])

        new_infos = []
        for (x, y), values in cnt_dict.items():
            if len(values) == 1: # 충돌하지 않음
                new_infos.append([x, y, values[0][0], values[0][1]])
            else:
                sum_k = sum(k for d, k in values)
                answer += sum_k
        infos = new_infos

    print(f'#{test_case} {answer}')