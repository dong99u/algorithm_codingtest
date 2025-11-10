def dfs(curr_idx, curr_point, curr_calorie):
    global answer
    answer = max(answer, curr_point)

    if curr_idx == n:
        return

    next_calorie = curr_calorie + arr[curr_idx][1]

    if next_calorie <= l:
        dfs(curr_idx + 1, curr_point + arr[curr_idx][0], next_calorie)

    dfs(curr_idx + 1, curr_point, curr_calorie)


t = int(input())

for test_case in range(1, t + 1):
    n, l = map(int, input().split())

    arr = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    answer = 0
    dfs(0, 0, 0)

    print(f'#{test_case} {answer}')
