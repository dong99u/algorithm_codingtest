def find_combi(curr_idx, cnt, selected):
    if cnt == n // 2:
        combi.append(selected[:])
        return

    for i in range(curr_idx, n):
        selected.append(i)
        find_combi(i + 1, cnt + 1, selected)
        selected.pop()

def dfs(curr_idx, cnt, selected, lst):
    if cnt == 2:
        a, b = selected[0], selected[1]
        return s[a][b] + s[b][a]

    result = 0
    for i in range(curr_idx, n // 2):
        selected.append(lst[i])
        result += dfs(i + 1, cnt + 1, selected, lst)
        selected.pop()

    return result


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    s = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    combi = []
    find_combi(0, 0, [])

    answer = float('inf')
    for c in combi:
        left = []
        for i in range(n):
            if i not in c:
                left.append(i)

        a = dfs(0, 0, [], c)
        b = dfs(0, 0, [], left)

        answer = min(answer, abs(a - b))

    print(f'#{test_case} {answer}')
