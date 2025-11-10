t = int(input())

for test_case in range(1, t + 1):
    bits = input()
    n = len(bits)

    answer = 0

    first = '0' * n

    i = 0
    while first != bits:
        if first[i] != bits[i]:
            num = bits[i]

            first = first[:i] + (num * (n - i))
            answer += 1

        i += 1

    print(f'#{test_case} {answer}')