INF = float('inf')
t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    m = int(input())

    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = True

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    answer = 0

    for i in range(1, n + 1):
        count = 0

        for j in range(1, n + 1):
            if graph[j][i]:
                count += 1

        for j in range(1, n + 1):
            if graph[i][j]:
                count += 1

        if count == n - 1:
            answer += 1

    print(f'#{test_case} {answer}')