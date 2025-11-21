def dfs(idx, cnt, sum_val):

    if cnt >= 1:
        if sum_val == k:
            return 1

    if idx == n:
        return 0


    return dfs(idx + 1, cnt, sum_val) + dfs(idx + 1, cnt + 1, sum_val + arr[idx])


t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = dfs(0, 0, 0)

    print(f'#{test_case} {answer}')