def in_range(x, y):
    return 1 <= x < n - 1 and 1 <= y < n - 1

def move(x, y):
    if not maps[x][y]:
        return
    cnt, dir_num = maps[x][y]
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny):
        next_maps[nx][ny].append((cnt // 2, 3 - dir_num))
        return

    next_maps[nx][ny].append((cnt, dir_num))

def set_max(x, y):
    if not next_maps[x][y]:
        return
    max_cnt = -1
    result_dir_num = 0
    sum_cnt = 0

    for idx, (cnt, dir_num) in enumerate(next_maps[x][y]):
        sum_cnt += cnt
        if max_cnt < cnt:
            result_dir_num = dir_num
            max_cnt = cnt

    temp[x][y] = (sum_cnt, result_dir_num)

t = int(input())

mapper = {
    1: 0,
    2: 3,
    3: 2,
    4: 1
}

for test_case in range(1, t + 1):
    n, m, k = map(int, input().split())

    maps = [[None] * n for _ in range(n)]

    # 상, 우, 좌, 하
    dxs = [-1, 0, 0, 1]
    dys = [0, 1, -1, 0]

    for _ in range(k):
        x, y, cnt, dir_num = map(int, input().split())
        dir_num = mapper[dir_num]
        maps[x][y] = (cnt, dir_num)


    for _ in range(m):
        next_maps = [[[] for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                move(x, y)
        temp = [[None] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                set_max(x, y)
        maps = temp
    answer = 0

    for x in range(n):
        for y in range(n):
            if maps[x][y]:
                answer += maps[x][y][0]

    print(f'#{test_case} {answer}')

