def dfs(idx, weight):
    global answer

    if idx == n or weight > k:
        return 0

    state = (idx, weight)

    if state in memo:
        return memo[state]

    result = 0

    result = dfs(idx + 1, weight)

    if weight + V[idx] <= k:
        result = max(result, dfs(idx + 1, weight + V[idx]) + C[idx])

    memo[state] = result

    return result

t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    V = []
    C = []

    for _ in range(n):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)

    memo = {}

    answer = dfs(0, 0)

    print(f'#{test_case} {answer}')
