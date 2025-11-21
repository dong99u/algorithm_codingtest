t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    possible = {0}

    for score in arr:
        possible = possible | {p + score for p in possible}

    print(f'#{test_case} {len(possible)}')