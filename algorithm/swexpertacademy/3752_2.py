t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    scores = list(map(int, input().split()))

    possible = {0}

    for score in scores:
        new_scores = set()

        for p in possible:
            new_scores.add(score + p)

        possible = possible | new_scores

    print(f'#{test_case} {len(possible)}')