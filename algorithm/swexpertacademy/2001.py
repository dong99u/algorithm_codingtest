import pprint

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i - 1][j] + arr[i - 1][j - 1] - prefix_sum[i - 1][j - 1]

    for x1 in range(1, N - M + 2):
        for y1 in range(1, N - M + 2):
            x2 = x1 + M - 1
            y2 = y1 + M - 1

            val = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
            answer = max(answer, val)

    print(f'#{test_case} {answer}')


