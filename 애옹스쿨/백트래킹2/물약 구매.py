n = int(input())
arr = [0] + list(map(int, input().split()))
discount = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    temp = int(input())
    for j in range(temp):
        idx, disc = map(int, input().split())
        discount[i][idx] = disc
    
min_val = float("inf")  
total = 0 
visited = [False for _ in range(n+1)]

def recur(cur):
    global total, min_val
    if total >= min_val:
        return
    if cur == n+1:
        min_val = min(min_val, total)
        return
    

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            total += arr[i]
            for j in range(1, n+1):
                arr[j] -= discount[i][j]
            temp_list = [0 for _ in range(n+1)]
            for k in range(1, n+1):
                if arr[k] < 1:
                    temp_list[k] = 1 - arr[k]
                    arr[k] = 1
            recur(cur + 1)
            for k in range(1, n+1):
                arr[k] -= temp_list[k]
            for j in range(1, n+1):
                arr[j] += discount[i][j]
            total -= arr[i]
            visited[i] = False


    
recur(1)
print(min_val)
