import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = list(map(int, list(input())))
target = list(map(int, list(input())))

def dfs(cur, cnt):
    if cur >= 2 and arr[cur - 2] != target[cur - 2]:
        return 1 << 60
    
    if cur == n:
        if arr == target:
            return cnt
        else:
            return 1 << 60

    temp = 1 << 60
    # 안누른다. 
    temp = min(temp, dfs(cur+1, cnt))

    # 누른다.
    if cur == 0:
        arr[cur] = (arr[cur] + 1) % 2
        arr[cur + 1] = (arr[cur + 1] + 1) % 2
        temp = min(temp, dfs(cur+1, cnt+1))
        arr[cur] = (arr[cur] + 1) % 2
        arr[cur + 1] = (arr[cur + 1] + 1) % 2
    elif cur == n-1:
        arr[cur] = (arr[cur] + 1) % 2
        arr[cur - 1] = (arr[cur - 1] - 1) % 2
        temp = min(temp, dfs(cur+1, cnt+1))
        arr[cur] = (arr[cur] + 1) % 2
        arr[cur - 1] = (arr[cur - 1] - 1) % 2
    else:
        arr[cur - 1] = (arr[cur - 1] - 1) % 2
        arr[cur] = (arr[cur] + 1) % 2
        arr[cur + 1] = (arr[cur + 1] + 1) % 2
        temp = min(temp, dfs(cur+1, cnt+1))
        arr[cur - 1] = (arr[cur - 1] - 1) % 2
        arr[cur] = (arr[cur] + 1) % 2
        arr[cur + 1] = (arr[cur + 1] + 1) % 2

    return temp

    
ans = dfs(0, 0)
print(-1 if ans == 1 << 60 else ans)