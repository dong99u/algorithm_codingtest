t = int(input())

for test_case in range(1, t + 1):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))

    time = 1
    total = 0
    is_valid = True
    while True:
        if time % m == 0:
            total += k
        cnt = arr.count(time)
        if cnt <= 0:
            time += 1
            continue
        n -= cnt
        if total < cnt:
            is_valid = False
            break
        total -= cnt
        time += 1
        if n == 0:
            break

    print(f'#{test_case} {"Possible" if is_valid else "Impossible"}')
