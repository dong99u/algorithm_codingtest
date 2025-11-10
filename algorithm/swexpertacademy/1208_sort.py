for test_case in range(1, 11):
    dump_count = int(input())
    arr = list(map(int, input().split()))

    for _ in range(dump_count):
        arr.sort()

        if arr[-1] - arr[0] <= 1:
            break

        arr[-1] -= 1
        arr[0] += 1

    arr.sort()

    answer = arr[-1] - arr[0]

    print(f'#{test_case} {answer}')