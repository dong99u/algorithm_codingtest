def in_range(curr_x, curr_y, bc_x, bc_y, c):
    return abs(bc_x - curr_x) + abs(bc_y - curr_y) <= c

def get_charge(xa, ya, xb, yb):
    max_charge = 0

    for i in range(len(bcs) + 1):
        for j in range(len(bcs) + 1):
            charge_a = 0
            charge_b = 0

            if i > 0:
                x, y, c, p = bcs[i - 1]
                if in_range(xa, ya, x, y, c):
                    charge_a = p

            if j > 0:
                x, y, c, p = bcs[j - 1]
                if in_range(xb, yb, x, y, c):
                    charge_b = p

            if i > 0 and i == j:
                x, y, c, p = bcs[i - 1]
                if in_range(xa, ya, x, y, c) and in_range(xb, yb, x, y, c):
                    total = p
                else:
                    total = charge_a + charge_b
            else:
                total = charge_a + charge_b

            max_charge = max(max_charge, total)

    return max_charge


t = int(input())

for test_case in range(1, t + 1):
    m, a = map(int, input().split())

    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]

    moves_a = list(map(int, input().split()))
    moves_b = list(map(int, input().split()))

    bcs = [
        list(map(int, input().split()))
        for _ in range(a)
    ]

    xa, ya = 1, 1
    xb, yb = 10, 10

    total_charge = 0

    total_charge += get_charge(xa, ya, xb, yb)

    for i in range(m):
        xa += dx[moves_a[i]]
        ya += dy[moves_a[i]]
        xb += dx[moves_b[i]]
        yb += dy[moves_b[i]]

        total_charge += get_charge(xa, ya, xb, yb)

    print(f'#{test_case} {total_charge}')
