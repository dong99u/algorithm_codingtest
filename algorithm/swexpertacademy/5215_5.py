def dfs(idx, score, calorie):
    global answer

    if calorie > l:
        return

    answer = max(answer, score)

    if idx == n:
        return

    dfs(idx + 1, score + arr[idx][0], calorie + arr[idx][1])
    dfs(idx + 1, score, calorie)

t = int(input())

for test_case in range(1, t + 1):
    n, l = map(int, input().split())
    arr = []
    for _ in range(n):
        s, c = map(int, input().split())
        arr.append((s, c))

    answer = 0

    dfs(0, 0, 0)
    print(f'#{test_case} {answer}')