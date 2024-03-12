n = int(input())
a, b = map(int, input().split())
arr = []
for _ in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)

dp = [[[[-1 for i in range(101)] for j in range(2)] for k in range(101)] for l in range(101)]

def recur(cur, max_yoyang, rst_cnt, studied):
    if max_yoyang < 0:
        return -(1 << 60)
    
    if rst_cnt >= 2:
        return -(1 << 60)
    
    if cur == n:
        if studied >= b:
            return 0
        return -(1 << 60)
    
    if dp[cur][max_yoyang][rst_cnt][studied] != -1:
        return dp[cur][max_yoyang][rst_cnt][studied]
    


    ret = 0
    # 정독실 사용
    ret = max(recur(cur+1, max_yoyang, 0, studied + 1) + arr[cur][0], ret)

    # 소학습실 사용
    ret = max(recur(cur+1, max_yoyang, 0, studied + 1) + arr[cur][1], ret)

    # 휴게실
    ret = max(recur(cur+1, max_yoyang, rst_cnt + 1, studied) + arr[cur][2], ret)

    # 요양
    ret = max(recur(cur+1, max_yoyang - 1, 0, studied) + arr[cur][3], ret)
    dp[cur][max_yoyang][rst_cnt][studied] = ret
    return dp[cur][max_yoyang][rst_cnt][studied]



print(recur(0, a, 0, 0))