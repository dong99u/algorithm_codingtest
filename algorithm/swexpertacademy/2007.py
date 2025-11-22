t = int(input())

for test_case in range(1, t + 1):
    arr = input()
    n = len(arr)

    find = False
    answer = 0
    for i in range(n):
        for j in range(10):
            word = arr[i:i + j + 1]
            next_word = arr[i + j + 1: i + j + 1 + j + 1]
            if word == next_word:
                find = True
                answer = j + 1
                break
        if find:
            break

    print(f'#{test_case} {answer}')

