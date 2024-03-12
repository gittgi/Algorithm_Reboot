pull_list = list(map(int, input().split()))


# cur가 플레이어, pull은 몇개 뽑을건지(b1, b2, b3), box는 어디 박스(k1, k2)
# return 은 패자
def recur(cur, l, r):
    if l < 0 or r < 0:
        return (cur + 1) % 2
    
    if l == 0 and r < pull_list[0] or r == 0 and l < pull_list[0]:
        return cur % 2
   
    if dp[cur % 2][l][r] != -1:
        return dp[cur % 2][l][r]
    
    # 내가 이기는 경우가 한번이라도 있으면 이김
    win = False
    for i in range(3):
        pull_number = pull_list[i]
        if recur(cur + 1, l - pull_number, r) == (cur + 1) % 2:
            win = True
        if recur(cur + 1, l, r - pull_number) == (cur + 1) % 2:
            win = True

    
    if win:
        dp[cur % 2][l][r] = (cur + 1) % 2
    else:
        dp[cur % 2][l][r] = cur % 2
    return dp[cur % 2][l][r]
            


for _ in range(5):
    l, r = map(int, input().split())
    dp = [[[-1 for i in range(r+1)] for j in range(l+1)] for k in range(2)]

    if recur(0, l, r) == 0:
        print("B")
    else:
        print("A")


