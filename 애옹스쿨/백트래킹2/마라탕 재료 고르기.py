n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
include = [False for _ in range(n)]
ans = -float("inf")

def recur(cur, cnt):
    global ans
    if cnt == k:
        ans = max(ans, check())
        return
    
    if cur == n:
        return
    

    # 재료 미포함
    recur(cur+1, cnt)

    # 재료 포함
    include[cur] = True
    recur(cur+1, cnt+1)
    include[cur] = False


def check():
    total = 0
    for i in range(n):
        if include[i]:
            for j in range(i + 1, n):
                if include[j]:
                    total += arr[i][j]

    return total

recur(0, 0)
print(ans)