n = int(input())
arr = []
for _ in range(n):
    r, g, b = map(int, input().split())
    arr.append((r,g,b))
gom_r, gom_g, gom_b = map(int, input().split())

temp_color = [0, 0, 0]
ans = float("inf")
def recur(cur, cnt):
    global ans
    if cnt > 7:
        return
    if cur == n:
        if cnt >= 2:
            mun_r = temp_color[0] // cnt
            mun_g = temp_color[1] // cnt
            mun_b = temp_color[2] // cnt
            diff = abs(gom_r - mun_r) + abs(gom_g - mun_g) +abs(gom_b - mun_b)
 
            ans = min(ans, diff)
        return
    
    # 안섞기
    recur(cur + 1, cnt)

    # 섞기
    temp_color[0] += arr[cur][0]
    temp_color[1] += arr[cur][1]
    temp_color[2] += arr[cur][2]

    recur(cur + 1, cnt + 1)

    temp_color[0] -= arr[cur][0]
    temp_color[1] -= arr[cur][1]
    temp_color[2] -= arr[cur][2]

recur(0, 0)
print(ans)