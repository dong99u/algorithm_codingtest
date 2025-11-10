t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    lst = [0] * (5000 + 1)

    for _ in range(n):
        s, e = map(int, input().split())
        for i in range(s, e + 1):
            lst[i] += 1

    p = int(input())

    result = []
    for _ in range(p):
        idx = int(input())
        result.append(str(lst[idx]))

    print(f'#{test_case} {" ".join(result)}')