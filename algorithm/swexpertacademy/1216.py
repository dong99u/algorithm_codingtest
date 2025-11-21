def check(strs):
    return strs == strs[::-1]  # 파이썬다운 회문 검사

for test_case in range(1, 10 + 1):
    t = int(input())
    n = 100
    grid = [list(input()) for _ in range(n)]

    answer = 1

    # 가로 방향
    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n + 1):
                substring = ''.join(grid[i][j:k])
                if check(substring):
                    answer = max(answer, len(substring))

    # 세로 방향
    for j in range(n):
        col = [grid[i][j] for i in range(n)]
        for i in range(n):
            for k in range(i + 1, n + 1):
                substring = ''.join(col[i:k])
                if check(substring):
                    answer = max(answer, len(substring))

    print(f'#{t} {answer}')