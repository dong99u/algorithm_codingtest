t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if board[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        if cnt == k:
            answer += 1

    for j in range(n):
        cnt = 0
        for i in range(n):
            if board[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        if cnt == k:
            answer += 1

    print(f'#{test_case} {answer}')




