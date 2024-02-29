n = int(input())
arr = []
for _ in range(n):
    s, b = map(int, input().split())
    arr.append([s, b])

sour = 1
bitter = 0
min_val = float("inf")
def recur(cur, cnt):

    global sour, bitter, min_val
    if cur == n:
        if cnt > 0:
            min_val = min(min_val, abs(sour - bitter))
        return
    

    # 미포함
    recur(cur+1, cnt)

    # 포함
    sour *= arr[cur][0]
    bitter += arr[cur][1]
    recur(cur + 1, cnt + 1)
    sour //= arr[cur][0]
    bitter -= arr[cur][1]

recur(0, 0)
print(min_val)