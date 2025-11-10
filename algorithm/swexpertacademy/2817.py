def dfs(idx, sum_val, cnt):
    if idx == n:
        if cnt > 0 and sum_val == k:
            return 1
        return 0

    state = (idx, sum_val, cnt)

    if state in memo:
        return memo[state]

    result = 0

    result += dfs(idx + 1, sum_val + arr[idx], cnt + 1)
    result += dfs(idx + 1, sum_val, cnt)

    memo[state] = result

    return result


t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    memo = {}
    answer = dfs(0, 0, 0)


    print(f'#{test_case} {answer}')