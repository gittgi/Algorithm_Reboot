w, h = map(int, input().split())

dp = [[[[0 for i in range(2)] for j in range(2)] for k in range(h)] for l in range(w)]

# crs : 교차로 연속 사용
# prv 0: x 방향 이동, 1: y 방향 이동
def recur(x, y, crs, prv):
    if crs >= 2:
        return 0

    if x == w:
        return 0
    
    if y == h:
        return 0
    
    if x == w-1 and y == h-1:
        return 1
    
    if dp[x][y][crs][prv] != -1:
        return dp[x][y][crs][prv]

    # 지금 진행 방향이 x일 때
    if prv == 0:
        dp[x][y][crs][prv] = (recur(x+1, y, 0, 0) + recur(x, y+1, crs+1, 1)) % 100000
    else:
        dp[x][y][crs][prv] = (recur(x+1, y, crs+1, 0) + recur(x, y+1, 0, 1)) % 100000
    
    return dp[x][y][crs][prv]

# 교차로 사용 여부 때문에, 시작점에서 x, y 방향으로 한칸씩 이동한 시점부터 계산
# 그렇지 않으면 직선으로 움직여도 교차로 사용한 경우와 안사용한 경우 둘다 dp에 찍힘...
print((recur(1, 0, 0, 0) + recur(0, 1, 0, 1)) % 100000)


dp = [[[[0 for i in range(2)] for j in range(2)] for k in range(h)] for l in range(w)]


# dp[x][y][이전교차여부][이전방향]
dp = [[[[0 for i in range(2)] for j in range(2)] for k in range(h)] for l in range(w)]

for i in range(w):
    for j in range(h):
        for c in range(2):
            for d in range(2):
                # 교차로를 사용하지 않았다 -> 방향이 그대로
                if c == 0:
                    if d == 0:
                        dp[i][j][c][d] += (dp[i-1][j][0]