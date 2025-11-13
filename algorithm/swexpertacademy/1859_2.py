t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    arr = list(map(int, input().split()))

    max_price = 0
    answer = 0

    for i in range(n - 1, -1, -1):
        if max_price < arr[i]:
            max_price = arr[i]
        else:
            answer += max_price - arr[i]

    print(f'#{test_case} {answer}')