n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
total = 0
ans = float("inf")
comb = []

# 절반만 뽑기
def recur(num_list):
    if len(num_list) == n//2:
        temp = 0
        temp_com = []
        temp2 = 0
        for i in range(n):
            if i not in num_list:
                temp_com.append(i)

        for i in range(n//2 - 1):
            for j in range(i + 1, n//2):
                x = num_list[i]
                y = num_list[j]
                a = temp_com[i]
                b = temp_com[j]
                temp += (arr[x][y] + arr[y][x])
                temp2 += (arr[a][b] + arr[b][a])

        global ans
        ans = min(ans, abs(temp - temp2))
        return

    for i in range(n):
        if i not in num_list:
            recur(num_list + [i])

    
recur([])
    

print(ans)
