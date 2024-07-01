n , m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 왼쪽으로 이동한 것 체크
# 오른쪽으로 이동한 것 체크
# 두개를 서로 비교해서 update

dpr = [[0 for i in range(m)] for j in range(n)]
dpl = [[0 for i in range(m)] for j in range(n)]
dp = [[0 for i in range(m)] for j in range(n)]

dpr[0][0] = arr[0][0]
dpl[0][0] = arr[0][0]
dp[0][0] = arr[0][0]

for i in range(1, m):
    dpr[0][i] = dpr[0][i-1] + arr[0][i]
    dpl[0][i] = dpl[0][i-1] + arr[0][i]
    dp[0][i] = dp[0][i-1] + arr[0][i]
    


for i in range(1, n):
    # 좌에서 우로 먼저
    # 맨 왼쪽은 dp 기준으로 초기화
    dpr[i][0] = dp[i-1][0] + arr[i][0]
    for j in range(1, m):
        dpr[i][j] = max(dpr[i][j-1], dp[i-1][j]) + arr[i][j]
    
    
    # 그다음 우에서 좌 비교
    # 맨 오른쪽은 dp 기준으로 초기화
    dpl[i][-1] = dp[i-1][-1] + arr[i][-1]
    for j in range(m-1)[::-1]:
        dpl[i][j] = max(dpl[i][j+1], dp[i-1][j]) + arr[i][j]

    # 왼쪽 오른쪽 비교 (위에서 내려온건 각각 구할때 이미 계산됨)
    for j in range(m):
        dp[i][j] = max(dpr[i][j], dpl[i][j])



print(dp[n-1][m-1])

