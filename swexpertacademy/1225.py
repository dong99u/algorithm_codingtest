from collections import deque

for test_case in range(1, 10 + 1):
    n = int(input())

    q = deque(list(map(int, input().split())))

    while True:
        for i in range(1, 5 + 1):
            num = q.popleft()
            num -= i

            if num <= 0:
                q.append(0)
                break

            q.append(num)

        if q[-1] == 0:
            break

    print(f'#{test_case} {" ".join(map(str, q))}')
