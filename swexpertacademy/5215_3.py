def dfs(idx, point, calorie):
    global answer
    answer = max(answer, point)

    if idx == n:
        return

    next_calorie = calorie + arr[idx][1]

    if next_calorie <= l:
        dfs(idx + 1, point + arr[idx][0], next_calorie)

    dfs(idx + 1, point, calorie)


t = int(input())

for test_case in range(1, t + 1):
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)] # 점수, 칼로리
    answer = 0

    dfs(0, 0, 0)

    print(f'#{test_case} {answer}')