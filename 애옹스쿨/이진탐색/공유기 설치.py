n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

s = 1
e = arr[-1] - arr[0]
max_val = 0
while s <= e:
    mid = (s+e) // 2
    # mid == 거리
    # 1번 부터 설치해도 됨(어차피 양끝에 설치하는게 최대효율)
    now_idx = 0
    prev_val = -float('inf')
    iptime = 0
    min_temp = float('inf')
    while now_idx <= n-1 and iptime < c:
        now_val = arr[now_idx]
        if now_val - prev_val >= mid:
            iptime += 1
            min_temp = min(min_temp, now_val - prev_val)
            prev_val = now_val

        now_idx += 1
     
    


    if iptime >= c:
        max_val = max(max_val, min_temp)
        s = mid + 1
    else:
        e = mid - 1

print(max_val) 
            



