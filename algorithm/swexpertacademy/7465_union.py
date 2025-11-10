def find(x):
    if parent[x] != x: # 루트가 아니라면
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1


t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        union(u, v)

    answer = len(set(find(i) for i in range(1, n + 1)))

    print(f'#{test_case} {answer}')

