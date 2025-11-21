def get_d(inst):
    if inst == 'U':
        return 0
    elif inst == 'D':
        return 1
    elif inst == 'L':
        return 2
    elif inst == 'R':
        return 3

def find_start_point():
    d = 0
    x, y = 0, 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] in '^v<>':
                x, y = i, j
                if grid[i][j] == '^':
                    d = 0
                elif grid[i][j] == 'v':
                    d = 1
                elif grid[i][j] == '<':
                    d = 2
                else:
                    d = 3
                return i, j, d

def move(x, y, d):
    grid[x][y] = tank[d]

    nx, ny = x + dx[d], y + dy[d]

    if not in_range(nx, ny):
        return x, y
    if grid[nx][ny] in '*#-': # 벽돌, 강철, 물로는 움직일 수 없음.
        return x, y

    # 움직일 수 있다면
    grid[nx][ny] = tank[d]
    grid[x][y] = '.'

    return nx, ny

def shoot(x, y, d):
    while True:
        nx, ny = x + dx[d], y + dy[d]

        if not in_range(nx, ny):
            return
        if grid[nx][ny] == '*':
            grid[nx][ny] = '.'
            return
        if grid[nx][ny] == '#':
            return

        x, y = nx, ny

def in_range(x, y):
    return 0 <= x < h and 0 <= y < w

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tank = {
    0: '^',
    1: 'v',
    2: '<',
    3: '>'
}

for test_case in range(1, t + 1):
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))

    n = int(input())
    insts = list(input())

    x, y, d = find_start_point()

    for inst in insts:
        if inst == 'S':
            shoot(x, y, d)
        else:
            d = get_d(inst)
            x, y = move(x, y, d)

    print(f'#{test_case}', end=' ')

    for row in grid:
        print(''.join(row))