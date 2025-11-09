t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    arr = [[1] * i for i in range(1, n + 1)]

    for i in range(n):
        for j in range(i + 1):
            if i == 0:
                continue
            if j == 0 or j == i:
                continue

            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(f'#{test_case}')
    for row in arr:
        for num in row:
            print(num, end=' ')
        print()

