def is_valid(nums):
    odd = 0
    even = 0
    for i in range(len(nums)):
        c = int(nums[i])

        if i % 2 == 0:
            odd += c
        else:
            even += c

    return (odd * 3 + even) % 10 == 0

t = int(input())

d = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    code_len = 56

    code = ''
    for row in arr:
        idx = row.rfind('1')
        if idx == -1:
            continue
        else:
            code = row[idx - code_len + 1:idx + 1]
            break

    answer = 0
    nums = []

    for i in range(0, code_len, 7):
        nums.append(d[code[i:i + 7]])

    if is_valid(nums):
        answer = sum(nums)

    print(f'#{test_case} {answer if answer != 0 else 0}')

