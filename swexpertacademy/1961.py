T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]

    answer1 = [[0] * N for _ in range(N)]
    answer2 = [[0] * N for _ in range(N)]
    answer3 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            answer1[j][N - 1 - i] = square[i][j]

    for i in range(N):
        for j in range(N):
            answer2[j][N - 1 - i] = answer1[i][j]

    for i in range(N):
        for j in range(N):
            answer3[j][N - 1 - i] = answer2[i][j]

    print(f'#{test_case}')

    for i in range(N):
        # 90도 회전 결과
        row1 = ''.join(map(str, answer1[i]))
        # 180도 회전 결과
        row2 = ''.join(map(str, answer2[i]))
        # 270도 회전 결과
        row3 = ''.join(map(str, answer3[i]))

        print(f"{row1} {row2} {row3}")
