n = int(input())

arr = [0] * (n+1)

for i in range(1, n+1):
    arr[i] = int(input())


max_cnt = 0

def dfs(x, numbers, origin):
    numbers.append(x)
    if not visited[arr[x]]:
        visited[arr[x]] = True
        ans = dfs(arr[x], numbers, origin)
     
        return ans
    
    else:
        if arr[x] == origin:
            return numbers

    

temp = []

for i in range(1, n+1):
    visited = [False] * (n+1)
    visited[i] = True
    a = dfs(i, [], i)
 
    if a:
        temp.append(a)


visited = [False] * (n+1)
ans = []
for i in temp:
    for j in i:
        if visited[j]:
            break
    else:
        ans += i
        for num in i:
            visited[num] = True

print(len(ans))
for i in sorted(ans):
    print(i)
