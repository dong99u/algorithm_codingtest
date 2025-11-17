t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    i = 1

    s = set()
    while True:
        num_str = str(n * i)
        s.update(num_str)  # 문자열 각 문자를 set에 추가

        if len(s) == 10:  # 0~9 모두 있으면 10개
            break
        i += 1

    print(f'#{test_case} {i * n}')
