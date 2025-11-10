T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if board[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 0
        if cnt == K:
            answer += 1

    for j in range(N):
        cnt = 0
        for i in range(N):
            if board[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 0
        if cnt == K:
            answer += 1

    print(f'#{test_case} {answer}')

