import sys
input = sys.stdin.readline
sys.setrecursionlimit(100010)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
not_allowed = [False for _ in range(n + 1)]
dp = [[-1 for i in range(100110)] for j in range(2)]

for i in arr:
    not_allowed[i] = True

def recur(cur, call):
    # 대답을 못함 -> cur가 짐
    if call > n or (call != 0 and not_allowed[call]):
        return cur % 2
    
    if dp[cur%2][call] != -1:
        return dp[cur%2][call]
  
    for i in range(call + 1, call + 1 + k):
        # 상대가 대답하지 못해야 내가 이김 -> 한번이라도 대답하면 내가 짐
        if recur(cur + 1, i) == cur % 2:
            dp[cur%2][call] = cur % 2
            return dp[cur%2][call]
    dp[cur%2][call] = (cur + 1) % 2
    return dp[cur%2][call]

    

print((recur(0, 0) + 1) % 2)


