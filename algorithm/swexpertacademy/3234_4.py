def dfs(left, right, visited):
    if left < right:
        return 0

    if visited == (1 << n) - 1:
        return 1

    state = (left, right, visited)

    if state in memo:
        return memo[state]

    result = 0
    for i in range(n):
        if not ((1 << i) & visited):
            new_visited = visited | (1 << i)

            result += dfs(left + arr[i], right, new_visited)
            result += dfs(left, right + arr[i], new_visited)

    memo[state] = result

    return result


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    memo = {}
    result = dfs(0, 0, 0)

    print(f'#{test_case} {result}')


