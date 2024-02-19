n = int(input())
arr = list(map(int, input().split()))

arr.sort()
# 홀수
if n % 2:
    ans = arr[n//2]

else:
    ans = arr[n//2 - 1]

print(ans)

