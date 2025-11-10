from collections import deque

for test_case in range(1, 10 + 1):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    max_num = max(arr)

    graph = [[] for _ in range(max_num + 1)]

    for i in range(0, n, 2):
        u, v = arr[i], arr[i + 1]
        graph[u].append(v)

    visited = [False] * (max_num + 1)
    dist = [0] * (max_num + 1)

    q = deque([k])
    visited[k] = True

    while q:
        now = q.popleft()

        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                dist[next] = dist[now] + 1
                q.append(next)

    answer = 0
    max_dist = 0
    for i in range(len(dist)):
        if max_dist < dist[i]:
            max_dist = dist[i]
            answer = i
        elif max_dist == dist[i]:
            answer = max(answer, i)

    print(f'#{test_case} {answer}')



