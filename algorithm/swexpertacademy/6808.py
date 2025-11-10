def get_points(my_cards):
    a = 0 # 규영이 점수 총합
    b = 0 # 인영이 점수 총합
    for i in range(9):
        if cards[i] < my_cards[i]: # 규영이꺼보다 인영이의 숫자가 더 클 경우
            b += cards[i] + my_cards[i]
        elif cards[i] > my_cards[i]:
            a += cards[i] + my_cards[i]

    return a, b # 규영, 인영

def dfs(cnt):
    global win_cnt, lose_cnt

    if cnt == 9:
        a, b = get_points(selected)
        if a > b:
            win_cnt += 1
        elif a < b:
            lose_cnt += 1
        return

    for i in range(9):
        if not visited[i]:
            visited[i] = True
            selected.append(my_cards[i])
            dfs(cnt + 1)
            selected.pop()
            visited[i] = False


t = int(input())

for test_case in range(1, t + 1):
    cards = list(map(int, input().split())) # 규영이가 내는 카드의 순서
    my_cards = [] # 인영이가 받는 카드

    for num in range(1, 18 + 1):
        if num not in cards:
            my_cards.append(num)

    selected = []

    win_cnt = 0
    lose_cnt = 0
    visited = [False] * 9

    dfs(0)

    print(f'#{test_case} {win_cnt} {lose_cnt}')
