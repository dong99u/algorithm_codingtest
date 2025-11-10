t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    m = n // 2
    answer = 0

    # 하나의 for문으로!
    for i in range(n):
        distance = abs(i - m)  # 중심으로부터의 거리
        for j in range(distance, n - distance):
            answer += board[i][j]

    print(f'#{test_case} {answer}')