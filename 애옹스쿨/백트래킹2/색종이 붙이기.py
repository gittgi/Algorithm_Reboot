arr = list(list(map(int, input().split())) for _ in range(10))
papers = [5 for _ in range(6)]
papers[0] = 0
visited = [[0 for i in range(10)] for j in range(10)]

def check(x, y, l):
    possible = 0
    for k in range(l):
        flag = False
        for i in range(x, x+1+k):
            for j in range(y, y+1+k):
                if arr[i][j] == 0 or visited[i][j] == 1:
                    flag = True
                    break
            if flag == True:
                break
            
        else:
            possible = k + 1
    return possible

ans = float("inf")
def recur(x, y, cnt):
    global ans
    if cnt >= ans:
        return

    if y == 10:
        x += 1
        y = 0
    
    if x == 10:
        ans = min(cnt, ans)
        return
    
    if arr[x][y] == 0 or visited[x][y] == 1:
        recur(x, y+1, cnt)
        return
   
    possible = check(x, y, min(5, 10 - max(x, y)))
    for k in range(possible):
        if papers[k + 1] > 0:
            papers[k + 1] -= 1
            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    visited[i][j] = 1
            recur(x, y+1, cnt+1)
            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    visited[i][j] = 0
            papers[k + 1] += 1
    

recur(0, 0, 0)
if ans == float("inf"):
    print(-1)
else:
    print(ans)