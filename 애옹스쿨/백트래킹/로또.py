
def recur(cur, start, k):
    if cur == 6:
        print(*ans)
        return
    
    for i in range(start, k):
    
        if not visited[i]:
            visited[i] = True
            ans[cur] = arr[i]
            recur(cur + 1, i + 1, k)
            visited[i] = False
    
        


while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        break

    k = arr.pop(0)
    ans = [0 for i in range(6)]
    visited = [False for i in range(k)]


    recur(0, 0, k)
    print()
