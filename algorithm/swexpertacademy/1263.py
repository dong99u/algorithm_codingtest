t = int(input())

for test_case in range(1, t + 1):
    data = list(map(int, input().split()))
    n = data[0]

    data = data[1:]
    graph = []

    for i in range(0, n * n, n):
        graph.append(data[i:i + n])

    INF = float('inf')

    dp = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                dp[i + 1][j + 1] = graph[i][j]
            if i == j:
                dp[i + 1][j + 1] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    result = []
    for i in range(1, n + 1):
        cc = 0
        for j in range(1, n + 1):
            cc += dp[i][j]

        result.append(cc)

    print(f'#{test_case} {min(result)}')