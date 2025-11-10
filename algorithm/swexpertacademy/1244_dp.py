import sys
sys.setrecursionlimit(10 ** 6)

def get_sum(arr):
    result = 0
    for i in range(n):
        result += arr[n - i - 1] * (10 ** i)

    return result

def dfs(cnt, nums):
    global answer

    state = (''.join(map(str, nums)), cnt)
    if state in visited:
        return
    visited.add(state)

    if cnt == k:
        answer = max(answer, get_sum(nums))
        return

    for i in range(n):
        for j in range(i + 1, n):
            nums[i], nums[j] = nums[j], nums[i]
            dfs(cnt + 1, nums)
            nums[i], nums[j] = nums[j], nums[i]

t = int(input())

for test_case in range(1, t + 1):
    arr, k = input().split()
    arr = list(map(int, list(arr)))
    k = int(k)
    n = len(arr)

    answer = 0

    visited = set()

    dfs(0, arr)

    print(f'#{test_case} {answer}')
