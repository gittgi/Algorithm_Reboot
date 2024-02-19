import sys
input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))
ans = 0
def recur(cur, total):
    global ans
    if cur == n:
        if total == s:
            ans += 1
        return
    
  
    recur(cur+1, total)
    recur(cur+1, total+arr[cur])


recur(0, 0)
if s == 0:
    print(ans - 1)
else:
    print(ans)
