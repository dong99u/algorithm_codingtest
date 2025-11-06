for test_case in range(1, 10 + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0

    for i in range(2, n - 2):
        max_height = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])

        cnt = arr[i] - max_height
        if cnt > 0:
            answer += cnt

    print(f'#{test_case} {answer}')
