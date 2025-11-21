t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        v, c = map(int, input().split())
        arr.append((v, c))

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        size, value = arr[i - 1]

        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]

            if j >= size:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - size] + value)

    print(f'#{test_case} {dp[n][k]}')