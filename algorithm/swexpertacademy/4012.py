from itertools import combinations

def get_diff(a, b):
    c_a = combinations(a, 2)
    c_b = combinations(b, 2)

    sum_a = 0
    sum_b = 0

    for i, j in c_a:
        sum_a += arr[i][j] + arr[j][i]

    for i, j in c_b:
        sum_b += arr[i][j] + arr[j][i]

    return abs(sum_b - sum_a)

def dfs(idx, selected):
    global answer

    if len(selected) == n // 2:
        left = s - selected
        answer = min(answer, get_diff(selected, left))
        return

    if idx == n:
        return

    selected.add(idx)
    dfs(idx + 1, selected)
    selected.remove(idx)

    dfs(idx + 1, selected)



t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    arr = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    s = set([i for i in range(n)])
    answer = float('inf')
    dfs(0, set())

    print(f'#{test_case} {answer}')