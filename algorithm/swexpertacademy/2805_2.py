def in_range(i, j):
    return abs(i - mx) + abs(j - my) <= (n // 2)

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    maps = [
        list(map(int, list(input())))
        for _ in range(n)
    ]

    mx = my = n // 2

    answer = 0
    for i in range(n):
        for j in range(n):
            if in_range(i, j):
                answer += maps[i][j]

    print(f'#{test_case} {answer}')