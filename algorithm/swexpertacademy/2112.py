def check():
    for j in range(w):
        max_cnt = 1
        cnt = 1
        for i in range(1, d):
            if grid[i - 1][j] == grid[i][j]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
        if max_cnt < k:
            return False

    return True

def dfs(row, used):
    global answer

    if used >= answer:
        return

    if row == d:
        if check(): answer = used
        return

    dfs(row + 1, used)

    temp = grid[row][:]
    grid[row] = [0] * w
    dfs(row + 1, used + 1)
    grid[row] = temp

    grid[row] = [1] * w
    dfs(row + 1, used + 1)
    grid[row] = temp

t = int(input())

for test_case in range(1, t + 1):
    d, w, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(d)]

    if check():
        print(f'#{test_case} 0')
    else:
        answer = d
        dfs(0, 0)

        print(f'#{test_case} {answer}')