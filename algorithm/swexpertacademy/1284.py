t = int(input())

for test_case in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())

    a_price = p * w
    b_price = q + (0 if w <= r else (w - r) * s)

    print(f'#{test_case} {min(a_price, b_price)}')