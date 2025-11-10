import math

for test_case in range(1, 10 + 1):
    n = int(input())
    tree = [None] * (n + 1)

    for _ in range(n):
        info = input().split()
        node = int(info[0])
        value = info[1]
        tree[node] = value

    valid = True

    for i in range(1, n + 1):
        left = i * 2
        right = i * 2 + 1

        is_leaf = left > n

        is_operator = tree[i] in ['+', '-', '*', '/']

        if is_leaf:
            if is_operator:
                valid = False
                break
        else:
            if not is_operator:
                valid = False
                break

    print(f'#{test_case} {1 if valid else 0}')










