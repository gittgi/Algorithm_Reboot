k = int(input())
bu = list(input().split())
arr = [0 for i in range(k+1)]
visited = [False for i in range(10)]
ans = []
def recur(cur):
    if not check(cur):
        return
    else:
        if cur == k + 1:
            ans.append(arr[:])
            return
    
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            arr[cur] = i
            recur(cur + 1)
            visited[i] = False


def check(cur):
    if cur <= 1:
        return True

    if bu[cur-2] == "<":
        if arr[cur-2] < arr[cur-1]:
            return True
        else:
            return False
    else:
        if arr[cur-2] > arr[cur-1]:
            return True
        else:
            return False


recur(0)
for i in range(k+1):
    print(ans[-1][i], end="")
print()
for i in range(k+1):
    print(ans[0][i], end="")

