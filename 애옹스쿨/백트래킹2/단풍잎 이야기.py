n, m, k = map(int, input().split())
quests = [list(map(int, input().split())) for _ in range(m)]

skills = [False for _ in range(1 + 2*n)]

ans = 0

def recur(cur, cnt):
    global ans
    if cnt == n:
        ans = max(ans, check())
        return
    if cur == (1 + 2*n):
        return
    
    # 스킬 미포함
    recur(cur + 1, cnt)

    # 스킬 포함
    skills[cur] = True
    recur(cur + 1, cnt + 1)
    skills[cur] = False


def check():
    cnt = 0
    for q in quests:
        for s in q:
            if not skills[s]:
                break
        else:
            cnt += 1
    return cnt

recur(1, 0)
print(ans)

    
