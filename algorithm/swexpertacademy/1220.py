for test_case in range(1, 10 + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    stack = []

    for j in range(n):
        stack = []
        for i in range(n):
            if grid[i][j] == 1:
                stack.append(grid[i][j])
            elif grid[i][j] == 2:
                if not stack:
                    continue
                while stack:
                    stack.pop()
                answer += 1

    print(f'#{test_case} {answer}')