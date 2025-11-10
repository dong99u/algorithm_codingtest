def turn_90(arr):
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            temp[j][n - 1 - i] = arr[i][j]

    return temp

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr1 = turn_90(arr)
    arr2 = turn_90(arr1)
    arr3 = turn_90(arr2)

    print(f'#{test_case}')
    for i in range(n):
        row1 = ''.join(map(str, arr1[i]))
        row2 = ''.join(map(str, arr2[i]))
        row3 = ''.join(map(str, arr3[i]))

        print(f'{row1} {row2} {row3}')
