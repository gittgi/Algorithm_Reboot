n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
r, g, b = map(int, input().split())
colors = [False for _ in range(n)]
ans = float("inf")

def recur(cur, cnt):
    global ans
    if cnt == 7 or cur == n:
        if cnt > 1:
            ans = min(ans, check())
        return
    
    # 미포함
    recur(cur+1, cnt)

    # 포함
    colors[cur] = True
    recur(cur+1, cnt+1)
    colors[cur] = False


def check():
    red = 0
    green = 0
    blue = 0
    cnt = 0
    for i in range(n):
        if colors[i]:
            red += arr[i][0]
            green += arr[i][1]
            blue += arr[i][2]
            cnt += 1
    
    return abs(r - red//cnt) + abs(g - green//cnt) + abs(b - blue//cnt)
    
recur(0,0)
print(ans)