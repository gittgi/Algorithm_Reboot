from collections import deque

n, m = map(int, input().split())
wuq = list(map(int, input().split()))
visited = [0 for i in range(1000010)]
q = deque()
possible = []
for i in range(m):
    if visited[wuq[i]] != 0:
        continue
    visited[wuq[i]] = 1
    q.append(wuq[i])
    possible.append(wuq[i])
    for j in range(i+1, m):
        if visited[wuq[i]+wuq[j]] == 0:
            visited[wuq[i]+wuq[j]] = 1
            q.append(wuq[i]+wuq[j])
            possible.append(wuq[i]+wuq[j])



# while q:
#     x = q.popleft()

#     for i in possible:
#         nx = x + i
#         if nx == m:
#             print(visited[x] + 1)
#             break
#         if visited[nx] == 0:
#             visited[nx] = visited[x] + 1
#             q.append(nx)
    
# else:
#     print(-1)
            
dp = [1000010 for i in range(1000010)]
for i in possible:
    dp[i] = 1

for i in range(1, n+1):
    if dp[i] != 1000010:
        continue
    
    min_val = 1000010
    for j in possible:
        if i - j >= 0:
            min_val = min(min_val, dp[i - j])
    dp[i] = min_val + 1

print(dp[n] if dp[n] < 1000010 else -1)