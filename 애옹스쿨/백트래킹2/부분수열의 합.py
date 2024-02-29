n, s = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
ans = 0
def recur(cur, cnt):
    global total, ans
    if cur == n:
        if total == s:
            if cnt > 0:
                ans += 1
        return
    
    # 미포함
    recur(cur + 1, cnt)

    # 포함
    total += arr[cur]
    recur(cur+1, cnt+1)
    total -= arr[cur]



recur(0, 0)
print(ans)