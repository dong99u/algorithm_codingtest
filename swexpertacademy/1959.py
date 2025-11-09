t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    answer = 0
    if n <= m:
        for j in range(m - n + 1):
            sum_val = 0
            for i in range(n):
                sum_val += A[i] * B[j + i]

            answer = max(answer, sum_val)
    else:
        for i in range(n - m + 1):
            sum_val = 0
            for j in range(m):
                sum_val += B[j] * A[i + j]

            answer = max(answer, sum_val)

    print(f'#{test_case} {answer}')
