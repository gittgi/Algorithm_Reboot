import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
arr = list(map(int, input().split()))
dp = [[[-1 for i in range(3)] for j in range(3)] for k in range(n)]

# cur:내가있는위치
def recur(cur, rev_cnt, direction):
    # 등교길을 벗어날 수 없다.
    if cur >= n or cur < 0:
        return -(1 << 60)
    
    # 0인칸을 밟으면 더이상 진행할 수 없다.
    if arr[cur] == 0:
        return -(1 << 60)
    
    # 방향 전환은 두번 이상 할 수 없다.
    if rev_cnt > 2:
        return -(1 << 60)
    
    # 도착하면 시간 반환
    if cur == n-1:
        return 0
    
    if dp[cur][rev_cnt][direction + 1] != -1:
        return dp[cur][rev_cnt][direction + 1]
    
    max_val = -1
    # 방향 전환 하기
    max_val = max(max_val, recur(cur + (arr[cur] * -1 * direction), rev_cnt + 1, -1 * direction) + 1)
    # 방향 전환 하지 않기
    max_val = max(max_val, recur(cur + (arr[cur] * direction), rev_cnt, direction) + 1)
    dp[cur][rev_cnt][direction + 1] = max_val
    return max_val

ans = recur(0, 0, 1)
print(ans if ans != 0 else -1)
    


    



    
