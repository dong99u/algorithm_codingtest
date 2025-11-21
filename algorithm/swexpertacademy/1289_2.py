t = int(input())

for test_case in range(1, t + 1):
    origin = list(map(int, list(input())))
    state = 0

    answer = 0
    for num in origin:
        if num != state:
            answer += 1
            state = num

    print(f'#{test_case} {answer}')
