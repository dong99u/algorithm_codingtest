def in_range(x, y):
    return 0 <= x < h and 0 <= y < w

def shoot(x, y, direction):
    while True:
        nx, ny = x + dxs[direction], y + dys[direction]
        if not in_range(nx, ny):
            return
        if maps[nx][ny] == '#':
            return
        elif maps[nx][ny] == '.' or maps[nx][ny] == '-':
            x, y = nx, ny
            continue
        elif maps[nx][ny] == '*':
            maps[nx][ny] = '.'
            return

def get_start_point_and_direction():
    for i in range(h):
        for j in range(w):
            if maps[i][j] in ['^', 'v', '<', '>']:
                return i, j, dir_to_dir_num[maps[i][j]]


t = int(input())

inst_to_dir_num = {
    'U': 2,
    'D': 0,
    'L': 3,
    'R': 1,
}

dir_to_dir_num = {
    '^': 2,
    'v': 0,
    '<': 3,
    '>': 1
}

dir_num_to_dir = {
    2: '^',
    0: 'v',
    3: '<',
    1: '>'
}

for test_case in range(1, t + 1):
    h, w = map(int, input().split())
    maps = [
        list(input())
        for _ in range(h)
    ]
    n = int(input())
    inst = input()


    x, y, dir_num = get_start_point_and_direction() # 현재 위치 파악

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    for ins in inst:
        if ins == 'S':
            shoot(x, y, dir_num)
        else:
            next_dir_num = inst_to_dir_num[ins]
            nx, ny = x + dxs[next_dir_num], y + dys[next_dir_num]

            if not in_range(nx, ny) or maps[nx][ny] != '.':
                dir_num = next_dir_num
                maps[x][y] = dir_num_to_dir[inst_to_dir_num[ins]]
                continue

            maps[x][y] = '.'
            maps[nx][ny] = dir_num_to_dir[inst_to_dir_num[ins]]
            dir_num = next_dir_num
            x, y = nx, ny

    print(f'#{test_case}', end=' ')
    for i in range(h):
        for j in range(w):
            print(maps[i][j], end='')
        print()
