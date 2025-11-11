t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    V = []
    C = []

    for _ in range(n):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(k + 1):
            dp[i][w] = dp[i - 1][w]

            if w >= V[i - 1]:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - V[i - 1]] + C[i - 1])

    print(f'#{test_case} {dp[n][k]}')