def get_height(point_num):
    i = 1
    result = 1

    while True:
        if point_num <= result:
            return i, result
        i += 1
        result += i

def get_coord(point_num):
    height, last_point_num = get_height(point_num)
    diff = last_point_num - point_num
    return (height - diff, 1 + diff) # x, y

def get_point_num(x, y):
    height = x + y - 1

    start_point_num = 0
    for i in range(height):
        start_point_num += i
    start_point_num += 1

    point_num = start_point_num
    for i in range(1, height + 1):
        j = height + 1 - i
        if (i, j) == (x, y):
            return point_num
        point_num += 1

t = int(input())

for test_case in range(1, t + 1):
    p, q = map(int, input().split())

    px, py = get_coord(p)
    qx, qy = get_coord(q)

    sum_x = px + qx
    sum_y = py + qy

    answer = get_point_num(sum_x, sum_y)

    print(f'#{test_case} {answer}')
