import sys
input = sys.stdin.readline

n, l, r, x = map(int, input().split())

arr = list(map(int, input().split()))
ans = 0
def recur(cur, involved, total, max_val, min_val):
    global ans
    if cur == n:
        if involved >= 2:
            if l <= total <= r:
                if max_val - min_val >= x:
                    ans += 1
    
        return
    
    recur(cur+1, involved, total, max_val, min_val)
    
    if arr[cur] > max_val:
        max_val = arr[cur]
    if arr[cur] < min_val:
        min_val = arr[cur]
    
    recur(cur+1, involved+1, total+arr[cur], max_val, min_val)


recur(0, 0, 0, 0, 10**9)

print(ans)