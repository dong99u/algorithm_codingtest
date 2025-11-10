T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    max_price = 0

    # 뒤에서부터 순회! ⭐
    for i in range(N - 1, -1, -1):
        if arr[i] > max_price:
            # 현재 가격이 더 크면 최댓값 갱신
            max_price = arr[i]
        else:
            # 현재 가격이 작으면 사서 max_price에 팔기
            answer += max_price - arr[i]

    print(f'#{test_case} {answer}')