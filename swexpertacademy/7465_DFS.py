def dfs(v):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            dfs(next)

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)

    answer = 0
    for v in range(1, n + 1):
        if not visited[v]:
            answer += 1
            dfs(v)

    print(f'#{test_case} {answer}')
