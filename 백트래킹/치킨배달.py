from collections import deque



N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append((i,j))


visited_rec = [False] * len(chicken)
selected_rec = [False] * M
comb = []
def rec(now, start):
    if now == M:
        comb.append(selected_rec[:])
        return
    for i in range(start, len(chicken)):            
        if visited_rec[i]:
            continue
        selected_rec[now] = i
        visited_rec[i] = True
        rec(now+ 1, i+1)
        visited_rec[i] =False

def bfs(x, y):
    distance = []
    for cx, cy in chicken:
        distance.append(abs(x-cx) + abs(y-cy))
    
    return distance

chicken_df = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            chicken_df.append(bfs(i, j))

# print(chicken_df)

rec(0, 0)
# print(comb)
ans = float("inf")
for i in comb:
    total = 0
    for j in range(len(chicken_df)):
        new_dist = []
        for k in i:
            new_dist.append(chicken_df[j][k])
        
        total += min(new_dist)

    
    if ans > total:
        ans = total
        # print(i)

print(ans)