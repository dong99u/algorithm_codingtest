def dfs(idx, weight, val):
    global answer

    if weight > k:
        return
    answer = max(answer, val)
    if idx == n:
        return

    dfs(idx + 1, weight + V[idx], val + C[idx])
    dfs(idx + 1, weight, val)

t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    V = []
    C = []

    for _ in range(n):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)

    answer = 0

    dfs(0, 0, 0)

    print(f'#{test_case} {answer}')
