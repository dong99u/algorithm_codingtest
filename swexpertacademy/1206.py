for test_case in range(1, 10 + 1):
    N = int(input())
    heights = list(map(int, input().split()))

    answer = 0
    for i in range(2, N - 2):
        max_height = max(heights[i - 1], heights[i - 2], heights[i + 1], heights[i + 2])

        if heights[i] <= max_height:
            continue

        answer += heights[i] - max_height

    print(f'#{test_case} {answer}')


