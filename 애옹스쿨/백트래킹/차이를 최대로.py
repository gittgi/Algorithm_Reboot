import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
visited = [False for _ in range(n)]
max_val = -float("inf")
ans_arr = [0 for _ in range(n)]
def recur(cur):
    global max_val
    if cur == n:
        val = 0
        for i in range(n-1):
            val += abs(ans_arr[i] - ans_arr[i+1])
        max_val = max(max_val, val)
        return


    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans_arr[cur] = arr[i]
            recur(cur + 1)
            visited[i] = False


recur(0)
print(max_val)