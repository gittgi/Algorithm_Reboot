n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
total = 0
ans = float("inf")
comb = []

# 재귀로 조합을 찾고, 조합이 찾아지면 그 자리에서 최소값 계산
# 따로 조합을 만들어서 메모리에 저장하고 나중에 한꺼번에 최소값을 계산하려고 하면 메모리초과..
def recur(num_list, index):
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

    # 재귀적으로 조합을 하기 (if 와 in을 사용하니까 시간초과 남)
    for i in range(index, n):
        recur(num_list + [i], i + 1) 

    
recur([], 0)
    

print(ans)
