t = int(input())

for test_case in range(1, t + 1):
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    n, k = map(int, input().split())

    points = []

    for _ in range(n):
        mid, fin, report = map(int, input().split())
        points.append((mid, fin, report))

    sorted_points = sorted(points, key=lambda x: (x[0] * 0.35 + x[1] * 0.45 + x[2] * 0.2), reverse=True)

    rating = sorted_points.index(points[k - 1])

    cut_line = n // 10

    print(f'#{test_case} {grade[rating // cut_line]}')


