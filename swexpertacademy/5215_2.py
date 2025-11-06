def dfs(idx):
    global answer

    if idx == n:
        total_point = sum(arr[i][0] for i in selected)
        total_calorie = sum(arr[i][1] for i in selected)

        if total_calorie <= l:
            answer = max(answer, total_point)
        return

    selected.append(idx)
    dfs(idx + 1)

    selected.pop()
    dfs(idx + 1)


t = int(input())

for test_case in range(1, t + 1):
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    selected = []

    dfs(0)

    print(f'#{test_case} {answer}')