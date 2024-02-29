arr = list(map(int, input().split()))
y_list = [0 for _ in range(10)]
ans = 0
score = 0
def recur(cur):
    global ans, score
    if cur == 10:
        if score >= 5:
            ans += 1
        return
    

    for i in range(1, 6):
        if cur >= 2 and y_list[cur - 1] == y_list[cur - 2] and y_list[cur - 1] == i:
            continue
        y_list[cur] = i
        # 맞는 경우
        if arr[cur] == i:
            score += 1
            recur(cur + 1)
            score -= 1
        # 틀리는 경우    
        else:
            recur(cur + 1)
        
    

recur(0)
print(ans)
        

