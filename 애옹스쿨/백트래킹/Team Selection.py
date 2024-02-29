# 각 능력치를 보았을 때, 하나도 5등안에 들지 않는 애들은 버린다

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
top_5 = [0 for i in range(5)]
for j in range(5):
    temp = []
    for i in range(n):
        temp.append(arr[i][j])
    temp.sort(reverse=True)
    top_5[j] = temp[4]

suffix_top_5 = [0 for _ in range(5)]
suffix_top_5[-1] = top_5[-1]
for i in range(3, -1, -1):
    suffix_top_5[i] = suffix_top_5[i+1] + top_5[i]


visited = [False for _ in range(n)]

total = 0
max_total = 0

def recur(cur):
    global max_total, total


    if cur == 5:
        max_total = max(max_total, total)
        return
    
    if total + suffix_top_5[cur] < max_total:
        return 
    

    for i in range(n):
        if not visited[i]:
            if arr[i][cur] >= top_5[cur]:
                visited[i] = True
                total += arr[i][cur]

                recur(cur + 1)
                total -= arr[i][cur]
                visited[i] = False

recur(0)
print(max_total)


