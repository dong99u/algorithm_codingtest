for test_case in range(1, 10 + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    for _ in range(n):
        arr.sort()
        if abs(arr[-1] - arr[0]) <= 1:
            break
        arr[-1] -= 1
        arr[0] += 1

    answer = max(arr) - min(arr)
    print(f'#{test_case} {answer}')