import heapq

for test_case in range(1, 11):
    dump_count = int(input())
    arr = list(map(int, input().split()))

    min_heap = arr[:]
    max_heap = [-x for x in arr]

    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    for _ in range(dump_count):
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)

        if max_val - min_val <= 1:
            heapq.heappush(max_heap, -max_val)
            heapq.heappush(min_heap, min_val)
            break

        # 높이 변경
        heapq.heappush(max_heap, -(max_val - 1))
        heapq.heappush(min_heap, min_val + 1)

    answer = -max_heap[0] - min_heap[0]
    print(f'#{test_case} {answer}')