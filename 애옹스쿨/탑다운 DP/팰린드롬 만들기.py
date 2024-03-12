import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = list(input().split())
ans = ["" for _ in range(2*n + 1)]
for i in range(n):
    ans[2*i + 1] = arr[i]

num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]



min_val = 1 << 60
def recur(cur, cnt):
    global min_val
    if cur == n+1:
        if "".join(ans) == "".join(ans[::-1]):
            min_val = min(min_val, cnt)
        return
    
    recur(cur + 1, cnt)

    for i in num_list:
        ans[cur*2] = i
        recur(cur + 1, cnt + 1)
        ans[cur*2] = ""
    

recur(0, 0)
print(min_val)