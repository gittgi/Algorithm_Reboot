n = int(input())
arr = [0]
for i in range(n):
    arr.append(int(input()))

max_val = 0
cur_pick = [0 for i in range(n+1)]
num_pick = [0 for i in range(n+1)]
ans = []

def dfs(cur, cnt):
    global max_val, ans

    if cur == n+1:
        for i in range(n+1):
            if cur_pick[i] != num_pick[i]:
                return
        if max_val < cnt:
            max_val = cnt
            temp = []
            for i in range(1, n+1):
                if cur_pick[i] > 0:
                    temp.append(i)
            ans = temp
        return


    # 포함 안하고 넘기기
    dfs(cur+1, cnt)

    # 포함하고 넘기기
    cur_pick[cur] = 1
    num_pick[arr[cur]] += 1
    dfs(cur+1, cnt+1)
    num_pick[arr[cur]] -= 1
    cur_pick[cur] = 0

dfs(1, 0)
print(max_val)
ans.sort()
for i in ans:
    print(i)