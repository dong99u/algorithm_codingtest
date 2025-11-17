t = int(input())

for test_case in range(1, t + 1):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    is_valid = True
    for i in range(n):
        time = arr[i]

        made = (time // m) * k

        given = i + 1

        if made < given:
            is_valid = False
            break

    print(f'#{test_case} {"Possible" if is_valid else "Impossible"}')