def dfs(v, length):
    global answer
    visited[v] = True
    answer = max(answer, length + 1)
    for next in graph[v]:
        if not visited[next]:
            dfs(next, length + 1)

    visited[v] = False


t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)


    answer = 0
    for v in range(1, n + 1):
        visited = [False] * (n + 1)
        dfs(v, 0)

    print(f'#{test_case} {answer}')