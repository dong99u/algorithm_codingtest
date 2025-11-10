def dfs(left, right, used_mask):
    if left < right:
        return 0

    if used_mask == (1 << n) - 1:
        return 1

    state = (left, right, used_mask)
    if state in memo:
        return memo[state]

    result = 0

    for i in range(n):
        if not (used_mask & (1 << i)):
            new_mask = used_mask | (1 << i)

            result += dfs(left + weights[i], right, new_mask)

            result += dfs(left, right + weights[i], new_mask)

    memo[state] = result
    return result

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    weights = list(map(int, input().split()))

    memo = {}

    answer = dfs(0, 0, 0)

    print(f'#{test_case} {answer}')