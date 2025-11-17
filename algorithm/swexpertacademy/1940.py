t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    dist = 0
    v = 0
    for _ in range(n):
        commands = list(map(int, input().split()))
        if commands[0] == 1:
            v += commands[1]
        elif commands[0] == 2:
            v -= commands[1]
            if v < 0:
                v = 0

        dist += v

    print(f'#{test_case} {dist}')