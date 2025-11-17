def dfs(idx, calorie):
    if idx == n or calorie > l:
        return 0

    if memo[idx][calorie] != -1:
        return memo[idx][calorie]

    result = 0

    if calorie + arr[idx][1] <= l:
        result = dfs(idx + 1, calorie + arr[idx][1]) + arr[idx][0]

    result = max(result, dfs(idx + 1, calorie))

    memo[idx][calorie] = result

    return result


t = int(input())

for test_case in range(1, t + 1):
    n, l = map(int, input().split())

    arr = []
    for _ in range(n):
        p, c = map(int, input().split())
        arr.append((p, c))

    memo = [[-1] * (l + 1) for _ in range(n)]

    answer = dfs(0, 0)

    print(f'#{test_case} {answer}')