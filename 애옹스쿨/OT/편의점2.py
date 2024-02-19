n = int(input())
arr_x = []
arr_y = []

for _ in range(n):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

arr_x.sort()
arr_y.sort()

# 홀수
if n % 2:
    ans_x = arr_x[n//2]
    ans_y = arr_y[n//2]
else:
    ans_x = arr_x[n//2 - 1]
    ans_y = arr_y[n//2 - 1]

ans = 0
for i in range(n):
    ans += abs(arr_x[i] - ans_x)
    ans += abs(arr_y[i] - ans_y)

print(ans)