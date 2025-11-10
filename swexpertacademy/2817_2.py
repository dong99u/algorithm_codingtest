def dfs(idx, cnt, sum_val):
    global answer

    if idx == n:
        if cnt > 0 and sum_val == k:
            answer += 1
        return

    dfs(idx + 1, cnt + 1, sum_val + arr[idx])
    dfs(idx + 1, cnt, sum_val)


t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = 0
    dfs(0, 0, 0)

    print(f'#{test_case} {answer}')