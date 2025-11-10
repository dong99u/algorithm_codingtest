import pprint

t = int(input())

for test_case in range(1, t + 1):
    n, m = 5, 15

    arr = [[None] * m for _ in range(n)]

    for i in range(n):
        row = list(input())

        for idx, elem in enumerate(row):
            arr[i][idx] = elem

    answer = []
    for j in range(m):
        word = []
        for i in range(n):
            if arr[i][j]:
                word.append(arr[i][j])

        if word:
            answer.append(''.join(word))

    print(f'#{test_case} {"".join(answer)}')