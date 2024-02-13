import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n
ans[-1] = -1
temp = [[0, 0] for _ in range(n)]
temp[-1] = [n-1, arr[n-1]] 
for i in range(n-2, -1, -1):
    if arr[i] != arr[i+1]:
        ans[i] = i+1+1
        temp[i] = [i+1, arr[i+1]]
    elif arr[i] != temp[i+1][1]:
        ans[i] = temp[i+1][0] + 1
        temp[i] = temp[i+1]
    else:
        ans[i] = -1
        temp[i] = temp[i+1]
print(temp)
print(*ans)