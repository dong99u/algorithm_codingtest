T = int(input())

d = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

for test_case in range(1, T + 1):

    n, m = map(int, input().split())

    arr = [
        input()
        for _ in range(n)
    ]

    code = ''

    for idx, row in enumerate(arr):
        end_index = row.rfind('1')
        if end_index == -1:
            continue
        code = row[end_index - 55:end_index + 1]
        break

    answer = []

    for i in range(0, 56, 7):
        answer.append(int(d[code[i: i + 7]]))

    odd = 0
    even = 0
    valid = False
    for i in range(len(answer)):
        if i % 2 == 0:
            odd += answer[i]
        else:
            even += answer[i]

    if ((odd * 3) + even) % 10 == 0:
        valid = True



    print(f'#{test_case} {sum(answer) if valid else 0}')



