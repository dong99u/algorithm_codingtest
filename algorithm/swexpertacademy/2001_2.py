t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + arr[i - 1][j - 1] - prefix_sum[i - 1][j - 1]

    answer = 0

    for x1 in range(1, n - m + 2):
        for y1 in range(1, n - m + 2):
            x2, y2 = x1 + m - 1, y1 + m - 1

            val = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]

            answer = max(answer, val)

    print(f'#{test_case} {answer}')

