t = int(input())

for test_case in range(1, t + 1):
    arr = list(map(int, input().split()))
    arr.sort()

    answer = round(sum(arr[1:-1]) / 8)

    print(f'#{test_case} {answer}')